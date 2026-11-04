# Registro de decisiones y fundamentos

Fecha de incorporación: 2026-10-21. Fuentes inspeccionadas en `37b529c7016e9d7bb53090fcfdc840bdf0603240`.

Este registro conserva el porqué de lo que ya está escrito. **No aprueba retrospectivamente el diseño.** Los ADR de S4 se declaran aceptados el 5 de octubre de 2026 dentro de la propuesta; esa declaración se registra como antecedente documental, no como una aprobación humana comprobada por esta revisión.

## Estados y cambios

- `documentada`: elección vigente en las fuentes, sin validación independiente nueva.
- `en_revision`: hay una observación concreta o evidencia incompleta; no propagar una solución supuesta.
- `propuesta`: alternativa nueva todavía no adoptada.
- `confirmada`: resolución con evidencia explícita de quién la adoptó y cómo se verificó.
- `sustituida`: se conserva y enlaza al ID que la reemplaza.

Al crear una decisión, usar un ID nuevo y los campos: estado, fecha, fuente, contexto, decisión, motivo, alternativas, consecuencias, consumidores, validación/aprobación y reemplaza. Las entradas iniciales no reemplazan decisiones anteriores. No borrar su motivo al corregirlas; agregar la resolución y, si corresponde, una entrada sucesora. Toda entrada nueva debe citar su archivo y sección o etiqueta estable; una línea sola puede desplazarse.

Los ADR-01 a ADR-08 se encuentran en [S4, registro de decisiones de arquitectura](latex/subdoc04/subdocumento/OVERFORE-Subdocumento4.tex), sección 4.1.2. Las etiquetas `tab:registro-decision-adr-XX-...` permiten localizar sus tablas. Las justificaciones resumidas a continuación provienen de esas tablas.

## DEC-001 — Un servicio desplegable por módulo

- **Estado:** documentada; origen S4 ADR-01, tabla `tab:registro-decision-adr-01-servicios-modulares`.
- **Contexto y decisión:** nueve módulos, cinco también en faena; adoptar nueve servicios modulares, cada uno con almacén y ciclo de versión propios.
- **Motivo:** despliegue independiente y operación por TI del cliente; la matriz de la propuesta asigna 4,35 a servicios modulares, 2,80 a monolito y 3,20 a microservicios de grano fino.
- **Alternativas y consecuencias:** monolito limita independencia; microservicios añaden complejidad operativa. La elección exige contratos versionados y compatibilidad nube/Nodo.
- **Consumidores:** S3, S4, S5, S7/T14, S9 y S13. Cambiar cantidad o nombres exige revisar módulos, dominios y EDT juntos.
- **Validación:** se localizó fundamento; no se revalidaron pesos ni factibilidad de todas las tecnologías. Aprobación independiente no registrada.

## DEC-002 — Cinco módulos en faena y un escritor por agregado

- **Estado:** documentada; origen S4 ADR-02, tabla `tab:registro-decision-adr-02-nodo-faena`; S5, 5.1.1.
- **Decisión:** Operación Mina, Trazabilidad y Embarque, Conciliación Metalúrgica, Acreditación y Acceso, y Seguridad y Salud Ocupacional tienen funciones locales. Cada agregado tiene un único sitio escritor.
- **Motivo:** faena debe continuar durante cortes; almacenar para reenviar no basta para validar portería ni calcular balances. Escritura activa del mismo agregado en ambos sitios crearía conflictos.
- **Alternativas y consecuencias:** se descartan Nodo sólo de reenvío y réplica completa con doble escritura. Maestros y hechos se sincronizan conservando propietario, orden y bitácora.
- **Consumidores:** S3, S4, S5/A5, S7, S8, S9 y S13. No convertir una copia local de lectura en una segunda fuente de escritura sin nueva decisión.
- **Validación:** evidencia documental, sin prueba de operación sin enlace. Conflicto de ubicación del motor: DEC-014 / R-06.

