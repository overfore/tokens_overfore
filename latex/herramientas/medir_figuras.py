# -*- coding: utf-8 -*-
"""Lista, por subdocumento, las figuras cuyo texto queda bajo 9 pt en la página impresa.

uso (desde la carpeta latex/, después de compilar):
  python herramientas/medir_figuras.py                 todos los PDF de salida/
  python herramientas/medir_figuras.py S4 T-14         sólo esos documentos
  python herramientas/medir_figuras.py --todas         muestra también las que cumplen
  python herramientas/medir_figuras.py --md informe.md además escribe la lista en Markdown
  python herramientas/medir_figuras.py --carpeta salida-borrador   mide los PDF de otra carpeta

Cómo mide: LaTeX no sabe qué letra hay dentro de una imagen, así que la herramienta lee el PDF
ya compilado. Cada figura (imagen de más de 4 cm con título «Figura …» debajo) se dibuja a
576 ppp, se separan las letras, se agrupan en líneas de texto y en cada línea se mide la altura
de las minúsculas. Letra en pt = altura x / (0,52 · píxeles por punto). Se informa el
percentil 5 de las líneas de la figura, que es la letra más chica sin contar ruido.
La medida es aproximada (± 0,3 pt): una figura entre 9,0 y 9,3 pt se marca «en el límite».
Mínimo exigido: 9 pt (Art. 40.4 de las Bases administrativas y Comunicado 10, §4).
"""
import glob, os, re, sys
from concurrent.futures import ProcessPoolExecutor

import numpy as np
import pymupdf

AQUI = os.path.dirname(os.path.abspath(__file__))
SALIDA = os.path.join(os.path.dirname(AQUI), 'salida')
MINIMO = 9.0
LIMITE = 9.3
PX_PT = 8.0          # píxeles por punto tipográfico (576 ppp)
XH = 0.52            # altura x / cuerpo en Arial, Helvetica, Open Sans y similares


def componentes(bina):
    """Cajas de las componentes 8-conexas, a partir de tramos horizontales (unión-búsqueda)."""
    padre = []

    def raiz(a):
        while padre[a] != a:
            padre[a] = padre[padre[a]]
            a = padre[a]
        return a

    previos, tramos = [], []
    for y in range(bina.shape[0]):
        d = np.diff(np.concatenate(([0], bina[y].view(np.int8), [0])))
        actuales = []
        j = 0
        for x0, x1 in zip(np.flatnonzero(d == 1), np.flatnonzero(d == -1)):
            idx = len(padre)
            padre.append(idx)
            while j < len(previos) and previos[j][2] < x0 - 1:
                j += 1
            k = j
            while k < len(previos) and previos[k][1] <= x1:
                a, b = raiz(idx), raiz(previos[k][3])
                if a != b:
                    padre[a] = b
                k += 1
            actuales.append((y, x0, x1, idx))
        tramos.extend(actuales)
        previos = actuales
    caja = {}
    for y, x0, x1, idx in tramos:
        r = raiz(idx)
        c = caja.get(r)
        if c is None:
            caja[r] = [x0, y, x1, y + 1, x1 - x0]
        else:
            c[0] = min(c[0], x0); c[1] = min(c[1], y); c[2] = max(c[2], x1); c[3] = max(c[3], y + 1); c[4] += x1 - x0
    return list(caja.values())


def alturas_x(comps):
    """Agrupa letras que comparten línea base y están próximas; devuelve la altura x de cada línea."""
    letras = sorted((y1, x0, x1, y1 - y0) for x0, y0, x1, y1, n in comps
                    if 6 <= y1 - y0 <= 120 and x1 - x0 <= 1.7 * (y1 - y0) and 0.12 <= n / ((x1 - x0) * (y1 - y0)) <= 0.8)
    usadas = [False] * len(letras)
    lineas = []
    for i, (base, x0, x1, h) in enumerate(letras):
        if usadas[i]:
            continue
        grupo = [(x0, x1, h)]
        usadas[i] = True
        for j in range(i + 1, len(letras)):
            b2, a0, a1, h2 = letras[j]
            if b2 - base > 2:
                break
            if not usadas[j] and 0.5 <= h2 / h <= 2.2:
                grupo.append((a0, a1, h2))
                usadas[j] = True
        grupo.sort()
        trozo = [grupo[0]]
        for g in grupo[1:]:
            if g[0] - trozo[-1][1] > 2.5 * np.median([t[2] for t in trozo]):   # otra columna de texto
                if len(trozo) >= 5:
                    lineas.append(trozo)
                trozo = [g]
            else:
                trozo.append(g)
        if len(trozo) >= 5:
            lineas.append(trozo)
    return [sorted(x[2] for x in t)[int(len(t) * 0.3)] for t in lineas]


def documento(pdf):
    m = re.search(r'Formulario-(T-\d+)|Subdocumento(\d+)(-Anexos)?', os.path.basename(pdf))
    if not m:
        return os.path.basename(pdf)[:-4]
    return m.group(1) or 'S%s%s' % (m.group(2), ' anexos' if m.group(3) else '')


