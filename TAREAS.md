# Tareas y revisión compartida

Estado: entrega 2 existente; entrega 3 por desarrollar. Actualización inicial: 2026-10-21.

## Uso y estados

Antes de trabajar, registrar responsable, commit de partida y archivos previstos en la ficha de la tarea. Mantener IDs al cambiar el estado. Si se divide una tarea, asignar IDs nuevos y enlazar el origen.

Estados: `pendiente`, `en_curso`, `en_revision`, `bloqueada`, `cerrada`. Una tarea bloqueada indica su dependencia concreta; no confundirla con una tarea que nadie tomó. La lista no autoriza automáticamente cambios fuera de la solicitud activa.

Para cerrar: añadir commit o diff, archivos efectivamente cambiados, fuente/decisión utilizada, comandos y resultados, revisión cruzada y revisor. Si sólo hubo autorrevisión de un cambio técnico compartido, mantener `en_revision` e indicar la revisión independiente pendiente. Los agentes no se asignan aprobaciones del equipo ni de la comisión.

Si dos agentes trabajan en checkouts distintos, sus reclamaciones sólo se conocen al compartir o integrar cambios. La tabla no reemplaza un coordinador ni un acuerdo de archivos; releerla y comprobar el commit antes de integrar.

## Cola de trabajo

El origen de R-01 a R-10 y E3-01/E3-02 es el [informe interno de revisión](revision-comision/informe-revision-2026-10-21.md). Sus observaciones requieren contrastarse con las fuentes; no son decisiones aprobadas de la comisión.

| ID | Prioridad / instancia | Trabajo | Estado | Responsable | Revisor |
|---|---|---|---|---|---|
| INT-02 | Coordinación | Actualizar main con la rama remota más reciente, conservar diagramas y publicar | cerrada | Codex, sesión 2026-11-03 | Autorrevisión de sincronización |
| INT-01 | Coordinación | Integrar ramas en main y actualizar copia local preservando cambios | en_revision | Codex, sesión 2026-11-02 | Autorrevisión; independiente pendiente |
| C-00 | Coordinación | Incorporar instrucciones, fuentes, decisiones y esta cola | cerrada | Codex, sesión 2026-10-21 | Autorrevisión documental registrada; no independiente |
| R-01 | Alta / revisión entrega 2 | Sustentar desglose y HH de ramas 1.1 y 1.4 antes de presupuestar | pendiente | Sin asignar | Sin asignar |
| R-02 | Alta / herramienta | Evitar PDF antiguo o inválido en salida de entrega | pendiente | Sin asignar | Sin asignar |
| R-03 | Alta / diseño | Revisar afirmación de MFA de la botonera | pendiente | Sin asignar | Sin asignar |
| R-04 | Media / entrega 2 | Resolver equivalencia de actores S2/S6 | en_revision | Claude, vía LC-02 (DEC-018) | Pendiente |
| R-05 | Media / entrega 2 | Alinear organigrama y dotación por período | en_revision | Claude, vía LC-02 (DEC-017); faltan Figuras 1.1 y 1.2 | Pendiente |
| R-06 | Media / entrega 2 | Resolver ubicación del motor de conciliación | cerrada | Claude, sesión 2026-10-29 (vía S13-01) | David (Grupo 1), revisada el 2026-10-29 |
| R-07 | Media / herramienta | Hacer que --revisar señale errores mediante código de salida | pendiente | Sin asignar | Sin asignar |
| R-08 | Media / forma | Revisar nueve avisos de tablas explicativas | pendiente | Sin asignar | Sin asignar |
| R-09 | Verificación / entrega 2 | Compilar propuesta completa y revisar PDF finales | pendiente | Sin asignar | Sin asignar |
| R-10 | Media / documentación | Conciliar pendientes históricos del README con evidencia actual | pendiente | Sin asignar | Sin asignar |
| F-01 | Alta / forma | Llevar a 9 pt las cartas Gantt de T-14 y las figuras de S4 sin origen en draw.io | en_revision | Claude, sesión 2026-10-21 | Pendiente (sólo autorrevisión) |
| F-02 | Alta / forma | Figuras 4.10 y 4.21 a 4.24 de S4 en vista general y por partes, a 9 pt por parte | en_revision | Claude, sesión 2026-10-31 (a pedido del usuario, Grupo 2) | Pendiente (sólo autorrevisión) |
| S13-01 | Alta / entrega 2 | Corregir S13: ubicación del motor de conciliación (DEC-014 / R-06) y cuantificación del beneficio de la innovación 4 (O-13.1) | cerrada | Claude, sesión 2026-10-29, por encargo de David (Grupo 1) | David (Grupo 1), revisada el 2026-10-29 |
| F-03 | Alta / presentación | Dependencias y ruta crítica en las cartas Gantt de las ramas de T-14 | en_revision | Claude, sesión 2026-10-29, rama grupo6 | Pendiente (sólo autorrevisión) |
| LC-01 | Media / lectura de cierre | Corregir erratas, oraciones rotas, citas inexistentes e indicios «dudosos» que señaló la Primera Revisión del Informe 2 y que siguen en el LaTeX | en_revision | Claude, sesión 2026-11-03, rama claude/kind-heisenberg-egckbe | Pendiente (sólo autorrevisión) |
| LC-02 | Alta / revisión del profesor | Corregir lo pendiente de la Primera Revisión del Informe 2 tomando la decisión de menor cambio; figuras en md aparte | en_revision | Claude, sesión 2026-11-03, rama claude/kind-heisenberg-egckbe, a pedido del usuario | Pendiente (sólo autorrevisión) |
| LC-03 | Alta / revisión del profesor | Figuras de las decisiones de LC-02 y 800 HH del plan de riesgos dentro de la EDT (T-14, T-15, S7, S8) | en_revision | Claude, sesión 2026-11-04, rama claude/kind-heisenberg-egckbe, a pedido del usuario | Pendiente (sólo autorrevisión) |
| E3-01 | Planificada / entrega 3 | Documento económico, planilla, flujo, curva S, VAN/TIR e innovaciones | pendiente | Sin asignar | Sin asignar |
| E3-02 | Planificada / entrega 3 | Prototipo navegable y evidencia de requisitos UX/UI | pendiente | Sin asignar | Sin asignar |

