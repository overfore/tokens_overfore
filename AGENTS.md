# Instrucciones compartidas para agentes

Estas instrucciones aplican a todo el repositorio y a cualquier herramienta de IA. El objetivo es conservar las decisiones de ingeniería y permitir correcciones verificables entre subdocumentos. Las instrucciones explícitas del usuario para la tarea tienen prioridad; no alteran por sí mismas las exigencias de la licitación.

## Lectura inicial

1. Leer [FUENTE_DE_VERDAD.md](FUENTE_DE_VERDAD.md): estado de entrega, fuentes, datos y mapa de documentos.
2. Consultar [DECISIONES.md](DECISIONES.md): motivos, alternativas, dependencias y conflictos del tema que se va a modificar.
3. Consultar [TAREAS.md](TAREAS.md): trabajo pendiente, responsable, archivos afectados y criterio de cierre.
4. Leer la exigencia original en `bases/` y `comunicados/`, el subdocumento afectado y sus formularios y figuras. El resumen de otro agente no sustituye las fuentes.

El estado actual es **entrega 2; entrega 3 en preparación**. No denunciar como incumplimiento actual la ausencia de artefactos que corresponden a una entrega posterior.

## Antes de editar

- Revisar `git status --short`, rama y commit de partida. No sobrescribir trabajo ajeno, descartar cambios, hacer reset, limpiar archivos ni reescribir historial para facilitar una tarea.
- Registrar o reclamar una tarea en `TAREAS.md`: responsable identificable, commit de partida, alcance y archivos previstos. La tabla coordina, pero no es un bloqueo técnico. Si otro agente reclama los mismos archivos, acordar la separación o integrar secuencialmente; no asumir que el último en guardar tiene razón.
- Identificar las decisiones que dependen del cambio y sus consumidores mediante el mapa de `FUENTE_DE_VERDAD.md` y búsquedas en `.tex`, tablas, anexos y figuras. No cambiar un valor compartido sólo donde se encontró.
- Distinguir hechos del caso, restricciones, decisiones documentadas, supuestos y propuestas pendientes. Una contradicción abierta no tiene un valor ganador por defecto.
- Las correcciones locales y reversibles dentro del alcance autorizado pueden avanzar sin pedir permiso para cada edición. Si falta una decisión del equipo que cambia alcance, tecnología o compromisos, preparar alternativas y evidencia, registrar el conflicto y solicitar esa decisión antes de propagarla.

## Al cambiar una decisión

- Conservar el motivo y las alternativas del registro existente. No reemplazar una decisión por preferencia de herramienta, estilo del modelo o porque otro documento usa otro valor.
- Registrar un nuevo ID `DEC-NNN`, fecha, estado, fuente, motivo, alternativas, consecuencias, documentos afectados, validación y decisión reemplazada. No reutilizar IDs ni borrar el historial de decisiones sustituidas.
- Un agente puede proponer una decisión, pero no atribuir aprobación humana o de la comisión sin evidencia. El estado «documentada» sólo indica que el repositorio la declara.
- Actualizar fuente de origen, consumidores, `DECISIONES.md`, `FUENTE_DE_VERDAD.md` y la tarea en el mismo cambio coherente. Si la actualización excede el alcance asignado, dejar el cambio como propuesta sin integrar parcialmente una nueva línea base.
- No inventar la razón histórica de una decisión. Si el texto no la explica, registrar «fundamento no localizado» y una tarea de investigación.

## Edición y validación

- Los contenidos de la oferta se editan en `latex/subdocNN/`. La documentación de coordinación se mantiene en los Markdown de raíz y `revision-comision/`.
- No modificar `latex/comun/overfore.cls`, `latex/comun/reglas.py` ni `latex/compilar.py` salvo que la tarea autorice expresamente ese archivo o función. Que exista una tarea pendiente no es autorización automática para ejecutarla.
- Usar los comandos de la clase y conservar títulos obligatorios, nombres de archivo, referencias APA y separación entre oferta técnica y económica. No introducir precios de oferta en los subdocumentos técnicos.
- No ejecutar dos compilaciones sobre el mismo checkout simultáneamente: comparten auxiliares, referencias y folios. No versionar PDF ni auxiliares nuevos como parte de una tarea documental; respetar la excepción existente de `*-ref.aux`.
- Para cambios de contenido, ejecutar desde `latex/`: `python compilar.py --reglas` y la compilación del documento afectado. Para cambios que alteran paginación, la entrega requiere compilación completa y foliación continua. Si no hay compilador o falla el entorno, informar el límite y dejar la validación pendiente; nunca afirmar que el PDF compila por haber pasado las reglas.
- Para cambios sólo de documentación, comprobar enlaces locales, consistencia de IDs, fuentes y `git diff --check`. No exigir recompilar toda la propuesta sin cambios de contenido.

## Revisión y cierre

El autor presenta: qué cambió, por qué, fuentes y decisiones utilizadas, documentos afectados, verificaciones ejecutadas y límites pendientes. El revisor contrasta las fuentes y recalcula las cifras relevantes; no valida sólo por concordar con el autor.

Para un cambio técnico compartido, revisar con la sección 8 de [Prompt_Revision_Subdocumentos.md](revision-comision/Prompt_Revision_Subdocumentos.md) y comprobar texto, tabla y figura de ambos lados. Si hay un revisor independiente disponible, registrar su identidad y resultado. Si sólo hubo autorrevisión, indicarlo: la revisión independiente queda pendiente y la tarea permanece `en_revision`.

Una tarea sólo pasa a `cerrada` cuando cumple su criterio de aceptación, tiene evidencia de validación y registra revisión. Los hallazgos automáticos o de IA se registran como observaciones hasta comprobar su fundamento; no se convierten en exigencias de las bases.

Al hacer commit, incluir únicamente archivos propios de la tarea. No incorporar cambios ajenos ni hacer push, merge o publicación sin autorización aplicable. El commit de coordinación inicial sólo incorpora documentación; no resuelve por sí mismo las tareas técnicas.
