# -*- coding: utf-8 -*-
"""Convierte los .docx antiguos de OVERFORE a LaTeX con la clase overfore.

Fase 1: lee todos los documentos, detecta títulos, tablas, figuras y sus números
antiguos, y calcula el número nuevo que les dará la clase.
Fase 2: escribe cada .tex, reescribiendo las referencias con la tabla de
equivalencias global, y copia las imágenes con nombres ordenados.
"""
import os, re, sys, shutil, json, unicodedata, collections
from lxml import etree

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
M = '{http://schemas.openxmlformats.org/officeDocument/2006/math}'
A = '{http://schemas.openxmlformats.org/drawingml/2006/main}'
WP = '{http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing}'
R = '{http://schemas.openxmlformats.org/officeDocument/2006/relationships}'
PR = '{http://schemas.openxmlformats.org/package/2006/relationships}'

OLD = sys.argv[1]          # carpeta con los docx descomprimidos
OUT = sys.argv[2]          # carpeta latex/
REPORT = sys.argv[3]       # archivo de informe (markdown)

# --------------------------------------------------------------------------- catálogo de documentos
FORM_DE = {1: [6], 3: [12], 4: [11], 6: [9, 10], 7: [14, 15, 18], 8: [16], 9: [13, 17], 12: [8], 13: [19]}

def catalogo():
    docs = []
    for n in range(1, 15):
        s = 'OVERFORE-Subdocumento%d' % n
        if os.path.isdir(os.path.join(OLD, s)):
            docs.append(dict(key='S%d' % n, src=s, modo='subdoc', sub=n,
                             carpeta='subdoc%02d/subdocumento' % n, nombre=s))
        a = s + '-Anexos'
        if os.path.isdir(os.path.join(OLD, a)):
            docs.append(dict(key='A%d' % n, src=a, modo='anexo', sub=n,
                             carpeta='subdoc%02d/anexos' % n, nombre=a))
        for t in sorted(FORM_DE.get(n, [])):
            f = 'OVERFORE-Formulario-T-%d' % t
            if os.path.isdir(os.path.join(OLD, f)):
                docs.append(dict(key='T%d' % t, src=f, modo='formulario', sub=n, form=t,
                                 carpeta='subdoc%02d/formulario-T-%02d' % (n, t), nombre=f))
    return docs

# --------------------------------------------------------------------------- utilidades
def txt(e):
    out = []
    for x in e.iter():
        if x.tag == W + 't' and x.text:
            out.append(x.text)
        elif x.tag == W + 'tab':
            out.append(' ')
        elif x.tag == M + 't' and x.text:
            out.append(x.text)
    return ''.join(out)

def slug(s, n=6):
    s = unicodedata.normalize('NFKD', s).encode('ascii', 'ignore').decode().lower()
    s = re.sub(r'[^a-z0-9]+', ' ', s).split()
    stop = {'de', 'del', 'la', 'el', 'los', 'las', 'y', 'en', 'a', 'por', 'con', 'para', 'su', 'sus', 'un', 'una', 'que', 'o', 'e', 'al'}
    s = [w for w in s if w not in stop]
    return '-'.join(s[:n]) or 'x'

ESC = {'\\': r'\textbackslash{}', '{': r'\{', '}': r'\}', '#': r'\#', '$': r'\$', '%': r'\%',
       '&': r'\&', '_': r'\_', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}',
       '\u00a0': '~', '\u2011': '-', '\u200b': '', '\u00ad': '', '\t': ' '}
def esc(s):
    return ''.join(ESC.get(c, c) for c in s)

# --------------------------------------------------------------------------- lectura de un docx
class Doc:
    def __init__(self, info):
        self.__dict__.update(info)
        d = os.path.join(OLD, info['src'])
        self.dir = d
        self.root = etree.parse(os.path.join(d, 'word', 'document.xml')).getroot()
        st = etree.parse(os.path.join(d, 'word', 'styles.xml')).getroot()
        self.stylename = {}
        for s in st.findall(W + 'style'):
            n = s.find(W + 'name')
            if n is not None:
                self.stylename[s.get(W + 'styleId')] = n.get(W + 'val').lower()
        self.rels = {}
        rp = os.path.join(d, 'word', '_rels', 'document.xml.rels')
        for r in etree.parse(rp).getroot():
            self.rels[r.get('Id')] = (r.get('Target'), r.get('TargetMode'))
        self.numfmt = {}
        np_ = os.path.join(d, 'word', 'numbering.xml')
        if os.path.exists(np_):
            nr = etree.parse(np_).getroot()
            absf = {}
            for a in nr.findall(W + 'abstractNum'):
                lv = {}
                for l in a.findall(W + 'lvl'):
                    f = l.find(W + 'numFmt')
                    lv[l.get(W + 'ilvl')] = f.get(W + 'val') if f is not None else 'bullet'
                absf[a.get(W + 'abstractNumId')] = lv
            for n in nr.findall(W + 'num'):
                an = n.find(W + 'abstractNumId').get(W + 'val')
                self.numfmt[n.get(W + 'numId')] = absf.get(an, {})
        self.items = []        # tablas/figuras/títulos con números antiguos y nuevos
        self.labels = set()
        self.avisos = []

    def style(self, p):
        ps = p.find(W + 'pPr/' + W + 'pStyle')
        return self.stylename.get(ps.get(W + 'val'), '') if ps is not None else ''

# --------------------------------------------------------------------------- bloques
def bloques(doc):
    """Aplana el cuerpo (abre los controles de contenido) y marca la orientación de cada bloque."""
    body = doc.root.find(W + 'body')
    out = []
    def walk(parent):
        for el in parent:
            if el.tag == W + 'sdt':
                c = el.find(W + 'sdtContent')
                if c is not None:
                    walk(c)
            elif el.tag in (W + 'p', W + 'tbl'):
                out.append(el)
    walk(body)
    # orientación: cada sectPr cierra una sección
    orient = []
    pend = []
    def sect_orient(sp):
        pg = sp.find(W + 'pgSz')
        if pg is None:
            return 'v'
        w, h = int(float(pg.get(W + 'w', 12240))), int(float(pg.get(W + 'h', 15840)))
        return 'h' if w > h else 'v'
    for el in out:
        pend.append(el)
        sp = el.find(W + 'pPr/' + W + 'sectPr') if el.tag == W + 'p' else None
        if sp is not None:
            o = sect_orient(sp)
            orient += [o] * len(pend)
            pend = []
    fin = body.find(W + 'sectPr')
    o = sect_orient(fin) if fin is not None else 'v'
    orient += [o] * len(pend)
    return list(zip(out, orient))

def tamano(p):
    for r in p.iter(W + 'r'):
        if txt(r).strip():
            sz = r.find(W + 'rPr/' + W + 'sz')
            if sz is not None:
                return int(float(sz.get(W + 'val')))
            return None
    return None