## Fichas y criterios de aceptación

### INT-02 — Actualización local preservando diagramas

- **Autorización:** solicitud del usuario de traer lo más actualizado, conservar su carpeta `diagramas/`, hacer commit y push.
- **Responsable y base:** Codex, sesión 2026-11-03; `main` en `f778818`. La rama remota más reciente es `origin/claude/kind-heisenberg-egckbe` en `c994e1a`, que contiene la base y cinco commits posteriores.
- **Alcance y archivos previstos:** integrar esos commits sin editar su contenido técnico y registrar la sincronización en `TAREAS.md`. No modificar ni incorporar al índice `diagramas/`, que está excluida de Git.
- **Preservación:** respaldo externo de los dos archivos locales en `C:/Users/Claudio Cabello/.codex/backups/tokens-overfore-diagramas-20261103-204601/`, con manifiesto SHA-256 previo.
- **Criterio:** integración sin conflictos, reglas y diferencias verificadas, comparación SHA-256 sin cambios en diagramas y push de `main` con comprobación de igualdad con `origin/main`. Las revisiones técnicas existentes mantienen su estado.
- **Validación 2026-11-03:** integración sin conflictos; contenido idéntico a `c994e1a` salvo esta ficha de coordinación. `python compilar.py --reglas`: 0 errores y los 9 avisos existentes de R-08. `git diff --cached --check`: sin errores. Los dos archivos de `diagramas/` conservan nombres, tamaños y SHA-256 del manifiesto previo; no se incorporan al índice.
- **Límite y revisión:** sólo sincronización y autorrevisión; no se editó contenido técnico ni se repitió la compilación completa. LC-02 conserva su evidencia de compilación de origen y su revisión independiente pendiente. Ninguna tarea técnica se cierra con esta sincronización.
- **Publicación:** commit de integración de esta ficha en `main`, con push autorizado a `origin/main`; el historial remoto registra el resultado. Cierre de coordinación condicionado a comprobar igualdad de ambas ramas después del push.

### C-00 — Coordinación inicial

- **Base:** `37b529c7016e9d7bb53090fcfdc840bdf0603240`. Alcance autorizado: documentación y commit local de coordinación, no correcciones de la oferta.
- **Archivos:** `AGENTS.md`, `CLAUDE.md`, `FUENTE_DE_VERDAD.md`, `DECISIONES.md`, `TAREAS.md`, `README.md`, prompt de revisión e informe archivado en `revision-comision/`.
- **Criterio:** instrucciones comunes sin reglas duplicadas para Claude, 15 decisiones con estado y fundamento, matriz de consumidores, tareas de todos los hallazgos y pendientes de entrega 3 separados. Corregir orden de fuentes del prompt según Art. 5 y BTT 1.3, sin cambiar las bases.
- **Validación 2026-10-21:** comprobación de 8 documentos y 37 enlaces locales, 15 IDs de decisión únicos y 13 fichas con su fila en la cola: sin errores. `git diff --check`: sin errores. Autorrevisión de las relaciones, estados y fuentes del cambio documental; sin revisión independiente. No se modificaron fuentes LaTeX ni herramientas, por lo que no se recompiló la propuesta. Los comandos de reglas previos no cuentan como verificación de un cambio técnico posterior.
- **Commit de cierre:** el commit documental que incorpora esta ficha; localizarlo con `git log -- TAREAS.md`. No se inserta su propio hash en el contenido para evitar una referencia circular. R-01 a R-10 y E3-01/E3-02 permanecen pendientes.

### R-01 — Desglose y estimación de la EDT

- **Origen:** comparación de ramas del informe; DEC-011. Autoridad: T14, T15, S7, alcance S3 y caso, capítulo 13.
- **Alcance previsto:** S7, T14/T15/T18 y figuras; revisar arrastre a S1, S6, S8, S9 y S13. Responsable, revisor y commit de partida: por asignar.
- **Criterio:** distinguir HH de duración; justificar paquetes grandes de módulos, conectores y migración por resultados, perfiles y productividad. Presentar desglose verificable, sin repartir paquetes para igualar conteos ni usar sprints como única prueba de tamaño. Comprobar que integración, canales y pruebas no se cobren dos veces. Reconciliar sumas, capacidad mensual, hitos y curvas; actualizar fuentes y consumidores si cambia el esfuerzo. No existe un nuevo total aprobado.