## DEC-003 — Eventos con entrega al menos una vez e idempotencia

- **Estado:** documentada; origen S4 ADR-03, tabla `tab:registro-decision-adr-03-integracion-eventos`.
- **Decisión:** bandeja de salida transaccional, orden por agregado, identificador de origen y deduplicación en consumidores.
- **Motivo:** varios módulos consumen el mismo hecho y los cortes deben retrasar su entrega sin perderlo.
- **Alternativas y consecuencias:** llamadas síncronas dependen del enlace; el ADR evalúa también un bus con interfaz Kafka. La elección exige consumidores idempotentes; no afirmar entrega exactamente una vez de extremo a extremo por esta decisión.
- **Consumidores:** S3, S4, S5, S6/T10, S7 y S9. Una sustitución de bus requiere reevaluar garantías y pruebas, no sólo nombres.
- **Validación:** no se comprobaron por separado las afirmaciones comparativas sobre todos los productos del ADR.

## DEC-004 — Un conector por sistema existente

- **Estado:** documentada; origen S4 ADR-04, tabla `tab:registro-decision-adr-04-conector-sistema`.
- **Decisión:** conectores propios con capa anticorrupción en el Integrador de Sistemas.
- **Motivo:** mantener sistemas existentes, aislar sus interfaces poco documentadas y evitar que un cambio externo obligue a modificar varios módulos.
- **Alternativas y consecuencias:** frente a integración punto a punto y plataforma comercial central. El inventario y el supuesto SUP-16 determinan interfaces reales; cambios de interfaz afectan esfuerzo y riesgo.
- **Consumidores:** S2/A2, S3/T12, S4, S5, S7/T14/T15, S8 y S9.
- **Validación:** arquitectura documentada; estimación agregada de conectores pendiente de revisión en R-01.

## DEC-005 — Historiador mediante espejo y diodo de datos

- **Estado:** documentada; origen S4 ADR-05, tabla `tab:registro-decision-adr-05-lectura-historiador`.
- **Decisión:** espejo en DMZ industrial alimentado por diodo; cliente OPC UA con Read y Subscribe. Selección de 5.000 señales cada cinco segundos, frente a 14.500 etiquetas existentes.
- **Motivo:** evitar flujo hacia la red de control y disponer de datos dentro del turno.
- **Alternativas y consecuencias:** cliente directo tras cortafuegos o exportación de archivos; se debe dimensionar espejo, conectores y almacenamiento. 5.000 señales seleccionadas no reemplaza la volumetría del historiador del caso.
- **Consumidores:** S4/T11, S5, S7, S8, S9 y S13.
- **Validación:** diseño declarado; compatibilidad de infraestructura y prueba del diodo no ejecutadas.

## DEC-006 — Botonera y aplicación con contenedor nativo

- **Estado:** documentada; origen S4 ADR-06, tabla `tab:registro-decision-adr-06-canales-terreno`.
- **Decisión:** botonera sin pantalla para pala; App SITCO Terreno con núcleo web y contenedor Windows para otras tareas de terreno.
- **Motivo:** guantes, sol y ciclo de trabajo de la pala; la aplicación requiere lector, persistencia y protección de claves que fundamentan el contenedor.
- **Alternativas y consecuencias:** tableta en pala, PWA y aplicación enteramente nativa. El diseño impone condiciones de dispositivos, soporte, actualización y pruebas sin enlace; no imponer una compra distinta sin revisar especificaciones.
- **Consumidores:** S3, S4/T11, S5, S6/T10, S7, S9 y futuro prototipo.
- **Validación:** justificación localizada; no se probó la aplicación. Identidad de la botonera queda separada en DEC-007.

## DEC-007 — Identidad por población; segundo factor de botonera observado