def tiene_imagen(p):
    return p.find('.//' + A + 'blip') is not None

CAP_RX = re.compile(r'^\s*(Tabla|Figura|Ilustraci[oó]n)\s+(T-\d+\.\d+|\d+\.[A-Z]\.\d+|[A-Z]\.\d+[a-z]?|\d+(?:\.\d+)?[a-z]?)\s*\.?\s*(?:[—–\-:]\s*)?(.*)$', re.S)
SKIP_TIT = {'índice', 'indice', 'listado de tablas', 'listado de figuras', 'listado de ilustraciones'}

def es_titulo(doc, p):
    t = txt(p).strip()
    if not t or len(t) > 180:
        return False
    if p.getparent().tag == W + 'tc':
        return False
    st = doc.style(p)
    if st.startswith('heading'):
        return not CAP_RX.match(t) and not t.startswith('Fuente')
    sz = tamano(p)
    if sz and sz >= 26 and not CAP_RX.match(t):
        return True
    return False

def nivel_estilo(doc, p):
    st = doc.style(p)
    m = re.match(r'heading (\d)', st)
    if m:
        return int(m.group(1))
    sz = tamano(p) or 22
    return 1 if sz >= 34 else 2 if sz >= 27 else 3

# --------------------------------------------------------------------------- fase 1: estructura y números
NUM_RX = re.compile(r'^((?:[A-Z]|\d+)(?:\.\d+)*)(\.)?\s+(.+)$', re.S)

def analizar(doc):
    bl = bloques(doc)
    # inicio del contenido: primer título después del último índice o listado antiguo
    desde = 0
    for i, (el, o) in enumerate(bl):
        instr = ''.join(x.text or '' for x in el.iter(W + 'instrText'))
        t0 = txt(el).strip().lower() if el.tag == W + 'p' else ''
        if 'TOC' in instr or t0 in SKIP_TIT or t0.startswith('listado de') or t0.startswith('este formulario no incluye'):
            desde = i + 1
    start = None
    for i, (el, o) in enumerate(bl):
        if i < desde:
            continue
        if el.tag == W + 'p' and es_titulo(doc, el):
            t = txt(el).strip().lower()
            if t in SKIP_TIT or t.startswith('listado de'):
                continue
            if any(a.tag == W + 'tc' for a in el.iterancestors()):
                continue
            start = i
            break
    if start is None:
        doc.avisos.append('No se encontró el inicio del contenido')
        start = 0
    bl = bl[start:]
    doc.bl = bl
    # títulos
    tit = []
    for i, (el, o) in enumerate(bl):
        if el.tag == W + 'p' and es_titulo(doc, el):
            t = re.sub(r'\s+', ' ', txt(el)).strip()
            if t.lower() in SKIP_TIT:
                continue
            tit.append((i, t, nivel_estilo(doc, el)))
    # niveles y números
    base = None
    if doc.modo == 'formulario':
        depths = []
        for i, t, ln in tit:
            m = NUM_RX.match(t)
            if m and not re.match(r'^(Referencias|Declaraci)', t):
                depths.append(m.group(1).count('.') + 1)
        base = min(depths) if depths else 1
    cont = [0, 0, 0, 0, 0]
    doc.titulos = {}
    secmap = {}
    for i, t, ln in tit:
        kind = None; numviejo = None; texto = t; nivel = None
        if doc.modo == 'subdoc':
            m = re.match(r'^Cap[ií]tulo\s+(\d+)\s*[•·\.\-—:]?\s*(.*)$', t)
            if m:
                nivel = 1; numviejo = m.group(1); texto = m.group(2)
            else:
                m = NUM_RX.match(t)
                if m and re.match(r'^\d+(\.\d+)+$', m.group(1)):
                    numviejo = m.group(1); nivel = numviejo.count('.') + 1; texto = m.group(3)
        elif doc.modo == 'anexo':
            m = re.match(r'^Anexo\s+([A-Z])\s*[—–\-:\.]\s*(.*)$', t)
            if m:
                nivel = 1; numviejo = m.group(1); texto = m.group(2)
            else:
                m = NUM_RX.match(t)
                if m and re.match(r'^[A-Z](\.\d+)+$', m.group(1)):
                    numviejo = m.group(1); nivel = numviejo.count('.') + 1; texto = m.group(3)
        else:
            m = NUM_RX.match(t)
            if m and not re.match(r'^(Referencias|Declaraci)', t):
                numviejo = m.group(1)
                nivel = numviejo.count('.') + 1 - (base - 1)
                if re.match(r'^[A-Z]', numviejo):
                    nivel = numviejo.count('.') + 1
                texto = m.group(3)
                if nivel < 1:
                    nivel = 1
        texto = texto.strip().strip('—–-').strip()
        if nivel is None:
            # sin número
            if ln <= 1 or re.match(r'^(Referencias|Declaraci[oó]n de uso de IA|Anexos del Subdocumento)', t):
                if doc.modo == 'formulario' and not re.match(r'^(Referencias|Declaraci)', t):
                    nivel = 1; kind = 'num'
                else:
                    nivel = 1; kind = 'sinnum'
            else:
                nivel = min(ln, 4); kind = 'estrella'
        else:
            kind = 'num'
        nuevo = None
        if kind == 'num':
            cont[nivel - 1] += 1
            for k in range(nivel, 5):
                cont[k] = 0
            if doc.modo == 'subdoc':
                partes = [str(doc.sub)] + [str(c) for c in cont[1:nivel]]
            else:
                partes = [chr(64 + cont[0])] + [str(c) for c in cont[1:nivel]]
            nuevo = '.'.join(partes)
            if numviejo and numviejo != nuevo:
                secmap[numviejo] = nuevo
                if doc.modo != 'formulario':
                    doc.avisos.append('Título "%s %s" queda numerado %s' % (numviejo, texto[:50], nuevo))
        doc.titulos[i] = dict(kind=kind, nivel=nivel, texto=texto, viejo=numviejo, nuevo=nuevo)
    doc.secmap = secmap
    # tablas, figuras, títulos de tabla y fuentes
    analizar_objetos(doc)

