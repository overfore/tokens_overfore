# -*- coding: utf-8 -*-
"""Reglas de contenido de la propuesta OVERFORE (Comunicado 10).

Se aplican antes de compilar (compilar.py). Un ERROR impide compilar; un AVISO
sólo se informa.

Reglas (E = error, A = aviso):
  E  titulo-seguido      Un título no puede ir seguido de una tabla, una figura u otro título.   [subdoc]
  E  marcador            No pueden quedar marcadores: [ ... ], INSERTAR, borrador.            [todos]
  E  termino-prohibido   OVERFORE en mayúsculas en el texto, universidad o curso, Terraform,
                         «con apoyo de Claude» en fuentes, restos de nombres de archivo.     [todos]
  E  tabla-columnas      En el subdoc, una tabla tiene como máximo 5 columnas.                [subdoc]
  E  tabla-pagina        En el subdoc, una tabla no ocupa más de una página (tras compilar).  [subdoc]
  E  celda-frases        En el subdoc, ninguna celda tiene más de una frase.                  [subdoc]
  E  celda-vacia         Ninguna celda queda vacía (se escribe «—» o «No aplica»).                  [todos]
  E  ficha-en-texto      Fichas o tablas escritas como párrafos («ID | …» o «Etiqueta: valor»
                         repetido) en lugar de tabla o tablasintitulo.                          [todos]
  A  concepto-descripcion  Tabla con forma «Concepto / Descripción».                          [subdoc]
  E  sin-titulo          Toda tabla y figura tiene título y fuente.                            [subdoc]
  E  sin-cita            Toda tabla y figura se cita en el texto antes de aparecer.            [subdoc]
  E  sin-explicacion     Después de cada tabla y figura viene texto que la explica.            [subdoc]
  A  capitulo-sin-figuras  Un capítulo técnico sin figuras integradas.                         [subdoc]
  E  indice-obligatorio  Están todos los títulos del índice obligatorio, con su número, texto y orden.  [subdoc]
  E  titulo-agregado     No se agregan títulos del mismo nivel que los declarados.            [subdoc]
La tabla de la Declaración de uso de IA queda fuera de las reglas de tamaño de tabla:
su forma la fija el propio comunicado.
"""
import json, os, re

AQUI = os.path.dirname(os.path.abspath(__file__))
CAPITULOS_TECNICOS = {3, 4, 5, 6, 7, 8, 9, 10, 11, 13}
TITULOS = {
    'capitulo': 1, 'anexo': 1, 'apartado': 1,
    'seccion': 2, 'subseccion': 3, 'subsubseccion': 4, 'seccionsinnumero': 1,
}


class Hallazgo:
    def __init__(self, nivel, regla, linea, msg):
        self.nivel, self.regla, self.linea, self.msg = nivel, regla, linea, msg

    def texto(self, archivo):
        return '%s:%d: %s [%s] %s' % (archivo, self.linea, 'ERROR' if self.nivel == 'E' else 'AVISO', self.regla, self.msg)


# --------------------------------------------------------------------------- lectura del .tex
def sin_comentarios(s):
    return re.sub(r'(?<!\\)%.*', '', s)


def argumento(s, i):
    """Lee un argumento {..} desde s[i] (salta espacios). Devuelve (contenido, posición siguiente)."""
    while i < len(s) and s[i] in ' \t\r\n':
        i += 1
    if i >= len(s) or s[i] != '{':
        return None, i
    n = 0
    for j in range(i, len(s)):
        c = s[j]
        if c == '\\':
            continue
        if c == '{' and s[j - 1] != '\\':
            n += 1
        elif c == '}' and s[j - 1] != '\\':
            n -= 1
            if n == 0:
                return s[i + 1:j], j + 1
    return s[i + 1:], len(s)


def dividir(s, sep):
    """Divide s por el separador (& o \\\\) sólo en el nivel superior de llaves."""
    partes, n, ini, i = [], 0, 0, 0
    while i < len(s):
        c = s[i]
        if c == '\\':
            if sep == r'\\' and s.startswith(r'\\', i) and n == 0:
                partes.append(s[ini:i]); i += 2
                # \\* o \\[..]
                if i < len(s) and s[i] == '*':
                    i += 1
                if i < len(s) and s[i] == '[':
                    k = s.find(']', i)
                    i = k + 1 if k > 0 else i
                ini = i
                continue
            i += 2
            continue
        if c == '{':
            n += 1
        elif c == '}':
            n -= 1
        elif c == sep and n == 0 and sep == '&':
            partes.append(s[ini:i]); ini = i + 1
        i += 1
    partes.append(s[ini:])
    return partes