- **Estado:** en_revision; origen S4 ADR-07, tabla `tab:registro-decision-adr-07-identidad-poblacion`, y sección 4.1.8.
- **Decisión documentada:** directorio federado para personal propio, identidad externa para terceros y credencial/PIN para acceso local. La botonera no usa PIN y el texto llama segundo factor al contraste con el operador asignado en despacho.
- **Motivo declarado:** evitar administrar todas las identidades temporales en el directorio corporativo y no depender de biometría sin acuerdo sindical.
- **Alternativas y consecuencias:** todas las identidades en directorio o biometría obligatoria. Cambiar el mecanismo afecta usabilidad, autoría y funcionamiento sin enlace.
- **Observación:** asignación conocida por el sistema y certificado del dispositivo no demuestran por sí solos un segundo factor del operador. No concluir automáticamente que toda interacción de botonera exige MFA: primero delimitar la acción y el requisito.
- **Consumidores:** S2/A2, S3/T12, S4, S5, S7, S8, S9 y prototipo. **Tarea R-03.** Resolución/aprobación pendiente.

## DEC-008 — Almacenes por módulo y analítica separada

- **Estado:** documentada; origen S4 ADR-08, tabla `tab:registro-decision-adr-08-almacen-propio`; S5, 5.1.1.
- **Decisión:** almacén transaccional por módulo y proyecciones/eventos para indicadores, sin lectura directa de la base de otro dominio.
- **Motivo:** las consultas de gestión no deben degradar registro de terreno ni portería.
- **Alternativas y consecuencias:** base compartida o réplica transaccional de lectura. Se requiere consistencia eventual, latencias explícitas y pruebas de aislamiento.
- **Consumidores:** S3, S4, S5/A5, S7, S9 y S13. No unificar esquemas ni añadir consultas cruzadas sólo para simplificar un capítulo.
- **Validación:** decisión documentada, sin prueba de rendimiento nueva.

## DEC-009 — Gestión contractual predictiva y construcción adaptativa

- **Estado:** documentada; origen [S6](latex/subdoc06/subdocumento/OVERFORE-Subdocumento6.tex), introducción, 6.1.1 y 6.2; T9/T10.
- **Decisión:** hitos, líneas base y cambios bajo gestión PMBOK; desarrollo en sprints de dos semanas y prácticas DevSecOps. En operación se declara flujo continuo de mantención.
- **Motivo:** fechas contractuales fijas con detalles que dependen de usuarios y terceros. Se adapta el detalle sin cambiar unilateralmente alcance ni hitos.
- **Alternativas:** no se localizó en este análisis una comparación formal completa; no inventarla.
- **Consumidores:** S7/T14/T15/T18, S8, S9 y S13. Diferenciar refinamiento de cambio contractual.
- **Validación:** coherencia documental parcial; no equivale a validar todas las estimaciones por sprint.

## DEC-010 — Etapas según dependencias y prioridad del caso

- **Estado:** documentada; origen [S3](latex/subdoc03/subdocumento/OVERFORE-Subdocumento3.tex), 3.2.2, y Caso Minería, capítulo 13.
- **Decisión:** el reparto funcional se desarrolla en S3 y debe conservar los meses contractuales. El caso prioriza trazabilidad/conciliación, luego terreno/personas y después analítica avanzada, pero exige criterio propio para el reparto.
- **Motivo:** exigencias de compradores, dependencias técnicas, acceso a terceros y capacidad de absorción del cliente.
- **Alternativas y consecuencias:** no copiar el orden de preferencia como si fuera instrucción suficiente. Un traslado entre etapas cambia cronograma, recursos, pruebas, riesgos e innovaciones.
- **Consumidores:** S4, S5, S6, S7, S8, S9, S13 y T12.
- **Validación:** consultar la tabla y explicación originales para cada función; esta entrada no enumera ni redefine todo el alcance.

## DEC-011 — Esfuerzo y nivelación derivados de fichas T14