def analizar_objetos(doc):
    bl = doc.bl
    n = len(bl)
    doc.cap_de = {}       # índice de tabla/imagen -> índice del párrafo de título
    doc.usados = set()    # párrafos absorbidos (título, fuente, nota)
    doc.fuente_de = {}
    doc.nota_de = {}
    def sig(i, paso=1):
        j = i + paso
        while 0 <= j < n:
            el = bl[j][0]
            if el.tag == W + 'p' and not txt(el).strip() and not tiene_imagen(el) and el.find('.//' + M + 'oMath') is None:
                j += paso; continue
            return j
        return None
    for i, (el, o) in enumerate(bl):
        if el.tag != W + 'p' or i in doc.titulos:
            continue
        t = txt(el).strip()
        m = CAP_RX.match(t)
        if not m:
            continue
        label = m.group(1)
        st = doc.style(el)
        resto = m.group(3).strip()
        if not (st.startswith('heading') or 'caption' in st or re.match(r'^\s*\S+\s+\S+\s*\.?\s*[—–]', t) or re.match(r'^\s*\S+\s+\S+\.\s', t)):
            continue
        if label == 'Tabla':
            j = sig(i)
            k = sig(i, -1)
            if j is not None and bl[j][0].tag == W + 'tbl':
                doc.cap_de[j] = i
            elif k is not None and bl[k][0].tag == W + 'tbl' and k not in doc.cap_de:
                doc.cap_de[k] = i
            else:
                continue
        else:
            k = sig(i, -1)
            j = sig(i)
            if k is not None and bl[k][0].tag == W + 'p' and tiene_imagen(bl[k][0]) and k not in doc.cap_de:
                doc.cap_de[k] = i
            elif j is not None and bl[j][0].tag == W + 'p' and tiene_imagen(bl[j][0]):
                doc.cap_de[j] = i
            else:
                continue
        doc.usados.add(i)
    # fuentes y notas tras cada objeto (o tras su título si el título va después)
    for obj, capi in doc.cap_de.items():
        last = max(obj, capi)
        j = sig(last)
        for _ in range(3):
            if j is None:
                break
            el = bl[j][0]
            if el.tag != W + 'p':
                break
            t = txt(el).strip()
            if re.match(r'^Nota[\.:]', t) and obj not in doc.nota_de:
                doc.nota_de[obj] = j; doc.usados.add(j); j = sig(j); continue
            if re.match(r'^Fuentes?\s*:', t):
                doc.fuente_de[obj] = j; doc.usados.add(j)
            break
    # números nuevos de tablas y figuras, en orden del documento
    sec = None
    ctab = collections.Counter(); cfig = collections.Counter()
    doc.objnum = {}
    for i, (el, o) in enumerate(bl):
        if i in doc.titulos and doc.titulos[i]['kind'] == 'num' and doc.titulos[i]['nivel'] == 1:
            sec = doc.titulos[i]['nuevo']
        if i in doc.cap_de:
            capi = doc.cap_de[i]
            t = txt(bl[capi][0]).strip()
            m = CAP_RX.match(t)
            kind = 'Tabla' if el.tag == W + 'tbl' else 'Figura'
            if doc.modo == 'subdoc':
                pref = str(doc.sub)
            else:
                pref = sec
            cnt = ctab if kind == 'Tabla' else cfig
            cnt[pref] += 1
            nuevo = ('%s.%d' % (pref, cnt[pref])) if pref else str(cnt[pref])
            texto = m.group(3).strip()
            fuente_inline = None
            fm = re.search(r'\s*Fuentes?\s*:\s*(.+)$', texto)
            if fm:
                fuente_inline = 'Fuente: ' + fm.group(1).strip()
                texto = texto[:fm.start()].strip()
            texto = texto.lstrip('—–-.: ').strip()
            lab = ('tab:' if kind == 'Tabla' else 'fig:') + slug(texto)
            base = lab; k = 2
            while lab in doc.labels:
                lab = '%s-%d' % (base, k); k += 1
            doc.labels.add(lab)
            item = dict(tipo=kind, viejo=m.group(2), nuevo=nuevo, label=lab, texto=texto,
                        fuente_inline=fuente_inline, bloque=i)
            doc.items.append(item)
            doc.objnum[i] = item

# --------------------------------------------------------------------------- registro global de referencias
class Registro:
    def __init__(self, docs):
        self.docs = {d.key: d for d in docs}
        self.por_doc = {}
        for d in docs:
            m = {}
            for it in d.items:
                m.setdefault((it['tipo'], it['viejo']), it)
            self.por_doc[d.key] = m
        self.cambios = []      # (doc, antes, después)
        self.dudas = []

    def buscar(self, key, tipo, viejo):
        return self.por_doc.get(key, {}).get((tipo, viejo))

REF_NUM = r'(?:T-\d+\.\d+|\d+\.[A-Z]\.\d+|[A-Z]\.\d+[a-z]?|\d+\.\d+[a-z]?|\d+)'
REF_RX = re.compile(r'\b(?P<kw>[Tt]ablas?|[Ff]iguras?|[Ii]lustraci(?:ón|ones))\s+(?P<lista>' + REF_NUM +
                    r'(?:\s*(?:,|y|e|a|al|o)\s+' + REF_NUM + r')*)(?P<qual>\s+(?:del?|de\s+los|de\s+la)\s+(?:Anexos?\s+(?:[A-Z]\s+)?del\s+Subdocumento\s+\d+|Anexo\s+[A-Z](?:\s+del\s+Subdocumento\s+\d+)?|Formulario\s+T-\d+|Subdocumento\s+\d+))?')
ANEXO_RX = re.compile(r'\b(?P<kw>Anexos?)\s+(?P<n>\d+)\.(?P<l>[A-Z])(?P<rest>(?:\s*(?:,|y|a|e)\s+\d+\.[A-Z])*)')
FORMSEC_RX = re.compile(r'\b(?P<pre>Formulario\s+T-(?P<t>\d+),?\s+(?:secci[oó]n\s+|apartado\s+)?)(?P<n>\d+(?:\.\d+)*)\b')
OWNSEC_RX = re.compile(r'\b(?P<kw>secci[oó]n|apartado)\s+(?P<n>\d+(?:\.\d+)*)\b(?!\s*,\s*p\.)(?![\.\d])')

