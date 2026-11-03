# -*- coding: utf-8 -*-
"""Revisa, en los PDF ya compilados, que las tablas y figuras citadas existan y que el índice
esté al día con el documento.

uso (desde la carpeta latex/, después de compilar):
  python herramientas/revisar_referencias.py              todos los PDF de salida/
  python herramientas/revisar_referencias.py S4 T-14      sólo esos documentos
  python herramientas/revisar_referencias.py --md archivo.md   además escribe la lista en Markdown

Qué revisa en cada documento:
  1. Citas en el texto: toda «Tabla 4.3», «Figura 5.1» o «Tablas 4.8 a 4.15» apunta a una tabla o
     figura que existe. Si el número es de otro capítulo (Figura 3.6 dentro del Subdocumento 4)
     se busca en ese subdocumento; si el texto dice «del Formulario T-14» o «de los Anexos del
     Subdocumento 2», en ese documento.
  2. Listado de Tablas y Listado de Figuras: cada entrada existe en el documento, con el mismo
     título y el mismo folio; toda tabla o figura del documento aparece en el listado.
  3. Índice: cada título del índice está en el documento y en el folio indicado.
  4. Numeración: sin saltos ni números repetidos.
  5. Diagramas draw.io del repositorio (figuras/drawio/): los números de tabla o figura escritos
     dentro del dibujo existen. El texto de una imagen PNG no se puede leer desde el PDF, así que
     una figura sin su draw.io en el repositorio no se revisa por dentro.
"""
import glob, html, os, re, sys, unicodedata
import xml.etree.ElementTree as ET

import pymupdf

AQUI = os.path.dirname(os.path.abspath(__file__))
LATEX = os.path.dirname(AQUI)
SALIDA = os.path.join(LATEX, 'salida')
NUM = r'(?:[A-Z]\.\d+|\d+\.\d+)'
LIDER = r'(?:\s*\.){2,}\s*(\d+)'


def documento(pdf):
    m = re.search(r'Formulario-(T-\d+)|Subdocumento(\d+)(-Anexos)?', os.path.basename(pdf))
    if not m:
        return os.path.basename(pdf)[:-4]
    return m.group(1) or 'S%s%s' % (m.group(2), ' anexos' if m.group(3) else '')


def clave_doc(d):
    m = re.match(r'(S|T-)(\d+)', d)
    return (0 if d.startswith('S') else 1, int(m.group(2)) if m else 99, d)


def norm(t):
    t = unicodedata.normalize('NFKD', t)
    t = ''.join(c for c in t if not unicodedata.combining(c)).lower()
    return re.sub(r'[^a-z0-9]+', ' ', t).strip()


def unir(t):
    """une palabras cortadas al final de línea y junta las líneas"""
    t = re.sub(r'(\w)-\n(\w)', r'\1\2', t)
    return re.sub(r'\s+', ' ', t)