- **Estado:** en_revision; origen [T14](latex/subdoc07/formulario-T-14/OVERFORE-Formulario-T-14.tex), sección A y diccionario, y [T15](latex/subdoc07/formulario-T-15/OVERFORE-Formulario-T-15.tex), secciones A–C.
- **Decisión documentada:** conservar horas por perfil y repartirlas por igual entre los meses del paquete; los roles continuos incluyen saldos de dedicación. PERT aplica factores y despeja M para reproducir E de la ficha.
- **Motivo declarado:** trazabilidad entre paquetes, meses, curvas y dotación, con hitos contractuales y capacidad de los perfiles.
- **Observación:** 29 paquetes de dirección suman 5.088 HH y 28 de software, 21.062 HH. La diferencia de 4,14 veces es de esfuerzo, no duración. Conteos parecidos no invalidan el reparto, pero hay módulos y conectores completos agrupados y las HH por sprint no sustentan por sí solas el tamaño funcional.
- **Consecuencia:** no reducir software ni multiplicar paquetes para igualar conteos. Revisar desde alcance y productividad, sin duplicar integración, canales y pruebas; actualizar T15 y todos los derivados si cambia la base.
- **Consumidores:** S1, S6, S7/T18, S8, S9, S13 y economía futura. **Tarea R-01.** Resolución/aprobación pendiente.

## DEC-012 — Universo de actores sin equivalencia resuelta

- **Estado:** en_revision; fuentes [S2](latex/subdoc02/subdocumento/OVERFORE-Subdocumento2.tex), 2.4, y S6, gestión de interesados y comunicaciones.
- **Observación:** S2 identifica 19 grupos; S6 usa 14 y calcula 91 canales. Una agrupación puede explicar diferencias, pero no se localizó su equivalencia explícita.
- **Motivo de cada conteo:** S2 distingue internos/externos y ámbitos; el fundamento que reconcilia ambos universos no está localizado. No declarar 19 como solución universal por preferencia.
- **Consecuencias y consumidores:** actores, matrices y figuras de S2/S6; acciones de S3, S7 y riesgos S8. **Tarea R-04.** La resolución debe comprobar cobertura, no sólo cambiar una cifra.
- **Resolución (2026-11-03):** ver DEC-018. Se adopta el registro de 19 grupos de S2, que S3 ya usa y cuyo Anexo C cubre grupo por grupo.

## DEC-013 — Dotación en texto y organigrama sin período común

- **Estado:** en_revision; fuente [S1](latex/subdoc01/subdocumento/OVERFORE-Subdocumento1.tex), 1.5, figura 1.2, A1 y T15.
- **Observación:** texto declara 8 desarrolladores M3–M11 y 7 M13–M17; figura 1.2 muestra 5 sin período.
- **Fundamento:** el texto vincula dotación con períodos de T15; no se localizó una justificación temporal del 5 de la figura. No elegir dotación nueva sin nivelación.
- **Consecuencias y consumidores:** A1, S6, S7/T14/T15 y figuras; separar personas distintas de equivalentes de jornada completa. **Tarea R-05.** Resolución pendiente.
- **Resolución (2026-11-03):** ver DEC-017. Se adopta la dotación de A1 (Anexo F), que coincide con T14/T15; las Figuras 1.1 y 1.2 quedan pendientes de redibujo.

## DEC-014 — Motor de conciliación con ubicación contradictoria