def resolver(reg, cur, tipo, num, qual, contexto):
    """Devuelve (doc_key, item) o (None, None)."""
    tipo = 'Figura' if tipo.lower().startswith(('fig', 'ilu')) else 'Tabla'
    q = qual or ''
    mq = re.search(r'Formulario\s+T-(\d+)', q)
    if mq:
        key = 'T' + mq.group(1)
        it = reg.buscar(key, tipo, num)
        mt = re.match(r'^T-\d+\.(\d+)$', num)
        if it is None and mt:
            it = reg.buscar(key, tipo, mt.group(1))
        return (key, it) if it else (None, None)
    mq = re.search(r'Subdocumento\s+(\d+)', q)
    qsub = int(mq.group(1)) if mq else None
    m = re.match(r'^T-(\d+)\.(\d+)$', num)
    if m:
        key = 'T' + m.group(1)
        # algunos formularios numeraban "Tabla 3" pero se citaban como "Tabla T-13.3"
        it = reg.buscar(key, tipo, num) or reg.buscar(key, tipo, m.group(2))
        return (key, it) if it else (None, None)
    m = re.match(r'^(\d+)\.([A-Z])\.(\d+)$', num)
    if m:
        key = 'A' + m.group(1)
        return key, reg.buscar(key, tipo, '%s.%s' % (m.group(2), m.group(3)))
    m = re.match(r'^(\d+)\.\d+[a-z]?$', num)
    if m:
        key = 'S' + m.group(1)
        it = reg.buscar(key, tipo, num)
        if it:
            return key, it
        # el anexo del subdocumento a veces usa la numeración del capítulo
        return None, None
    m = re.match(r'^[A-Z]\.\d+[a-z]?$', num)
    if m:
        cands = []
        if qsub:
            cands.append('A%d' % qsub)
        elif 'Anexo' in q:
            if cur.modo == 'subdoc':
                cands.append('A%d' % cur.sub)
            elif cur.modo == 'anexo':
                cands.append(cur.key)
        else:
            if cur.modo == 'anexo':
                cands.append(cur.key)
            elif cur.modo == 'subdoc':
                cands.append('A%d' % cur.sub)
            else:
                cands.append(cur.key)
                ms = re.findall(r'Subdocumento\s+(\d+)', contexto)
                if ms:
                    cands.append('A%s' % ms[-1])
        for key in cands:
            it = reg.buscar(key, tipo, num)
            if it:
                return key, it
        return None, None
    if re.match(r'^\d+$', num):
        # "Tabla 8" citada desde otro documento: el formulario nombrado antes en la frase
        mf = re.findall(r'Formulario\s+T-(\d+)', contexto[-160:])
        if mf and cur.modo != 'formulario':
            key = 'T' + mf[-1]
            it = reg.buscar(key, tipo, num)
            if it:
                return key, it
        if cur.modo == 'formulario':
            it = reg.buscar(cur.key, tipo, num)
            if it:
                return cur.key, it
        if cur.modo in ('anexo',):
            it = reg.buscar(cur.key, tipo, num)
            if it:
                return cur.key, it
        return None, None
    return None, None

def reescribir(reg, cur, texto):
    """Devuelve una lista de piezas ('t', texto) o ('r', latex) con las referencias renumeradas."""
    piezas = []
    pos = 0
    hits = []
    for m in REF_RX.finditer(texto):
        hits.append(('obj', m))
    for m in ANEXO_RX.finditer(texto):
        hits.append(('anx', m))
    if cur.modo == 'formulario' or True:
        for m in FORMSEC_RX.finditer(texto):
            hits.append(('fsec', m))
    if cur.modo == 'formulario' and cur.secmap:
        for m in OWNSEC_RX.finditer(texto):
            hits.append(('osec', m))
    hits.sort(key=lambda h: (h[1].start(), -h[1].end()))
    usados_hasta = -1
    for kind, m in hits:
        if m.start() < usados_hasta:
            continue
        rep = None
        if kind == 'obj':
            rep = reemplazo_obj(reg, cur, m, texto)
        elif kind == 'anx':
            rep = reemplazo_anexo(reg, cur, m)
        elif kind == 'fsec':
            d = reg.docs.get('T' + m.group('t'))
            if d is not None and m.group('n') in d.secmap and 'paquete' not in texto[max(0, m.start() - 5):m.end() + 12]:
                rep = [('t', m.group('pre') + d.secmap[m.group('n')])]
        elif kind == 'osec':
            n = m.group('n')
            ctx = texto[max(0, m.start() - 40):m.start()]
            if n in cur.secmap and not re.search(r'\(\s*[A-ZÁÉÍÓÚ][\w\s\.,&]*\d{4}[a-z]?\s*,\s*$', ctx) and 'Bases' not in ctx and 'Subdocumento' not in ctx:
                rep = [('t', m.group('kw') + ' ' + cur.secmap[n])]
        if rep is None:
            if kind == 'obj':
                reg.dudas.append((cur.key, m.group(0)))
            continue
        piezas.append(('t', texto[pos:m.start()]))
        piezas.extend(rep)
        pos = m.end()
        usados_hasta = m.end()
        nuevo = ''.join(p[1] if p[0] == 't' else re.sub(r'\\refext\{([^}]*)\}\{([^}]*)\}', lambda x: '[%s:%s]' % (x.group(1), x.group(2)), re.sub(r'\\ref\{([^}]*)\}', r'[\1]', p[1])) for p in rep)
        reg.cambios.append((cur.key, m.group(0), nuevo))
    piezas.append(('t', texto[pos:]))
    return piezas

def reemplazo_obj(reg, cur, m, texto):
    kw = m.group('kw'); lista = m.group('lista'); qual = m.group('qual') or ''
    contexto = texto[:m.start()]
    nums = re.findall(REF_NUM, lista)
    seps = re.split(REF_NUM, lista)[1:-1]
    out = []
    destino_otro = None
    resueltos = []
    for num in nums:
        key, it = resolver(reg, cur, kw, num, qual, contexto)
        if it is None:
            return None
        resueltos.append((key, it, num))
    # ¿hace falta reescribir? si algún número o el formato cambian
    rep = [('t', kw + ' ')]
    for k, (key, it, num) in enumerate(resueltos):
        if key == cur.key:
            rep.append(('r', r'\ref{%s}' % it['label']))
        else:
            rep.append(('r', r'\refext{%s}{%s}' % (key, it['label'])))
            destino_otro = key
        if k < len(seps):
            rep.append(('t', seps[k]))
    # calificador: se mantiene; si el número antiguo traía el documento (T-14.5, 1.E.2) se agrega
    if qual:
        rep.append(('t', qual))
    elif destino_otro:
        d = reg.docs[destino_otro]
        num0 = resueltos[0][2]
        if d.modo == 'formulario':
            rep.append(('t', ' del Formulario T-%d' % d.form))
        elif d.modo == 'anexo' and (re.match(r'^\d+\.[A-Z]', num0) or cur.modo != 'subdoc' or d.sub != getattr(cur, 'sub', None)):
            rep.append(('t', ' de los Anexos del Subdocumento %d' % d.sub))
    return rep

def reemplazo_anexo(reg, cur, m):
    kw = m.group('kw'); n = int(m.group('n')); l = m.group('l')
    resto = m.group('rest') or ''
    letras = [l] + re.findall(r'\d+\.([A-Z])', resto)
    seps = re.findall(r'\s*(?:,|y|a|e)\s+', resto)
    s = kw + ' ' + letras[0]
    for k, x in enumerate(letras[1:]):
        s += seps[k] + x
    return [('t', s + ' del Subdocumento %d' % n)]