### R-02 — Publicación de PDF sólo tras éxito

- **Origen:** hallazgo 3. Archivo previsto: `latex/compilar.py`, sólo cuando una tarea autorice corregirlo.
- **Criterio:** una compilación fallida, tablas largas o falta de estabilización no deben publicar resultados inválidos ni mezclar archivos anteriores con la nueva entrega. Probar el caso de un PDF antiguo existente y un fallo posterior; verificar también publicación normal tras éxito. El informe contiene reproducción aislada, no una corrección.

### R-03 — Identidad y MFA de botonera

- **Origen:** hallazgo 4; DEC-007. Archivos previstos: S4/ADR-07, T12 y consumidores de identidad S3, S5, S7, S8 y S9.
- **Criterio:** delimitar acceso/autenticación y declaración de autoría, identificar requisito exacto, amenaza y controles. No presentar la asignación del despacho o certificado del dispositivo como prueba suficiente de segundo factor del operador. Si hace falta otro factor, justificarlo para guantes, turnos y operación sin enlace. Registrar resolución y propagarla a figuras y pruebas.

### R-04 — Actores S2/S6

- **Origen:** hallazgo 5; DEC-012. Archivos previstos: S2/A2, S6 y figuras; contrastar S3, S7 y S8.
- **Criterio:** catálogo único o equivalencia explícita 19/14 que cubra todos los actores; ajustar matrices, comunicaciones y fórmula de canales para el universo realmente usado. No sustituir 91 por 171 sin resolver la agrupación.

### R-05 — Dotación y organigrama

- **Origen:** hallazgo 6; DEC-013. Archivos previstos: S1/A1, figura 1.2, T14/T15 y menciones S6/S7.
- **Criterio:** cada cantidad debe tener perfil y período; conciliar 5 en figura frente a 8/7 en texto con la nivelación real. Distinguir personas, perfiles y equivalentes de jornada completa. No aprobar una dotación por copiar el mayor número.

### R-06 — Ubicación del motor de conciliación

- **Origen:** hallazgo 7; DEC-014. Archivos previstos: S13/A13/T19; consumidores S3/S4/S5/S7/S9.
- **Criterio:** definir qué se ejecuta en Nodo y qué en nube, qué ocurre sin enlace y qué capacidad se utiliza; alinear texto, diagrama, pruebas y base del costo operacional. No decidir sólo cambiando una palabra.

### R-07 — Estado de --revisar

- **Origen:** hallazgo 8. Archivo previsto: `latex/compilar.py`, cuando se autorice corregirlo.
- **Criterio:** código de salida distinto de cero si la pasada falla y cero si tiene éxito; demostrar ambos casos. Que imprima ERROR no satisface el contrato del comando.

### R-08 — Tablas explicativas

- **Origen:** hallazgo 9. Archivos previstos: S3, S4 y, si se mueve detalle, A4; Comunicado 10, sección 5.
- **Criterio:** evaluar los nueve avisos contra contenido real. Pasar explicaciones a prosa o detalle de anexo, conservar motivos y alternativas ADR, actualizar referencias y revisar integración en PDF. No eliminar fundamento para silenciar avisos ni rebajar reglas comunes.

### R-09 — Validación de compilación y PDF

- **Origen:** límite de la revisión inicial. Alcance: 31 documentos y salida completa, en un solo proceso de compilación coordinado.
- **Criterio:** reglas, compilación completa estable, revisión de referencias, foliación, texto/tablas/figuras legibles al tamaño impreso. Registrar entorno, commit y resultado. Al 2026-10-21 sólo se verificaron reglas (0 errores, 9 avisos), 901 referencias y 147 llamadas a imágenes estáticas; compilación integrada de S1 agotó el tiempo. Esto no prueba que las fuentes no compilen. No declarar verificadas las 1.273 páginas del README sin render actual.

### R-10 — Pendientes históricos y estado del README

- **Origen:** README, «Estado actual», e inspección de figura 6.10 que ya dice OpenTofu.
- **Alcance:** contrastar organigrama S1, figuras 6.10/6.11, EDT T14, RBS S8, dotación, beneficio de innovación 4 y actores. No se da por revisada la figura 6.11 a partir de la 6.10.
- **Criterio:** cada pendiente queda con evidencia de resolución o tarea concreta; verificar beneficio de innovación 4 en S13/A13/T19 sin inventar un valor nuevo. Actualizar el README y el registro; no borrar un pendiente por antigüedad.

### F-01 — Letra mínima de 9 pt en figuras de T-14 y S4

