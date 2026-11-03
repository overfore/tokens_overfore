# -*- coding: utf-8 -*-
"""Compila la propuesta de OVERFORE con folio continuo entre todos los archivos.

Uso:
    python compilar.py                  compila todo, en orden, con folio continuo
    python compilar.py ruta/al/doc.tex  compila un solo documento (usa los folios ya calculados)
    python compilar.py --reglas         sólo revisa las reglas en todos los documentos
    python compilar.py --revisar        una pasada rápida sobre todo, para encontrar errores
    python compilar.py --borrador       compila todo aunque haya errores de reglas (sólo para ver
                                        cómo queda); los PDF van a salida-borrador/
    python compilar.py --borrador ruta/al/doc.tex   lo mismo para un documento

Orden: Subdocumento 1, sus Anexos, sus Formularios T (de menor a mayor), luego el
Subdocumento 2, y así sucesivamente. El primer folio de cada archivo es el último
folio del anterior + 1. Los PDF finales quedan en salida/ con su nombre oficial.

Antes de compilar se verifica:
  1. que cada documento use la clase overfore en uno de sus tres modos;
  2. las reglas de contenido de comun/reglas.py (un ERROR impide compilar; un AVISO no).
Después de compilar se verifica que ninguna tabla del subdocumento pase de una página.
El índice y los listados de tablas y figuras se recalculan en cada compilación: se
repite la compilación hasta que no cambien.
"""
import os, re, sys, shutil, hashlib, subprocess, concurrent.futures as cf

RAIZ = os.path.dirname(os.path.abspath(__file__))
COMUN = os.path.join(RAIZ, 'comun')
SALIDA = os.path.join(RAIZ, 'salida')
SALIDA_BORRADOR = os.path.join(RAIZ, 'salida-borrador')
CLASE_RX = re.compile(r'^\s*\\documentclass\s*\[\s*(subdoc|anexo|formulario)\s*\]\s*\{\.\./\.\./comun/overfore\}', re.M)
sys.path.insert(0, COMUN)
import reglas  # noqa: E402


def xelatex():
    for c in ('xelatex', os.path.expandvars(r'%LOCALAPPDATA%\Programs\MiKTeX\miktex\bin\x64\xelatex.exe')):
        if shutil.which(c) or os.path.exists(c):
            return shutil.which(c) or c
    sys.exit('No se encontró xelatex. Instale MiKTeX.')


def documentos():
    """Busca los documentos que existen y los ordena: subdocumento, anexos y formularios T
    de menor a mayor, subdocumento por subdocumento. No exige que estén los 14: cada
    entrega incorpora los que corresponden. Reescribe comun/documentos.tex con lo encontrado."""
    docs = []
    subdocs = sorted((int(m.group(1)), d) for d in os.listdir(RAIZ)
                     for m in [re.match(r'^subdoc(\d+)$', d)] if m and os.path.isdir(os.path.join(RAIZ, d)))
    for n, d in subdocs:
        base = os.path.join(RAIZ, d)
        partes = [('S%d' % n, 'subdocumento'), ('A%d' % n, 'anexos')]
        formularios = sorted((int(m.group(1)), f) for f in os.listdir(base)
                             for m in [re.match(r'^formulario-T-(\d+)$', f)] if m)
        partes += [('T%d' % t, f) for t, f in formularios]
        for clave, carpeta in partes:
            ruta = os.path.join(base, carpeta)
            if not os.path.isdir(ruta):
                continue
            tex = [f for f in os.listdir(ruta) if f.endswith('.tex')]
            if len(tex) == 1:
                docs.append((clave, os.path.join(ruta, tex[0])))
    lineas = ['% Generado por compilar.py: clave de cada documento y su ruta (desde latex/).']
    for clave, tex in docs:
        rel = os.path.splitext(os.path.relpath(tex, RAIZ))[0].replace(os.sep, '/')
        lineas.append('\\ovdoc{%s}{%s}' % (clave, rel))
    with open(os.path.join(COMUN, 'documentos.tex'), 'w', encoding='utf8') as f:
        f.write('\n'.join(lineas) + '\n')
    return docs


def verificar_clase(tex):
    with open(tex, encoding='utf8') as f:
        cab = f.read(3000)
    sin_coment = '\n'.join(l.split('%')[0] for l in cab.splitlines())
    clases = re.findall(r'\\documentclass', sin_coment)
    if len(clases) != 1 or not CLASE_RX.search(sin_coment):
        return ('%s no usa la clase oficial. La primera línea debe ser\n'
                '  \\documentclass[subdoc]{../../comun/overfore}   (o [anexo] o [formulario])' % os.path.basename(tex))
    return None


