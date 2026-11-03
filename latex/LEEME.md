# Propuesta OVERFORE en LaTeX

## Estructura

```
latex/
  compilar.py              compila todo con folio continuo (o un solo documento)
  comun/
    overfore.cls           el formato: subdoc, anexo y formulario (único lugar donde se define)
    documentos.tex         orden de los documentos y su ruta
    folios.tex             primer folio de cada archivo (lo escribe compilar.py)
    imagenes/              logo, isotipo, firma y arco de portada
  subdoc01/
    subdocumento/          OVERFORE-Subdocumento1.tex + figuras/
    anexos/                OVERFORE-Subdocumento1-Anexos.tex + figuras/
    formulario-T-06/       OVERFORE-Formulario-T-6.tex + figuras/
  subdoc02/ ...
  salida/                  los PDF finales con su nombre oficial, listos para el ZIP
```

Cada documento tiene su propia carpeta `figuras/`. Las figuras numeradas se llaman
según su número y título (`fig-4-23-vista-general-arquitectura-fisica.png`); las
imágenes sin número (firmas en cartas, logos de terceros) se llaman `img-NN.png`.

## Compilar

- **Todo, con folio continuo:** `python compilar.py` (desde la carpeta `latex`).
  Orden: Subdocumento 1, sus Anexos, sus Formularios T de menor a mayor; luego el
  Subdocumento 2, y así. Cada archivo empieza en el folio siguiente al último del anterior.
  Al cambiar el largo de un documento, vuelva a correr `python compilar.py` para
  que todos los folios posteriores se corran.
- **Un documento:** guardar en VS Code (LaTeX Workshop compila solo) o
  `python compilar.py subdoc04/subdocumento/OVERFORE-Subdocumento4.tex`.

## Letra de las figuras

LaTeX no sabe qué letra hay dentro de una imagen, así que la letra mínima de 9 pt de las
figuras se revisa sobre los PDF ya compilados de `salida/`:

- `python herramientas/medir_figuras.py` lista, por documento, las figuras bajo 9 pt y las
  que quedan en el límite (9,0 a 9,3 pt), con su folio y título, y un resumen por documento.
- `python herramientas/medir_figuras.py S4 T-14` revisa sólo esos documentos.
- `--todas` muestra también las que cumplen; `--md archivo.md` guarda la lista en Markdown.

La medida es aproximada (± 0,3 pt): se mide la altura de las minúsculas del texto más chico
de cada figura tal como se imprime. Necesita `pymupdf` y `numpy`
(`pip install pymupdf numpy`).

## Referencias a tablas y figuras

`python herramientas/revisar_referencias.py` (o con documentos: `... S4 T-12`) revisa los PDF de
`salida/`: que toda «Tabla x.y» o «Figura x.y» citada exista (en el mismo documento, en el
subdocumento de ese capítulo o en el documento que nombra la cita), que el Listado de Tablas,
el Listado de Figuras y el Índice coincidan en título y folio con el documento, que la numeración
no tenga saltos ni repetidos, y que los números escritos dentro de los draw.io del repositorio
existan. `--md archivo.md` guarda la lista.

## Reglas

Un **error** impide compilar; un **aviso** sólo se muestra. `python compilar.py --reglas`
revisa todo sin compilar. Cada mensaje indica archivo y línea.

Para ver cómo queda aunque haya errores: `python compilar.py --borrador` (todo, a
`salida-borrador/`) o `python compilar.py --borrador ruta/doc.tex`. Las páginas salen
marcadas «BORRADOR · NO ENTREGAR». Ver también `GUIA_RAPIDA.md`.

**Formato (todos los documentos)**

1. La primera línea debe ser `\documentclass[subdoc]{../../comun/overfore}`
   (o `[anexo]` o `[formulario]`).
2. No se da formato propio: nada de colores, tamaños o tipos de letra, negritas ni
   subrayado. La cursiva (`\emph{...}`) sí se permite.

**Contenido** (definidas en `comun/reglas.py`)

| Regla | Nivel | Aplica a |
|---|---|---|
| Un título no va seguido de una tabla, una figura u otro título | error | subdoc |
| No quedan marcadores: `[Título]`, `[XX]`, «INSERTAR», «borrador» | error | todos |
| Sin «OVERFORE» en mayúsculas en el texto, universidad o curso, «Terraform», «con apoyo de Claude» ni nombres de archivo `.md` | error | todos |
| Tabla con más de 5 columnas | error | subdoc |
| Tabla de más de una página (se revisa al compilar) | error | subdoc |
| Celda con más de una frase | error | subdoc |
| Celda vacía (se escribe «—» o «No aplica») | error | todos |
| Tabla con forma «Concepto / Descripción» | aviso | subdoc |
| Tabla o figura sin título o sin fuente | error | subdoc |
| Tabla o figura que no se cita (`\ref`) antes de aparecer | error | subdoc |
| Tabla o figura sin texto que la explique después | error | subdoc |
| Capítulo técnico (3–11 y 13) sin figuras | aviso | subdoc |
| Falta un título del índice obligatorio, o está renombrado, en otro orden o en otro nivel | error | subdoc |
| Título agregado al nivel de los declarados (por ejemplo, un 2.6) | error | subdoc |

La tabla de la Declaración de uso de IA queda fuera de las reglas de tamaño, cita y
explicación: su forma la fija el comunicado. Las siglas de autor entre corchetes de
APA (`[PMI]`, `[ISO]`) no cuentan como marcadores.

El índice obligatorio está en `comun/indice_obligatorio.json` (copiado del
Comunicado 10). El índice y los listados de tablas y figuras se recalculan en cada
compilación: `compilar.py` repite la compilación hasta que dejan de cambiar.

## Cómo se escribe

| Para | Se escribe |
|---|---|
| Título de primer nivel | `\capitulo{...}` (subdoc), `\anexo{...}` (anexo), `\apartado{...}` (formulario) |
| Niveles siguientes | `\seccion{...}`, `\subseccion{...}`, `\subsubseccion{...}` |
| Título sin número | `\seccionsinnumero{Referencias}` |
| Tabla | `\begin{tabla}{I{0.3}C{0.2}D{0.5}}{Título.}{tab:etiqueta}{\cab{Col 1} & \cab{Col 2} & \cab{Col 3}}{Fuente: elaboración propia.}` … filas … `\end{tabla}` |
| Columnas de tabla | `I{f}` izquierda, `C{f}` centro, `D{f}` derecha; `f` es la fracción del ancho |
| Figura | `\figura{ancho en cm}{archivo}{Título.}{fig:etiqueta}{Fuente: elaboración propia.}` |
| Citar tabla o figura del mismo documento | `la Tabla~\ref{tab:etiqueta}` |
| Citar de otro documento | `\refext{S4}{tab:etiqueta}` y en el preámbulo `\externos{S4}` |
| Página horizontal | `\begin{horizontal}` … `\end{horizontal}` |
| Nota bajo una tabla | `\nota{Nota. ...}` |

Los números de tablas, figuras y secciones los pone la clase: en el subdocumento
por capítulo (Tabla 4.2) y en anexos y formularios por sección (Tabla B.1).
Nunca se escriben a mano.

Claves de documento para `\refext`: `S1`…`S13` (subdocumentos), `A1`…`A13`
(anexos) y `T6`, `T9`…`T19` (formularios).

## Live Share

Abrir la carpeta `latex` en VS Code. El anfitrión de la sesión de Live Share es
quien compila (tiene MiKTeX y LaTeX Workshop); los invitados editan y ven el PDF.