- **Origen:** medición de figuras bajo 9 pt sobre los PDF (Art. 40.4 de las Bases administrativas; Comunicado 10, §4), pedida por el usuario el 2026-10-21. Base: `45010f3`.
- **Alcance autorizado:** las 18 cartas Gantt de T-14 (C.1 a C.18) y las 11 figuras de S4 que no estaban en el draw.io del equipo (4.1, 4.16, 4.19, 4.26, 4.27, 4.28, 4.32, 4.33, 4.34, 4.35 y 4.36). Sin cambios de texto, color ni contenido; sólo tamaño de letra y reparto del espacio. Las 14 figuras de S4 que ya están en el draw.io del equipo y las de S1, S3, S5 a S9 quedan fuera.
- **Archivos:** PNG de esas figuras, su origen en `figuras/drawio/` (un `.drawio.xml` por figura y uno combinado por documento), `\figura` con el ancho real y entorno `horizontal` en T-14 y S4, `*-ref.aux` y `comun/folios.tex` recalculados.
- **Criterio:** letra mínima de 9 pt medida en el PDF compilado; mismo contenido que el PNG anterior. C.1 usa filas apretadas por decisión del usuario.
- **Validación 2026-10-21:** `python compilar.py --reglas`: 0 errores (los 9 avisos de R-08). Compilación completa: 31 documentos sin error, 1.283 folios (antes 1.273: S4 pasa de 113 a 122 páginas y T-14 de 128 a 129). Letra mínima medida en el PDF compilado: 9,00 pt en las 29 figuras. Comparación visual de cada figura nueva con la anterior hecha por el autor. Revisión independiente pendiente.

### F-02 — Figuras 4.10 y 4.21 a 4.24 de S4: vista general y por partes

- **Origen:** `revision-comision/Revision_Informe2_OVERFORE_v2.md` y `revision-comision/Figuras_bajo_9pt.md` (S4: 4.10, 4.21, 4.22, 4.23 y 4.24 bajo 9 pt); Art. 40.4 de las Bases administrativas y Comunicado 10, §4 (vista general y después las partes, sin recortes ni ampliaciones). Base: `6c8f675` (`main`), integrado en `grupo2`.
- **Alcance:** sólo S4. Figuras 4.10, 4.21, 4.22, 4.23 y 4.24 con páginas de draw.io entregadas por el usuario (`OVERFORE_S4_figuras_v4.drawio.xml`, sin modificar su diseño). El `.tex` integrado incluye además los grupos por partes de 4.6, 4.8 y 4.15 (`s4-revision-6a/6b`, `8a/8b`, `15a/15b`), de la integración previa con Codex (rama local `codex/s4-figuras-20261031`); su revisión no está registrada aquí. Reemplazan las versiones agrandadas de 4.10, 4.15, 4.21 y 4.22 del commit `56cd40b` (Gabriel Sanzana, 2026-10-29): sus PNG de 45 MB y XML dejan de usarse y se retiran; se avisa a Gabriel.
- **Archivos:** `latex/subdoc04/subdocumento/OVERFORE-Subdocumento4.tex` (grupos de figuras, textos de presentación y referencias); `figuras/s4-revision-*.png` (los `.pdf` no se versionan, ver `.gitignore`) y `figuras/drawio/s4-revision-*.drawio.xml` más `OVERFORE_S4_figuras_v4_general_y_partes.drawio` como origen. Las figuras antiguas reemplazadas se retiran de `figuras/`.
- **Criterio:** texto de 9 pt o más en cada parte, medido en el PDF compilado; numeración 4.10, 4.10a, 4.10b, 4.21 a 4.21d, 4.22 a 4.22b, 4.23 a 4.23c, 4.24a y 4.24b (la 4.24 no tiene vista general); cada figura citada en el texto antes de aparecer.
- **Validación 2026-10-31:** `python compilar.py --borrador` sobre S4 suelto: sin errores de reglas (avisos de R-08 sin cambio) y PDF de 145 páginas. Letra medida en el PDF compilado: 9 pt o más en todas las figuras salvo la vista general de la 4.23, de unos 6,9 pt; ésta es el plano de conjunto que acompañan las partes 4.23a a 4.23c, que cumplen. **Pendiente:** compilación completa de los 31 documentos con foliación continua y recalcular `*-ref.aux` y `comun/folios.tex` (cambió la paginación de S4); actualizar `Figuras_bajo_9pt.md`; revisión independiente. No se afirma que la propuesta completa compile.

### S13-01 — Motor de conciliación e innovación 4 en S13

