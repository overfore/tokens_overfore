# Propuesta OVERFORE · Licitación TFEP-01/2026 · Caso 01 Minería

**Entrada para agentes (Codex, Claude y otros):** leer [AGENTS.md](AGENTS.md),
[FUENTE_DE_VERDAD.md](FUENTE_DE_VERDAD.md), [DECISIONES.md](DECISIONES.md) y
[TAREAS.md](TAREAS.md) antes de editar. `CLAUDE.md` remite a las mismas instrucciones.
Estado confirmado: **entrega 2 existente; entrega 3 en preparación**. Las decisiones
documentadas y los conflictos abiertos se distinguen en el registro; no cambiar una
elección de un subdocumento sin revisar su motivo y sus consumidores.

Repositorio de trabajo de la oferta de **OVERFORE S.A.** (proponente) a la **Compañía
Minera Altos de Aranda** (mandante) para la Licitación N° TFEP-01/2026. La solución
ofertada se llama **SITCO Aranda** (Sistema Integrado de Trazabilidad, Conciliación y
Cumplimiento Operacional).

Este archivo explica qué hay en cada carpeta, para que una persona o una IA sepa dónde
está cada cosa sin tener que abrir todo.

## Responsables por documento

**Entrega Informe 1**

| Documento | Responsable |
|---|---|
| Subdocumento 1 y T-6 | **Grupo 3** |
| Subdocumento 2 | **Grupo 1** |
| Subdocumento 3 y T-12 | **Grupo 1** |
| Subdocumento 4 y T-11 | **Grupo 2** (arquitectura lógica) y **Grupo 3** (arquitectura física) |
| Subdocumento 5 | **Grupo 2** |
| Subdocumento 13 y T-19 | **Grupo 1** |

**Entrega Informe 2**

| Documento | Responsable |
|---|---|
| Subdocumento 6, T-9 y T-10 | **Grupo 4** |
| Subdocumento 7, T-14, T-15 y T-18 | **Grupo 6** |
| Subdocumento 8 y T-16 | **Grupo 7** |
| Subdocumento 9, T-13 y T-17 | **Grupo 5** |

### Subgrupos de trabajo

| Grupo | Integrantes |
|---|---|
| Grupo 1 | Claudio Cabello · Benjamín Velásquez · David Martinez |
| Grupo 2 | Patricio Figueroa · Lucas Zamora · Gabriel Sanzana |
| Grupo 3 | Marcelo Flores · Benjamín Rodriguez · Kavon Kermani |
| Grupo 4 | Claudio Cabello · Benjamín Rodriguez |
| Grupo 5 | Benjamín Velásquez · David Martinez |
| Grupo 6 | Patricio Figueroa · Lucas Zamora · Gabriel Sanzana · Marcelo Flores · Kavon Kermani |
| Grupo 7 | Claudio Cabello · Benjamín Rodriguez · Benjamín Velásquez · David Martinez |

### Ramas de trabajo

El trabajo se organiza en una rama por grupo:

| Rama | Grupo | Documentos a cargo |
|---|---|---|
| `grupo1` | Grupo 1 | Subdocumento 2 · Subdocumento 3 y T-12 · Subdocumento 13 y T-19 |
| `grupo2` | Grupo 2 | Subdocumento 4 y T-11 (arquitectura lógica) · Subdocumento 5 |
| `grupo3` | Grupo 3 | Subdocumento 1 y T-6 · Subdocumento 4 y T-11 (arquitectura física) |
| `grupo4` | Grupo 4 | Subdocumento 6, T-9 y T-10 |
| `grupo5` | Grupo 5 | Subdocumento 9, T-13 y T-17 |
| `grupo6` | Grupo 6 | Subdocumento 7, T-14, T-15 y T-18 |
| `grupo7` | Grupo 7 | Subdocumento 8 y T-16 |

Reglas:

1. Cada grupo sube a su rama los cambios de los documentos de los que es responsable.
2. Si un grupo modifica un documento de otro grupo, debe hacer merge de ese cambio a
   la rama del grupo responsable de ese documento, o bien a `main`.

## Mapa del repositorio