class Doc:
    def __init__(self, pdf):
        self.nombre = documento(pdf)
        self.paginas = []           # (folio, texto, es_indice)
        d = pymupdf.open(pdf)
        for p in d:
            t = p.get_text()
            f = re.search(r'Folio\s+(\d+)', t)
            indice = bool(re.search(LIDER + r'\s*$', t, re.M)) or bool(re.search(r'^(Índice|Listado de (Tablas|Figuras))\s*$', t, re.M))
            self.paginas.append((f.group(1) if f else '?', t, indice))
        self.captions = {}          # ('Tabla','4.3') -> (folio, título)
        self.repetidos = []
        for folio, t, ind in self.paginas:
            if ind:
                continue
            lineas = t.split('\n')
            for i, l in enumerate(lineas):
                m = re.match(r'^(Figura|Tabla)\s+(%s)\s+—\s+(.*)$' % NUM, l.strip())
                if m:
                    tit = (m.group(3) + ' ' + ' '.join(lineas[i + 1:i + 3])).strip()
                    k = (m.group(1), m.group(2))
                    if k in self.captions:
                        self.repetidos.append(k)
                    else:
                        self.captions[k] = (folio, tit)
        # listados e índice
        texto_ind = '\n'.join(t for f, t, ind in self.paginas if ind)
        texto_ind = re.sub(r'^(OVERFORE S\.A\. · Licitación.*|Media firma · Representante Legal|Folio \d+)$', '', texto_ind,
                           flags=re.M)        # encabezado y pie de página cortan las entradas del índice
        texto_ind = unir(texto_ind)
        self.listado = {}
        for m in re.finditer(r'(Figura|Tabla)\s+(%s)\s+—\s+(.*?)(?:\s*\.)+\s*(\d+)\s*(?=(?:Figura|Tabla)\s+%s\s+—|Listado|$)' % (NUM, NUM), texto_ind):
            self.listado[(m.group(1), m.group(2))] = (m.group(4), m.group(3))
        sin_listados = re.split(r'Listado de (?:Tablas|Figuras)', texto_ind)[0]
        self.toc = []
        for m in re.finditer(r'(?:^|\s)((?:Capítulo \d+ — )|(?:\d+(?:\.\d+)+)\s)\s*(.*?)%s' % LIDER, sin_listados):
            self.toc.append((m.group(1).strip(), m.group(2).strip(), m.group(3)))

    def cuerpo(self):
        return [(f, t) for f, t, ind in self.paginas if not ind]


def expandir(prefijo_lista):
    """«4.8 a 4.15» → 4.8 … 4.15 ; «4.2, 4.3 y 4.5» → cada uno"""
    nums = re.findall(NUM + r'|\ba\b|–', prefijo_lista)
    out = []
    i = 0
    while i < len(nums):
        n = nums[i]
        if n in ('a', '–') and out and i + 1 < len(nums):
            ini, fin = out[-1], nums[i + 1]
            p1, a = ini.split('.')
            p2, b = fin.split('.')
            if p1 == p2 and a.isdigit() and b.isdigit():
                out += ['%s.%d' % (p1, k) for k in range(int(a) + 1, int(b) + 1)]
            else:
                out.append(fin)
            i += 2
            continue
        if n not in ('a', '–'):
            out.append(n)
        i += 1
    return out


# formularios que acompañan a cada subdocumento (Formulario T-21 de las Bases administrativas)
FORM_DE = {1: [6], 3: [12], 4: [11], 6: [9, 10], 7: [14, 15, 18], 8: [16], 9: [13, 17], 12: [8], 13: [19]}


def subdoc_de(nombre):
    if nombre.startswith('S'):
        return int(re.match(r'S(\d+)', nombre).group(1))
    t = int(nombre[2:])
    return next((s for s, fs in FORM_DE.items() if t in fs), None)


DOC_DESPUES = re.compile(r'\s*(?:,\s*)?(?:del Anexo [A-Z]\s+)?(?:del?|de los|de las|en el|en la)\s+'
                         r'(?:OVERFORE-)?(?:Formulario[\s-]+(T-\d+)|(?:[Aa]nexos? del )?Subdocumento[\s]*(\d+)(-Anexos)?)')
DOC_ANTES = re.compile(r'(?:Formulario[\s-]+(T-\d+)|Subdoc(?:umento|\.)\s*(\d+)(?:[^;()]{0,40}?(Anexos?))?)(?:(?!\.\s)[^;]){0,45}$')


def destinos(nombre, numero, contexto, antes=''):
    """documentos donde puede estar la tabla o figura citada, en orden de preferencia"""
    pref = numero.split('.')[0]
    m = DOC_DESPUES.match(contexto)
    if m:
        if m.group(1):
            return [m.group(1)]
        anexos = m.group(3) or re.match(r'\s*(?:,\s*)?(?:del Anexo|de los Anexos|del anexo|de los anexos)', contexto) or pref.isalpha()
        return ['S%s%s' % (m.group(2), ' anexos' if anexos else '')]
    previos = []
    m = DOC_ANTES.search(antes)
    if m and pref.isalpha():
        previos = [m.group(1)] if m.group(1) else ['S%s anexos' % m.group(2), 'S%s' % m.group(2)]
    if pref.isdigit():
        return previos + ['S' + pref]           # número con dígito: cuerpo del subdocumento de ese capítulo
    # número con letra: el propio documento, sus anexos o los formularios del mismo subdocumento
    s = subdoc_de(nombre)
    cand = previos + [nombre]
    if s:
        cand += ['S%d anexos' % s] + ['T-%d' % t for t in FORM_DE.get(s, [])] + ['S%d' % s]
    return cand