- **Estado:** documentada el 2026-10-29 (resolución abajo); antes en_revision. Fuente [S13](latex/subdoc13/subdocumento/OVERFORE-Subdocumento13.tex), 13.3, apartados de integración y costos (líneas 166 y 178 en la base inspeccionada).
- **Observación y motivos declarados:** integración ubica motor en Nodo de Faena; el costo bajo se fundamenta en cálculo por turno en nube ya dimensionada. No se localizó una separación de funciones que reconcilie ambos textos.
- **Consecuencias:** validar continuidad sin enlace y recursos antes de decidir dónde corre cada parte. Consultar DEC-002 y DEC-008.
- **Consumidores:** S3, S4, S5, S7/T14/T15, S9, A13, T19 y economía futura. **Tarea R-06.**
- **Resolución (2026-10-29):** alternativa A, aceptada por David (Grupo 1) en la sesión de trabajo; no hay aprobación del equipo completo ni revisión independiente. El motor (factores y sesgo) corre en la nube; el Nodo de Faena conserva el balance del turno con los factores vigentes, que bajan como copia de lectura (S4 ADR-02, S5 5.1.1; un solo sitio escritor). Sin enlace, el Nodo mantiene el balance con los últimos factores y el motor procesa los turnos del corte al sincronizar. La meta de detección en 24 horas vale «con el enlace disponible» y se cuenta desde la sincronización tras un corte. Alternativas descartadas: motor completo en el Nodo (contradice la propiedad de parámetros de S5 y exige capacidad y historia local no dimensionadas) y reparto mixto con detección por turno en el Nodo (más capacidad y esfuerzo).
- **Aplicado en:** S13 (13.3), T-19 (fichas de la innovación 3) y A13 (prueba de detección). **Pendiente en otros grupos:** T-14 1.7.3.2 dice «Motor de reconciliación en la capa analítica», que contradice S5 (esa capa pertenece a Indicadores); T-13 no verifica el balance del turno ni el motor en la prueba de corte de 48 h.

## DEC-015 — Innovaciones distintas del alcance base

- **Estado:** documentada; fuente S13, introducción, tabla `tab:cartera-innovaciones`, secciones 13.1–13.5, A13 y T19.
- **Decisión:** cartera de control anticipado de arsénico, clasificación asistida de detenciones, factores de conciliación con incertidumbre, servicio con traspaso programado y balance de dilución evitada.
- **Motivo:** desarrollar cinco tipos de innovación del Art. 28 y los siete elementos del Art. 29, explicitando qué añaden sobre requisitos base.
- **Consecuencias:** indicadores, línea base, meta y fecha no son intercambiables con beneficios monetarios garantizados. Conservar distinción entre compromiso y beneficio esperado; no sumar dos veces beneficios del alcance base y de la innovación.
- **Alternativas:** consultar justificación de cada innovación en S13/A13; no se registra una selección comparativa global que no se haya localizado.
- **Consumidores:** S3, S4, S5, S7/T14/T15, S8, S9 y economía. Revisar DEC-014 y el pendiente de innovación 4 del README (R-10).
- **Validación:** valor económico pendiente de entrega 3; no adoptar beneficios nuevos para cuadrar VAN/TIR.

## DEC-016 — Hipótesis de carga del traspaso programado (innovación 4)

- **Estado:** propuesta del 2026-10-29, escrita en S13, T-19 y A13 por indicación de David (Grupo 1); sin validación del gerente de servicio ni del equipo. No reemplaza ninguna decisión.
- **Contexto:** el Caso no informa el volumen de solicitudes funcionales; O-13.1 pedía cuantificar el beneficio en horas y días hábiles sin precios (Art. 50.2).
- **Hipótesis:** bloque 1 (informes y tableros) 4 solicitudes de 4 h = 16 HH al mes; bloque 2 (reglas de alerta y plantillas) 3 de 4 h = 12; bloque 3 (usuarios y roles internos) 20 de 0,5 h = 10. Suman 38 HH al mes, un 25 % de una persona a jornada completa (152 HH, T-15). Cambio funcional: 5 días hábiles en el servicio completo (plazo de análisis de impacto de S6) a 1 día hábil con el cliente.
- **Cálculo derivado:** meses del cliente por año con M1 = enero de 2027: bloque 1, 10 + 12 + 8 = 30; bloque 2, 4 + 12 + 8 = 24; bloque 3, 0 + 10 + 8 = 18. Horas: 2029, 160 + 48 = 208; 2030, 192 + 144 + 100 = 436; 2031 (ene a ago), 128 + 96 + 80 = 304; total 948.
- **Coherencia con otros documentos:** 27 solicitudes funcionales al mes frente a los 1.250 contactos mensuales de la mesa de ayuda (A2, SUP-27); la bolsa evolutiva de 960 HH al año (80 al mes, T-14 1.8.5.1) es de cambios extraordinarios y no se toca; el cliente tiene once personas de TI (Caso, cap. 8) y no se exige un especialista dedicado.
- **Límites:** las horas que pasan al cliente no rebajan líneas del T-15 (la mesa trabaja en turnos fijos y la bolsa es fija), por lo que «Efecto en el costo operacional» de la ficha 4 no tiene base en HH; requiere una decisión propia. Con la meta de 80 % al mes 45, hasta un 20 % de las solicitudes sigue en el adjudicatario. Plazo de 5 días hábiles: analogía con S6, no medida.
- **Consumidores:** S13 (13.4, impacto económico), T-19 (ficha 4), A13 (D.3 y tabla de supuestos F), Oferta Económica. **Tarea S13-01 / R-10.** Validación: medición de la mesa de ayuda en los meses 21 a 26.

