# Fuente de verdad y mapa de autoridad

Actualización inicial: 2026-10-21. Línea base inspeccionada: `37b529c7016e9d7bb53090fcfdc840bdf0603240`.

Este archivo es el punto de entrada a las fuentes; no sustituye las bases ni convierte el texto actual en un diseño validado. Los valores repetidos aquí son un índice: al cambiarlos, actualizar su origen y consumidores en el mismo cambio.

## Estado de trabajo

- **Confirmado por el usuario el 2026-10-21:** el repositorio está hasta la entrega 2 y se debe preparar la entrega 3.
- La revisión del 2026-10-21 es un diagnóstico interno, no un acta de la comisión: [informe de revisión](revision-comision/informe-revision-2026-10-21.md).
- Los pendientes de entrega 3 están separados de las correcciones de entrega 2 en [TAREAS.md](TAREAS.md).
- No se ha confirmado en esta revisión la compilación completa ni la legibilidad de todos los PDF. El README conserva antecedentes de compilaciones previas; no son prueba de una compilación nueva.

## Cómo resolver fuentes

1. Consultar el **Artículo 5, numerales 5.1 a 5.4**, de [Bases administrativas](bases/bases-administrativas.md). Allí se ordenan Bases Administrativas y anexos; Bases Técnicas del caso y anexos; aclaraciones formales; oferta técnica; oferta económica; resolución; contrato; informes aprobados; otros antecedentes del cliente. No sustituir ese orden por la lista de un prompt.
2. Las [Bases técnicas transversales](bases/bases-tecnicas-transversales.md), sección 1.3, desarrollan el piso técnico contractual. El caso aporta valores «Según caso» y puede endurecer requisitos, no rebajarlos. Leer también la sección 1.7 para interpretar umbrales.
3. El [Comunicado 10](comunicados/comunicado-10-estructura-obligatoria.md) fija estructura y forma, y complementa T-7 y T-21. Aplicar sus aclaraciones en su materia sin usarlas para inventar una derogación contractual.
4. La propuesta, manual de formato y prompts internos son fuentes subordinadas. Un hallazgo de un agente no es una aclaración del cliente.
5. Si el texto extraído tiene OCR defectuoso o no resuelve una discrepancia, registrar el conflicto y buscar el original. No inventar un orden adicional ni una aprobación.

Las instrucciones del usuario delimitan el trabajo de los agentes; cuando una decisión solicitada afecte una obligación de la licitación, explicar ese impacto y no modificar retrospectivamente el contenido de las bases.

## Clasificación de afirmaciones

| Clase | Qué significa | Evidencia necesaria |
|---|---|---|
| Dato del caso | Cifra o condición entregada por el mandante | Base, capítulo/sección, página y unidad |
| Exigencia | Obligación o criterio de evaluación | Artículo, RT o comunicado aplicable |
| Decisión documentada | Elección que la propuesta declara | Registro `DEC-NNN`, motivo y ubicación original |
| Supuesto | Condición aún por validar | Código SUP, fundamento, responsable y contingencia |
| Cálculo derivado | Resultado reproducible | Entradas, fórmula, unidad y criterio de redondeo |
| Propuesta pendiente | Alternativa todavía no adoptada | Autor, opciones, impacto y tarea |
| Conflicto abierto | Dos afirmaciones incompatibles o sin equivalencia | Ambas fuentes y tarea; no tiene valor oficial elegido |

## Mapa de autoridad por subdocumento

Los códigos S, A y T coinciden con `latex/comun/documentos.tex`. Este mapa indica dónde se desarrolla cada materia; no declara infalible al documento de origen.