def texto_plano(s):
    s = re.sub(r'\\(?:ref\*?|refext)\{[^}]*\}(?:\{[^}]*\})?', '1', s)
    s = re.sub(r'\\(?:newline|par|hline|quad|,)\b', ' ', s)
    s = re.sub(r'\\multirow\{[^}]*\}\{[^}]*\}', '', s)
    s = re.sub(r'\\multicolumn\{[^}]*\}\{[^}]*\}', '', s)
    s = re.sub(r'\\[a-zA-Z@]+\*?', ' ', s)
    s = s.replace('{', ' ').replace('}', ' ').replace('~', ' ')
    return re.sub(r'\s+', ' ', s).strip()


def num_columnas(spec):
    n = len(re.findall(r'[ICDpmb]\{', spec))
    n += len(re.findall(r'(?<![\\{a-zA-Z])[lcrX](?![a-zA-Z{])', re.sub(r'\{[^}]*\}', '', spec)))
    return n


class Bloque:
    def __init__(self, tipo, ini, fin, **kw):
        self.tipo, self.ini, self.fin = tipo, ini, fin
        self.__dict__.update(kw)


def bloques(cuerpo):
    """Recorre el cuerpo y devuelve la secuencia de títulos, tablas, figuras, listas y texto."""
    out = []
    pat = re.compile(r'\\(capitulo|anexo|apartado|seccion|subseccion|subsubseccion|seccionsinnumero)(\*?)(?=\s*\{)'
                     r'|\\begin\{(tabla|tablasintitulo|itemize|enumerate|referencias)\}'
                     r'|\\(figura|imagen)(?=\s*\{)'
                     r'|\\(fuente|nota)(?=\s*\{)'
                     r'|\\(?:begin|end)\{horizontal\}')
    i = 0
    while True:
        m = pat.search(cuerpo, i)
        tramo = cuerpo[i:m.start() if m else len(cuerpo)]
        for par in re.finditer(r'(?:[^\n]|\n(?!\s*\n))+', tramo):
            t = texto_plano(par.group(0))
            if t:
                out.append(Bloque('texto', i + par.start(), i + par.end(), texto=t))
        if not m:
            break
        if m.group(1):
            arg, j = argumento(cuerpo, m.end())
            out.append(Bloque('titulo', m.start(), j, cmd=m.group(1), estrella=bool(m.group(2)), texto=texto_plano(arg or '')))
            i = j
        elif m.group(3) in ('tabla', 'tablasintitulo'):
            env = m.group(3)
            fin = cuerpo.find(r'\end{%s}' % env, m.end())
            fin = len(cuerpo) if fin < 0 else fin
            j = m.end()
            if env == 'tabla':
                args = []
                for _ in range(5):
                    a, j = argumento(cuerpo, j)
                    args.append(a or '')
                spec, titulo, etiqueta, cab, fuente = args
            else:
                spec, j = argumento(cuerpo, j)
                cab, j = argumento(cuerpo, j)
                titulo = etiqueta = fuente = ''
            filas = [f for f in dividir(cuerpo[j:fin], r'\\') if f.strip()]
            out.append(Bloque('tabla', m.start(), fin + len(r'\end{%s}' % env), env=env, spec=spec or '',
                              titulo=texto_plano(titulo), etiqueta=etiqueta.strip(), fuente=texto_plano(fuente),
                              cab=cab or '', filas=filas, cuerpo_ini=j))
            i = fin + len(r'\end{%s}' % env)
        elif m.group(3):
            env = m.group(3)
            fin = cuerpo.find(r'\end{%s}' % env, m.end())
            # listas anidadas
            prof, k = 1, m.end()
            while True:
                a = re.search(r'\\(begin|end)\{%s\}' % env, cuerpo[k:])
                if not a:
                    fin = len(cuerpo); break
                prof += 1 if a.group(1) == 'begin' else -1
                k += a.end()
                if prof == 0:
                    fin = k; break
            out.append(Bloque('lista' if env != 'referencias' else 'referencias', m.start(), fin,
                              texto=texto_plano(cuerpo[m.end():fin])))
            i = fin
        elif m.group(4):
            n = 5 if m.group(4) == 'figura' else 2
            j = m.end(); args = []
            for _ in range(n):
                a, j = argumento(cuerpo, j)
                args.append(a or '')
            if m.group(4) == 'figura':
                out.append(Bloque('figura', m.start(), j, titulo=texto_plano(args[2]), etiqueta=args[3].strip(),
                                  fuente=texto_plano(args[4])))
            else:
                out.append(Bloque('imagen', m.start(), j))
            i = j
        elif m.group(5):
            a, j = argumento(cuerpo, m.end())
            out.append(Bloque(m.group(5), m.start(), j, texto=texto_plano(a or '')))
            i = j
        else:
            i = m.end()
    return out