- **Origen:** DEC-014 / R-06 y observación O-13.1 de `revision-comision/Revision_Informe2_OVERFORE_v2.md`; DEC-015 y R-10. Se divide de R-06 para el alcance de esta rama; R-06 sigue enlazada.
- **Rama y base:** `grupo1` (Grupo 1), con `origin/main` incorporado en `05eaa60`.
- **Alcance:** `latex/subdoc13/` (S13, A13, T-19). No se modificaron otros subdocumentos.
- **Motor de conciliación:** alternativa A (nube; el Nodo de Faena conserva el balance del turno con los factores vigentes), aceptada por David (DEC-014); la meta de 24 h vale con el enlace disponible.
- **Criterio:** texto, figuras, T-19, anexo y pruebas con una sola ubicación del motor y su comportamiento sin enlace; beneficio de la innovación 4 en horas y días hábiles con derivación reproducible y supuesto explícito; sin precios; sin tocar totales del T-15. Validar con `python compilar.py --reglas` y compilación de los documentos afectados.
- **Estado 2026-10-29:** aplicado el Bloque 1 (motor en la nube, balance del turno en el Nodo, meta de 24 h «con el enlace disponible») en S13 (innovación 3: diseño de la incorporación, impacto económico y tabla del indicador), T-19 (filas del motor) y A13 (prueba de detección), y unificado «un día hábil» en S13 (innovación 4, «Problema que resuelve»).- **Innovación 4 (O-13.1):** cuantificada como hipótesis de diseño (DEC-016: 16, 12 y 10 HH al mes por bloque; 208, 436 y 304 HH en 2029, 2030 y ene-ago 2031; 948 en total; cambio funcional de 5 a 1 día hábil) en S13 (impacto económico), T-19 (ficha 4), A13 (D.3 y tabla F). No se creó un SUP nuevo: el A13 ya declara sus hipótesis de diseño en su tabla F, y un SUP nuevo obligaría a cambiar el conteo de 35 supuestos en S2 y A2.
- **Revisión:** revisada por David (Grupo 1) el 2026-10-29. Decisiones de David el 2026-10-29: figura A.1 del A13 (9,1 pt, en el límite) se deja como está; «Efecto en el costo operacional» de la ficha 4 del T-19 se reescribe sin modificar otros subdocumentos.
- **Validación:** `python compilar.py --reglas` con 0 errores; compilación completa (`python compilar.py`): 31 documentos sin error en 4 pasadas, 1.296 folios (S13 folios 1213 a 1246, A13 1247 a 1279, T-19 1280 a 1296, 17 págs.); «Efecto en el costo operacional» del T-19 reescrito y T-19 recompilado sin cambio de folios; letra de las figuras medida con `herramientas/medir_figuras.py` (S13 sin figuras bajo 9 pt; A.1 en 9,1 pt, aceptada por David). Cerrada el 2026-10-29 por indicación de David.
### F-03 — Dependencias y ruta crítica en las cartas Gantt de T-14

- **Origen:** pedido del usuario el 2026-10-29 para la presentación. Base: `bcd1ac7`, rama `grupo6`. Sin cambios de fechas, barras, paquetes ni EDT.
- **Fuentes:** tabla «Red de precedencias y cálculo de la ruta crítica» del T-14 (A01–B11, holgura cero = ruta crítica) y dependencias que el texto del proyecto declara con «tras», «después», «antes de» o «una vez», cada una con su cita.
- **Representación:** flecha entre barras de la misma figura; código del paquete predecesor junto a la barra cuando está en otra figura; borde rojo en los paquetes de actividades con holgura cero. Las 18 cartas llevan la leyenda completa. C.1 encadena las fases del Art. 17° (borde rojo en las seis fases de la ruta crítica) y el inicio de la Operación; las cartas de rama unen además cada paquete con el hito que gatilla, según la tabla de hitos del T-14. En C.16 a C.18 el inicio de los servicios de 1.8 depende del paso a producción de la Etapa 2 (1.6.4.2), y 1.8.10.1 del plan de reversibilidad (1.1.9.2); cuando la barra ocupa todo el ancho, el código va dentro de ella.
- **Legibilidad (2026-10-29, segunda pasada):** en las cartas de rama se quitaron las líneas verticales hacia la fila de hitos, que cruzaban barras y etiquetas; el rombo del hito ya está en la fila del paquete y una flecha une el fin de la barra con él. Flechas de 1,8 pt con trazo ortogonal según el tipo de relación (FC, CC, FF), y llegada al mes intermedio de la barra cuando la red lo indica (1.4.3.4→1.4.2.1). Las predecesoras de otra figura van en un recuadro con flecha a la barra e indican tipo y desfase cuando no son FC sin desfase. Un recuadro rojo a la derecha de cada barra crítica nombra la sucesora crítica en otra figura (una por actividad de la red). Se agregó 1.6.2.2→1.7.5.2 (FC, T-14 línea 2090). C.2 no tiene dependencias declaradas entre sus paquetes.
- **Tercera pasada (2026-10-29), por observaciones del usuario:** etiquetas de hitos de la fila superior separadas cuando se tocan (H9 y H10); predecesoras que no caben en una línea van en un recuadro de dos líneas en el espacio libre de la fila vecina (1.4.5.1), en vez de texto blanco que salía de la barra; flechas entre paquetes con un tronco común por predecesor, que baja junto al fin de la barra y entra al sucesor por la izquierda, dibujadas detrás de las barras; puntas de flecha más pequeñas (trazo 1,6); la leyenda «Ruta crítica» muestra el recuadro y la flecha roja. C.1 usa el mismo trazo. Revisión visual de las 18 cartas con tres agentes; los cruces que quedan son de la línea roja de inicio de la Operación con H12, que es de la carta original.
- **Dependencias del texto no dibujadas** porque contradicen las fechas de las barras: 1.1.5.2→1.4.2.3, 1.6.2.2→1.4.4.3, 1.4.6.3→1.4.4.2, 1.2.1.2→1.4.2.1, 1.6.5.1→1.6.3.1, 1.6.5.1→1.6.3.2, 1.6.4.2→1.6.5.3, 1.6.2.2→1.7.5.1, 1.6.3.1→1.7.3.3 y 1.8.8.3→1.8.4.1. Requieren decisión del equipo.
- **Observaciones de la revisión con las bases (no corregidas):** el cálculo CPM no tiene errores aritméticos y la ruta crítica cierra en H5, H7, H10 y H12 (Art. 17). La carta Gantt muestra H10 en 1.4.6.4 y 1.5.2.2, que la tabla de hitos no lista; la ventana de A15 (mes 5) empieza antes que la barra de 1.4.3.4 (mes 6); la fila A01 de la tabla PERT dice «Meses 1 a 2» con Z = 4,00.
- **Validación 2026-10-29:** reglas sin errores, T-14 compila con 129 páginas (folios sin cambio) y la letra mínima de las 18 cartas mide 9,00 pt en el PDF. Revisión independiente pendiente.
- **Validación de la tercera pasada:** reglas sin errores; T-14 con 129 páginas; letra mínima 9,00 pt en C.1 a C.15 y 9,02 pt en C.16 a C.18.
- **Validación de la segunda pasada:** reglas sin errores; T-14 compila con 129 páginas (folios sin cambio; el párrafo explicativo se compactó para no agregar página) y la letra mínima de las 18 cartas mide 9,00 pt en el PDF, incluidos los recuadros de código. Revisión independiente pendiente.