# --------------------------------------------------------------------------- fase 2: escritura
def math_latex(m):
    """OMML sencillo -> LaTeX (texto, fracciones, sub/superíndices, raíces)."""
    def conv(e):
        tag = e.tag
        if tag == M + 'r':
            t = ''.join(x.text or '' for x in e.iter(M + 't'))
            return mathtext(t)
        if tag == M + 'f':
            return r'\frac{%s}{%s}' % (conv_all(e.find(M + 'num')), conv_all(e.find(M + 'den')))
        if tag == M + 'sSup':
            return '{%s}^{%s}' % (conv_all(e.find(M + 'e')), conv_all(e.find(M + 'sup')))
        if tag == M + 'sSub':
            return '{%s}_{%s}' % (conv_all(e.find(M + 'e')), conv_all(e.find(M + 'sub')))
        if tag == M + 'sSubSup':
            return '{%s}_{%s}^{%s}' % (conv_all(e.find(M + 'e')), conv_all(e.find(M + 'sub')), conv_all(e.find(M + 'sup')))
        if tag == M + 'rad':
            return r'\sqrt{%s}' % conv_all(e.find(M + 'e'))
        if tag == M + 'd':
            return r'\left(%s\right)' % ','.join(conv_all(x) for x in e.findall(M + 'e'))
        if tag in (M + 'fPr', M + 'ctrlPr', M + 'rPr', M + 'sSupPr', M + 'sSubPr', M + 'dPr', M + 'radPr'):
            return ''
        return conv_all(e)
    def conv_all(e):
        if e is None:
            return ''
        return ''.join(conv(c) for c in e)
    return conv_all(m)

MATHMAP = {'×': r'\times ', '≈': r'\approx ', '≤': r'\leq ', '≥': r'\geq ', '−': '-', '·': r'\cdot ',
           'σ': r'\sigma ', 'μ': r'\mu ', 'Σ': r'\Sigma ', '±': r'\pm ', '%': r'\%', ',': '{,}', '→': r'\to ',
           '√': r'\surd ', 'Δ': r'\Delta ', '∑': r'\sum ', '≠': r'\neq ',
           '²': '^{2}', '³': '^{3}', '¹': '^{1}', 'ₚ': '_{p}', 'ᵢ': '_{i}', 'ⱼ': '_{j}', 'ₙ': '_{n}',
           '₀': '_{0}', '₁': '_{1}', '₂': '_{2}', '₃': '_{3}', '₄': '_{4}', '₅': '_{5}', 'ₖ': '_{k}', 'ₜ': '_{t}'}
def mathtext(t):
    out = []
    for c in t:
        if c in MATHMAP:
            out.append(MATHMAP[c])
        elif c.isalpha() and ord(c) > 127:
            out.append(r'\text{%s}' % c)
        elif c in '#$&_{}~^\\':
            out.append(esc(c))
        else:
            out.append(c)
    s = ''.join(out)
    # palabras de más de una letra en texto recto
    s = re.sub(r'(?<![\\a-zA-Z])([A-Za-z]{2,})', r'\\mathrm{\1}', s)
    return s