```
.
├── README.md                     este archivo (contexto general)
├── bases/                        lo que pide el mandante: 3 bases, fuente de toda regla
│   ├── bases-administrativas.md
│   ├── bases-tecnicas-transversales.md
│   └── bases-tecnicas-caso-mineria.md
├── comunicados/                  aclaraciones oficiales posteriores a las bases
│   └── comunicado-10-estructura-obligatoria.md
├── plantillas-word/              formato de referencia en Word (origen del formato LaTeX)
│   ├── OVERFORE_Manual_de_Formato_nuevo.docx   formato del subdocumento + manual de reglas
│   ├── OVERFORE_Plantilla_Anexos.docx          formato de los anexos
│   └── OVERFORE_Plantilla_Formularios.docx     formato de los formularios T
└── latex/                        la propuesta misma, en LaTeX (aquí se trabaja)
    ├── README: LEEME.md · GUIA_RAPIDA.md
    ├── compilar.py               compila, revisa reglas y encadena el folio
    ├── comun/                    clase, reglas, imágenes comunes, índice obligatorio
    ├── subdoc01/ … subdoc13/     un subdocumento por carpeta, con sus anexos y formularios
    ├── herramientas/             convertidor de Word a LaTeX (uso único, ya ejecutado)
    ├── informes/                 equivalencias de numeración y reglas pendientes
    ├── salida/                   PDF finales para el ZIP (sólo si no hay errores)
    └── salida-borrador/          PDF de prueba, marcados «BORRADOR · NO ENTREGAR»
```

## 1. Las bases (`bases/`)

Son tres y gobiernan la propuesta. Para resolver discrepancias, consultar el Art. 5
de las Bases Administrativas y la relación con las Bases Técnicas Transversales en
su sección 1.3. El manual de formato y los prompts internos no sustituyen esas
fuentes. El procedimiento común está en [FUENTE_DE_VERDAD.md](FUENTE_DE_VERDAD.md).

| Archivo | Qué contiene | Cuándo leerlo |
|---|---|---|
| `bases-administrativas.md` | El proceso y el contrato. Capítulos 1–26: antecedentes, objeto y estructura de la contratación, requisitos transversales obligatorios, innovación (Arts. 28–30), garantías, requisitos formales (Art. 40: formato, foliación, firma), calendario, informes preparatorios, apertura, evaluación técnica y económica, contrato, niveles de servicio y penalidades. **Capítulo A**: formularios administrativos A-1 a A-6 (Sobre N° 1). **Capítulo B**: formularios técnicos T-6 a T-22 (Sobre N° 2; el **T-7** fija los 14 subdocumentos, el **T-21** su ponderación y el **T-22** qué se entrega en cada informe). **Capítulo C**: formularios económicos E-21 a E-26 (Sobre N° 3). | Plazos, formato y forma de entrega, qué formulario va dónde, cómo se evalúa, qué invalida una oferta. |
| `bases-tecnicas-transversales.md` | Requisitos técnicos comunes a cualquier caso. Capítulos 1–26: arquitectura de referencia, modelo híbrido nube/on-premise, ambientes y entrega continua, datos e integración, site principal y secundario, hardware, desempeño, disponibilidad, seguridad, identidad, usabilidad, observabilidad, sostenibilidad, módulos transversales, canales, IA, gobierno del proyecto, implantación, operación y soporte, capacitación, información corporativa, video, prototipo UX/UI, innovaciones. **Capítulo A**: índice de requisitos (códigos RT-xx). **B**: plantilla de volumetría. **C**: checklist de entregables. | Qué debe cumplir la solución técnicamente; trazabilidad en el Formulario T-12. |
| `bases-tecnicas-caso-mineria.md` | El caso concreto. Título I: el mandante (Compañía Minera Altos de Aranda, cifras, sitios). Título II: la operación actual (ciclo del mineral, sistemas existentes, conectividad, indicadores del problema). Título III: entrevistas a quienes operan. Título IV: lo que se espera (expectativas, restricciones no negociables, exclusiones, normativa, horizonte y etapas). Título V: volumetría y parámetros «según caso». | Problema, cifras, volumetría y restricciones; toda cifra de la propuesta debe salir de aquí o de un cálculo mostrado. |

## 2. Comunicados (`comunicados/`)