### LC-01 — Lectura de cierre tras la Primera Revisión del Informe 2

- **Estado:** en_revision. Responsable: Claude, sesión 2026-11-03, a pedido del usuario («qué cosas son obvias de corregir»). Commit de partida: `e7f2195` (main). Revisión independiente pendiente.
- **Origen:** `revisiones-profesor/G01 - OVERFORE - Primera Revisión Informe 2.pdf` y `revision-comision/Revision_Informe2_OVERFORE_v3.md`. Cada frase citada por el profesor como errata se buscó en el LaTeX actual; sólo se corrigen las que siguen.
- **Alcance:** correcciones locales de redacción y de referencias que no cambian decisiones, cifras ni compromisos. Se agrega `\externos{S6}` al T-9 para que resuelvan sus referencias al S6.
  - S2 2.2.3: «referencia de la industria» → «meta interna de 25 minutos» (caso, cap. 7.2, columna «Meta interna», verificado en el PDF del caso).
  - Oraciones rotas: S3 (2), S4 (párrafo SOLID), S5 (3); puntos pegados en S4, T-14 y S13.
  - S4: se retira la frase de plantilla «Las Figuras 4.Xa, 4.Xb presentan este recorrido por partes» en 4.6 y 4.8; en 4.15 se fusiona con el párrafo anterior porque es la única cita de esas figuras.
  - T-9: «Figura 6.4a/6.4b» → referencias a las Figuras de S6 que existen (ecosistema y matriz de poder e interés).
  - T-12, RT-19.08 y RT-19.10: «Tabla 6.2» inexistente → Formulario T-9, Tabla «Plan de comunicaciones».
  - S8-Anexos: el Comunicado 10 se atribuye al mandante (CMAA, 2026d) y no al docente; T-16: se retira esa entrada, que no se citaba.
  - S8: leyenda de la Figura 8.3 sin la «zona inherente» que la figura no muestra.
  - Declaraciones de IA: sin cambios. El paso a mayúscula de los nombres de herramienta se revirtió a pedido del usuario; las celdas quedan como en `e7f2195`.
- **Clase (autorizado por el usuario el 2026-11-03):** `latex/comun/overfore.cls`, línea 225, `\newcommand` → `\newcommand*` en `\ov@textoIA`. La comparación `\ifx` con el `\def` de `\seccionsinnumero` nunca era verdadera, por lo que la excepción que deja a la tabla de la Declaración de uso de IA pasar de página no se activaba y la compilación normal se detenía en 9 subdocumentos. Las demás tablas del cuerpo siguen limitadas a una página. Comprobado con un documento mínimo; `python compilar.py` (modo normal): 31 documentos sin error, estable en 5 pasadas, 1.317 folios, PDF en `latex/salida/` (no versionados).
- **Fuera de alcance (requiere decisión del equipo):** 14 frente a 19 grupos de interés (DEC-012), dotación del S1 (DEC-013), sitio y correo institucional, figuras bajo 9 pt, parciales del T-12, EDT y Gantt del S7, riesgos internos del S8.
- **Validación 2026-11-03:** `python compilar.py --reglas`: 0 errores (los 9 avisos de R-08). `python compilar.py --borrador`: 31 documentos sin error, estable en 3 pasadas, 1.317 folios; la compilación normal sigue detenida por la Declaración de IA (fuera de alcance). T-9 recompilado tras agregar `\externos{S6}`: 0 referencias indefinidas; T-12, S4 y S8-Anexos también con 0. Cada corrección se comprobó en el texto de los PDF: «Tabla 6.2» 0, «presentan este recorrido» 0, «Moya» 0, «zona inherente» en la leyenda 0. Entorno: TeX Live 2023 en Linux. No se versionan PDF ni auxiliares. Sólo autorrevisión.

### LC-02 — Pendientes de la Primera Revisión del Informe 2 con decisiones de menor cambio

