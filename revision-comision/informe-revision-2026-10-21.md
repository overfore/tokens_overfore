# Revisión de LATEX-INFORME3

> Diagnóstico interno archivado para seguimiento. Describe la revisión anterior al commit de coordinación; no es una aprobación de la comisión. El estado de cada corrección se mantiene en `TAREAS.md` en la raíz.

Fecha: 21 de octubre de 2026. Commit revisado: `37b529c7016e9d7bb53090fcfdc840bdf0603240`.

Repositorio: https://github.com/claudioignav/LATEX-INFORME3

## Dictamen

La base documental está bien organizada y tiene una automatización útil. El usuario confirmó que el repositorio corresponde al cierre de la entrega 2 y que la entrega 3 se desarrollará después. Por tanto, la ausencia de artefactos económicos y del prototipo no se considera un defecto de la entrega actual: son pendientes de la siguiente instancia. Sí hay defectos concretos del compilador y contradicciones técnicas que sus reglas no detectan.

La revisión comprende el inventario completo, las reglas de los 31 documentos, las referencias e imágenes y una lectura selectiva de las bases, arquitectura, alcance, metodología, planificación e innovaciones. No constituye una comprobación exhaustiva de cada cifra, cita bibliográfica o especificación de proveedor.

## Hallazgos prioritarios

### 1. Pendiente de la siguiente entrega: entregables económicos del Informe 3

El Formulario T-22 exige proveedores y adquisiciones clave, curva S, costos, VAN y TIR y valorización de las cinco innovaciones. Además exige una planilla con gastos operacionales, inversión, administración, recursos humanos, proveedores y flujo mensual y acumulado. No hay planillas XLSX/XLS/CSV ni una propuesta económica identificable en el repositorio. Las curvas de horas del T-15 no sustituyen el flujo monetario.

Evidencia: `bases/bases-administrativas.md`, sección «Informe y presentación 3», desde la línea 2795 aproximadamente; `latex/subdoc07/formulario-T-15/OVERFORE-Formulario-T-15.tex`, líneas 297–322. La ausencia se limita a este repositorio: podrían existir entregables externos que no se incorporaron.

Acción: preparar el documento económico y la planilla con trazabilidad hacia las actividades y perfiles de T-14 y T-15. Mantener los montos de oferta fuera de los subdocumentos técnicos, conforme al Art. 50.2.

### 2. Pendiente de la siguiente entrega: prototipo interactivo para Informe 3

Las Bases Técnicas Transversales, capítulo 25.1, exigen el prototipo con el Informe 3. No se encontró su implementación ni un enlace de entrega identificado. El propio T-12 deja pendientes la publicación del enlace, interactividad y otros criterios de RT-25.01 a RT-25.09. El enlace institucional de Overfore no constituye por sí mismo evidencia del prototipo.

Evidencia: `bases/bases-tecnicas-transversales.md:1419`; `latex/subdoc03/formulario-T-12/OVERFORE-Formulario-T-12.tex:502` y filas siguientes.

Acción: incorporar enlace verificable, mapa del sitio, flujos navegables y evidencia de las resoluciones y accesibilidad exigidas. Si vive fuera del repositorio, documentar dónde está y cómo se evalúa.

### 3. Alta: una compilación fallida puede exportar un PDF antiguo a salida/

En `todo()`, el script copia cualquier PDF existente al directorio de entrega antes de comprobar errores de compilación, tablas largas o falta de estabilización. Si un documento compiló anteriormente y luego falla, el PDF viejo sigue existiendo y se copia como si perteneciera a la entrega actual. El proceso termina con código 1, pero la carpeta que se describe como lista para entregar ya queda poblada.

Evidencia: `latex/compilar.py:233`, copia; `latex/compilar.py:241`, comprobación posterior. Reproducción aislada con un PDF anterior y compilación simulada fallida: el archivo se exportó y el proceso terminó con código 1.

Acción: validar todo antes de publicar; preparar la salida en un directorio temporal y reemplazar la entrega sólo después del éxito completo. Evitar que queden archivos de una entrega previa mezclados con la nueva.

### 4. Alta: el contraste con el despacho no demuestra un segundo factor de autenticación

El ADR-07 y la sección de identidad llaman «segundo factor» a comprobar que la credencial coincide con el operador asignado a la pala. Esa asignación es un dato que ya tiene el sistema; no demuestra que quien presenta la credencial controle otro factor. Una persona con la credencial ajena puede pasar la misma comparación si la asignación permanece vigente. El certificado de la botonera autentica el dispositivo, no demuestra por sí solo la identidad del operador.

Evidencia: `latex/subdoc04/subdocumento/OVERFORE-Subdocumento4.tex:235`, 238 y 716. NIST SP 800-63B-4 exige demostrar posesión y control de dos factores distintos para AAL2: https://pages.nist.gov/800-63-4/sp800-63b.html#aal2

Acción: describir este mecanismo como comprobación de coherencia de la autoría, delimitar si esa acción exige MFA y, cuando corresponda, aportar un factor independiente. La revisión detecta una afirmación no sustentada del diseño; no verifica un sistema implementado ni afirma que toda interacción de la botonera esté obligada a MFA por las bases.