| Archivo | Qué contiene |
|---|---|
| `comunicado-10-estructura-obligatoria.md` | Índice obligatorio de los 14 capítulos (títulos exactos, numeración y orden), reglas de redacción, figuras, tablas, referencias APA 7, uso de IA y la Declaración de uso de IA, nombres de archivo y recordatorios del Art. 40. Su índice está copiado en `latex/comun/indice_obligatorio.json`, que usan las reglas. |

## 3. Estructura de la oferta técnica

Cada **subdocumento es obligatorio** (uno por capítulo del Formulario T-7). Algunos
llevan además un archivo de **Anexos** y uno o más **Formularios T**, cada uno en su
propio archivo. El Formulario que acompaña a cada capítulo lo fija el Comunicado 10:

| Capítulo / subdocumento | Anexos | Formularios T | En `latex/` |
|---|---|---|---|
| 1 · Introducción | sí | T-6 | ✔ subdoc01 |
| 2 · Introducción al Problema y Necesidad | sí (obligatorio: listados de requerimientos y supuestos) | — | ✔ subdoc02 |
| 3 · Introducción al Alcance de la Solución | sí | T-12 | ✔ subdoc03 |
| 4 · Arquitectura lógica y física | sí | T-11 | ✔ subdoc04 |
| 5 · Modelo y gestión de datos | sí | — | ✔ subdoc05 |
| 6 · Metodologías | sí | T-9, T-10 | ✔ subdoc06 |
| 7 · Plan de trabajo | no | T-14, T-15, T-18 | ✔ subdoc07 |
| 8 · Riesgos | sí | T-16 | ✔ subdoc08 |
| 9 · Plan de calidad | sí | T-13, T-17 | ✔ subdoc09 |
| 10 · Servicios | — | — | ✘ falta |
| 11 · Planes en operación | — | — | ✘ falta |
| 12 · Equipo de trabajo, subcontrataciones y alianzas | — | T-8 | ✘ falta (y T-8) |
| 13 · Innovaciones | sí | T-19 | ✔ subdoc13 |
| 14 · Ventajas, beneficios y consolidación | — | — | ✘ falta |

En cada instancia se entregan sólo los subdocumentos que pide el Formulario T-22.

**Nombres oficiales de archivo** (un archivo mal nombrado se considera no presentado,
Art. 40.4): `OVERFORE-SubdocumentoX.pdf`, `OVERFORE-SubdocumentoX-Anexos.pdf`,
`OVERFORE-Formulario-T-X.pdf`. Todo va en un ZIP.

## 4. La propuesta en LaTeX (`latex/`)

### Carpeta por subdocumento

```
latex/subdocNN/
├── subdocumento/            OVERFORE-SubdocumentoN.tex  + figuras/
├── anexos/                  OVERFORE-SubdocumentoN-Anexos.tex  + figuras/   (si existe)
└── formulario-T-XX/         OVERFORE-Formulario-T-X.tex  + figuras/         (uno por formulario)
```

- Las imágenes de cada documento están en su propia `figuras/`, con el número que les
  da el formato: `fig-4-23-vista-general-arquitectura-fisica.png` (subdoc) o
  `fig-A-1-....png` (anexo o formulario).
- Junto a cada `.tex` quedan el PDF y los auxiliares de LaTeX. No borrar los
  `*-ref.aux`: son la copia que leen los otros documentos para citarlo.

### `latex/comun/`

| Archivo | Qué es |
|---|---|
| `overfore.cls` | La clase: único lugar donde se define el formato. Tres modos: `subdoc`, `anexo`, `formulario`. Pone portada, índice, listados, encabezado, pie con media firma y folio, títulos, tablas y figuras. Bloquea el formato propio. |
| `reglas.py` | Reglas de contenido del Comunicado 10 (errores y avisos). |
| `indice_obligatorio.json` | Los 14 capítulos con sus títulos obligatorios. |
| `documentos.tex` | Orden de los documentos (S1, A1, T6, S2, …) y su ruta. Define el orden del folio. |
| `folios.tex` | Primer folio de cada archivo; lo escribe `compilar.py`. |
| `imagenes/` | Logo, isotipo, firma (`firma.png` y `firma-recorte.png`) y arco de portada. |