def medir(pdf):
    doc = pymupdf.open(pdf)
    vistos, res = set(), []
    for p in doc:
        folio = re.search(r'Folio\s+(\d+)', p.get_text())
        for img in p.get_images(full=True):
            for r in p.get_image_rects(img[0]):
                if r.width < 4 / 2.54 * 72 or (img[0], p.number) in vistos:
                    continue
                vistos.add((img[0], p.number))
                tit = p.get_text('text', clip=pymupdf.Rect(r.x0 - 40, r.y1, r.x1 + 40, r.y1 + 40)).replace('\n', ' ')
                num = re.search(r'Figura\s+([A-Z]?\d*\.?\d+)', tit)
                if not num:            # logo, firma u otra imagen sin título de figura
                    continue
                pix = p.get_pixmap(clip=r, matrix=pymupdf.Matrix(PX_PT, PX_PT), colorspace=pymupdf.csGRAY)
                a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width)
                pts = sorted(h / (XH * PX_PT) for h in alturas_x(componentes(a < 150)))
                titulo = re.sub(r'\s+', ' ', tit[tit.find('Figura'):]).split('Fuente:')[0]
                titulo = re.sub(r'^Figura\s+\S+\s*[—-]\s*', '', titulo).strip()
                res.append(dict(doc=documento(pdf), figura=num.group(1), folio=folio.group(1) if folio else '?',
                                pagina=p.number + 1, titulo=titulo,
                                letra=round(pts[max(0, int(len(pts) * 0.05))], 1) if pts else None))
    return res


def clave_doc(d):
    m = re.match(r'(S|T-)(\d+)', d)
    return (0 if d.startswith('S') else 1, int(m.group(2)) if m else 99, d)


def main():
    args = sys.argv[1:]
    todas = '--todas' in args
    md = args[args.index('--md') + 1] if '--md' in args else None
    dir_arg = args[args.index('--carpeta') + 1] if '--carpeta' in args else None
    carpeta = dir_arg or SALIDA
    if not os.path.isdir(carpeta):
        carpeta = os.path.join(os.path.dirname(AQUI), carpeta)     # relativa a latex/
    filtro = {a.upper().replace('ANEXOS', 'anexos') for a in args if not a.startswith('--') and a not in (md, dir_arg)}
    pdfs = sorted(glob.glob(os.path.join(carpeta, '*.pdf')))
    if filtro:
        pdfs = [f for f in pdfs if documento(f) in filtro or documento(f).split()[0] in filtro]
    if not pdfs:
        sys.exit('No hay PDF en %s que coincidan; compila primero.' % carpeta)
    figuras = []
    with ProcessPoolExecutor() as ex:
        for r in ex.map(medir, pdfs):
            figuras += r
    figuras.sort(key=lambda f: (clave_doc(f['doc']), f['pagina']))
    malas = [f for f in figuras if f['letra'] is not None and f['letra'] < MINIMO]
    justas = [f for f in figuras if f['letra'] is not None and MINIMO <= f['letra'] < LIMITE]
    sin = [f for f in figuras if f['letra'] is None]
    mostrar = figuras if todas else malas + justas

    def estado(f):
        if f['letra'] is None:
            return 'sin texto medible'
        return 'NO CUMPLE' if f['letra'] < MINIMO else ('en el límite' if f['letra'] < LIMITE else 'cumple')

    filas = []
    actual = None
    for f in sorted(mostrar, key=lambda f: (clave_doc(f['doc']), f['pagina'])):
        if f['doc'] != actual:
            actual = f['doc']
            print('\n' + actual)
        letra = ('%.1f pt' % f['letra']).replace('.', ',') if f['letra'] is not None else '—'
        print('  Figura %-6s folio %-5s %-8s %-13s %s' % (f['figura'], f['folio'], letra, estado(f), f['titulo'][:60]))
        filas.append((f['doc'], f['figura'], f['folio'], letra, estado(f), f['titulo']))

    print('\nResumen por documento (figuras medidas / bajo 9 pt / en el límite)')
    docs = sorted({f['doc'] for f in figuras}, key=clave_doc)
    resumen = []
    for d in docs:
        n = sum(1 for f in figuras if f['doc'] == d)
        b = sum(1 for f in malas if f['doc'] == d)
        j = sum(1 for f in justas if f['doc'] == d)
        resumen.append((d, n, b, j))
        print('  %-12s %3d  %3d  %3d%s' % (d, n, b, j, '  ←' if b else ''))
    print('\n%d figuras medidas: %d bajo 9 pt, %d en el límite (9,0 a 9,3 pt)%s.' % (
        len(figuras), len(malas), len(justas), ', %d sin texto medible' % len(sin) if sin else ''))

    if md:
        with open(md, 'w', encoding='utf-8') as out:
            out.write('# Figuras bajo 9 pt\n\nMedición de `herramientas/medir_figuras.py` sobre los PDF de `%s/`. '
                      % os.path.basename(os.path.normpath(carpeta)) +
                      'La letra es la del texto más chico de cada figura tal como se imprime (± 0,3 pt).\n\n')
            out.write('| Doc | Figura | Folio | Letra | Estado | Título |\n|---|---|---|---|---|---|\n')
            for fila in filas:
                out.write('| %s | %s | %s | %s | %s | %s |\n' % fila)
            out.write('\n| Doc | Figuras | Bajo 9 pt | En el límite |\n|---|---|---|---|\n')
            for d, n, b, j in resumen:
                out.write('| %s | %d | %d | %d |\n' % (d, n, b, j))
        print('Lista escrita en', md)
    return 1 if malas else 0


if __name__ == '__main__':
    sys.exit(main())