class Escritor:
    def __init__(self, doc, reg):
        self.doc = doc; self.reg = reg
        self.figdir = os.path.join(OUT, doc.carpeta, 'figuras')
        os.makedirs(self.figdir, exist_ok=True)
        self.nimg = 0
        self.externos = set()

    # ---- texto con formato de un párrafo o celda
    def runs(self, p):
        segs = []   # (tipo, valor, italica)
        def add(t, it):
            if segs and segs[-1][0] == 't' and segs[-1][2] == it:
                segs[-1] = ('t', segs[-1][1] + t, it)
            else:
                segs.append(('t', t, it))
        def walk(e, link=None):
            for c in e:
                tag = c.tag
                if tag == W + 'r':
                    rp = c.find(W + 'rPr')
                    it = rp is not None and rp.find(W + 'i') is not None and rp.find(W + 'i').get(W + 'val') not in ('0', 'false')
                    va = rp.find(W + 'vertAlign') if rp is not None else None
                    for x in c:
                        if x.tag == W + 't' and x.text:
                            if va is not None and va.get(W + 'val') in ('superscript', 'subscript'):
                                cmd = r'\textsuperscript' if va.get(W + 'val') == 'superscript' else r'\textsubscript'
                                segs.append(('r', '%s{%s}' % (cmd, esc(x.text)), False))
                            else:
                                add(x.text, it)
                        elif x.tag == W + 'tab':
                            add(' ', it)
                        elif x.tag == W + 'br' and x.get(W + 'type') not in ('page', 'column'):
                            segs.append(('r', r'\newline ', False))
                        elif x.tag == W + 'noBreakHyphen':
                            add('-', it)
                        elif x.tag == W + 'sym':
                            add('•', it)
                elif tag == W + 'hyperlink':
                    rid = c.get(R + 'id')
                    if rid and rid in self.doc.rels and self.doc.rels[rid][1] == 'External':
                        url = self.doc.rels[rid][0]
                        inner = ''.join(txt(x) for x in c)
                        segs.append(('r', r'\href{%s}{%s}' % (url.replace('%', r'\%').replace('#', r'\#'), esc(inner)), False))
                    else:
                        walk(c)
                elif tag in (W + 'smartTag', W + 'ins', W + 'customXml', W + 'fldSimple', W + 'sdt', W + 'sdtContent'):
                    walk(c)
                elif tag == M + 'oMath':
                    segs.append(('r', '$%s$' % math_latex(c), False))
                elif tag == M + 'oMathPara':
                    for mm in c.iter(M + 'oMath'):
                        segs.append(('r', r'\[%s\]' % math_latex(mm), False))
        walk(p)
        return segs

    def latex_texto(self, p, referencias=True, quitar=None):
        segs = self.runs(p)
        out = []
        for k, (tipo, val, it) in enumerate(segs):
            if tipo == 'r':
                out.append(val); continue
            if quitar and k == 0:
                val = quitar(val)
            piezas = reescribir(self.reg, self.doc, val) if referencias else [('t', val)]
            s = ''
            for pt, pv in piezas:
                if pt == 't':
                    s += esc(pv)
                else:
                    s += pv
                    m = re.search(r'\\refext\{([^}]*)\}', pv)
                    if m:
                        self.externos.add(m.group(1))
            if it and s.strip():
                s = r'\emph{%s}' % s
            out.append(s)
        s = ''.join(out)
        s = re.sub(r'[ \u00a0]{2,}', ' ', s)
        return s.strip()

    # ---- imágenes
    def imagenes(self, p):
        res = []
        for d in p.iter(WP + 'inline', WP + 'anchor'):
            b = d.find('.//' + A + 'blip')
            if b is None:
                continue
            rid = b.get(R + 'embed')
            tgt = self.doc.rels.get(rid, (None,))[0]
            if not tgt:
                continue
            ext = d.find(WP + 'extent')
            cm = round(int(ext.get('cx')) / 360000, 2) if ext is not None else 15
            res.append((os.path.join(self.doc.dir, 'word', tgt.replace('/', os.sep)), cm))
        return res

    def copiar_img(self, src, nombre):
        ext = os.path.splitext(src)[1].lower()
        dst = os.path.join(self.figdir, nombre + ext)
        shutil.copy(src, dst)
        return nombre

    # ---- tablas
    def tabla(self, tbl, item, fuente, nota, ancho_cm=None):
        grid = [int(float(g.get(W + 'w', 0))) for g in tbl.find(W + 'tblGrid').findall(W + 'gridCol')] if tbl.find(W + 'tblGrid') is not None else []
        rows = tbl.findall(W + 'tr')
        if not grid:
            grid = [1] * max(len(r.findall(W + 'tc')) for r in rows)
        tot = float(sum(grid)) or 1.0
        # el ancho real suele estar en las celdas (tcW), no en la cuadrícula
        for r in rows:
            tcs = r.findall(W + 'tc')
            if len(tcs) != len(grid) or r.find(W + 'trPr/' + W + 'gridBefore') is not None:
                continue
            ws = []
            for tc in tcs:
                w = tc.find(W + 'tcPr/' + W + 'tcW')
                gs = tc.find(W + 'tcPr/' + W + 'gridSpan')
                if w is None or gs is not None or w.get(W + 'type') not in ('dxa', None):
                    ws = None; break
                ws.append(int(float(w.get(W + 'w', 0))))
            if ws and all(x > 0 for x in ws) and max(ws) != min(ws):
                grid = ws; tot = float(sum(grid))
                break
        frac = [g / tot for g in grid]
        ncol = len(grid)
        # matriz de celdas: (fila, col) -> (tc, span, vmerge)
        celdas = []
        for r in rows:
            fila = []
            c = 0
            gb = r.find(W + 'trPr/' + W + 'gridBefore')
            if gb is not None:
                c += int(gb.get(W + 'val'))
            for tc in r.findall(W + 'tc'):
                pr = tc.find(W + 'tcPr')
                span = 1; vm = None
                if pr is not None:
                    gs = pr.find(W + 'gridSpan')
                    if gs is not None:
                        span = int(gs.get(W + 'val'))
                    v = pr.find(W + 'vMerge')
                    if v is not None:
                        vm = v.get(W + 'val') or 'continue'
                fila.append(dict(tc=tc, col=c, span=span, vm=vm))
                c += span
            celdas.append(fila)
        # alineación por columna (mayoría de las celdas del cuerpo)
        alin = []
        for ci in range(ncol):
            votos = collections.Counter()
            for fila in celdas[1:]:
                for ce in fila:
                    if ce['col'] == ci and ce['span'] == 1:
                        for pp in ce['tc'].findall(W + 'p'):
                            jc = pp.find(W + 'pPr/' + W + 'jc')
                            v = jc.get(W + 'val') if jc is not None else 'left'
                            votos[{'center': 'C', 'right': 'D', 'end': 'D'}.get(v, 'I')] += 1
            alin.append(votos.most_common(1)[0][0] if votos else 'I')
        spec = ''.join('%s{%.3f}' % (alin[k], frac[k]) for k in range(ncol))
        # filas fusionadas verticalmente: cuántas filas abarca cada inicio
        alto = {}
        for ri, fila in enumerate(celdas):
            for ce in fila:
                if ce['vm'] == 'restart':
                    k = 1
                    while ri + k < len(celdas) and any(x['col'] == ce['col'] and x['vm'] == 'continue' for x in celdas[ri + k]):
                        k += 1
                    alto[(ri, ce['col'])] = k
        # contenido de las celdas que inician fusiones verticales
        contenido = {}
        for ri, fila in enumerate(celdas):
            for ce in fila:
                v = self.celda(ce['tc'], ri == 0)
                # códigos de anexo antiguos en celdas ("1.A" -> "A")
                m = re.match(r'^(\d+)\.([A-Z])$', v)
                if m and int(m.group(1)) == self.doc.sub and self.doc.modo in ('anexo', 'subdoc'):
                    v = m.group(2)
                contenido[(ri, ce['col'])] = v
        def fila_latex(ri, cab=False):
            partes = []
            for ce in celdas[ri]:
                c = ce['col']; span = ce['span']
                w = sum(frac[c:c + span])
                if ce['vm'] == 'continue':
                    # buscar la fila de inicio y si esta es la última fila del bloque
                    r0 = ri
                    while r0 > 0 and not any(x['col'] == c and x['vm'] == 'restart' for x in celdas[r0]):
                        r0 -= 1
                    k = alto.get((r0, c), 1)
                    if ri == r0 + k - 1 and k > 1:
                        cont = contenido.get((r0, c), '')
                        val = r'\multirow{-%d}{=}{%s}' % (k, cont)
                    else:
                        val = ''
                elif ce['vm'] == 'restart' and alto.get((ri, c), 1) > 1:
                    val = ''
                else:
                    val = contenido[(ri, c)]
                if cab and val:
                    val = r'\cab{%s}' % val
                if span > 1:
                    val = r'\multicolumn{%d}{%s{%.3f}}{%s}' % (span, alin[c] if not cab else 'I', w, val)
                partes.append(val)
            # completar columnas que falten
            usadas = sum(ce['span'] for ce in celdas[ri]) + (celdas[ri][0]['col'] if celdas[ri] else 0)
            partes += [''] * max(0, ncol - usadas)
            return ' & '.join(partes)
        head = fila_latex(0, cab=True)
        body = [fila_latex(ri) + r' \\' for ri in range(1, len(celdas))]
        out = []
        if item:
            fu = fuente or item.get('fuente_inline') or 'Fuente: elaboración propia.'
            out.append(r'\begin{tabla}{%s}{%s}{%s}' % (spec, item['tex'], item['label']))
            out.append('  {%s}' % head)
            out.append('  {%s}' % fu)
            out += body
            out.append(r'\end{tabla}')
        else:
            out.append(r'\begin{tablasintitulo}{%s}{%s}' % (spec, head))
            out += body
            out.append(r'\end{tablasintitulo}')
            if fuente:
                out.append(r'\fuente{%s}' % fuente)
        if nota:
            out.append(r'\nota{%s}' % nota)
        return '\n'.join(out)

    def celda(self, tc, cab):
        partes = []
        lista = []
        for el in tc:
            if el.tag == W + 'p':
                imgs = self.imagenes(el)
                for src, cm in imgs:
                    self.nimg += 1
                    nom = self.copiar_img(src, 'img-tabla-%02d' % self.nimg)
                    partes.append(r'\imagen{%s}{%s}' % (min(cm, 6), nom))
                t = self.latex_texto(el, referencias=not cab)
                if not t:
                    continue
                if el.find(W + 'pPr/' + W + 'numPr') is not None or re.match(r'^[•·▪\-–]\s', txt(el).strip()):
                    t = re.sub(r'^[•·▪\-–]\s*', '', t)
                    partes.append(r'\textbullet~' + t)
                else:
                    partes.append(t)
            elif el.tag == W + 'tbl':
                # tabla anidada: se aplana como texto
                for p in el.iter(W + 'p'):
                    t = self.latex_texto(p)
                    if t:
                        partes.append(t)
        return r'\newline '.join(partes)

    # ---- documento completo
    def escribir(self):
        d = self.doc
        bl = d.bl
        cuerpo = []
        lista_abierta = []      # pila de ('itemize'|'enumerate')
        horizontal = False
        def cerrar_listas(hasta=0):
            while len(lista_abierta) > hasta:
                cuerpo.append(r'\end{%s}' % lista_abierta.pop())
        for i, (el, o) in enumerate(bl):
            # páginas horizontales
            if o == 'h' and not horizontal:
                cerrar_listas(); cuerpo.append(r'\begin{horizontal}'); horizontal = True
            elif o == 'v' and horizontal:
                cerrar_listas(); cuerpo.append(r'\end{horizontal}'); horizontal = False
            if i in d.usados:
                continue
            if i in d.titulos:
                cerrar_listas()
                t = d.titulos[i]
                texto = self.latex_texto_plano(t['texto'])
                if t['kind'] == 'sinnum':
                    cuerpo.append('\n' + r'\seccionsinnumero{%s}' % texto)
                elif t['kind'] == 'estrella':
                    cmd = {1: r'\seccion*', 2: r'\seccion*', 3: r'\subseccion*', 4: r'\subsubseccion*'}[t['nivel']]
                    cuerpo.append('\n%s{%s}' % (cmd, texto))
                else:
                    if t['nivel'] == 1:
                        cmd = {'subdoc': r'\capitulo', 'anexo': r'\anexo', 'formulario': r'\apartado'}[d.modo]
                    else:
                        cmd = {2: r'\seccion', 3: r'\subseccion', 4: r'\subsubseccion', 5: r'\subsubseccion'}[t['nivel']]
                    cuerpo.append('\n%s{%s}' % (cmd, texto))
                continue
            if el.tag == W + 'tbl':
                cerrar_listas()
                item = d.objnum.get(i)
                fuente = self.latex_texto(bl[d.fuente_de[i]][0]) if i in d.fuente_de else None
                nota = self.latex_texto(bl[d.nota_de[i]][0]) if i in d.nota_de else None
                if item:
                    item['tex'] = self.latex_texto_plano(item['texto'])
                else:
                    d.avisos.append('Tabla sin título en el original (queda sin número): "%s"' % txt(el)[:60])
                cuerpo.append(self.tabla(el, item, fuente, nota))
                continue
            # párrafo
            if tiene_imagen(el):
                cerrar_listas()
                imgs = self.imagenes(el)
                item = d.objnum.get(i)
                for k, (src, cm) in enumerate(imgs):
                    if item and k == len(imgs) - 1:
                        nom = 'fig-%s-%s' % (item['nuevo'].replace('.', '-'), slug(item['texto'], 5))
                        self.copiar_img(src, nom)
                        fuente = self.latex_texto(bl[d.fuente_de[i]][0]) if i in d.fuente_de else (item.get('fuente_inline') or 'Fuente: elaboración propia.')
                        cuerpo.append(r'\figura{%s}{%s}{%s}{%s}{%s}' % (cm, nom, self.latex_texto_plano(item['texto']), item['label'], fuente))
                    else:
                        self.nimg += 1
                        nom = self.copiar_img(src, 'img-%02d' % self.nimg)
                        cuerpo.append(r'\imagen{%s}{%s}' % (cm, nom))
                t = self.latex_texto(el)
                if t:
                    cuerpo.append(t + '\n')
                continue
            t = self.latex_texto(el)
            if not t:
                continue
            numpr = el.find(W + 'pPr/' + W + 'numPr')
            bullet_lit = re.match(r'^[•▪]\s', txt(el).strip())
            if numpr is not None or bullet_lit:
                ilvl = 0; fmt = 'bullet'
                if numpr is not None:
                    il = numpr.find(W + 'ilvl'); ilvl = int(il.get(W + 'val')) if il is not None else 0
                    nid = numpr.find(W + 'numId'); nid = nid.get(W + 'val') if nid is not None else None
                    if nid == '0':
                        numpr = None
                    else:
                        fmt = d.numfmt.get(nid, {}).get(str(ilvl), 'bullet')
                if numpr is not None or bullet_lit:
                    env = 'itemize' if fmt in ('bullet', 'none') else 'enumerate'
                    nivel = min(ilvl, 1) + 1
                    while len(lista_abierta) > nivel:
                        cuerpo.append(r'\end{%s}' % lista_abierta.pop())
                    while len(lista_abierta) < nivel:
                        cuerpo.append(r'\begin{%s}' % env); lista_abierta.append(env)
                    if lista_abierta[-1] != env:
                        cuerpo.append(r'\end{%s}' % lista_abierta.pop())
                        cuerpo.append(r'\begin{%s}' % env); lista_abierta.append(env)
                    if bullet_lit:
                        t = re.sub(r'^\\?[•▪]\s*', '', t)
                    cuerpo.append(r'\item ' + t)
                    continue
            cerrar_listas()
            if re.match(r'^Fuentes?\s*:', txt(el).strip()):
                cuerpo.append(r'\fuente{%s}' % t)
            elif d.titulos and self.es_referencia(i):
                cuerpo.append(r'\item ' + t)
            else:
                cuerpo.append(t + '\n')
        cerrar_listas()
        if horizontal:
            cuerpo.append(r'\end{horizontal}')
        cuerpo = self.envolver_referencias(cuerpo)
        return cuerpo

    def es_referencia(self, i):
        """Párrafo dentro de la sección Referencias (lista APA)."""
        d = self.doc
        prev = [k for k in d.titulos if k < i]
        if not prev:
            return False
        t = d.titulos[max(prev)]
        if not t['texto'].lower().startswith('referencias'):
            return False
        txtp = txt(d.bl[i][0]).strip()
        if re.match(r'^(La lista|Las fuentes|Las referencias|Esta lista|Este (sub)?documento)', txtp) or 'APA 7' in txtp[:200]:
            return False
        return bool(re.search(r'\(\d{4}[a-z]?[,\)]|\(s\.\s?f\.\)|\(n\.d\.\)', txtp[:250]))

    def envolver_referencias(self, cuerpo):
        # agrupa los \item de Referencias en el entorno referencias
        # todo \item que quede fuera de una lista es una referencia bibliográfica
        res = []
        nivel = 0
        abierta = False
        for line in cuerpo:
            s = line.strip()
            es_item = line.startswith(r'\item ')
            if es_item and nivel == 0:
                if not abierta:
                    res.append(r'\begin{referencias}'); abierta = True
                res.append(line)
                continue
            if abierta and not es_item:
                res.append(r'\end{referencias}'); abierta = False
            nivel += len(re.findall(r'\\begin\{(?:itemize|enumerate)\}', line))
            nivel -= len(re.findall(r'\\end\{(?:itemize|enumerate)\}', line))
            res.append(line)
        if abierta:
            res.append(r'\end{referencias}')
        return res

    def latex_texto_plano(self, s):
        return esc(re.sub(r'\s+', ' ', s).strip())