- **Estado:** en_revision. Responsable: Claude, sesión 2026-11-03, a pedido del usuario: «hacer todos los cambios posibles y tomar las decisiones que menos cambien». Commit de partida: `f778818`. Revisión independiente pendiente.
- **Criterio de decisión:** ante una contradicción gana la fuente con más consumidores (T-14/T-15 para dotación y HH; S2/S3 para interesados) y se corrige el documento que menos arrastra. Decisiones registradas en DEC-017 a DEC-021.
- **Corregido:**
  - S1: ISO/IEC 42001 en un solo párrafo, roles del JP en el Anexo E, 45 personas explicadas, «meses 14 y 15» en el Anexo F, escala de las referencias argumentada, correo con dominio propio y sin sitio personal.
  - S2: Tabla 2.5 («1» en vez de «SUP-30»), leyenda de la Figura 2.1, citas de Google con a/b/c, nueva subsección de conceptos de la industria (conciliación, liquidación con arsénico e IEC 62443) con dos referencias.
  - S3: análisis de escalabilidad (qué se satura primero), coherente con S4.
  - S4: fuente PMI retirada de los ocho ADR y su referencia; fin de soporte de Angular 22 (noviembre de 2027); frase repetida «se desarrollan en el Subdocumento 5».
  - S5: SSO como imagen indexada; histórico ambiental con resolución diaria (DEC-020); celda RTO de la Tabla 5.5 sin explicación.
  - S6 y T-9/T-10: 19 grupos y 171 canales (DEC-018); autorización de la ventana entre sesiones; acreditación del personal y traspaso a TI; anillos para tabletas.
  - S7 y T-14: justificación del primer nivel de la EDT y de las etapas; paquetes de nivel de esfuerzo; imputación en la Tabla 7.1; holgura cero y primera defensa; criterio del 1.4.6.2 explicado con la regla del tres; texto de la rama 1.7.
  - S8, A8 y T-16: justificación de las respuestas con beneficio/costo bajo 1; R-10 en la tabla de temas del caso; R-15 fuera de la exposición agregada (5,06 → 2,01, 60 %); precisión redondeada; páginas relativas en fuentes.
  - S9, A9 y T-17: TMMi junto a SAMM; capacidad de interacción en segundos; pruebas en detenciones justificadas; puerta 5 sin pasos en detención; criterio 14 en H7 y H12; remisión a T-14; escalamiento de campañas atrasadas.
  - S13, A13 y T-19: valorización de la innovación 1 (USD 0,95 a 1,4 millones al año, beneficio del cliente); innovación 3 en toneladas y defensa frente a la práctica habitual; rama 1.7 en 3.000 HH; innovación 5 con cuatro módulos; páginas relativas en fuentes.
- **Fuera de alcance (requiere el equipo o rehacer cálculos):** figuras ([Figuras_Pendientes.md](revision-comision/Figuras_Pendientes.md)); reglas de negocio del Cap. 17.1; parciales del T-12; ADR de región y CIO y conversión de ADR a texto; latencia y costo de Brazil South; LTE del rajo; CPM con duraciones estimadas y reserva de cronograma; medida de tamaño; sacar los riesgos internos y agregar los externos del S8; 704 + 96 HH en T-14/T-15; reserva de gestión; Montecarlo; volumen; lectura de cierre humana.
- **Validación 2026-11-03:** `python compilar.py --reglas`: 0 errores (los 9 avisos de R-08). `python compilar.py` en modo normal: 31 documentos sin error, estable en 3 pasadas, 1.326 folios (9 más que antes por el texto agregado). Entorno: TeX Live 2023 en Linux. Las cifras nuevas quedaron en `FUENTE_DE_VERDAD.md`; las 800 HH preventivas del S8 quedan como conflicto abierto. No se versionan PDF ni auxiliares. Sólo autorrevisión.

### LC-03 — Figuras de LC-02 y 800 HH del plan de riesgos en la EDT

- **Estado:** en_revision. Responsable: Claude, sesión 2026-11-04, a pedido del usuario («las fotos pendientes… y también el cambio de la EDT y HH… exportar con 300 ppp»; «edt, riesgos y gantt»). Revisión independiente pendiente.
- **Figuras (300 ppp, mxGraph desde `diagramas/Diagramas OVERFORE.drawio`; curvas con matplotlib):** 1.1, 1.2, 6.4, 6.5 y 9.1 (commit `2457afa`); B.1/7.1, B.2, C.2, D.1/7.2 y D.2. Medidas en [Figuras_Pendientes.md](revision-comision/Figuras_Pendientes.md); todas sobre 9 pt.
- **EDT y HH (DEC-022):** paquetes 1.1.3.3 (704 HH) y 1.1.3.4 (96 HH); 1.1.3 renombrado «Gestión y respuesta a riesgos»; total 183.866 HH en 177 paquetes; ramas 1.1–1.7 61.194 HH; implementación 57.654 y operación 126.212 HH; 45 personas como máximo, sin cambio. Actualizados T-14 (fichas, PERT, roles, perfiles, ramas), T-15 (etapas, tabla mensual, operación, paquetes), S7, S8 y S8-Anexos (umbrales sobre 61.194 HH). Gantt C.2 en sus tres copias draw.io.
- **Fuera de alcance (sigue pendiente):** registro de riesgos sin los internos y con los externos (tarea siguiente); dependencias, sprints, puertas y reserva en las cartas Gantt (F-03); figuras 4.23, 4.36, 6.7, 6.9, 7.3, 7.4 y 9.3.
- **Validación 2026-11-04:** `python compilar.py --reglas`: 0 errores (los 9 avisos de R-08). `python compilar.py` en modo normal: 31 documentos sin error y sin referencias indefinidas, 1.328 folios. Figuras medidas con el método de `medir_figuras.py`. Entorno: TeX Live 2023 en Linux. No se versionan PDF ni auxiliares. Sólo autorrevisión.