## DEC-017 — Dotación de apoyo según el Anexo F y el T-15

- **Estado:** documentada el 2026-11-03 por Claude a pedido del usuario («tomar la decisión que menos cambie»); sin validación del equipo. Reemplaza la resolución pendiente de DEC-013.
- **Decisión:** las cifras de dotación son las del Anexo F del S1, que coinciden con las fichas del T-14 y la nivelación del T-15: 8 desarrolladores en M3–M11, 7 en M13–M17; hasta 10 técnicos de terreno; 30 personas de apoyo en M14–M15; 45 personas distintas en M14 con equipo clave y externos.
- **Motivo:** el T-14 y el T-15 sostienen las HH, las curvas, el máximo de 45 y la economía; cambiarlos para igualar las figuras alteraría toda la planificación. Las figuras 1.1 y 1.2 («5 desarrolladores», «3 técnicos») no tenían período ni cálculo.
- **Recálculo:** M13 = 7 + 1 + 2 + 4 + 8 = 22; M14 y M15 = 22 + 8 analistas de operación = 30 (Anexo F). Por eso el anexo pasa de «meses 13 a 15» a «14 y 15».
- **Aplicado en:** S1 (1.2, frase de las 45 personas), A1 (Anexo F). **Pendiente:** Figuras 1.1 y 1.2 ([Figuras_Pendientes.md](revision-comision/Figuras_Pendientes.md)).

## DEC-018 — Un solo registro de 19 grupos de interés

- **Estado:** documentada el 2026-11-03 por Claude a pedido del usuario; sin validación del equipo. Resuelve DEC-012.
- **Decisión:** el registro de interesados de toda la propuesta es el de S2, 2.4: 19 grupos, 14 internos y 5 externos. S6 y T-9 lo adoptan y calculan 171 canales (19 × 18 / 2).
- **Motivo:** S2 y S3 ya usan 19, y el Anexo C de S3-Anexos tiene una estrategia por cada uno; el S6 era el único con 14 y su conjunto no coincidía con los 14 internos (incluía compradores y autoridad ambiental, según la revisión del profesor). Cambiar S6 y T-9 es el menor cambio.
- **Aplicado en:** S6 (6.1.4 y 6.1.5) y T-9 (identificación y canales). **Pendiente:** Figuras 6.4 y 6.5, que dibujan 14 grupos.

## DEC-019 — Contacto institucional sin cuenta gratuita ni sitio personal