def revisar_reglas(tex, mostrar=True):
    """Devuelve el número de errores; imprime errores y avisos."""
    hz = reglas.revisar(tex)
    if mostrar:
        for h in hz:
            print(h.texto(os.path.relpath(tex, RAIZ)))
    return sum(1 for h in hz if h.nivel == 'E')


def huella_indices(tex):
    base = os.path.splitext(tex)[0]
    h = hashlib.md5()
    for ext in ('.toc', '.lot', '.lof'):
        if os.path.exists(base + ext):
            with open(base + ext, 'rb') as f:
                h.update(f.read())
    return h.hexdigest()


def compilar(tex, exe, borrador=False):
    d, nombre = os.path.split(tex)
    base = os.path.splitext(nombre)[0]
    # en borrador la clase avisa en vez de detenerse y marca cada página como BORRADOR
    entrada = (r'\def\ovborrador{1}\input{%s}' % nombre) if borrador else nombre
    r = subprocess.run([exe, '-interaction=nonstopmode', '-halt-on-error', '-file-line-error', '-jobname=' + base, entrada],
                       cwd=d, capture_output=True, text=True, encoding='utf8', errors='replace')
    log = os.path.join(d, base + '.log')
    paginas = None
    errores = []
    if os.path.exists(log):
        with open(log, encoding='utf8', errors='replace') as f:
            texto = f.read()
        m = re.search(r'Output written on .*?\((\d+) pages?', texto, re.S)
        paginas = int(m.group(1)) if m else None
        for m in re.finditer(r'^(?:\S+:\d+: |! )(.*)$', texto, re.M):
            if 'ignored error' not in m.group(1):
                errores.append(m.group(1).strip())
    return base, paginas, (r.returncode == 0), errores[:3]


def copiar_aux(tex):
    """Copia estable del .aux para que otros documentos lean sus referencias sin carreras."""
    base = os.path.splitext(tex)[0]
    if os.path.exists(base + '.aux'):
        shutil.copy(base + '.aux', base + '-ref.aux')


def tablas_largas(tex):
    hz = reglas.tablas_largas(os.path.splitext(tex)[0] + '.aux', tex)
    for h in hz:
        print(h.texto(os.path.relpath(tex, RAIZ)))
    return len(hz)


def escribir_folios(docs, paginas):
    folio = 1
    lineas = ['% Generado por compilar.py: primer folio de cada archivo (folio continuo).']
    for clave, tex in docs:
        base = os.path.splitext(os.path.basename(tex))[0]
        lineas.append('\\folioinicial{%s}{%d}' % (base, folio))
        folio += paginas.get(base) or 0
    nuevo = '\n'.join(lineas) + '\n'
    ruta = os.path.join(COMUN, 'folios.tex')
    viejo = open(ruta, encoding='utf8').read() if os.path.exists(ruta) else ''
    with open(ruta, 'w', encoding='utf8') as f:
        f.write(nuevo)
    return nuevo != viejo, folio - 1