### 5. Media: el universo de interesados cambia entre S2 y S6 sin equivalencia

S2 identifica 19 grupos, 14 internos y 5 externos. S6 gestiona 14 grupos y calcula 91 canales potenciales. Si se tratara del mismo universo de 19 grupos, serían 171. Una agrupación distinta puede ser válida, pero debe existir un mapeo explícito que muestre quién representa a cada grupo y garantice su cobertura.

Evidencia: `latex/subdoc02/subdocumento/OVERFORE-Subdocumento2.tex:159` y 181; `latex/subdoc06/subdocumento/OVERFORE-Subdocumento6.tex:63`, 70 y 84.

Acción: unificar el catálogo o documentar la agrupación y ajustar matriz, figuras, comunicaciones y cálculo.

### 6. Media: el organigrama no coincide con la dotación de desarrollo

La figura 1.2 muestra «5 desarrolladores en tres equipos Scrum». El texto de S1 indica ocho desarrolladores en M3–M11 y siete en M13–M17. La imagen no señala un período que explique esa diferencia y, como resumen del equipo, deja una dotación contradictoria.

Evidencia: `latex/subdoc01/subdocumento/OVERFORE-Subdocumento1.tex:118`; imagen `latex/subdoc01/subdocumento/figuras/fig-1-2-organizacion-proyecto-sitco-aranda.png`, inspeccionada visualmente.

Acción: actualizar la figura desde la misma fuente de dotación que T-15 o indicar claramente el período representado.

### 7. Media: ubicación contradictoria del motor de conciliación

S13 ubica el motor en los servicios del Nodo de Faena. Doce líneas después justifica su costo operacional diciendo que el cálculo se ejecuta en la nube. Sin aclarar qué cálculo corre en cada sitio, queda incierto el dimensionamiento y su comportamiento cuando falla el enlace.

Evidencia: `latex/subdoc13/subdocumento/OVERFORE-Subdocumento13.tex:166` frente a 178.

Acción: fijar la ubicación y, si hay procesamiento en ambos sitios, distinguir funciones, recursos y operación sin conexión.

### 8. Media: --revisar no comunica el fallo mediante el código de salida

`revisar()` imprime los errores de la pasada, pero no termina con un estado de error ni devuelve uno que el bloque principal use. Un proceso automático que mire sólo el código de salida puede aceptar una revisión fallida.

Evidencia: `latex/compilar.py:286` y bloque principal. Una pasada simulada con error devolvió `None`, sin lanzar `SystemExit`; el script alcanza su final normal.

Acción: terminar con código distinto de cero si hay fallos. Agregar una prueba de ese contrato del comando.

### 9. Media: nueve avisos incluyen formatos que el comunicado rechaza

La ejecución real de `--reglas` produjo nueve avisos «concepto-descripcion»: uno en S3 y ocho registros ADR de S4. El Comunicado 10, sección 5, rechaza las tablas explicativas del tipo «Concepto / Descripción» en el cuerpo. El detector es heurístico, pero las ocho tablas ADR efectivamente organizan explicaciones por campo. Un aviso no equivale a aceptación de la comisión.

Evidencia: `comunicados/comunicado-10-estructura-obligatoria.md`, sección 5; `latex/subdoc04/subdocumento/OVERFORE-Subdocumento4.tex:153` y ocho tablas sucesivas hasta la línea 244; S3, línea 318.

Acción: convertir la explicación en prosa, conservar una síntesis comparativa cuando corresponda y llevar el registro completo al anexo.

## Aspectos bien resueltos

- Separación de bases, comunicados, plantillas y propuesta; README con responsables y mapa de documentos.
- Clase LaTeX común que concentra identidad visual, títulos, tablas, portadas y foliación.
- Archivos separados para subdocumentos, anexos y formularios; referencias mediante etiquetas en vez de numeración manual.
- Reglas automáticas de estructura, marcadores, tablas y referencias previas que reducen errores repetitivos.
- Arquitectura vinculada al caso: continuidad sin enlace, separación OT/IT, escritor único por agregado, bandeja de salida transaccional y consumidores idempotentes.
- Innovaciones con indicadores, hitos y distinción entre compromisos y beneficios esperados sujetos a supuestos.
- T-14/T-15 vinculan actividades, horas, etapas y perfiles, una base útil para construir la evaluación económica.

## Verificación realizada y límites