- **Estado:** documentada el 2026-11-03 por Claude a pedido del usuario; sin validación del equipo.
- **Decisión:** en la Tabla 1.1 del S1 el contacto pasa a `licitaciones@overfore.cl` y se retira la fila del sitio web, que apuntaba a una página personal en GitHub.
- **Motivo:** el profesor pide «contacto y sitio con dominio de la empresa, o sin sitio web». Retirar la fila es el menor cambio; publicar un dominio propio queda como alternativa del equipo.
- **Límites:** el sitio web sigue siendo el entregable de RT-23.01 a RT-23.04 en la instancia que fija el T-22, y el T-12 conserva su dirección actual hasta que el equipo publique uno con dominio propio.

## DEC-020 — Histórico ambiental migrado con resolución diaria

- **Estado:** supuesto documentado el 2026-11-03 por Claude a pedido del usuario; sin validación del equipo.
- **Decisión:** el histórico de monitoreo ambiental se migra con una lectura por instrumento y día (186 × 365 × 10 = 680.000 filas, 6,3 GB); la resolución de 1.440 lecturas diarias del Anexo D del S4 rige desde que SITCO opera la instrumentación.
- **Motivo:** mantiene el volumen de migración, el almacenamiento y el cronograma ya dimensionados. El caso no informa la frecuencia del histórico existente; si fuera la de la operación, el volumen crecería unas mil veces y se migraría como serie comprimida.
- **Aplicado en:** S5 (5.3.1, tabla de alcance) y S5-Anexos.

## DEC-021 — Compromisos agregados en la lectura de cierre LC-02

- **Estado:** propuesta del 2026-11-03, escrita por Claude a pedido del usuario; requiere validación del equipo antes de la entrega final.
- **Decisiones:** (1) entre sesiones del Comité de Operación, el líder de operación autoriza cada intervención de la ventana de 03:00 a 05:00 con lista de verificación y registro (S6); (2) despliegue por anillos también para la App SITCO Terreno (S6, T-10); (3) TMMi con línea base en M2, nivel 2 en M12 y nivel 3 en M21, junto a SAMM (S9); (4) criterio 14 del caso (90 % de cambios de material con la botonera, ya comprometido en S3) en las condiciones de H7 y H12 (T-17); (5) puerta 5 prohíbe pasar a producción durante una detención programada (S9-Anexos); (6) R-15 se excluye de la exposición agregada para no contar dos veces sus componentes (S8, A8).
- **Motivo:** responden observaciones de la Primera Revisión del Informe 2 sin cambiar HH, hitos ni dotación.
- **Pendiente:** el despliegue por anillos de tabletas no tiene paquete propio en el T-14; si el equipo lo exige, se agrega con horas tomadas de 1.6.4.

## DEC-022 — Las 800 HH del plan de riesgos dentro de la EDT

- **Estado:** documentada el 2026-11-04 por Claude a pedido del usuario, que aprobó las cuatro recomendaciones; sin validación del equipo. Cierra el conflicto abierto en LC-02.
- **Decisión:** (1) las 800 HH preventivas del S8 (Anexo G) pasan a la EDT y el total del contrato sube de 183.066 a 183.866 HH; (2) se agregan dos paquetes bajo el entregable 1.1.3, renombrado «Gestión y respuesta a riesgos» (M1–M21, 1.112 HH): 1.1.3.3 «Medidas preventivas del plan de riesgos» (704 HH, M2–M20, responsable JP) y 1.1.3.4 «Preparación y ensayos de pérdida total de sala» (96 HH, M6–M8, M15 y M21, responsable SRE); (3) el máximo sigue en 45 personas: las horas las ejecutan personas que ya están en el proyecto ese mes; (4) las HH de los riesgos internos que se retirarán del registro (tarea de riesgos) se mantienen en la EDT, porque son trabajo de dirección que igual se hace.
- **Motivo:** el profesor y la regla de zona alta del S8 piden que la respuesta a los riesgos esté en la EDT y el cronograma. Agregarlas como paquetes propios bajo 1.1.3 no mueve los demás paquetes, la dotación ni los hitos.
- **Recálculo:** ramas 1.1–1.7 de 60.394 a 61.194 HH; rama 1.1 de 29 a 31 paquetes y de 5.088 a 5.888 HH; 177 paquetes; implementación 57.654 HH y operación 126.212 HH (32 HH del ensayo de M21); máximo mensual 5.299 HH en M15. Imputación del T-15: M1–M12 a la Etapa 1, M13–M20 a la Etapa 2, M21 a la operación. Los umbrales del S8 (Anexo) se recalculan sobre 61.194 HH.
- **Aplicado en:** T-14 (fichas, clases PERT, roles, perfiles, ramas), T-15 (etapas, tabla mensual, operación, paquetes), S7 (introducción y Tabla 7.1), S8 y S8-Anexos; Figuras B.1/7.1, B.2, C.2, D.1/7.2 y D.2.