def no_existe(todos, tipo, numero, candidatos):
    """'' si la tabla o figura está en algún candidato compilado; si no, los documentos revisados"""
    revisados = [c for c in candidatos if c in todos]
    if not revisados or any((tipo, numero) in todos[c].captions for c in revisados):
        return ''
    return ', '.join(revisados)


def revisar(docs, todos):
    hallazgos = {}

    def add(doc, tipo, folio, msg):
        hallazgos.setdefault(doc, []).append((tipo, folio, msg))

    for d in docs:
        # 1. citas en el texto
        for folio, t in d.cuerpo():
            plano = unir(t)
            for m in re.finditer(r'\b(Tablas?|Figuras?)~?\s+(%s(?:\s*(?:,|y|a|–)\s*%s)*)' % (NUM, NUM), plano):
                tipo = 'Tabla' if m.group(1).startswith('Tabla') else 'Figura'
                ini = plano.rfind('\n', 0, m.start())
                if re.match(r'^\s*(Figura|Tabla)\s+%s\s+—' % NUM, plano[m.start():m.start() + 40]):
                    continue                              # es el título de la propia tabla o figura
                contexto = plano[m.end():m.end() + 90]
                antes = plano[max(0, m.start() - 90):m.start()]
                for n in expandir(m.group(2)):
                    falta = no_existe(todos, tipo, n, destinos(d.nombre, n, contexto, antes))
                    if falta:
                        add(d.nombre, 'cita', folio, 'cita %s %s, que no existe (buscada en %s)' % (tipo, n, falta))
        # 2. listados
        for k, (folio, tit) in sorted(d.listado.items()):
            if k not in d.captions:
                add(d.nombre, 'listado', folio, '%s %s está en el listado y no en el documento' % k)
                continue
            f2, t2 = d.captions[k]
            if f2 != folio:
                add(d.nombre, 'listado', folio, '%s %s: el listado dice folio %s y está en el %s' % (k[0], k[1], folio, f2))
            if not norm(t2).startswith(norm(tit)[:35]):
                add(d.nombre, 'listado', folio, '%s %s: título distinto en el listado («%s»)' % (k[0], k[1], tit[:60]))
        if d.listado:
            for k, (f2, t2) in sorted(d.captions.items()):
                if k not in d.listado:
                    add(d.nombre, 'listado', f2, '%s %s no aparece en el listado' % k)
        # 3. índice
        cuerpo = [(f, unir(t)) for f, t in d.cuerpo()]
        for num, tit, folio in d.toc:
            clave = norm(tit)[:30]
            num_n = num if not num.startswith('Capítulo') else ''
            hall = [f for f, t in cuerpo if clave and clave in norm(t) and (not num_n or (num_n + ' ') in t)]
            if not hall:
                add(d.nombre, 'índice', folio, 'el índice trae «%s %s» y no se encuentra en el documento' % (num, tit[:50]))
            elif folio not in hall:
                add(d.nombre, 'índice', folio, '«%s %s»: el índice dice folio %s y está en el %s' % (num, tit[:50], folio, hall[0]))
        # 4. numeración
        for k in d.repetidos:
            add(d.nombre, 'numeración', d.captions[k][0], '%s %s aparece dos veces' % k)
        for tipo in ('Tabla', 'Figura'):
            por_pref = {}
            for (t_, n) in d.captions:
                if t_ == tipo:
                    p, i = n.split('.')
                    por_pref.setdefault(p, set()).add(int(i))
            for p, s in por_pref.items():
                faltan = sorted(set(range(1, max(s) + 1)) - s)
                if faltan:
                    add(d.nombre, 'numeración', '', '%s %s: falta %s' % (tipo, p, ', '.join('%s.%d' % (p, i) for i in faltan)))
    # 5. draw.io del repositorio
    for xml in sorted(glob.glob(os.path.join(LATEX, '**', 'figuras', 'drawio', '*.drawio.xml'), recursive=True)):
        rel = os.path.relpath(xml, LATEX)
        m = re.search(r'subdoc(\d+)[\\/](subdocumento|anexos|formulario-(T-\d+))', rel)
        if not m:
            continue
        doc = m.group(3).replace('T-0', 'T-') if m.group(3) else 'S%d%s' % (int(m.group(1)), ' anexos' if m.group(2) == 'anexos' else '')
        if doc not in todos:
            continue
        try:
            raiz = ET.parse(xml).getroot()
        except ET.ParseError:
            continue
        texto = ' '.join(html.unescape(re.sub(r'<[^>]+>', ' ', c.get('value') or '')) for c in raiz.iter('mxCell'))
        for mm in re.finditer(r'\b(Tablas?|Figuras?)\s+(%s(?:\s*(?:,|y|a|–)\s*%s)*)' % (NUM, NUM), texto):
            tipo = 'Tabla' if mm.group(1).startswith('Tabla') else 'Figura'
            for n in expandir(mm.group(2)):
                falta = no_existe(todos, tipo, n, destinos(doc, n, texto[mm.end():mm.end() + 90], texto[max(0, mm.start() - 90):mm.start()]))
                if falta:
                    add(doc, 'dibujo', '', '%s nombra %s %s, que no existe (buscada en %s)' % (os.path.basename(xml), tipo, n, falta))
    return hallazgos