# --------------------------------------------------------------------------- reglas
PALABRAS_MARCADOR = r'(?i)\b(t[ií]tulo|nombre|campo|contenido|elemento|descripci[oó]n|texto|completar|insertar|pendiente|' \
                    r'agregar|xx+|d[ií]a|mes|año|fecha|cite|ver|figura|tabla|anexo|referencia|link|url|todo)\b'

def es_marcador(c):
    c = c.strip()
    if re.search(r'\.\.\.|…|cite\s*:|^\s*$', c):
        return True
    if re.fullmatch(r'[NnXx]|T-\[?XX\]?|XX|N°?', c):
        return True
    palabras = re.findall(r'[^\s,;/]+', c)
    sigla = all(re.match(r'^([A-ZÁÉÍÓÚÑ0-9][\w\-\.&]*|y|e|&|de|del)$', w) for w in palabras)
    if sigla and not re.search(PALABRAS_MARCADOR, c):
        return False
    return bool(re.search(PALABRAS_MARCADOR, c)) or bool(re.search(r'\b[a-záéíóúñ]{3,}\b', c))

PROHIBIDOS = [
    (r'\bOVERFORE\b(?!-)', 'En el texto la empresa se escribe «Overfore» (OVERFORE sólo en nombres de archivo)'),
    (r'\bPUCV\b|Pontificia|Universidad Católica|Escuela de Informática|\bFEP\s?0\d|Formulación y Evaluación de Proyectos',
     'Mención a la universidad o al curso'),
    (r'\bTerraform\b', 'La herramienta de infraestructura como código es OpenTofu'),
    (r'con (?:el )?apoyo de (?:Claude|ChatGPT|Codex|la IA|IA)\b', 'El uso de IA se declara en su tabla, no en la fuente'),
    (r'\(\d\)\.md\b|(?<!/)\b[\w\-]+\.md\b|archivos comparados', 'Resto de nombre de archivo o nota de trabajo'),
]

ABREV =r'(?:N°|n°|Nº|p|pp|Art|art|S\.A|Ltda|SpA|etc|Sr|Sra|Dr|Ing|cap|Cap|núm|aprox|vol|ed|ej|i\.e|e\.g|vs|Inc|Co|Corp|Fig|Tab|v)\.'

def frases(t):
    t = re.sub(ABREV, 'X', t)
    t = re.sub(r'(\d)\.(\d)', r'\1\2', t)
    t = re.sub(r'(\d)\.(?=\s)', r'\1', t)                # numeraciones: «1. Presentación»
    t = re.sub(r'\b[A-Z]\.(?=\s*[A-Z]\.)', 'X', t)       # siglas con puntos
    return len(re.findall(r'[\.!?]\s+[A-ZÁÉÍÓÚÑ¿¡«"]', t)) + 1