dentro_ref = [False]

# --------------------------------------------------------------------------- portada: datos del documento
INFORME_GLOBAL = ['n']
def metadatos(doc):
    full = ' '.join(txt(p) for p in doc.root.find(W + 'body').iter(W + 'p'))[:4000]
    md = {}
    m = re.search(r'Informe Preparatorio N°\s*(\d+)', full)
    md['informe'] = 'Informe Preparatorio N° %s' % (m.group(1) if m else INFORME_GLOBAL[0])
    m = re.search(r'(\d{1,2} de [a-záéíóú]+ de 20\d\d)', full)
    md['fecha'] = m.group(1) if m else '[día] de [mes] de 2026'
    if doc.modo == 'subdoc':
        # nombre del subdocumento: línea siguiente a "Subdocumento N" en la portada
        ps = [re.sub(r'\s+', ' ', txt(p)).strip() for p in doc.root.find(W + 'body')[:20] if p.tag == W + 'p']
        nombre = None
        for k, t in enumerate(ps):
            if re.search(r'Subdocumento\s+%d\b' % doc.sub, t) and k + 1 < len(ps):
                nombre = ps[k + 1]; break
        md['nombre'] = nombre or '[Nombre del subdocumento]'
    if doc.modo == 'formulario':
        ps = [re.sub(r'\s+', ' ', txt(p)).strip() for p in list(doc.root.find(W + 'body'))[:12] if p.tag == W + 'p']
        nombre = None
        for k, t in enumerate(ps):
            if re.match(r'^T-%d$' % doc.form, t) and k + 1 < len(ps):
                nombre = ps[k + 1]; break
        md['nombre'] = nombre or '[Nombre oficial del formulario]'
    return md