Claves de documento (para `\refext{clave}{etiqueta}`): `S1`…`S13` subdocumentos,
`A1`…`A13` anexos, `T6`, `T9`…`T19` formularios.

### Formato y numeración

- **Subdocumento**: «Capítulo N · Título», secciones N.1, N.2…; tablas y figuras N.1, N.2…
- **Anexos**: «Anexo A — Título», secciones A.1…; tablas y figuras por anexo: A.1, B.1…
- **Formularios**: secciones «A.», «B.»…; tablas y figuras por sección: A.1, B.1…
- Los números los pone la clase; las citas usan `\ref` y se actualizan solas.
- Folio continuo entre todos los archivos, en este orden: subdoc 1, sus anexos, sus
  formularios de menor a mayor, subdoc 2, y así. Hoy: 1 a 1273.

### Compilar y reglas

Ver `latex/GUIA_RAPIDA.md`, que tiene el paso a paso. Todos los comandos se escriben en
una terminal abierta en la carpeta `latex/`:

```bash
cd latex
```

**Versión de entrega (original).** Sólo compila si no hay errores de reglas.

| Qué quiero | Comando | Resultado |
|---|---|---|
| Todos los documentos, con folio continuo | `python compilar.py` | PDF en `salida/` (~15 a 45 min) |
| Un solo documento | `python compilar.py subdoc04/subdocumento/OVERFORE-Subdocumento4.tex` | PDF junto al `.tex` (1 a 2 min) |

**Borrador.** Compila aunque haya errores de reglas; cada página lleva la marca
«BORRADOR · NO ENTREGAR». Sirve para ver cómo queda, no para entregar.

| Qué quiero | Comando | Resultado |
|---|---|---|
| Todos los documentos | `python compilar.py --borrador` | PDF en `salida-borrador/` |
| Un solo documento | `python compilar.py --borrador subdoc04/subdocumento/OVERFORE-Subdocumento4.tex` | PDF junto al `.tex` |

**Revisar sin compilar.**

| Qué quiero | Comando |
|---|---|
| Ver los errores y avisos de reglas de todos los documentos (segundos) | `python compilar.py --reglas` |
| Una pasada rápida de LaTeX sobre todo, para encontrar errores de compilación | `python compilar.py --revisar` |

**Rutas de cada tipo de documento** (cambiar el número):

| Documento | Ruta |
|---|---|
| Subdocumento | `subdoc04/subdocumento/OVERFORE-Subdocumento4.tex` |
| Anexos | `subdoc04/anexos/OVERFORE-Subdocumento4-Anexos.tex` |
| Formulario | `subdoc04/formulario-T-11/OVERFORE-Formulario-T-11.tex` |

**En VS Code:** al guardar se compila el documento abierto (receta «OVERFORE (este
documento)»); la receta «OVERFORE borrador» lo compila como borrador.

Cuidados:
- No correr dos compilaciones al mismo tiempo: comparten los archivos `.aux` y `.toc`.
- Compilar un solo documento usa el folio ya calculado. Si un documento cambió de número
  de páginas, correr `python compilar.py` completo antes de entregar, para que el folio
  de los siguientes se corra.
- Si el comando termina con «no se estabilizaron», volver a correrlo.

Reglas que impiden compilar: usar otra clase u otro modo, dar formato propio (negrita,
color, tamaño o tipo de letra, subrayado), marcadores sin completar, celdas vacías, y
en el subdoc: título seguido de tabla, figura u otro título; tablas de más de 5
columnas o más de una página; celdas de más de una frase; tablas y figuras sin título,
fuente, cita previa o explicación posterior; índice obligatorio incompleto, renombrado,
fuera de orden o con títulos agregados del mismo nivel. También impiden compilar, en
todos los documentos: «OVERFORE» en mayúsculas dentro del texto (sólo va en nombres de
archivo), menciones a la universidad o al curso, «Terraform» (la herramienta es
OpenTofu), «con apoyo de Claude» en fuentes y restos de nombres de archivo. Avisos:
tabla «Concepto / Descripción» y capítulo técnico sin figuras.