### E3-01 — Economía de entrega 3

- **Origen:** hallazgo 1, reclasificado por confirmación del usuario; T22, informe 3. No es defecto de entrega 2.
- **Dependencia:** resolver o fijar una línea base explícita de R-01 antes de aprobar costos. Datos comerciales externos o supuestos deben identificarse y fecharse.
- **Criterio:** proveedores/adquisiciones, costos justificados, curva S monetaria, inversión y operación, RRHH, administración, proveedores, flujo mensual/acumulado, VAN/TIR y valorización de cinco innovaciones reconciliados con EDT, dotación y calendario. Separar propuesta económica de oferta técnica. Documentar supuestos y evitar doble conteo de beneficios.

### E3-02 — Prototipo de entrega 3

- **Origen:** hallazgo 2 reclasificado; BTT, capítulo 25 y RT-25.01 a RT-25.10; T12. No es defecto de entrega 2.
- **Criterio:** enlace navegable, alcance de vistas y flujos, mapa del sitio y navegación, sistema de diseño y evidencia de resoluciones y accesibilidad exigidas. Acreditar publicación y disponibilidad mínima; no sustituirlo por sitio institucional ni promesas de desarrollo contractual. Registrar dónde está el prototipo si se mantiene en otro repositorio.

### INT-01 — Integración de ramas en main

- **Estado:** en_revision. Responsable: Codex, sesión 2026-11-02. Revisión: autorrevisión; revisión independiente pendiente.
- **Autorización y base:** solicitud del usuario de integrar las demás ramas en main y actualizar después el checkout local. Base remota: `6c8f675`; base local: `b6d2c0e`.
- **Alcance:** integrar secuencialmente `origin/grupo2` (`5b6d43b`) y `origin/grupo6` (`bffbe21`); las demás ramas sólo aportan historial o ya están integradas. Preservar todos los cambios locales sin commit mediante respaldo antes del pull.
- **Archivos previstos:** `TAREAS.md`, cambios existentes de S4 y T-14 con sus figuras y draw.io, y derivados `*-ref.aux` y `latex/comun/folios.tex` si la compilación completa termina correctamente. Sin rediseño ni cambios en herramientas comunes.
- **Criterio:** merges sin conflictos sin resolver, reglas verificadas y compilación completa intentada con su resultado registrado; push de main y pull local fast-forward; restauración comprobada del trabajo previo. No cerrar las revisiones técnicas F-01/F-02/F-03 por el mero hecho de integrar.

- **Conflicto de coordinación resuelto:** grupo2 y grupo6 usaron F-02 para tareas distintas. Se conserva F-02 de grupo2 y se identifica como F-03 la tarea de Gantt de grupo6 (antes F-02 en esa rama), sin borrar sus antecedentes. Se conservaron ambas fichas y S13-01.

- **Validación de integración 2026-11-02:** `python compilar.py --reglas`: 0 errores y los 9 avisos ya registrados en R-08. `python compilar.py`: 31 documentos sin error, estable en 4 pasadas, 1.318 folios; S4: 149 páginas (394–542), T-14: 129 páginas (874–1002). Se actualizan los derivados de referencias y folios; no se versionan PDF ni auxiliares nuevos. Los 43 XML/draw.io modificados están bien formados; los 18 IDs de tarea son únicos y coinciden entre tabla y fichas; el enlace Markdown de TAREAS existe; sin marcadores de conflicto ni cambios en clase, reglas o compilador. Todas las ramas remotas son antecesoras del resultado. Autorrevisión de la integración; F-01, F-02 y F-03 mantienen su revisión técnica independiente pendiente.

- **Resultado de sincronización:** integración publicada en `origin/main` (`8df17a3`), seguida de `git pull --ff-only origin main` en el checkout original. Comparación `main...origin/main`: 0 commits de diferencia. Restauración verificada de las 45 rutas previas: fuentes ya integradas conservan su evolución; LEEME, reorganización local de las bases y herramienta de referencias quedan como trabajo local sin commit. Los derivados antiguos se conservan en respaldo y stash; en el checkout quedan los recompilados. Respaldo externo en `C:/Users/Claudio Cabello/.codex/backups/LATEX-INFORME3-antes-merge-20261102/` y stash `20b1a8d38d775f0ab7db960223d4915745a1fbf0`, ambos retenidos. `git diff --check`: sin errores. Integración y actualización ejecutadas; estado en_revision por revisión independiente pendiente, sin cerrar F-01/F-02/F-03.