- Repositorio clonado con historial y remoto originales. La ruta local de la sesión no es una condición del proyecto.
- Inventario: 31 documentos, correspondientes a 10 subdocumentos, 9 archivos de anexos y 12 formularios.
- Ejecución real de `python compilar.py --reglas`: código 0, 0 errores y 9 avisos.
- Revisión estática adicional: 901 usos de referencias locales y externas y 147 llamadas a imágenes; no se detectaron etiquetas de destino, declaraciones de documentos externos ni archivos de imagen faltantes. Es una comprobación de existencia, no una validación de la exactitud semántica ni de la numeración renderizada.
- Dos reproducciones aisladas del compilador con simulación controlada, sin modificar sus fuentes: exportación de PDF antiguo tras error y falta de señalización de error en `--revisar`.
- Inspección visual de dos figuras originales: organigrama del proyecto e integración continua. La figura 6.10 ya dice OpenTofu, aunque el README todavía la enumera entre los pendientes por Terraform.
- No se encontró XeLaTeX accesible en las rutas que prueba el script. La compilación integrada de S1 terminó con «Compilation timed out» y «exec failed: sandbox error: command timed out». Ese resultado no permite atribuir un error a las fuentes ni confirmar su compilación. No se confirma una compilación completa ni la legibilidad de las 1.273 páginas declaradas por el README.
- Los subdocumentos 10, 11, 12 y 14 y el T-8 faltan, pero T-22 no los exige en la lista técnica del Informe 2. Su ausencia no se usa aquí como evidencia suficiente de incumplimiento de esa entrega. La brecha específica del Informe 3 se fundamenta en sus entregables económicos y el capítulo 25.
- Al realizar este diagnóstico no se habían cambiado archivos versionados ni publicado correcciones. El posterior commit de coordinación incorpora documentación; no resuelve por sí mismo los hallazgos.

## Comparación específica de las ramas 1.1 y 1.4 de la EDT

El conteo de los paquetes hoja y la suma de sus HH en T-15 dan lo siguiente:

| Rama | Paquetes | Esfuerzo | Ventana declarada de la rama |
|---|---:|---:|---|
| 1.1 Dirección del proyecto | 29 | 5.088 HH | M1–M51, con actualizaciones puntuales del plan de salida después de la implementación |
| 1.4 Software del sistema | 28 | 21.062 HH | M1–M21 |

La razón es 21.062 / 5.088 = 4,14 veces el esfuerzo. No es una relación entre duraciones de calendario: las ramas tienen actividades concurrentes, dedicaciones distintas y recurrencias. La coordinación principal de ambas abarca M1–M21; 1.1 se extiende hasta M51 por actualizaciones puntuales, no por dirección continua de la implementación durante 51 meses.

Que software requiera cuatro veces las HH de dirección puede ser razonable para este caso. Construir la solución híbrida, sus módulos, conectores, canales, operación sin enlace y migración es una carga distinta de administrar el proyecto. El número de paquetes no es una unidad de tamaño ni exige igual esfuerzo por paquete.

La observación válida es la granularidad desigual. En 1.1 se separan productos como un acta de 24 HH y un espacio colaborativo de 16 HH. En 1.4 quedan como paquetes individuales el integrador de siete sistemas y radio de faena (1.520 HH), el módulo de Operación Mina (1.280 HH) y la digitalización de 193.000 formularios (3.184 HH). El promedio por paquete es de 175,45 HH en dirección y 752,21 HH en software. Los promedios son descriptivos; mezclan trabajo recurrente, coordinación y productos distintos.

Un paquete grande no es inválido por su tamaño si tiene límites, responsable, aceptación y una descomposición operativa verificable. La digitalización, por ejemplo, aporta volumen, puestos y jornadas como fundamento. Para Operación Mina, T-14 calcula 80 HH por 16 sprints = 1.280 HH, pero esa multiplicación muestra una asignación de capacidad, no demuestra por sí sola que el alcance funcional quepa en ella. El propio documento indica que obtiene O y P por factores y despeja M para reproducir E: ese PERT no aporta una estimación independiente de la cifra inicial.

Recomendación: conservar las ramas y descomponer los paquetes grandes de software en resultados verificables del caso —carguío y transporte, declaración de material, captura de detenciones, integración con despacho y operación sin conexión, según los límites de cada módulo— o adjuntar su desglose operativo por funcionalidades. Estimar y reconciliar las HH desde ese desglose, con perfiles y productividad sustentados, evitando duplicar trabajo ya incluido en canales, integración y pruebas. No multiplicar artificialmente paquetes para igualar conteos ni reducir HH sólo para que las ramas parezcan parejas.

Evidencia: `latex/subdoc07/formulario-T-15/OVERFORE-Formulario-T-15.tex`, filas de las ramas 1.1 y 1.4; `latex/subdoc07/formulario-T-14/OVERFORE-Formulario-T-14.tex:129`, 1309, 1349 y 1512. El caso exige coexistir con los sistemas existentes y justifica distribuir las etapas por dependencias y riesgos en su capítulo 13; el Comunicado 10, sección 7.1, exige paquetes estimables y asignables.

## Orden propuesto de trabajo

1. Sustentar el desglose y las HH de los paquetes grandes de software antes de valorizar la entrega 3.
2. Corregir la publicación de salida del compilador y el código de salida de `--revisar`.
3. Alinear identidad/MFA, actores, organigrama y ubicación del motor.
4. Resolver las tablas explicativas y actualizar los pendientes del README.
5. Desarrollar los artefactos económicos y el prototipo de la siguiente entrega sobre la planificación revisada.
6. Ejecutar la compilación completa y revisar visualmente los PDF finales antes de preparar el ZIP.