def revisar(ruta, cuerpo_total=None):
    with open(ruta, encoding='utf8') as f:
        fuente = f.read()
    s = sin_comentarios(fuente)
    m = re.search(r'\\documentclass\s*\[\s*(subdoc|anexo|formulario)\s*\]', s)
    modo = m.group(1) if m else None
    b0 = s.find(r'\begin{document}')
    b1 = s.find(r'\end{document}')
    if b0 < 0:
        return []
    cuerpo = s[b0 + len(r'\begin{document}'):b1 if b1 > 0 else len(s)]
    base = b0 + len(r'\begin{document}')
    linea = lambda pos: s.count('\n', 0, base + pos) + 1
    hz = []
    def add(nivel, regla, pos, msg):
        hz.append(Hallazgo(nivel, regla, linea(pos), msg))
    bl = bloques(cuerpo)
    subdoc = modo == 'subdoc'

    # sección actual (para exceptuar la Declaración de uso de IA)
    seccion_de = {}
    actual = ''
    for k, b in enumerate(bl):
        if b.tipo == 'titulo' and TITULOS[b.cmd] == 1:
            actual = b.texto
        seccion_de[k] = actual
    def es_ia(k):
        return seccion_de.get(k, '').lower().startswith('declaración de uso de ia')

    # ---- marcadores (todos los formatos)
    dentro_ref = []
    for b in bl:
        if b.tipo == 'referencias':
            dentro_ref.append((b.ini, b.fin))
    tablas_pos = [(b.ini, b.fin) for b in bl if b.tipo == 'tabla']
    for mm in re.finditer(r'\[([^\]\n]{1,90})\]', cuerpo):
        p = mm.start()
        if any(a <= p < z for a, z in dentro_ref):
            continue
        antes = cuerpo[max(0, p - 12):p]
        if re.search(r'(\\\\\*?|\\item|\\begin\{[a-z]+\}|\\[a-zA-Z]+)\s*$', antes):
            continue          # argumento opcional de LaTeX
        if '$' in cuerpo[max(0, p - 40):p] and cuerpo[max(0, p - 40):p].count('$') % 2 == 1:
            continue          # dentro de una fórmula
        if not es_marcador(mm.group(1)):
            continue          # siglas de autor en APA: [PMI], [ISO], [WRI y WBCSD]; códigos: [E2]
        add('E', 'marcador', p, 'Marcador sin completar: [%s]' % mm.group(1)[:60])
    for mm in re.finditer(r'INSERTAR|\bborrador\b|\bBORRADOR\b', cuerpo):
        p = mm.start()
        if mm.group(0).lower() == 'borrador' and (any(a <= p < z for a, z in tablas_pos) or any(a <= p < z for a, z in dentro_ref)):
            continue          # «Borrador de redacción» en la tabla de uso de IA es legítimo
        add('E', 'marcador', p, 'Marcador de borrador: «%s»' % cuerpo[p:p + 40].split('\n')[0])

    # ---- términos prohibidos (todos los formatos)
    for patron, msg in PROHIBIDOS:
        for mm in re.finditer(patron, cuerpo):
            add('E', 'termino-prohibido', mm.start(), '%s: «%s»' % (msg, mm.group(0)))

    # ---- celdas vacías (todos los formatos)
    for k, b in enumerate(bl):
        if b.tipo != 'tabla':
            continue
        ncol = num_columnas(b.spec) or 1
        cubiertas = set()          # (fila, col) cubiertas por \multirow{-n}
        filas = [dividir(f, '&') for f in b.filas]
        for r, celdas in enumerate(filas):
            c = 0
            for cel in celdas:
                span = 1
                mc = re.search(r'\\multicolumn\{(\d+)\}', cel)
                if mc:
                    span = int(mc.group(1))
                mr = re.search(r'\\multirow\{-?(\d+)\}', cel)
                if mr:
                    n = int(mr.group(1))
                    neg = '\\multirow{-' in cel
                    for x in range(1, n):
                        cubiertas.add((r - x if neg else r + x, c))
                c += span
        for r, celdas in enumerate(filas):
            c = 0
            for cel in celdas:
                span = 1
                mc = re.search(r'\\multicolumn\{(\d+)\}', cel)
                if mc:
                    span = int(mc.group(1))
                vacio = not texto_plano(re.sub(r'\\multicolumn\{\d+\}\{[^}]*\}', '', cel)) and r'\imagen' not in cel
                if vacio and (r, c) not in cubiertas and celdas != ['']:
                    add('E', 'celda-vacia', b.cuerpo_ini + sum(len(f) + 2 for f in b.filas[:r]),
                        'Celda vacía en la fila %d, columna %d de la tabla «%s» (escriba «—» o «No aplica»)' % (r + 1, c + 1, b.titulo[:50] or 'sin título'))
                c += span

    # ---- fichas o tablas escritas como texto suelto (todos los formatos)
    # «ID | campo | campo» en una línea, o tres o más párrafos seguidos «Etiqueta: valor»:
    # ese contenido va en el entorno tabla o tablasintitulo, no como párrafos.
    etiqueta = re.compile(r'([A-ZÁÉÍÓÚÑ¿][^:.\\{}\n]{1,45}):\s+\S')
    racha = []
    def cerrar_racha():
        if len(racha) >= 3:
            add('E', 'ficha-en-texto', racha[0][0],
                '%d párrafos seguidos «Etiqueta: valor» (%s…) fuera de tabla: use tablasintitulo'
                % (len(racha), ', '.join(e for _, e in racha[:3])))
        racha.clear()
    pos = 0
    for parrafo in re.split(r'\n\s*\n', cuerpo):
        ini = cuerpo.find(parrafo, pos)
        pos = ini + len(parrafo)
        p = parrafo.strip()
        if not p or any(a <= ini < z for a, z in tablas_pos):
            cerrar_racha()
            continue
        if not p.startswith('\\') and p.count(' | ') >= 1 and len(p) < 200:
            add('E', 'ficha-en-texto', ini, 'Encabezado de ficha con « | » fuera de tabla: «%s»' % p[:60])
        m = etiqueta.match(p)
        if m and len(m.group(1).split()) <= 6 and not p.startswith('\\'):
            racha.append((ini, m.group(1)))
        else:
            cerrar_racha()
    cerrar_racha()

    if not subdoc:
        return hz

    # ---- títulos, tablas y figuras en el subdocumento
    for k, b in enumerate(bl):
        sig = next((x for x in bl[k + 1:] if x.tipo not in ('fuente', 'nota')), None)
        if b.tipo == 'titulo' and sig is not None and sig.tipo in ('titulo', 'tabla', 'figura', 'imagen'):
            que = {'titulo': 'otro título', 'tabla': 'una tabla', 'figura': 'una figura', 'imagen': 'una imagen'}[sig.tipo]
            add('E', 'titulo-seguido', b.ini, 'El título «%s» va seguido directamente de %s; agregue un texto de introducción' % (b.texto[:60], que))
        if b.tipo in ('tabla', 'figura') and not es_ia(k):
            nombre = 'tabla' if b.tipo == 'tabla' else 'figura'
            if b.tipo == 'tabla' and b.env == 'tablasintitulo':
                add('E', 'sin-titulo', b.ini, 'Tabla sin título ni fuente: use el entorno tabla con título y fuente')
            else:
                if not b.titulo:
                    add('E', 'sin-titulo', b.ini, 'La %s no tiene título' % nombre)
                if not b.fuente:
                    add('E', 'sin-titulo', b.ini, 'La %s «%s» no indica su fuente' % (nombre, b.titulo[:50]))
                if b.etiqueta and not re.search(r'\\ref\*?\{%s\}' % re.escape(b.etiqueta), cuerpo[:b.ini]):
                    add('E', 'sin-cita', b.ini, 'La %s «%s» no se cita en el texto antes de aparecer (\\ref{%s})' % (nombre, b.titulo[:50], b.etiqueta))
            if sig is None or sig.tipo not in ('texto', 'lista'):
                add('E', 'sin-explicacion', b.fin, 'Después de la %s «%s» falta el texto que la explica' % (nombre, b.titulo[:50]))
        if b.tipo == 'tabla' and not es_ia(k):
            ncol = num_columnas(b.spec)
            if ncol > 5:
                add('E', 'tabla-columnas', b.ini, 'La tabla «%s» tiene %d columnas; en el subdocumento el máximo es 5 (el detalle va al anexo)' % (b.titulo[:50], ncol))
            filas = [dividir(f, '&') for f in b.filas]
            for r, celdas in enumerate(filas):
                for c, cel in enumerate(celdas):
                    t = texto_plano(cel)
                    if t and frases(t) > 1:
                        add('E', 'celda-frases', b.cuerpo_ini + sum(len(f) + 2 for f in b.filas[:r]),
                            'Celda con más de una frase en la tabla «%s», fila %d, columna %d: «%s»' % (b.titulo[:40], r + 1, c + 1, t[:70]))
            if ncol == 2 and filas:
                col2 = [len(texto_plano(f[1]).split()) for f in filas if len(f) > 1]
                if col2 and sum(col2) / len(col2) >= 12:
                    add('A', 'concepto-descripcion', b.ini, 'La tabla «%s» parece «Concepto / Descripción»: ese contenido va como texto' % b.titulo[:50])

    # ---- capítulo técnico sin figuras
    mnum = re.search(r'\\numsubdoc\{(\d+)\}', s)
    num = int(mnum.group(1)) if mnum else None
    if num in CAPITULOS_TECNICOS and not any(b.tipo == 'figura' for b in bl):
        add('A', 'capitulo-sin-figuras', 0, 'El capítulo %d es técnico y no tiene figuras integradas' % num)

    # ---- índice obligatorio
    with open(os.path.join(AQUI, 'indice_obligatorio.json'), encoding='utf8') as f:
        indice = json.load(f)
    oficial = indice.get(str(num))
    if oficial:
        norm = lambda t: re.sub(r'\s+', ' ', t).strip()
        cont = [0, 0, 0, 0]
        hay = []        # (número, texto, posición, nivel)
        for b in bl:
            if b.tipo != 'titulo' or b.estrella or b.cmd == 'seccionsinnumero':
                continue
            lv = TITULOS[b.cmd]
            cont[lv - 1] += 1
            for x in range(lv, 4):
                cont[x] = 0
            numero = '.'.join([str(num)] + [str(c) for c in cont[1:lv]])
            hay.append((numero, norm(b.texto), b.ini, lv))
        caps = [h for h in hay if h[3] == 1]
        if not caps:
            add('E', 'indice-obligatorio', 0, 'Falta el título del capítulo: \\capitulo{%s}' % oficial['titulo'])
        else:
            if len(caps) > 1:
                add('E', 'titulo-agregado', caps[1][2], 'El subdocumento tiene más de un capítulo')
            if caps[0][1] != norm(oficial['titulo']):
                add('E', 'indice-obligatorio', caps[0][2], 'El capítulo debe llamarse «%s» (dice «%s»)' % (oficial['titulo'], caps[0][1]))
        porn = {h[0]: h for h in hay}
        portexto = {}
        for h in hay:
            portexto.setdefault(h[1].lower(), h)
        declarados = {d['num'] for d in oficial['secciones']}
        for d in oficial['secciones']:
            h = porn.get(d['num'])
            if h is not None and h[1] == norm(d['titulo']):
                continue
            otro = portexto.get(norm(d['titulo']).lower())
            if otro is not None:
                add('E', 'indice-obligatorio', otro[2], 'El título obligatorio «%s» debe ser el %s y quedó como %s (orden, nivel o numeración distinta; o mayúsculas distintas)' % (d['titulo'], d['num'], otro[0]))
            elif h is None:
                add('E', 'indice-obligatorio', 0, 'Falta el título obligatorio %s %s' % (d['num'], d['titulo']))
            else:
                add('E', 'indice-obligatorio', h[2], 'El título %s debe ser «%s» (dice «%s»)' % (d['num'], d['titulo'], h[1]))
        # títulos agregados del mismo nivel que los declarados
        niveles_decl = {}
        for d in oficial['secciones']:
            padre = d['num'].rsplit('.', 1)[0]
            niveles_decl.setdefault((padre, d['num'].count('.') + 1), set()).add(d['num'])
        textos_decl = {norm(d['titulo']).lower() for d in oficial['secciones'] if d['num'].count('.') == 1}
        for numero, texto, pos, lv in hay:
            if lv == 2 and (numero not in declarados or texto.lower() not in textos_decl):
                add('E', 'titulo-agregado', pos, 'Título agregado al nivel de los declarados: %s %s (no existe en el índice obligatorio)' % (numero, texto[:60]))
    return hz