## DEC-023 — Registro de riesgos sin riesgos internos y con riesgos externos del caso

- **Estado:** documentada el 2026-11-04 por Claude a pedido del usuario («con los riesgos quítame esos y añádeme los nuevos»), con el criterio de menor cambio; sin validación del equipo.
- **Decisión:** (1) R-01 a R-04 se reformulan como exposición del cliente, como pide la revisión (ventanas de actualización que el cliente aprueba, cambio de servicio de nube que requiere su decisión, crecimiento de su operación, incidente que lo obliga a notificar), con las mismas P, I y respuestas; (2) R-13 se mantiene reformulado como el escepticismo del área de mantenimiento, porque es uno de los seis riesgos que exige el caso (cap. 19) y la revisión lo marca OK en esa función; (3) R-14, R-15, R-18, R-19, R-23 y R-24 se retiran del registro y se muestran en el T-16, sección F, con la medida de la propuesta que los resuelve; sus identificadores no se reutilizan; (4) se agregan R-25 invierno altiplánico (0,350 alta → 0,150 media), R-26 auditoría y recertificación de 2029 (0,125 → 0,030), R-27 exigencias del comprador de enero de 2029 (0,245 alta → 0,100) y R-28 emergencia o paralización (0,100 → 0,060); (5) la RBS conserva siete ramas con los nombres de la figura; la séptima pasa a «Entorno de la faena» y la quinta a «Contrato y plazo».
- **Motivo:** responde la observación crítica del S8 sin rehacer las fichas que quedan, sin renumerar (R-xx se citan en S2, S4, S5, T-12 y T-14) y sin cambiar HH de la EDT: las medidas de los riesgos retirados siguen en 1.1.3.3 (DEC-022).
- **Recálculo:** 22 riesgos; exposición 4,835 → 2,050 (58 %); 3 críticos y 8 altos antes, 12 bajos y 10 medios después; FMEA sobre 11 riesgos (R-25 con RPN 200); contingencia 1.339 HH netas; costo-beneficio de las medidas con costo sigue en 704 HH, 1.250 HH y 1,8. La simulación de la Etapa 1 conserva sus cinco eventos (tres del registro y dos causas internas) y sus resultados.
- **Aplicado en:** S8, S8-Anexos, T-16; Figuras 8.3, 8.4 y 8.6. **Pendiente:** reserva de gestión para lo no identificado y planes de contingencia de los riesgos que mantienen impacto alto (otras observaciones del S8).

## Cobertura y límites del registro inicial

S1 y S2 tienen conflictos registrados; S3 conserva el reparto de alcance; S4 aporta ocho ADR; S5 desarrolla propiedad y migración de datos; S6 define métodos; S7 aporta estimación; S8 gobierna riesgos; S9 pruebas; S13 innovaciones. Sus relaciones están en el mapa de autoridad.

Este registro no pretende haber extraído todas las decisiones, cálculos, certificaciones ni versiones de cada subdocumento. Antes de tocar una elección no registrada, localizar su motivo en el documento y sus bases y agregar una entrada; si falta, indicarlo. Para riesgos y calidad, el fundamento específico está en S8/T16 y S9/T13/T17, no en una justificación inventada por el agente.