| Materia | Fuente de la propuesta que se debe leer primero | Consumidores que deben revisarse al cambiarla |
|---|---|---|
| Empresa, integrantes, capacidades y alianzas | S1, A1 y T6, en `latex/subdoc01/` | S4, S6, S7/T14/T15 y S8/T16; organigramas |
| Problema, actores, catálogo y supuestos SUP | S2 y A2, en `latex/subdoc02/` | S3/T12, S4, S5, S6, S7, S8 y S13 |
| Alcance, módulos y reparto entre etapas | S3 y T12, en `latex/subdoc03/` | S4, S5, S7/T14/T15, S9 y S13/T19 |
| Arquitectura, tecnologías, ubicación, identidad y capacidad | S4, A4 y T11, en `latex/subdoc04/`; ADR-01 a ADR-08 | S3, S5, S6/T10, S7, S8, S9 y S13; todas sus figuras |
| Modelo, propiedad de datos, retención y migración | S5 y A5, en `latex/subdoc05/` | S3, S4, S7/T14/T15, S8, S9 y S13 |
| Metodología, cadencias y procesos | S6, T9 y T10, en `latex/subdoc06/` | S7/T14/T15/T18, S8 y S9 |
| EDT, paquetes, aceptación y esfuerzo por perfil | T14, en `latex/subdoc07/formulario-T-14/` | T15, T18, S1, S6, S7, S8, S9, S13/T19 y economía futura |
| Nivelación, curvas y personas por mes | T15, derivado de las fichas T14 | S1, S7, figuras y economía futura; no ajustar totales por separado |
| Hitos y cronograma | Art. 17 y E-25; desarrollo en S7/T14 | S3, S6, T15/T18, S8, S9 y S13 |
| Riesgos, responsables y respuestas | S8, A8 y T16, en `latex/subdoc08/` | S3, S4, S7/T14/T15, S9 y S13 |
| Pruebas, indicadores y criterios de aceptación | S9, A9, T13 y T17, en `latex/subdoc09/` | S3/T12, S4, S6, S7 y S13/T19 |
| Innovaciones, diferencia respecto al alcance base y beneficios | S13, A13 y T19, en `latex/subdoc13/` | S3, S4, S5, S7/T14/T15, S8, S9 y economía futura |
| Formato, índice y validación automática | Comunicado 10; `latex/comun/overfore.cls`, `latex/comun/reglas.py`, `latex/comun/indice_obligatorio.json` | Todos los documentos; cambiar sólo con autorización de la tarea |

Para cualquier edición, ampliar esta lista con los consumidores encontrados por búsqueda. La matriz no contiene todos los enlaces posibles.

## Datos y cálculos de referencia

| Elemento | Valor y clase | Origen y condición de uso |
|---|---|---|
| Plazo contractual | 56 meses; exigencia | Bases administrativas, Art. 17 |
| Desarrollo / marcha blanca E1 | M1–M12 / M13–M15; exigencia | Art. 17; no confundir con HH de estabilización posteriores |
| Desarrollo / marcha blanca E2 | M13–M18 / M19–M20; exigencia | Art. 17 |
| Operación | M21–M56, 36 meses; exigencia | Art. 17 |
| Personas con acceso a faena | 4.180 en régimen y hasta 8.500 en detención; dato del caso | Caso Minería, 14.1; no es dotación de Overfore |
| Equipos con telemetría / historiador | 52 equipos / 14.500 etiquetas; dato del caso | Caso Minería, 14.1; no equivale al número de señales seleccionadas por la propuesta |
| Esfuerzo de la línea base | 183.066 HH; cálculo de la propuesta, en revisión | T14/T15: 60.394 HH de ramas 1.1–1.7 + 122.672 HH de 1.8; revisar R-01 |
| Esfuerzo por período | 56.886 HH en M1–M20 + 126.180 HH en M21–M56 | T15, resumen por etapa; 3.508 HH de ramas 1.1–1.7 ocurren desde M21, no es contradicción por sí sola |
| Ramas 1.1 / 1.4 | 29 / 28 paquetes; 5.088 / 21.062 HH | Conteo y suma de hojas T15; razón 4,14 de esfuerzo, no de duración. R-01 |

No cambiar estas cifras para hacer coincidir resúmenes. Primero recalcular las fichas y después sus derivados. Este inventario inicial no sustituye la extracción de otros parámetros cuando una tarea los necesita.

## Conflictos que siguen abiertos

| Tema | Fuentes en tensión | Registro / tarea |
|---|---|---|
| Actores | S2: 19 grupos; S6: 14 y 91 canales, sin equivalencia explícita | DEC-012 / R-04 |
| Dotación de desarrollo | S1: 8 y 7 según período; figura 1.2: 5 sin período | DEC-013 / R-05 |
| Identidad de botonera | S4 ADR-07 llama segundo factor al contraste con despacho | DEC-007 / R-03 |
| Motor de conciliación | Resuelto en S13, T-19 y A13 (nube; balance del turno en el Nodo, DEC-014) | DEC-014 / R-06 |

Los motivos y consecuencias se consultan en [DECISIONES.md](DECISIONES.md). No copiar uno de los valores a todos los documentos sin resolver su fundamento.