PLANTILLA = r"""%% {nombre}.tex — generado desde {nombre}.docx
%% Formato: clase overfore, modo {modo}. El formato lo pone la clase; aquí sólo va el contenido.
\documentclass[{modo}]{{../../comun/overfore}}
\numsubdoc{{{sub}}}
{extra}\informe{{{informe}}}
\fecha{{{fecha}}}
{externos}
\begin{{document}}
{cuerpo}
\end{{document}}
"""

def main():
    docs = [Doc(i) for i in catalogo()]
    for d in docs:
        analizar(d)
    reg = Registro(docs)
    # número de informe: el que declaran los documentos que lo indican en la portada
    nums = collections.Counter()
    for d in docs:
        m = re.search(r'Informe Preparatorio N°\s*(\d+)', ' '.join(txt(p) for p in list(d.root.find(W + 'body'))[:40]))
        if m:
            nums[m.group(1)] += 1
    if nums:
        INFORME_GLOBAL[0] = nums.most_common(1)[0][0]
    # documentos.tex: clave -> ruta
    os.makedirs(os.path.join(OUT, 'comun'), exist_ok=True)
    with open(os.path.join(OUT, 'comun', 'documentos.tex'), 'w', encoding='utf8') as f:
        f.write('% Clave de cada documento y su ruta (desde la carpeta latex/). Lo usa \\externos.\n')
        for d in docs:
            f.write('\\ovdoc{%s}{%s/%s}\n' % (d.key, d.carpeta, d.nombre))
    resumen = []
    for d in docs:
        dest = os.path.join(OUT, d.carpeta)
        if os.path.isdir(os.path.join(dest, 'figuras')):
            shutil.rmtree(os.path.join(dest, 'figuras'))
        os.makedirs(dest, exist_ok=True)
        e = Escritor(d, reg)
        cuerpo = e.escribir()
        md = metadatos(d)
        extra = ''
        if d.modo == 'subdoc':
            extra = '\\nombresubdoc{%s}\n' % esc(md['nombre'])
        if d.modo == 'formulario':
            extra = '\\formulario{T-%d}{%s}\n' % (d.form, esc(md['nombre']))
        ext = ('\\externos{%s}' % ','.join(sorted(e.externos))) if e.externos else ''
        tex = PLANTILLA.format(nombre=d.nombre, modo=d.modo, sub=d.sub, extra=extra,
                               informe=md['informe'], fecha=md['fecha'], externos=ext,
                               cuerpo='\n'.join(cuerpo))
        tex = re.sub(r'\n{3,}', '\n\n', tex)
        with open(os.path.join(dest, d.nombre + '.tex'), 'w', encoding='utf8') as f:
            f.write(tex)
        resumen.append(d)
    # informe
    with open(REPORT, 'w', encoding='utf8') as f:
        f.write('# Equivalencias de numeración y referencias\n\n')
        f.write('Generado al convertir los documentos Word a LaTeX. En LaTeX los números ya no se escriben a mano: '
                'la clase los asigna y cada referencia (`\\ref`) se actualiza sola al compilar.\n\n')
        for d in resumen:
            camb = [it for it in d.items if it['viejo'] != it['nuevo']]
            f.write('## %s\n\n' % d.nombre)
            f.write('- Tablas: %d · Figuras: %d\n' % (sum(1 for x in d.items if x['tipo'] == 'Tabla'), sum(1 for x in d.items if x['tipo'] == 'Figura')))
            if d.secmap and d.modo == 'formulario':
                f.write('- Secciones renumeradas: ' + ', '.join('%s → %s' % (a, b) for a, b in d.secmap.items()) + '\n')
            if camb:
                f.write('\n| Antes | Ahora | Título |\n|---|---|---|\n')
                for it in camb:
                    f.write('| %s %s | %s %s | %s |\n' % (it['tipo'], it['viejo'], it['tipo'], it['nuevo'], it['texto'][:70].replace('|', '/')))
            for a in d.avisos:
                f.write('- Aviso: %s\n' % a)
            refs = [c for c in reg.cambios if c[0] == d.key]
            if refs:
                f.write('\n<details><summary>%d referencias reescritas</summary>\n\n' % len(refs))
                for k, a, b in refs:
                    f.write('- «%s» → «%s»\n' % (a, b))
                f.write('\n</details>\n')
            f.write('\n')
        dudas = collections.Counter(reg.dudas)
        f.write('## Referencias que no se pudieron resolver (quedaron como texto)\n\n')
        for (k, s), n in sorted(dudas.items()):
            f.write('- %s: «%s»%s\n' % (k, s, (' ×%d' % n) if n > 1 else ''))
    print('docs', len(docs), 'refs reescritas', len(reg.cambios), 'dudas', len(reg.dudas))

if __name__ == '__main__':
    main()