No se exige que estén todos los subdocumentos: `compilar.py` encuentra solo los que
existan en `latex/subdocNN/` y arma el orden y el folio con ellos, así que cada entrega
puede sumar subdocumentos nuevos.

### Estado actual

- El repositorio corresponde a la entrega 2; la entrega 3 se prepara a continuación.
  Su economía y prototipo son trabajo planificado, no defectos de la entrega actual.
- 31 documentos convertidos desde Word (10 subdocumentos, 9 archivos de anexos y 12 formularios).
- La compilación histórica reportada para la entrega tenía folios 1 a 1273 y PDF en
  `latex/salida/` (no versionados). La revisión del 21-10-2026 comprobó 0 errores y
  9 avisos de reglas, pero no confirmó una compilación completa nueva: ver R-09 en
  [TAREAS.md](TAREAS.md). Faltan los subdocumentos 10, 11, 12 y 14 y el Formulario T-8,
  que se suman en entregas posteriores.
- Sólo quedan avisos (no impiden compilar), listados en `latex/informes/pendientes_reglas.txt`.
- Correcciones de la revisión del Informe 2 aplicadas en los `.tex`. Quedan pendientes, a
  decisión del equipo: figuras (organigrama S1, Terraform en las figuras 6.10 y 6.11 del S6,
  EDT del T-14, RBS del S8), cifras (dotación S1/S7, beneficio de la innovación 4) y el
  número de grupos de interés (S2/S6).
- `latex/informes/equivalencias.md`: qué número tenía cada tabla, figura y sección en
  los Word antiguos y cuál tiene ahora, y qué referencias se reescribieron.
- El diagnóstico interno, sus límites y el análisis de las ramas 1.1/1.4 de la EDT
  están en [el informe de revisión](revision-comision/informe-revision-2026-10-21.md).
  La cola vigente de correcciones está en [TAREAS.md](TAREAS.md); los pendientes
  históricos de este apartado deben contrastarse mediante R-10.

## 5. Para una IA que trabaje aquí

- Aplicar primero [AGENTS.md](AGENTS.md). Registrar tarea y consultar motivo y
  consumidores en [DECISIONES.md](DECISIONES.md) antes de cambiar contenido compartido.
- Antes de escribir contenido, buscar la exigencia en `bases/` y la estructura en
  `comunicados/comunicado-10-estructura-obligatoria.md`. Citar las Bases con documento,
  capítulo o artículo y página.
- Nombres estándar de las tres bases (lista de referencias y cita en el texto):
  - Compañía Minera Altos de Aranda. (2026a). *Bases administrativas*. Licitación N° TFEP-01/2026. → (CMAA, 2026a, Art. X, p. Y)
  - Compañía Minera Altos de Aranda. (2026b). *Bases técnicas del caso Minería*. Licitación N° TFEP-01/2026. → (CMAA, 2026b, cap. X, p. Y)
  - Compañía Minera Altos de Aranda. (2026c). *Bases técnicas transversales*. Licitación N° TFEP-01/2026. → (CMAA, 2026c, cap. X, p. Y)
  - La primera cita de cada documento define la sigla: (Compañía Minera Altos de Aranda [CMAA], 2026b, …).
  - En una fuente de tabla o figura se nombra la base sólo si el dato sale de ella.
- La empresa se escribe «Overfore» en el texto. No mencionar la universidad ni el curso.
- Estilo: explicación simple y directa. Las revisiones humanas de la Declaración de uso de
  IA van en pasado, en tercera persona y con el objeto concreto que se verificó.
- El contenido de la propuesta se edita en los `.tex` dentro de `latex/subdocNN/`;
  la documentación de coordinación se mantiene aparte según `AGENTS.md`.
  No cambiar `latex/comun/overfore.cls`, `reglas.py` ni `compilar.py` sin que la tarea
  lo autorice: afectan el formato o la validación de todos los documentos.
- No dar formato propio en los `.tex`; usar los comandos de la clase (ver `latex/LEEME.md`).
- Tras editar, correr `python compilar.py ruta/doc.tex` (o `--reglas`) y corregir lo que marque.
- No incluir precios ni montos de la oferta en la oferta técnica (Art. 50.2).
- La terminología y los nombres de componentes deben ser iguales en todos los
  subdocumentos.