def tablas_largas(ruta_aux, ruta_tex):
    """Tras compilar: tablas del subdoc que ocupan más de una página."""
    hz = []
    if not os.path.exists(ruta_aux):
        return hz
    with open(ruta_tex, encoding='utf8') as f:
        s = f.read()
    if not re.search(r'\\documentclass\s*\[\s*subdoc\s*\]', s):
        return hz
    aux = open(ruta_aux, encoding='utf8', errors='replace').read()
    # tablas de la Declaración de uso de IA: su forma la fija el comunicado
    cuerpo = sin_comentarios(s)
    cuerpo = cuerpo[cuerpo.find(r'\begin{document}'):]
    exentas, sec = set(), ''
    for b in bloques(cuerpo):
        if b.tipo == 'titulo' and TITULOS[b.cmd] == 1:
            sec = b.texto.lower()
        if b.tipo == 'tabla' and sec.startswith('declaración de uso de ia'):
            exentas.add(b.etiqueta)
    ini = {m.group(1): m.group(2) for m in re.finditer(r'\\newlabel\{(tab:[^}]*)\}\{\{[^}]*\}\{([^}]*)\}', aux)}
    for m in re.finditer(r'\\ov@finTabla\{([^}]*)\}\{([^}]*)\}\{([^}]*)\}', aux):
        lab, fin, ia = m.group(1), m.group(2), m.group(3)
        if lab in exentas or lab not in ini:
            continue
        try:
            if int(fin) > int(ini[lab]):
                pos = s.find('{%s}' % lab)
                hz.append(Hallazgo('E', 'tabla-pagina', s.count('\n', 0, max(pos, 0)) + 1,
                                   'La tabla «%s» ocupa %d páginas; en el subdocumento no debe pasar de una (el listado completo va al anexo)' % (lab, int(fin) - int(ini[lab]) + 1)))
        except ValueError:
            pass
    return hz