def main():
    args = sys.argv[1:]
    md = args[args.index('--md') + 1] if '--md' in args else None
    filtro = {a for a in args if not a.startswith('--') and a != md}
    pdfs = sorted(glob.glob(os.path.join(SALIDA, '*.pdf')))
    if not pdfs:
        sys.exit('No hay PDF en %s; compila primero.' % SALIDA)
    todos = {}
    for f in pdfs:
        d = Doc(f)
        todos[d.nombre] = d
    pedidos = [d for n, d in sorted(todos.items(), key=lambda x: clave_doc(x[0]))
               if not filtro or n in filtro or n.split()[0] in filtro]
    hallazgos = revisar(pedidos, todos)
    filas = []
    for d in pedidos:
        hs = hallazgos.get(d.nombre, [])
        n_t = sum(1 for k in d.captions if k[0] == 'Tabla')
        n_f = sum(1 for k in d.captions if k[0] == 'Figura')
        print('\n%s  (%d tablas, %d figuras)%s' % (d.nombre, n_t, n_f, '  sin problemas' if not hs else ''))
        orden = {'cita': 0, 'listado': 1, 'índice': 2, 'numeración': 3, 'dibujo': 4}
        for tipo, folio, msg in sorted(hs, key=lambda h: (orden[h[0]], int(h[1]) if str(h[1]).isdigit() else 0)):
            print('  %-11s folio %-5s %s' % (tipo, folio or '—', msg))
            filas.append((d.nombre, tipo, folio or '—', msg))
    total = sum(len(v) for v in hallazgos.values())
    print('\n%d problemas en %d de %d documentos.' % (total, len(hallazgos), len(pedidos)))
    if md:
        with open(md, 'w', encoding='utf-8') as out:
            out.write('# Referencias a tablas y figuras\n\nRevisión de `herramientas/revisar_referencias.py` '
                      'sobre los PDF de `salida/`.\n\n| Doc | Tipo | Folio | Problema |\n|---|---|---|---|\n')
            for fila in filas:
                out.write('| %s | %s | %s | %s |\n' % fila)
        print('Lista escrita en', md)
    return 1 if total else 0


if __name__ == '__main__':
    sys.exit(main())