def pasada(docs, exe, n, borrador=False):
    paginas, fallas = {}, []
    with cf.ThreadPoolExecutor(max_workers=max(2, (os.cpu_count() or 4) // 2)) as ex:
        futuros = {ex.submit(compilar, tex, exe, borrador): (clave, tex) for clave, tex in docs}
        for fu in cf.as_completed(futuros):
            base, pag, ok, err = fu.result()
            paginas[base] = pag
            print('    %-38s %4s págs.%s' % (base, pag, '' if ok else '  ERROR'), flush=True)
            if not ok:
                fallas.append((base, err))
    # un error puede ser momentáneo (archivo bloqueado por otro proceso): se reintenta una vez, solo
    if fallas:
        por_base = {os.path.splitext(os.path.basename(t))[0]: t for _, t in docs}
        reintento = []
        for base, err in fallas:
            base, pag, ok, err = compilar(por_base[base], exe, borrador)
            print('    %-38s %4s págs.%s (reintento)' % (base, pag, '' if ok else '  ERROR'), flush=True)
            if ok:
                paginas[base] = pag
            else:
                reintento.append((base, err))
        fallas = reintento
    for clave, tex in docs:
        copiar_aux(tex)
    print('  pasada %d: %d documentos, %d con error' % (n, len(docs), len(fallas)), flush=True)
    return paginas, fallas


def verificar_todo(docs, borrador=False):
    malos = [e for e in (verificar_clase(t) for _, t in docs) if e]
    if malos:
        print('\n'.join(malos))
        return False
    errores = 0
    for _, tex in docs:
        errores += revisar_reglas(tex, mostrar=not borrador)
    if errores and borrador:
        print('BORRADOR: hay %d errores de reglas; se compila igual sólo para revisar. '
              'Los PDF quedan en salida-borrador/ y no sirven para entregar.' % errores)
        return True
    if errores:
        print('\n%d errores de reglas: no se compila hasta corregirlos.' % errores)
        print('Para ver cómo queda igual: python compilar.py --borrador')
        return False
    return True


def todo(borrador=False):
    exe = xelatex()
    docs = documentos()
    if not verificar_todo(docs, borrador):
        sys.exit(1)
    destino = SALIDA_BORRADOR if borrador else SALIDA
    paginas, fallas, n = {}, [], 0
    huellas = {}
    estable = False
    # se repite hasta que folios, índices y listados no cambien (mínimo tres pasadas)
    while n < 10:
        n += 1
        previas = paginas
        paginas, fallas = pasada(docs, exe, n, borrador)
        # un documento con error no cuenta bien sus páginas: se conserva el conteo anterior
        for base, _ in fallas:
            if previas.get(base):
                paginas[base] = previas[base]
        cambios, total = escribir_folios(docs, paginas)
        nuevas = {t: huella_indices(t) for _, t in docs}
        if n >= 3 and not cambios and nuevas == huellas and not fallas:
            estable = True
            break
        huellas = nuevas
    largas = sum(tablas_largas(t) for _, t in docs)
    os.makedirs(destino, exist_ok=True)
    print('\nFolios:')
    folio = 1
    for clave, tex in docs:
        base = os.path.splitext(os.path.basename(tex))[0]
        pdf = os.path.splitext(tex)[0] + '.pdf'
        p = paginas.get(base) or 0
        print('  %-40s folios %5d a %5d' % (base, folio, folio + p - 1))
        folio += p
        if os.path.exists(pdf):
            shutil.copy(pdf, os.path.join(destino, base + '.pdf'))
    print('\nTotal: %d folios. PDF en %s' % (folio - 1, destino))
    if fallas:
        print('\nDocumentos con error:')
        for base, err in fallas:
            print('  %s: %s' % (base, ' | '.join(err)))
    if not estable:
        print('\nEl folio o los índices no se estabilizaron en %d pasadas: vuelva a compilar.' % n)
    if fallas or largas or not estable:
        sys.exit(1)


def uno(tex, borrador=False):
    tex = os.path.abspath(tex)
    err = verificar_clase(tex)
    if err:
        print(err)
        sys.exit(1)
    if revisar_reglas(tex):
        if borrador:
            print('BORRADOR: hay errores de reglas (arriba); se compila igual sólo para revisar.')
        else:
            print('No se compila: corrija los errores de reglas indicados arriba.')
            print('Para ver cómo queda igual: python compilar.py --borrador "%s"' % os.path.relpath(tex, RAIZ))
            sys.exit(1)
    exe = xelatex()
    previa = None
    for k in range(4):
        base, pag, ok, errores = compilar(tex, exe, borrador)
        if not ok:
            print('Error en %s:\n  %s' % (base, '\n  '.join(errores)))
            sys.exit(1)
        h = huella_indices(tex)
        if k >= 1 and h == previa:
            break          # índice y listados al día
        previa = h
    copiar_aux(tex)
    if tablas_largas(tex):
        print('El PDF se generó, pero no cumple: hay tablas del subdocumento de más de una página.')
        sys.exit(1)
    print('%s: %s páginas' % (base, pag))


def solo_reglas():
    docs = documentos()
    e = 0
    for _, tex in docs:
        e += revisar_reglas(tex)
        e += tablas_largas(tex)
    print('\n%d errores en total.' % e)
    sys.exit(1 if e else 0)


def revisar():
    """Una sola pasada sobre todo, para encontrar errores de compilación rápido."""
    exe = xelatex()
    docs = documentos()
    paginas, fallas = pasada(docs, exe, 1)
    for base, err in fallas:
        print('  %s: %s' % (base, ' | '.join(err)))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--revisar':
        revisar()
    elif len(sys.argv) > 1 and sys.argv[1] == '--borrador':
        if len(sys.argv) > 2:
            uno(sys.argv[2], borrador=True)
        else:
            todo(borrador=True)
    elif len(sys.argv) > 1 and sys.argv[1] == '--reglas':
        solo_reglas()
    elif len(sys.argv) > 1:
        uno(sys.argv[1])
    else:
        todo()
