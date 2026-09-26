#### FORMULACIÓN DE PROYECTOS 

BASES TÉCNICAS TRANSVERSALES PARA LA PREPARACIÓN DE LA PROPUESTA 

Versión 1.0 Fecha Documento: 18-08-2026 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

##### Bases Técnicas Transversales 

Requisitos técnicos comunes a las trece industrias del llamado 

|Asignatura|Taller de Formulación de Proyectos Informáticos— ICl-5444|
|---|---|
|Unidad académica|Escuela de Informática, Pontificia Universidad Católica de Valparaíso|
|Profesor|Antonio Moya Villegas— antonio.moyaOpucv.cl|
|Objeto|Remquisiss de Eee,<br>infraestructura, calidad, operación y presentación<br>exigibles a toda solución ofertada|
|Ámbito|Las trece industrias del llamado, sin excepción|
|Documento base|Bases Administrativas TFEP-01/2026( FEPO1.26)|
|Documento complementario|Bases Técnicas del caso asignado a cada empresa proponente|
|Versión|1.0— agosto de 2026|



Este documento fija el piso técnico común del llamado. Todo lo que aquí se exige es exigible en las trece industrias; lo que cada industria tiene de propio —su proceso de negocio, sus volúmenes, sus integraciones y su regulación sectorial — se establece en las Bases Técnicas de cada caso. Los requisitos están codificados como RT-CC.NN y deben responderse uno a uno en el Formulario T-12 de las Bases Administrativas. 

Bases Técnicas Transversales TFEP-01/2026 1/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### CONTENIDO 

||-Disposiciones del documento|Objeto, ámbito, relación con los demás documentos, régimen de<br>o<br>cumplimiento y forma de responder.|1|
|---|---|---|
|II- Arquitectura de la solución|Modelo multicapa de referencia, modelo híbrido de nube y on-<br>premise, ambientes y entrega continua, datos, integración y<br>analítica.|25|
|II!- Infraestructura|Site principal on-premise, site secundario y recuperación ante<br>desastres, hardware, puestos de trabajo y equipamiento de<br>terreno.|6-8|
|IV- Requisitos no funcionales|Desempeñoy capacidad, disponibilidad y resiliencia, seguridad,<br>identidad, usabilidad y accesibilidad, observabilidad, sostenibilidad<br>y certificaciones.|9-15|
|V- Capacidades transversales|Módulos obligatorios en toda industria, canales digitales y<br>o.<br>a.<br>e<br>o,<br>movilidad, inteligencia artificial y automatización.|16-18|
|VI- Proyecto, implantación y<br>operación|Gobierno del proyecto, pruebas y criterios de aceptación, modelo<br>de operación, mesa de ayuda, mantención y capacitación.|7|
|.<br>.<br>.,<br>VII- Exigencias de presentación|Presencia digital del proponente, video de presentación, prototipo<br>.<br>.<br>8.<br>P P<br>:<br>P<br>P<br>P<br>interactivo de interfaz e innovaciones.|23-26|
|VII!- Anexos|Índice de requisitos,<br>plantilla de volumetría, checklist de<br>Ñ<br>da<br>'<br>entregables y glosario.|A-D|



###### Cómo se articula este documento con los demás 

Las Bases Administrativas gobiernan el proceso y el contrato: quién participa, qué garantías rinde, cómo se evalúa, qué plazos rigen y qué se penaliza. Su Capítulo 4 enuncia los requisitos transversales en el nivel de exigencia contractual. 

Este documento desarrolla técnicamente ese Capítulo 4 y lo lleva al nivel de requisito verificable. Donde las Bases Administrativas dicen «la solución deberá tener alta disponibilidad», aquí se dice cuál, medida cómo, probada cuándo y acreditada con qué evidencia. 

Las Bases Técnicas de cada caso, que se publican por separado, aportan el contexto de la industria, el proceso de negocio, los requerimientos funcionales, la volumetría real y los valores concretos de todo requisito marcado «Según caso» en este documento. 

Sobre el nivel de exigencia. 

Este pliego describe una plataforma de misión crítica, no un sistema de gestión convencional. Los umbrales, los estándares y los controles que contiene son los que hoy se exigen en el mercado a un proveedor que opera la infraestructura digital de una empresa. Una propuesta que los trate como formalidades a declarar, en lugar de como decisiones de ingeniería a resolver, quedará en evidencia en la matriz de cumplimiento y en la defensa técnica. 

Bases Técnicas Transversales TFEP-01/2026 2/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### TÍTULO 1 DISPOSICIONES DEL DOCUMENTO 

###### CAPÍTULO 1 - OBJETO, ÁMBITO Y RÉGIMEN DE CUMPLIMIENTO 

###### 1.1 Objeto 

Las presentes Bases Técnicas Transversales establecen los requisitos técnicos, de infraestructura, de calidad, de operación y de presentación que toda solución ofertada en la Licitación N” TFEP-01/2026 debe satisfacer, con independencia de la industria y del caso asignado a cada empresa proponente. 

El propósito de este documento es doble. Primero, fijar un piso técnico común y exigente que impida que la comparación entre ofertas se distorsione por diferencias de interpretación sobre qué es una plataforma de misión crítica. Segundo, liberar a las Bases Técnicas de cada caso de repetir aquello que es común, permitiéndoles concentrarse en lo que efectivamente distingue a una industria de otra: su proceso de negocio, sus volúmenes, sus integraciones, sus regulaciones sectoriales y sus criterios de aceptación propios. 

###### 1.2 Ámbito de aplicación 

Este documento aplica íntegramente a documento aplica íntegramente a aplica íntegramente a íntegramente a a los trece casos del llamado: trece casos del llamado: casos del llamado: del llamado: llamado: 

Este documento aplica íntegramente a documento aplica íntegramente a aplica íntegramente a íntegramente a a los trece casos del llamado: trece casos del llamado: casos del llamado: del llamado: llamado: COC 

||Minería— extrac|ción de recursos||Sala de cine— entre|tenimiento|
|---|---|---|---|---|---|
|2|Logística— empr|esa distribuidora|9|Cadena multitienda|—retail|
|3|Servicios de agua|potable— utilities|10||Transporte de carga||
|4|Consultas médica|s— salud y bienestar|11||Servicios financieros|—banca, seguros y cambio|
|5|Cadena de hotele|s— turismo y hospitalidad|12||Agroindustria||
|6|Portuaria— oper|ación marítima comercial|13|| Telecomunicaciones||
||Servicio de puert<br>marítima|o deportivo— recreación||||
|.3Re<br>sted<br>onfo<br>Bases<br>TFEP-|lación con los de<br>ocumento se lee<br>rme al orden de p<br> Administrativas<br>01/2026|más documentos del proceso<br> conjuntamente con las Bas<br>recedencia del Artículo 5” de l<br>Reglas del proceso, participac<br>adjudicación, contrato, nivele<br>penalidades y exigencia de in<br>cronograma obligatorio de 56<br>requisitos transversales de niv|<br>esAdmi<br>asBases<br>ión,gara<br>sdeserv<br>novación<br> meses(<br>elcontr|nistrativas y con la<br> Administrativas.<br>ntías, evaluación,<br>icio contractuales,<br>.Incluye el<br>Art. 177) y los<br>actual( Capítulo 4).|s Bases Técnicas del cas<br>Prevalecen sobre este<br>documento en materias<br>administrativas y<br>contractuales.|
|Bases<br>Trans<br>docum|Técnicas<br>versales( este<br>ento)|Cómo debe estar construida, <br>operada y presentada la soluc<br>0<br>verificables y comunesa las t|desplega<br>o,<br>ión,ent<br>.<br>rece indu|da, protegida,<br>oo<br>érminos técnicos<br>.<br>strias.|Desarrolla técnicamente el<br>,<br>Capítulo 4 de las Bases<br>o<br>.<br>Administrativas. No lo<br>contradice ni lo rebaja.|



###### 1.3 Relación con los demás documentos del proceso 

Este documento se lee conjuntamente con las Bases Administrativas y con las Bases Técnicas del caso, conforme al orden de precedencia del Artículo 5” de las Bases Administrativas. 

Bases Técnicas Transversales TFEP-01/2026 3/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

||Contexto de la industria, proceso de negocio,|Puede endurecer cualquier<br>requisito de este|
|---|---|---|
|o.<br>Bases Técnicas del caso|requerimientos funcionales, volúmenes reales,<br>.<br>.<br>.<br>.<br>.<br>integraciones, normativa sectorial, ventana operacional y|documento; nunca<br>.<br>rebajarlo. Aporta los valores|
||criterios de aceptación propios del caso.|de los requisitos marcados<br>«Según caso».|



###### 1.4 Régimen de cumplimiento 

Los requisitos de este documento se identifican con un código de la forma RT-CC.NN, donde CC es el número del capítulo y NN el correlativo dentro de él. Cada requisito tiene un carácter: 

||Significado|Efecto en la evaluación|
|---|---|---|
|Obligatorio|Requisito de cumplimiento forzoso. La<br>7<br>o<br>o<br>solución no es admisible sin él.|Su incumplimiento o su omisión producen puntaje<br>cero en el ítem afectado. El incumplimiento de un<br>requisito obligatorio de seguridad, continuidad o<br>arquitectura habilita la exclusión conforme al<br>Artículo 58” de las Bases Administrativas.|
|Deseable|Requisito que el CLIENTE valora pero no<br>exige. Diferencia una oferta buena de una<br>oferta destacada.|Su cumplimiento acreditado otorga puntaje<br>adicional dentro del ftem. Su ausencia no penaliza.|
|Según caso|Requisito obligatorio cuyo valor numérico,<br>umbral o alcance concreto lo fijan las Bases<br>Técnicas del caso.|Se evalúa contra el valor del caso. Si el caso no lo<br>fija, rige el valor por defecto que este documento<br>indique y, en su defecto, el criterio de la Comisión<br>Evaluadora.|



###### 1.5 Cómo debe responderse este documento 

El PROPONENTE deberá acreditar el cumplimiento de la totalidad de los requisitos en el Formulario T-12, Matriz de Cumplimiento Técnico y Trazabilidad, indicando por cada código RT: 

###### 1. Si cumple, cumple parcialmente o no cumple. 

2. El componente, servicio, producto o práctica concreta con que lo satisface, individualizado por nombre y versión. 

3. La sección y página de la Oferta Técnica donde se desarrolla. 

4. La evidencia con que se verificará durante la ejecución: entregable, prueba, informe o certificado. 

Declarar «cumple» sin individualizar el componente ni indicar dónde se desarrolla equivale a no declarar. La Comisión Evaluadora no buscará en la propuesta la respuesta que el PROPONENTE no señaló, y calificará el requisito como no acreditado. 

###### 1.6 Neutralidad tecnológica y criterio de vigencia 

Este documento no impone marcas, productos ni proveedores determinados. Cuando menciona un producto lo hace a título de referencia y admite equivalentes de prestaciones iguales o superiores, lo que el PROPONENTE deberá acreditar. 

Sí impone, en cambio, un criterio de vigencia. Todo componente ofertado —lenguaje, marco de trabajo, motor de base de datos, sistema operativo, biblioteca, dispositivo — deberá contar con soporte vigente del fabricante o de su comunidad al momento de la oferta, y con hoja de ruta de soporte que cubra, como mínimo, la totalidad 

Bases Técnicas Transversales TFEP-01/2026 4/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

del período contractual de 56 meses. El PROPONENTE deberá declarar, por cada componente principal, su versión, su fecha de fin de soporte y su plan de actualización. 

La obsolescencia programada de un componente durante la vigencia del Contrato no es un riesgo del CLIENTE. Si un componente alcanza su fin de soporte antes del mes 56, la actualización o la sustitución es de cargo del ADJUDICATARIO y debe estar prevista y costeada en la oferta. 

###### 1.7 Interpretación de los umbrales 

Todo umbral expresado en este documento es un mínimo exigido, salvo que se indique expresamente que constituye un máximo. Los tiempos de respuesta se entienden medidos en el percentil 95 sobre la experiencia real del usuario final, y no como promedio ni como medición sintética de laboratorio, salvo indicación expresa. 

Las mediciones de disponibilidad se calculan sobre la transacción de negocio completa de extremo a extremo. La disponibilidad de la infraestructura subyacente no es un sustituto válido: un componente activo que devuelve errores no cuenta como disponible. 

Bases Técnicas Transversales TFEP-01/2026 5/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### TÍTULO 11 

###### ARQUITECTURA DE LA SOLUCIÓN 

###### CAPÍTULO 2 - MODELO DE ARQUITECTURA DE REFERENCIA 

###### 2.1 Modelo multicapa exigido 

La solución deberá organizarse en las capas que se describen a continuación. Las capas son de existencia obligatoria; la tecnología con que se materializa cada una es decisión del PROPONENTE, que deberá justificarla. 

|Presentación|Interfaces de las personas usuarias: portal web,<br>aplicación móvil, terminales operacionales y<br>pantallas de terreno.|Diseño adaptativo, accesible y sin lógica de<br>negocio. Ninguna interfaz podrá acceder<br>directamente a la base de datos.|
|---|---|---|
|Borde y exposición|Único punto de entrada público: distribución de<br>contenidos, balanceo, protección perimetral y<br>terminación de cifrado.|CDN, WAF gestionado, protección contra<br>denegación de servicio en capas 3, 4 y 7, y<br>terminación TLS 1.3.|
|Puerta de enlace<br>de servicios|Publicación, autenticación, autorización,<br>cuotas, límites de tasa, versionado y<br>observabilidad de las interfaces de<br>programación.|Validación de esquema, inspección de carga<br>útil, trazabilidad por transacción y catálogo<br>de servicios.|
|Servicios de<br>negocio|Lógica del proceso de negocio del caso,<br>organizada en módulos con límites de contexto<br>explícitos.|Sin estado, desplegables de forma<br>independiente, con contratos versionados y<br>compatibilidad hacia atrás.|
|Integración y<br>eventos|Comunicación asíncrona, desacoplamiento,<br>orquestación y coreografía de procesos entre<br>módulos y con sistemas externos.|Bus o intermediario de mensajería con<br>persistencia, cola de mensajes fallidos,<br>reintento y deduplicación.|
|Datos|Persistencia transaccional, analítica,<br>documental, de series de tiempo y de archivos,<br>según lo requiera el caso.|Separación entre lo transaccional y lo<br>analítico. Cifrado en reposo. Respaldo y<br>retención declarados.|
|Seguridad<br>transversal|Identidad, autorización, gestión de secretos,<br>cifrado, registro de auditoría y detección.|Aplicada a todas las capas, no como capa<br>perimetral única.|
|Observabilidad<br>transversal|Métricas, registros y trazas distribuidas<br>correlacionadas.|Instrumentación conforme a<br>OpenTelemetry, cobertura de nube y on-<br>premise sin puntos ciegos.|



###### 2.2 Requisitos de arquitectura 

||La solución se organizará en las ocho capas del numeral 2.1. El PROPONENTE||
|---|---|---|
|RT-02.01|presentará el diagrama de la arquitectura lógica identificando cada capa, sus<br>componentes y las interfaces entre ellas.|Obligatorio|
||La arquitectura será modular, con límites de contexto explícitos y acoplamiento débil.||
|RT-02.02|Se rechazará toda arquitectura monolítica que no permita desplegar de forma<br>independiente sus componentes críticos.|Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 6/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-02.03|La descripción de la arquitectura se ajustará a ISO/IEC/IEEE 42010, con vistas lógica,<br>de procesos, de despliegue, de datos y de seguridad.|Obligatorio|
|---|---|---|
|RT-02.04|El PROPONENTE mantendrá un registro de decisiones de arquitectura( ADR) fechado,<br>con la alternativa escogida, las alternativas descartadas y el criterio de decisión. El<br>registro es entregable contractual y se actualizará durante toda la ejecución.|Obligatorio|
|RT-02.05|La capa de servicios de negocio será sin estado. El estado de sesión y el estado de<br>z<br>.<br>aiii<br>proceso residirán en almacenes externos con alta disponibilidad.|Obligatorio|
|RT-02.06|Toda operación de escritura expuesta a reintentos será idempotente, con clave de<br>a<br>idempotencia declarada por el cliente y ventana de deduplicación documentada.|Obligatorio|
|RT-02.07|Los flujos de eventos garantizarán entrega al menos una vez, con deduplicación en el<br>consumidor y orden garantizado dentro de la partición o del agregado cuando el<br>proceso lo exija.|Obligatorio|
|RT-02.08|La solución implementará patrones de resiliencia demostrables: reintento con<br>retroceso exponencial y variación aleatoria, cortacircuitos, mamparos de aislamiento,<br>límites de tasa y tiempo de espera explícito en toda llamada remota. No se admiten<br>llamadas remotas sin tiempo de espera.|Obligatorio|
|RT-02.09|La solución degradará de forma elegante: ante la indisponibilidad de un componente<br>no crítico deberá continuar operando en modo reducido, informando la degradación<br>a la persona usuaria, y nunca fallar de forma total.|Obligatorio|
|RT-02.10|Las capas de aplicación e integración escalarán horizontalmente de forma<br>automática, con umbrales, límites superiores y costo asociado declarados en la<br>oferta.|Obligatorio|
|RT-02.11|El PROPONENTE declarará explícitamente los puntos únicos de falla que subsistan en<br>su arquitectura y justificará por qué son aceptables. Omitir esta declaración cuando<br>existan puntos únicos de falla se evaluará como observación grave.|Obligatorio|
|RT-02.12|La solución admitirá su replicación a nuevas unidades, sitios, sucursales o filiales del<br>ES<br>.<br>Elo<br>.<br>A<br>.<br>.<br>CLIENTE sin rediseño arquitectónico, mediante parametrización o multi-tenencia.|Según caso<br>8|
|RT-02.13|El PROPONENTE presentará un modelo de dominio del negocio del caso, con las<br>E<br>o<br>P<br>.<br>8.<br>OS<br>entidades principales, sus relaciones y los eventos de negocio que las modifican.|.<br>.<br>Obligatorio|
|RT-02.14|Se valorará la aplicación documentada de patrones de arquitectura evolutiva que<br>permitan sustituir un componente sin reescribir la solución: capa anticorrupción<br>frente a sistemas heredados, estrangulamiento progresivo y abstracción de<br>proveedores.|Deseable|



###### 2.3 Estilo arquitectónico y su justificación 

El CLIENTE no impone un estilo arquitectónico. Sí exige que el escogido sea explícito, coherente con la escala del caso y justificado. El PROPONENTE deberá comparar al menos dos alternativas y explicar por qué descarta la no elegida, considerando la complejidad operacional que introduce, el tamaño y las competencias del equipo, el costo de infraestructura y la capacidad del CLIENTE de operarla al término del Contrato. 

Adoptar una arquitectura de microservicios para un caso cuyo volumen no la justifica es un error de ingeniería y se evaluará como tal. La sofisticación no reemplaza a la pertinencia. 

Bases Técnicas Transversales TFEP-01/2026 7/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### CAPÍTULO 3 - MODELO HÍBRIDO: NUBE Y ON-PREMISE 

###### 3.1 Distribución de cargas 

Conforme al Artículo 16” de las Bases Administrativas, la solución será obligatoriamente híbrida. El PROPONENTE deberá presentar una tabla de emplazamiento que asigne cada componente a nube o a onpremise y justifique la decisión. 

|Latencia tolerada por el proceso|Superior a 100 ms|Inferior a 50 ms o determinista|
|---|---|---|
|Consecuencia de la pérdida de<br>o.<br>conectividad|El proceso puede esperar<br>P<br>P<br>p|El proceso debe continuar sin<br>excepción|
|Volumeny costo de transferencia de<br>datos|Volumen moderado|Alto volumen generado localmente<br>.<br>,<br>(video, telemetría, sensores)|
|Acoplamiento con equipamiento<br>físico|Nulo o mediado por servicios|Directo: balanzas, PLC, lectores,<br>barreras, cámaras, básculas|
|Elasticidad de la demanda|Muy variable o estacional|Constante y predecible|
|Restricción regulatoria de residencia<br>.<br>o custodia|.<br>o,<br>Sin restricción|Con restricción sectorial declarada<br>en el caso|



###### 3.2 Requisitos del componente en nube 

|RT-03.01|El PROPONENTE declarará el proveedor de nube pública, la región primaria y la<br>región secundaria utilizadas. El proveedor deberá contar con presencia de región o<br>zona en Chile o en Sudamérica.|Obligatorio|
|---|---|---|
|RT-03.02|Todos los componentes con requisito de alta disponibilidad se desplegarán en al<br>E<br>E<br>menos dos zonas de disponibilidad. No se aceptará un diseño en una sola zona.|Obligatorio<br>8|
|RT-03.03|La totalidad de la infraestructura se definirá como código, versionada en el<br>repositorio del CLIENTE, revisable y reproducible. No se admite infraestructura<br>P<br>d<br>y<br>rep<br>creada manualmente por consola, salvo la cuenta raíz inicial, cuya creación deberá<br>documentarse.|Obligatorio|
|RT-03.04|La red se segmentará por capas, con subredes privadas para aplicación y datos, y<br>exposición pública restringida a la capa de borde. Ningún componente de datos será<br>alcanzable desde Internet.|Obligatorio|
|RT-03.05|El PROPONENTE privilegiará servicios administrados por sobre servicios<br>autoadministrados cuando ello reduzca el riesgo operacional, y justificará cada<br>excepción.|Obligatorio|
|RT-03.06|Se aplicarán prácticas FinOps: etiquetado obligatorio de todos los recursos por<br>ambiente, módulo y centro de costo; presupuestos con alertas de desviación; y<br>reporte mensual de consumo desglosado entregado al CLIENTE.|Obligatorio|
|RT-03.07|El PROPONENTE declarará su estrategia de reversibilidad y de mitigación del bloqueo<br>por proveedor, identificando qué componentes son portables, cuáles no lo son y cuál<br>sería el esfuerzo estimado de una migración.|Obligatorio|
|RT-03.08|La solución empleará instancias reservadas, planes de ahorro o capacidad<br>comprometida cuando el perfil de carga lo justifique, y lo reflejará en la estructura de<br>costos.|Deseable|



Bases Técnicas Transversales TFEP-01/2026 8/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-03.09<br>.3 Requisit|Se valorará el uso de cómputo sin servidor o de contenedores administrados para las<br>cargas de perfil variable, con el análisis comparativo de costo frente a instancias<br>permanentes.<br>os del componente on-premise y del borde operacional|Deseable|
|---|---|---|
||El componente on-premise operará de forma autónoma y degradada ante la pérdida||
|RT-03.10|total del enlace con la nube, durante un período mínimo de 24 horas continuas o el<br>mayor que fije el caso.|Obligatorio|
|RT-03.11|Durante la operación desconectada, la solución continuará registrando las<br>transacciones operacionales críticas de forma local, con integridad garantizada y sin<br>pérdida de datos.|Obligatorio|
|RT-03.12|Restablecido el enlace, la sincronización será automática, con reconciliación<br>determinista de conflictos, regla de resolución documentada y bitácora auditable de<br>las decisiones aplicadas.|Obligatorio|
|RT-03.13|El PROPONENTE declarará qué funciones NO estarán disponibles en modo<br>desconectado y qué procedimiento manual las suple. La ausencia de esta declaración<br>se evaluará como observación grave.|Obligatorio|
|RT-03.14|Los equipos on-premise críticos serán redundantes. El almacenamiento local tolerará<br>la falla de al menos un disco; el PROPONENTE declarará el nivel RAID escogido y lo<br>justificará frente a las alternativas.|Obligatorio|
|RT-03.15|Los sistemas on-premise se endurecerán conforme a los CIS Benchmarks aplicables,<br>o,<br>.<br>o,<br>con gestión centralizada de parches y ventana de aplicación acordada con el CLIENTE.|Obligatorio|
|RT-03.16|El monitoreo del componente on-premise se integrará a la misma plataforma de<br>Mm<br>.<br>o<br>observabilidad que la nube, con alertamiento unificado.|A<br>A<br>Obligatorio|
|RT-03.17|El enlace entre el sitio on-premise y la nube será redundante, con caminos físicos y<br>proveedores distintos, y conmutación automática con tiempo de conmutación<br>declarado.|Obligatorio|
|RT-03.18|Los dispositivos de borde y de terreno se administrarán de forma remota y<br>centralizada: inventario, configuración, actualización de firmware y de aplicación,<br>bloqueo y borrado remoto.|Obligatorio|
|RT-03.19<br>.4 Conectiv|Se valorará el procesamiento en el borde de las cargas que lo admitan— filtrado,<br>agregación previa, inferencia local<br>— reduciendo el volumen transferido y la<br>dependencia del enlace.<br>idad y redes|Deseable|
|RT-03.20|El PROPONENTE dimensionará el ancho de banda requerido por sitio, en régimen<br>normal y en peak, y lo justificará con el cálculo de volumen de transacciones y de<br>datos.|Obligatorio|
|RT-03.21|La conexión entre la red del CLIENTE y la nube se establecerá mediante enlace<br>privado dedicado o red privada virtual con cifrado, según lo que el volumeny la<br>criticidad justifiquen.|Obligatorio|



###### 3.3 Requisitos del componente on-premise y del borde operacional 

###### 3.4 Conectividad y redes 

Bases Técnicas Transversales TFEP-01/2026 9/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-03.22|El acceso remoto de las personas trabajadoras del CLIENTE, incluido el trabajo desde<br>el hogar, se resolverá con acceso a la red de confianza cero, con verificación de<br>postura del dispositivo. No se admite exponer servicios internos directamente a<br>Internet.|Obligatorio|
|---|---|---|
|RT-03.23|La red inalámbrica de los sitios operacionales, cuando el caso la requiera, contará con<br>segmentación por tipo de dispositivo, autenticación por certificado o credencial de<br>empresa y cobertura verificada mediante estudio de sitio.|Según caso|
|RT-03.24|El PROPONENTE declarará la calidad de servicio y la priorización de tráfico aplicada a<br>.<br>,<br>ds<br>7d<br>e<br>s<br>las transacciones operacionales críticas frente al tráfico administrativo.|Deseable|



###### CAPÍTULO 4 - AMBIENTES, ENTREGA CONTINUA Y GESTIÓN DE LA CONFIGURACIÓN 

###### 4.1 Ambientes obligatorios 

|Desarrollo|Construcción y prueba unitaria por parte del<br>:<br>equipo de desarrollo.|Aislado. Datos sintéticos o anonimizados.<br>,<br>ja<br>Reconstruible desde código.|
|---|---|---|
|QA|Pruebas funcionales, de integración, de<br>regresión y automatizadas.|Aislado. Datos de prueba controlados y<br>versionados. Reinicio a estado conocido.|
|Preproducción|Pruebas de aceptación, de carga, de resiliencia<br>o,<br>y ensayo del paso a producción.|Equivalente a producción en topología,<br>configuración y versiones. Volumen de<br>datos representativo.|
|Producción|Operación real.<br>A|Acceso restringido y auditado. Sin acceso<br>interactivo directo de desarrolladores.|
|Recuperación ante<br>desastres|Continuidad ante indisponibilidad de la región<br>o del sitio primario.|Replicación continua. Conmutación<br>probada semestralmente.|



###### 4.2 Requisitos de entrega continua 

|AAA|Los cinco ambientes del numeral 4.1 estarán habilitados y operativos como condición<br>del hito H3 del Formulario E-25.|Obligatorio|
|---|---|---|
|RT-04.02|Preproducción será equivalente a producción en topología, versiones de<br>componentes y configuración. Las diferencias que subsistan por costo se declararán<br>expresamentey se justificarán.|Obligatorio|
|RT-04.03|El código residirá en un sistema de control de versiones con ramas protegidas,<br>revisión obligatoria por pares y prohibición de escritura directa sobre la rama<br>principal.|Obligatorio|
|RT-04.04|Existirá trazabilidad completa entre requerimiento, incidencia, cambio de código<br>.<br>P<br>Ñ<br>q<br>!<br>!<br>89,<br>prueba ejecutada y despliegue realizado.|.<br>.<br>Obligatorio|
|RT-04.05|El flujo de integración continua ejecutará, como mínimo: compilación, pruebas<br>unitarias, análisis estático de código, análisis de composición de software, escaneo de<br>!<br>Bes<br>P<br>?<br>secretos y escaneo de imágenes de contenedor, con criterios de bloqueo automático<br>del despliegue.|.<br>.<br>Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 10/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-04.06|Los despliegues serán automatizados y reproducibles, con reversión automatizada y<br>o.<br>e<br>sd<br>sin intervención manual en el paso a producción.|Obligatorio|
|---|---|---|
|RT-04.07|La estrategia de despliegue permitirá liberar sin interrupción del servicio: azul-verde,<br>canario o despliegue progresivo. Se declarará cuál se emplea y se demostrará en<br>Preproducción antes de cada paso a producción.|Obligatorio|
|RT-04.08|Toda configuración estará externalizada del artefacto y gestionada por ambiente. Un<br>mismo artefacto deberá poder promoverse de QA a Preproducción y a Producción sin<br>recompilación.|Obligatorio|
|RT-04.09|Los secretos residirán en un gestor de secretos con rotación automática y auditoría<br>de acceso. Queda prohibida toda credencial embebida en código, imágenes o<br>archivos de configuración.|Obligatorio|
|RT-04.10|Las migraciones de esquema de base de datos serán versionadas, reversibles y<br>ejecutadas de forma automatizada, con estrategia de compatibilidad que permita<br>convivir dos versiones de la aplicación durante el despliegue.|Obligatorio|
|RT-04.11|La cobertura de pruebas automatizadas del código de lógica de negocio será de al<br>»<br>:<br>menos 70%, con umbral bloqueante en el flujo de integración continua.|Obligatorio|
|RT-04.12|El PROPONENTE declarará su frecuencia de despliegue objetivo, su tiempo desde el<br>compromiso de código hasta producción, su tasa de cambios fallidos y su tiempo de<br>restauración, y los medirá durante la Operación.|Obligatorio|
|RT-04.13|Los ambientes no productivos se apagarán o reducirán fuera del horario de uso, con<br>.<br>el ahorro reflejado en la estructura de costos.|Deseable|
|RT-04.14<br>APÍTULO|Se valorará la existencia de ambientes efímeros por rama o por incidencia, creados y<br>.<br>he:<br>destruidos automáticamente.<br> 5- DATOS, INTEGRACIÓN E INTEROPERABILIDAD|Deseable|
|.1Modelo|y gestión de datos<br>El PROPONENTE entregará el modelo de datos documentado y un diccionario de||
|RT-05.01|datos con el nombre, el tipo, el dominio de valores, la obligatoriedad, el propietario y<br>la sensibilidad de cada atributo.|Obligatorio|
|RT-05.02|El PROPONENTE justificará la selección del paradigma y del motor de persistencia:<br>relacional o no relacional, garantías transaccionales, y la posición escogida entre<br>consistencia y disponibilidad conforme al teorema CAP, para cada dominio de datos.|Obligatorio|
|RT-05.03|Toda operación de negocio será trazable: la solución permitirá reconstruir quién,<br>qué, cuándo, desde qué dispositivo y con qué valores anteriores y posteriores, para<br>cualquier registro y en cualquier momento del período de retención.|Obligatorio|
|RT-05.04|La calidad de datos se gestionará conforme a ISO/IEC 25012, con validación en el<br>punto de captura, indicadores de completitud, exactitud y consistencia, y tablero de<br>calidad disponible para el CLIENTE.|Obligatorio|
|RT-05.05|El almacenamiento transaccional y el analítico estarán separados. Ninguna consulta<br>A<br>,<br>-<br>y<br>analítica podrá degradar el desempeño<sup>de la operación.</ sup>|Obligatori<br>IBatorlo|



###### CAPÍTULO 5 - DATOS, INTEGRACIÓN E INTEROPERABILIDAD 

###### 5.1 Modelo y gestión de datos 

Bases Técnicas Transversales TFEP-01/2026 11/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-05.06|La solución permitirá exportar la totalidad de la información del CLIENTE en formatos<br>abiertos y documentados, en cualquier momento del Contrato, sin costo adicional y<br>sin intervención del ADJUDICATARIO.|Obligatorio|
|---|---|---|
|RT-05.07|El PROPONENTE declarará la política de retención, archivado y eliminación por cada<br>dominio de datos, coherente con la normativa aplicable al caso, e implementará un<br>procedimiento verificable de eliminación segura.|Obligatorio|
|RT-05.08|Los datos personales se tratarán conforme al Artículo 85” de las Bases<br>Administrativas, con seudonimización o cifrado a nivel de campo para las categorías<br>sensibles que el caso identifique.|Obligatorio|
|RT-05.09|El PROPONENTE presentará una estrategia de gestión de datos maestros que evite la<br>A<br>.<br>.<br>,<br>.<br>duplicación de entidades compartidas entre módulos y con sistemas externos.|.<br>.<br>Obligatorio|
|RT-05.10|Se valorará la implementación de un catálogo de datos con linaje automatizado, que<br>.<br>:<br>E<br>a<br>permita rastrear el origen de cada indicador de negocio hasta su fuente.|Deseable|



###### 5.2 Migración de datos 

|RT-05.11|El PROPONENTE presentará un plan de migración con alcance, origen, volumen,<br>reglas de transformación, criterios de calidad, estrategia de ejecución y plan de<br>reversión.|Obligatorio|
|---|---|---|
|RT-05.12|La migración incluirá una etapa de perfilado y saneamiento previo, con informe de<br>los defectos detectados en los datos de origen y la decisión adoptada sobre cada<br>uno.|Obligatorio|
|RT-05.13|Se ejecutarán al menos dos ensayos completos de migración sobre Preproducción<br>antes de la migración definitiva, con medición del tiempo total y del resultado de la<br>conciliación.|Obligatorio|
|RT-05.14|La conciliación posterior a la migración será cuantitativa y verificable: recuentos,<br>sumas de control y muestreo dirigido. Toda diferencia deberá quedar explicada.|Obligatorio|
|RT-05.15|Los datos históricos que no se migren quedarán accesibles en un repositorio de<br>,<br>5<br>0.<br>consulta durante el período de retención que fije el caso.|-<br>Según caso|



###### 5.3 Integración e interoperabilidad 

|RT-05.16|Los servicios síncronos se documentarán en OpenAPI 3.1 y los flujos dirigidos por<br>eventos en AsyncAPI 2.6 o superior. La documentación se generará desde el código y<br>se mantendrá actualizada automáticamente.|Obligatorio|
|---|---|---|
|RT-05.17|Los contratos de interfaz se versionarán semánticamente, con compatibilidad hacia<br>><br>da<br>.<br>:<br>A<br>:<br>atrás y política de obsolescencia con preaviso mínimo de seis meses.|Obligatorio|
|RT-05.18|La autenticación entre sistemas empleará OAuth 2.1 con credenciales de cliente o<br>autenticación mutua TLS. Queda prohibida la autenticación por clave estática en la<br>ruta de la dirección web.|Obligatorio|
|RT-05.19|Toda integración registrará la transacción de entrada y de salida, con identificador de<br>correlación común que permita seguir una operación de negocio a través de todos<br>los sistemas involucrados.|Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 12/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-05.20|Las integraciones con sistemas heredados o de terceros se aislarán mediante una<br>capa anticorrupción, de modo que un cambio en el sistema externo no propague su<br>modelo al núcleo de la solución.|Obligatorio|
|---|---|---|
|RT-05.21|El PROPONENTE declarará, por cada integración, el modo( síncrono o asíncrono), el<br>volumen esperado, la ventana de disponibilidad del sistema contraparte y el<br>comportamiento de la solución cuando ese sistema no responde.|Obligatorio|
|RT-05.22|La solución soportará la carga y descarga masiva de información en formatos<br>abiertos, con validación previa, informe de errores por registro y procesamiento<br>parcial.|Obligatorio|
|RT-05.23|Se emplearán los estándares sectoriales de intercambio que las Bases Técnicas del<br>.<br>ml<br>caso identifiquen.|'<br>Según caso|
|RT-05.24|Se valorará la publicación de un portal de servicios para desarrolladores con<br>documentación navegable, ambiente de pruebas y credenciales de prueba<br>autoservidas.|Deseable|



###### 5.4 Analítica e inteligencia de negocio 

|RT-05.25|La solución proveerá una capa analítica con tableros operacionales y de gestión,<br>PE<br>,<br>construidos sobre los indicadores que las Bases Técnicas del caso definan.|Obligatori<br>iii|
|---|---|---|
|RT-05.26|Los tableros permitirán filtrar por período, unidad organizacional y dimensiones<br>propias del caso, y profundizar desde el indicador agregado hasta la transacción de<br>origen.|Obligatorio|
|RT-05.27|El CLIENTE podrá construir sus propios informes sin intervención del ADJUDICATARIO,<br>mediante una herramienta de autoservicio con modelo semántico documentado.|Obligatorio|
|RT-05.28|Todo informe será exportable en formatos abiertos y programable para envío<br>po<br>.<br>automático por calendario.|.<br>.<br>Obligatorio|
|RT-05.29|La latencia máxima entre la ocurrencia de una transacción y su disponibilidad en la<br>ly<br>,<br>Ñ<br>hi<br>capa analítica será la que fije el caso y, en su defecto, no superará las 4 horas.|Según caso|
|RT-05.30|Se valorará la incorporación de analítica predictiva pertinente al proceso del caso,<br>con el modelo, sus variables, su métrica de desempeño y su plan de reentrenamiento<br>documentados.|Deseable|



Bases Técnicas Transversales TFEP-01/2026 13/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### TÍTULO 111 INFRAESTRUCTURA 

###### CAPÍTULO 6 - SITE PRINCIPAL ON-PREMISE 

###### 6.1 Alcance y dimensionamiento proporcional 

El PROPONENTE deberá habilitar un recinto técnico para el alojamiento de los servidores, el almacenamiento y los equipos de telecomunicaciones que soportan la operación on-premise del CLIENTE, con un nivel de disponibilidad de infraestructura de 99,95 %. El recinto se emplazará en el espacio físico que proporcione el CLIENTE, cuya ubicación y superficie se establecen en las Bases Técnicas del caso. 

Las exigencias de este capítulo se aplican de manera proporcional a la escala del componente on-premise que el caso requiera: 

|Sala técnica principal<br>pane|El caso requiere cómputo, almacenamiento y<br>rocesamiento sustantivos en las instalaciones del<br>P<br>CLIENTE.|o,<br>Se aplican integramente los<br>requisitos RT-06.01 a RT-06.24.|
|---|---|---|
|Sala técnica<br>secundaria o de sitio|Sitios operacionales que requieren cómputo local<br>para continuidad, pero no albergan el núcleo.|Se aplican los requisitos de energía,<br>climatización, control de acceso,<br>detección de incendio y monitoreo,<br>dimensionados al sitio.|
|.<br>Gabinete o borde<br>y<br>operacional|o,<br>.<br>.<br>o.<br>Puntos de operación con equipamiento mínimo:<br>ES<br>PO<br>pórtico, muelle, sala de máquinas, sucursal, faena.|Se aplican los requisitos de<br>protección eléctrica, control de<br>o.<br>.<br>acceso físico, monitoreo remoto y<br>condiciones ambientales del<br>equipo.|



El PROPONENTE deberá declarar expresamente qué tipología adopta en cada sitio del caso y justificar el dimensionamiento. Sobredimensionar el recinto es tan penalizado como subdimensionarlo: ambos revelan que el cálculo de capacidad no se hizo. 

###### 6.2 Requisitos de obra y habilitación 

|RT-06.01|El espacio asignado será de uso exclusivo de la solución y estará aislado de otras<br>dependencias del CLIENTE, con acceso independiente.|Obligatorio|
|---|---|---|
|RT-06.02|Los muros no estructurales del recinto contarán con blindaje perimetral; el<br>z<br>><br>:<br>:<br>PROPONENTE especificará el material y la resistencia.|Obligatorio|
|RT-06.03|El PROPONENTE entregará el plano de distribución interna del recinto, con la<br>separación de las zonas de generadores, baterías, climatización, servidores,<br>comunicaciones, trabajo y respaldo.|Obligatorio|
|RT-06.04|El piso técnico, la canalización, el cableado estructurado y el etiquetado se ejecutarán<br>o,<br>As<br>conforme a norma, con documentación de la certificación de cada enlace.|Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 14/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

||Los racks de servidores serán independientes de los racks de equipos de||
|---|---|---|
|RT-06.05|comunicación. Se declarará la ocupación proyectada de cada rack y su margen de<br>crecimiento.|Obligatorio|
|RT-06.06|La<br>obra<br>civil<br>d<br>ión<br>de<br>las<br>**in**stalaci<br>d<br>del CLIENTE;<br>a Obra civil<br>de separación de las<br>stalaciones es de cargo de<br>; su<br>especificación técnica y su coordinación son de cargo del PROPONENTE.|Obligatorio|



###### 6.3 Energía 

|RT-06.07|El suministro eléctrico de los equipos será ininterrumpido, con sistema de<br>alimentación ininterrumpida dimensionado para una autonomía mínima de 30<br>minutos a plena carga.|Obligatorio|
|---|---|---|
|RT-06.08|La capacidad de generación autónoma asegurará un rango mínimo de 24 horas<br>continuas de operación, con estanque de combustible dimensionado y contrato de<br>reabastecimiento declarado.|Obligatorio|
|RT-06.09|La instalación eléctrica del recinto será independiente de la del resto del edificio y<br>cumplirá la normativa eléctrica chilena vigente, incluida la NCh Elec. 2777 sobre<br>sistemas de puesta a tierra.|Obligatorio|
|RT-06.10|Se efectuará revisión y medición semestral de las instalaciones eléctricas del recinto,<br>con informe entregable al CLIENTE.|Obligatorio|
|RT-06.11|El PROPONENTE declarará la carga eléctrica proyectada en kW, el factor de potencia<br>A<br>,<br>]<br>.<br>y la eficiencia en el uso de la energía( PUE) estimada del recinto.|.<br>.<br>Obligatorio|
|RT-06.12|Se valorará la redundancia de alimentación en configuración 2N o N+1 con doble<br>ne<br>S<br>acometida y transferencia automática.|Deseable|



###### 6.4 Climatización y condiciones ambientales 

||El recinto contará con climatización de precisión para operación continua,||
|---|---|---|
|RT-06.13|redundante en configuración N+1, con control de temperatura y de humedad relativa<br>dentro de los rangos que recomienda el fabricante del equipamiento.|Obligatorio|
|RT-06.14|Se monitorearán en línea la temperatura, la humedad y la presencia de agua, con<br>alertamiento integrado a la plataforma de observabilidad.|Obligatori<br>igatono|
|RT-06.15|El ARORONENTE declarar Ruestrategja de contención de pasillo frío o caliente y su<br>efecto en la eficiencia energética.|nesezble|



###### 6.5 Detección y extinción de incendios 

|RT-06.16|El recinto contará con detección temprana por aspiración de aire con tecnología<br>A<br>.<br>.<br>.<br>.<br>.<br>láser, tipo AnaLASER o equivalente de prestaciones iguales o superiores.|.<br>Ñ<br>Obligatorio|
|---|---|---|
|RT-06.17|La extinción será automática mediante agente limpio tipo FM-200 o equivalente, con<br>Sl<br>di<br>8<br>ai<br>q<br>:<br>aprobación UL e instalación conforme a norma NFPA.|Obligatorio|
|RT-06.18|Se proveerá un sistema secundario de extintores portátiles habilitados, con<br>o,<br>A<br>mantencióny certificación vigentes.|.<br>.<br>Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 15/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

El sistema de detección y extinción se integrará al monitoreo en línea y notificará al RT-06.19 Obligatorio NOC y a la contraparte del CLIENTE. 

###### 6.6 Seguridad física y control de acceso 

|RT-06.20|El ingreso al recinto se controlará mediante seguridad física y control de acceso<br>biométrico basado principalmente en biometría facial, con AFIS como respaldo. Se<br>admite proponer sistemas de mayor seguridad.|Obligatorio|
|---|---|---|
|RT-06.21|Todo ingreso y egreso quedará registrado en una bitácora auditable, con<br>identificación de la persona, fecha, hora y motivo, conservada por el período de<br>retención declarado.|Obligatorio|
|RT-06.22|Entre el acceso principal y el término del pasillo de la zona de control se dispondrá un<br>espacio para la atención de personas en proceso de enrolamiento. Se evaluará mejor<br>.<br>.<br>o,<br>.<br>.<br>.<br>.<br>la existencia de una estación de enrolamiento fuera de las instalaciones del recinto<br>técnico.|Obligatorio|
|RT-06.23|Al término del pasillo se instalará un acceso que impida el paso de más de una<br>persona a la vez, con nueva verificación de identidad previa al ingreso.|.<br>A<br>Obligatorio|
|RT-06.24|El recinto contará con videovigilancia y monitoreo IP, con imágenes en línea y<br>disponibles para visualización de al menos los últimos 30 días. Las grabaciones<br>anteriores se respaldarán en un medio secundario recuperable y auditable.|Obligatorio|
|RT-06.25<br>.7 Respald|El PROPONENTE declarará el procedimiento de acceso de terceros— fabricantes,<br>.<br>o<br>;<br>.<br>:<br>mantenedores, auditores— con acompañamiento obligatorio y registro.<br>o y custodia de medios|Obligatorio|
|RT-06.26|Se habilitará un servicio de custodia de medios de respaldo para el sitio primario, en<br>un medio físico transportable a otro lugar cuando el CLIENTE lo determine. Se admite<br>proponer una solución más segura y eficiente, debidamente justificada.|Obligatorio|
|RT-06.27|El recinto de custodia cumplirá exigencias de luminosidad, humedad, ventilación y<br>cualquier otro factor que pueda afectar la calidad y la disponibilidad de los medios.|Obligatorio|
|RT-06.28|Se llevará un inventario de medios con rotación, verificación periódica de legibilidad<br>.<br>o<br>.<br>y registro de todo movimiento de entrada y de salida.|.<br>.<br>Obligatorio|
|.8 Espacio<br>RT-06.29|de operación del personal<br>El PROPONENTE habilitará el espacio físico necesario para el personal encargado de<br>la operación y administración de la plataforma, con estaciones de trabajo, telefonía,<br>SE<br>.<br>.<br>Da<br>conexión a Internet y todo elemento que permita realizar la labor en condiciones<br>adecuadas.|Obligatorio|
|RT-06.30|El espacio de operación estará separado de la sala de equipos y no requerirá el<br>E<br>:<br>E<br>A<br>ingreso al recinto técnico para las labores habituales de operación.|Obligatorio|
|RT-06.31|Las instalaciones sanitarias, las zonas de seguridad ante emergencia y las áreas<br>exteriores existentes en el edificio del CLIENTE podrán utilizarse y no deben<br>implementarse nuevamente. El PROPONENTE declarará de cuáles hará uso.|Obligatorio|



###### 6.7 Respaldo y custodia de medios 

###### 6.8 Espacio de operación del personal 

Bases Técnicas Transversales TFEP-01/2026 16/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### 6.9 Rutas de comunicaciones 

|RT-06.32|El acceso a las redes de comunicaciones estará provisto a través de rutas físicas<br>o<br>.<br>e<br>distintas, con ingreso al edificio por puntos separados.|.<br>.<br>Obligatorio|
|---|---|---|
|RT-06.33|El PROPONENTE proveerá toda la conectividad, la seguridad y las canalizaciones,<br>E<br>.<br>:<br>:<br>7<br>:<br>cañerías o ductos requeridos para cumplir los niveles de servicio comprometidos.|Obligatorio|
|RT-06.34<br>APÍTULO|Se privilegiará al PROPONENTE que ofrezca o provea especificaciones nuevas o<br>p<br>a<br>a<br>mejores que las aquí establecidas, debidamente fundamentadas.<br> 7- SITE SECUNDARIO Y RECUPERACIÓN ANTE DESASTRES|Deseable|
|.1 Configur<br>omplement<br>istintas, en<br>roducción <br>íticos.<br>RT-07.01|ación exigida<br>ariamente al sitio principal, el PROPONENTE deberá habilitar un sitio secundario <br> modalidad activo-activo o activo-pasivo, con replicación de datos en línea para<br> y características tecnológicas equivalentes a las del sitio principal en lo que respec<br>El PROPONENTE declarará la modalidad escogida— activo-activo o activo-pasivo— y<br>la justificará frente al costo, al RTO comprometido y a la complejidad operacional que<br>introduce.|en dependenci<br> el ambiente <br>ta a los servici<br>Obligatorio|
|RT-07.02|El sitio secundario estará emplazado a una distancia suficiente del principal para no<br>verse afectado por el mismo evento de fuerza mayor. El PROPONENTE declarará la<br>distancia y el análisis de amenazas comunes considerado.|Obligatorio|
|RT-07.03|La replicación de datos será continua, con medición y alertamiento del retraso de<br>SE<br>replicación.|.<br>.<br>Obligatorio|
|RT-07.04|El objetivo de tiempo de recuperación( RTO) no superará 4 horasy el objetivo de<br>punto de recuperación( RPO) no superará 15 minutos para los servicios críticos, salvo<br>exigencia superior del caso.|Obligatorio|
|RT-07.05|El procedimiento de conmutación estará documentado, automatizado en la mayor<br>medida posible y ejecutable por el personal del CLIENTE tras la transferencia de<br>conocimiento.|Obligatorio|
|RT-07.06|Existirá un procedimiento de retorno al sitio principal igualmente documentado y<br>-<br>.<br>:<br>probado, con reconciliación de los datos generados durante la contingencia.|Obligatorio|
|RT-07.07|El plan de recuperación ante desastres se probará al menos dos veces al año<br>mediante conmutación real, con informe de resultados, medición del RTO y del RPO<br>efectivamente alcanzados y plan de corrección de las brechas detectadas.|Obligatorio|
|RT-07.08|Se valorará que la conmutación sea automática ante la detección de indisponibilidad,<br>o<br>.<br>De<br>A<br>.<br>con criterio de disparo declarado y protección contra conmutación innecesaria.|Deseable|



###### CAPÍTULO 7 - SITE SECUNDARIO Y RECUPERACIÓN ANTE DESASTRES 

###### 7.1 Configuración exigida 

Complementariamente al sitio principal, el PROPONENTE deberá habilitar un sitio secundario en dependencias distintas, en modalidad activo-activo o activo-pasivo, con replicación de datos en línea para el ambiente de producción y características tecnológicas equivalentes a las del sitio principal en lo que respecta a los servicios 

críticos. 

###### 7.2 Niveles de servicio de infraestructura 

|Energía del recinto|99,95%|
|---|---|
|Climatización|99,95%|



Bases Técnicas Transversales TFEP-01/2026 17/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|Red y comunicaciones|99,95%|
|---|---|
|Servidores y cómputo|99,95%|
|Motor de base de datos|99,95%|
|Portal y canales de atención|99,95%|
|Transacción de negocio crítica de extremo a extremo|99,9%( Artículo 78” de las Bases Administrativas)|



Los niveles de disponibilidad de infraestructura son un medio, no un fin. El compromiso contractual que se mide y se penaliza es el del Artículo 78” de las Bases Administrativas, sobre la transacción de negocio de extremo a extremo. 

###### 7.3 Respaldos 

|RT-07.09|La política de respaldo seguirá el esquema 3-2-1-1-0: tres copias, en dos medios<br>distintos, una fuera de sitio, una inmutable o fuera de línea y cero errores de<br>verificación de restauración.|Obligatorio|
|---|---|---|
|RT-07.10|Los respaldos estarán cifrados en reposo y en tránsito, con clave gestionada de forma<br>independiente de la infraestructura respaldada.|Obligatorio|
|RT-07.11|Las copias inmutables estarán protegidas contra borrado y contra modificación<br>durante su período de retención, incluso frente a credenciales administrativas<br>comprometidas.|Obligatorio|
|RT-07.12|Se ejecutará y documentará una prueba de restauración al menos mensual, sobre<br>.<br>qua<br>:<br>E<br>2<br>una muestra representativa, con medición del tiempo efectivo de restauración.|Obligatorio|
|RT-07.13|El PROPONENTE declarará, por cada dominio de datos, la frecuencia de respaldo, el<br>,<br>y<br>]<br>.<br>o,<br>período de retención y el tiempo estimado de restauración completa.|E<br>E<br>Obligatorio|
|RT-07.14|Los respaldos permitirán la restauración granular: un registro, una tabla, un módulo o<br>.<br>el sistema completo.|Deseable|



###### CAPÍTULO 8 - HARDWARE, PUESTOS DE TRABAJO Y EQUIPAMIENTO DE TERRENO 

###### 8.1 Infraestructura de cómputo, almacenamiento y red 

|RT-08.01|El PROPONENTE especificará el equipamiento de cómputo con su marca, modelo de<br>referencia, procesador, memoria, almacenamiento local, interfaces y consumo, junto<br>con el cálculo de dimensionamiento que lo sustenta.|Obligatorio|
|---|---|---|
|RT-08.02|El almacenamiento será redundante, con tolerancia declarada a la falla de discos,<br>control de errores y monitoreo predictivo de salud de los medios.|Obligatorio<br>5|
|RT-08.03|Los conmutadores de núcleo, los cortafuegos y los balanceadores de carga estarán en<br>,<br>ps<br>Ñ<br>a<br>:<br>E<br>configuración de alta disponibilidad, sin punto único de falla.|.<br>.<br>Obligatorio|
|RT-08.04|Todo el equipamiento contará con fuentes de poder redundantes y conexión a<br>oEa<br>circuitos eléctricos distintos.|Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 18/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

||El PROPONENTE declarará el margen de crecimiento del dimensionamiento||
|---|---|---|
|RT-08.05|propuesto, expresado como porcentaje sobre la carga proyectada del caso, y el|Obligatorio|
||procedimiento de ampliación.||
|RT-08.06|El equipamiento será nuevo, sin uso previo, con garantía de fábrica vigente desde la<br>o,<br>recepción conforme.|Obligatorio|



###### 8.2 Puestos de trabajo de operación y de back office 

|RT-08.07|El PROPONENTE especificará las estaciones de trabajo requeridas para la operación y<br>la administración de la plataforma, en la cantidad que determine el<br>dimensionamiento del caso, con monitores duales.|Obligatorio|
|---|---|---|
|RT-08.08|Los puestos de trabajo cumplirán las condiciones ergonómicas de la NCh 2527 y los<br>.<br>,<br>ao<br>pan<br>equipos contarán con certificación de eficiencia energética.|Obligatorio|
|RT-08.09|Las estaciones estarán gestionadas de forma centralizada, con cifrado de disco,<br>control de dispositivos extraíbles, antivirus con detección y respuesta y actualización<br>automatizada.|Obligatorio|



###### 8.3 Equipamiento de terreno y dispositivos operacionales 

Conforme al Artículo 14.2 de las Bases Administrativas, la especificación técnica del hardware de terreno es de cargo del PROPONENTE aunque su adquisición corresponda al CLIENTE. 

|RT-08.10|El PROPONENTE especificará cada dispositivo de terreno con marca, modelo de<br>referencia, cantidad, características mínimas, accesorios, consumibles y costo<br>unitario estimado, aun cuando su compra sea de cargo del CLIENTE.|Obligatorio|
|---|---|---|
|RT-08.11|La especificación considerará las condiciones reales de uso del caso: intemperie,<br>humedad, polvo, vibración, temperatura, uso con guantes, luminosidad y autonomía<br>de batería requerida por turno.|Obligatorio|
|RT-08.12|Los dispositivos declararán su grado de protección contra polvo y agua y su<br>.<br>.<br>:<br>oz<br>resistencia a caídas, coherentes con el entorno de operación.|Obligatorio|
|RT-08.13|El PROPONENTE indicará el ciclo de vida esperado de cada dispositivo, la<br>disponibilidad de repuestos y el plan de reposición durante los 56 meses del<br>Contrato.|Obligatorio|
|RT-08.14|Los dispositivos se integrarán a la gestión centralizada de flota exigida en RT-03.18.|Obligatorio|
|RT-08.15|El PROPONENTE<br>3<br>idad d<br>da<br>tipo<br>de<br>di<br>¡ti<br>ifi**cad** <br>proveerá una unidad<br>decada<br>tipo<br>de<br>dispositivo especifi<br>opara<br>pruebas de aceptación por parte del CLIENTE, antes de la compra masiva.|Deseable|



###### 8.4 Garantías, repuestos y niveles de reemplazo 

|Hardware crítico|Soporte 24x7 con atención en sitio y compromiso de resolución en 4<br>horas.|
|---|---|
|Hardware no crítico|Soporte en horario hábil con compromiso de resolución en 24 horas.|
|Software de base y de plataforma|Soporte continuo del fabricante durante todo el período contractual.|



Bases Técnicas Transversales TFEP-01/2026 19/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|Stock de repuestos|Al menos 10% del parque instalado por tipo de componente crítico,<br>disponible en Chile.|
|---|---|
|Reemplazo de componente crítico en<br>falla|Máximo 4 horas desde la confirmación del diagnóstico.|
|Dispositivos de terreno|Stock de reemplazo en sitio equivalente al 10% del parque, con<br>configuración precargada.|



###### 8.5 Ciclo de vida y disposición final 

|RT-08.16|El PROPONENTE presentará el plan de ciclo de vida del equipamiento: recepción,<br>o<br>oz<br>a.<br>.<br>e<br>puesta en servicio, mantención, actualización, retiro y disposición final.|Obligatorio|
|---|---|---|
|RT-08.17|Todo medio de almacenamiento que salga de servicio será borrado de forma segura<br>e<br>ce<br>se<br>a<br>y verificable, con certificado de destrucción o de sanitización entregado al CLIENTE.|oblicarar<br>igatorio<br>8|
|RT-08.18|La disposición final de equipamiento electrónico se realizará con gestor autorizado,<br>conforme a la normativa de residuos aplicable, con certificado de disposición.|Obligatorio|
|RT-08.19|Se valorará una estrategia de reacondicionamiento o de extensión de vida útil que<br>reduzca el impacto ambiental, cuantificada en la propuesta.|D<br>bl<br>eseable|



Bases Técnicas Transversales TFEP-01/2026 20/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### TÍTULO IV REQUISITOS NO FUNCIONALES 

###### CAPÍTULO 9 - DESEMPEÑO, CAPACIDAD Y ESCALABILIDAD 

###### 9.1 Umbrales de desempeño 

Los siguientes umbrales son exigibles en producción, medidos en el percentil 95 sobre la experiencia real de la persona usuaria y bajo la carga de peak declarada en las Bases Técnicas del caso. 

|Carga inicial|de una página del portal|2 segundos||
|---|---|---|---|
|Navegación|entre vistas ya cargadas|1 segundo||
|Respuesta d|e una interfaz de programación de consulta simple|500ms||
|Respuesta d|e una interfaz de programación de escritura transaccional|800ms||
|a<br>Transacción|<br>.<br>Le:<br> operacional crítica de terreno, de extremo a extremo|Definido por el caso; en <br>segundos|su defecto, 3|
|Búsqueda c|on criterios compuestos|3 segundos||
|Generación|de un informe estándar en línea|30 segundos||
|Procesamie|nto por lotes|10.000 registros por|minuto|
|Carga de un|archivo de 100 MB|60 segundos||
|Tiempo de a|rranque en frío de un servicio|60 segundos||
|.2 Requisit<br>RT-09.01|os de capacidad y escalabilidad<br>El PROPONENTE presentará el cálculo de capacidad que sust<br>dimensionamiento, con los supuestos de usuarios concurrent<br>segundo, volumen de datos y crecimiento anual, tomados de|entasu<br>es, transacciones por<br> la volumetría del caso.|Obligatorio|
|RT-09.02|La solución soportará la concurrencia y el volumen de transa<br>E<br>.<br>y mantendrá los umbrales del numeral 9.1 bajo esa carga.|cciones que fije el caso,|-<br>Según caso|
|RT-09.03|La solución soportará, sin rediseño, un crecimiento de al men<br>dae<br>:<br>y<br>volumetría inicial del caso en un horizonte de tres años.|os tres veces la|Obligatorio|
|RT-09.04|El escalamiento de las capas de aplicación e integración será<br>.<br>o,<br>o<br>.<br>con tiempo de reacción declarado y sin pérdida de transacci|horizontal y automático,<br>ones en curso.|,<br>Ñ<br>Obligatorio|
|RT-09.05|El PROPONENTE identificará el componente que primero se<br>a<br>z<br>2<br>botella al crecer la carga y explicará cómo lo detectará y cóm|convertirá en cuello de<br>E<br>o lo resolverá.|Obligatorio|
|RT-09.06|Se ejecutarán pruebas de carga sobre Preproducción con un<br>1,5 veces el peak declarado, y pruebas de estrés hasta identi<br>de la solución.|volumen equivalente a<br>ficar el punto de quiebre|Obligatorio|
|RT-09.07|El informe de pruebas de carga incluirá la curva de tiempo d<br>carga, el punto de saturación, el consumo de recursos y el c<br>después del peak.|e respuesta frente a<br>omportamiento durante y|Obligatorio|



###### 9.2 Requisitos de capacidad y escalabilidad 

Bases Técnicas Transversales TFEP-01/2026 21/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-09.08|La solución degradará de forma controlada al superarse la capacidad: encolamiento,<br>limitación de tasa y mensaje explícito a la persona usuaria, nunca error genérico ni<br>pérdida silenciosa de transacciones.|Obligatorio|
|---|---|---|
|RT-09.09|Se gestionará la capacidad durante la Operación con proyección trimestral de<br>crecimiento, alertas anticipadas de agotamiento y propuesta de ajuste de<br>dimensionamiento y de costo.|Obligatorio|
||Se valorará la existencia de pruebas de carga automatizadas ejecutadas de forma||
|RT-09.10|periódica en el flujo de integración continua, con detección de regresiones de<br>desempeño.|Deseable|



###### CAPÍTULO 10 - DISPONIBILIDAD, CONTINUIDAD Y RESILIENCIA 

|RT-10.01|La solución alcanzará una disponibilidad mensual mínima de 99,9% para los servicios<br>clasificados como críticos, medida sobre la transacción de negocio de extremo a<br>extremo.|Obligatorio|
|---|---|---|
|RT-10.02|El PROPONENTE clasificará cada servicio de la solución en crítico, alto, medio o bajo,<br>justificando la clasificación con el impacto operacional de su indisponibilidad, y<br>aplicará a cada uno el nivel de servicio correspondiente del Artículo 78” de las Bases<br>Administrativas.|Obligatorio|
|RT-10.03|El plan de continuidad del negocio se elaborará conforme a ISO 22301, con análisis<br>de impacto en el negocio, escenarios de contingencia, procedimientos manuales de<br>respaldo y criterios de activación.|Obligatorio|
|RT-10.04|La continuidad TIC se estructurará conforme a ISO/IEC 27031, articulada con el plan<br>o,<br>,<br>de recuperación ante desastres del Capítulo 7.|Obligatorio<br>8|
|RT-10.05|Los mantenimientos programados se ejecutarán fuera de la ventana operacional<br>crítica que defina el caso, con aviso previo mínimo de diez días hábiles.|is|
|RT-10.06|La solución permitirá desplegar cambios sin interrupción del servicio. Las ventanas de<br>indisponibilidad programada serán excepcionales y deberán justificarse caso a caso.|Oblisatoño<br>E|
|RT-10.07|Se ejecutarán pruebas de resiliencia mediante inyección controlada de fallas— caída<br>de instancia, de zona, de dependencia externa, latencia elevada, saturación de<br>disco— antes de cada paso a producción y al menos una vez por semestre durante la<br>Operación.|Obiigatoríó|
|RT-10.08|El PROPONENTE documentará, por cada dependencia externa, el comportamiento de<br>la solución cuando esa dependencia no responde, responde con error o responde<br>con lentitud.|Obligatorio|
|RT-10.09|Se declarará un presupuesto de error por servicio crítico y su vinculación con el ritmo<br>de despliegue de cambios.|D<br>bl<br>eseable|



Bases Técnicas Transversales TFEP-01/2026 22/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### CAPÍTULO 11 - SEGURIDAD DE LA INFORMACIÓN 

###### 11.1 Gobierno y modelo de seguridad 

|RT-11.01|La arquitectura de seguridad se basará en el modelo Zero Trust conforme a NIST SP<br>800-207: verificación explícita de cada solicitud, privilegio mínimo y presunción de<br>compromiso.|Obligatorio|
|---|---|---|
|RT-11.02|El PROPONENTE entregará un modelado de amenazas documentado por cada<br>componente y por cada integración externa, con metodología declarada( STRIDE u<br>otra), y lo actualizará ante cada cambio arquitectónico relevante.|Obligatorio|
|RT-11.03|La información del CLIENTE se clasificará por nivel de sensibilidad, con controles<br>diferenciados por nivel documentados en una matriz.|Obligatorio<br>d|
|RT-11.04|Existirá un programa de gestión de vulnerabilidades con escaneo continuo y plazos<br>máximos de remediación de 7 días corridos para vulnerabilidades críticas, 15 días<br>para altas y 30 días para medias, contados desde su publicación o detección.|Obligatorio|
|RT-11.05|El PROPONENTE mantendrá una matriz de controles de seguridad trazable a ISO/IEC<br>27001 e ISO/IEC 27002, indicando el control, su implementación concreta en la<br>solución y la evidencia que lo acredita.|Obligatorio|
|RT-11.06|Se aplicarán los controles de ISO/IEC 27017 para los servicios en nube y de ISO/IEC<br>27018 para el tratamiento de datos personales en nube.|Obligatorio<br>8|



###### 11.2 Protección de la capa expuesta 

|RT-11.07|La publicación de servicios se realizará exclusivamente a través de la capa de borde,<br>con red de distribución de contenidos, cortafuegos de aplicaciones web con reglas<br>gestionadas y personalizadas, y protección contra denegación de servicio distribuida<br>en capas 3, 4 y 7.|Obligatorio|
|---|---|---|
|RT-11.08|El cifrado en tránsito empleará TLS 1.3, con prohibición expresa de TLS 1.0 y 1.1,<br>conjuntos de cifrado modernos, HSTS con precarga y gestión automatizada de<br>certificados con rotación y alerta anticipada de vencimiento.|Obligatorio|
|RT-11.09|La totalidad de los datos en reposo estará cifrada, con claves gestionadas en un<br>servicio de gestión de claves o en un módulo de seguridad de hardware, política de<br>rotación declarada y separación de funciones en la custodia de claves.|Obligatorio|
|RT-11.10|Los datos de categoría sensible que el caso identifique se cifrarán adicionalmente a<br>.<br>.<br>nivel de campo, de modo que el acceso a la base de datos no revele su contenido.|Según caso|
|RT-11.11|La puerta de enlace de servicios aplicará autenticación, autorización, cuotas, límites<br>O<br>.<br>oz<br>3<br>de tasa, validación de esquema e inspección de carga útil.|Obligatorio<br>8|
|RT-11.12|Los puntos de entrada públicos contarán con protección contra bots y abuso<br>automatizado, con reto progresivo que no degrade la accesibilidad ni bloquee a<br>personas usuarias legítimas.|Obligatorio|
|RT-11.13|El PROPONENTE declarará la superficie de exposición completa de la solución: cada<br>nombre de dominio, puerto y servicio alcanzable desde fuera de la red del CLIENTE.|Obligatori<br>da|



Bases Técnicas Transversales TFEP-01/2026 23/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### 11.3 Detección, respuesta y evidencia 

|RT-11.14|Los eventos de seguridad se registrarán de forma centralizada e inalterable, con<br>retención mínima de doce meses en línea y veinticuatro meses adicionales en archivo<br>recuperable.|Obligatorio|
|---|---|---|
|RT-11.15|Los eventos se correlacionarán en una plataforma SIEM, con casos de uso de<br>detección definidos específicamente para el proceso de negocio del caso, y no sólo<br>genéricos de infraestructura.|Obligatorio|
|RT-11.16|Se implementará detección y respuesta en puntos finales y en cargas de trabajo,<br>.<br>tanto en nube como on-premise.|Obligatorio|
|RT-11.17|El PROPONENTE dispondrá de un centro de operaciones de seguridad con cobertura<br>z<br>a<br>a<br>E<br>24x7, propio o subcontratado, y declarará su ubicación, dotación y procedimientos.|Obligatorio|
|RT-11.18|El plan de respuesta a incidentes de seguridad definirá clasificación, cadena de<br>escalamiento, plazos, responsables y protocolo de comunicación al CLIENTE dentro<br>de las dos horas de detectado un incidente de severidad crítica.|Obligatorio|
|RT-11.19|Toda brecha de seguridad o de datos personales se notificará al CLIENTE dentro de<br>las 24 horas de su detección, con informe preliminar, y el análisis de causa raíz se<br>entregará dentro de los cinco días hábiles siguientes.|Obligatorio|
|RT-11.20|Se ejecutarán pruebas de intrusión por un tercero independiente del<br>ADJUDICATARIO, anualmente y antes de cada paso a producción, con entrega íntegra<br>del informe al CLIENTE y plan de remediación con plazos.|Obligatorio|
|RT-11.21|Se realizarán ejercicios de simulación de incidente con participación del CLIENTE al<br>E<br>Sn<br>menos una vez al año durante la Operación.|Deseable|



###### 11.4 Seguridad del ciclo de desarrollo y de la cadena de suministro 

|RT-11.22|El flujo de integración continua incorporará análisis estático de código, análisis de<br>composición de software, análisis dinámico y escaneo de imágenes de contenedor,<br>con criterios de bloqueo automático del despliegue ante hallazgos críticos.|Obligatorio|
|---|---|---|
|RT-11.23|Cada versión liberada se acompañará de su inventario de componentes de software<br>en formato CycloneDX o SPDX, entregado al CLIENTE.|Obligatorio<br>8|
|RT-11.24|Los artefactos se firmarán y su procedencia se verificará conforme a SLSA nivel 3 o<br>]<br>superior.|a<br>E<br>Obligatorio|
|RT-11.25|Queda prohibido el uso de datos productivos reales en ambientes no productivos sin<br>anonimización o seudonimización verificable.|Obligatorio|
|RT-11.26|El PROPONENTE declarará el proceso de aprobación de nuevas dependencias de<br>terceros, incluyendo criterios de licencia, mantención activa y ausencia de<br>vulnerabilidades conocidas.|Obligatorio|
|RT-11.27|Las personas desarrolladoras no tendrán acceso interactivo directo al ambiente de<br>producción. Todo acceso excepcional será temporal, aprobado, registrado y con<br>sesión grabada.|Obligatorio|
|RT-11.28|Se aplicará el marco OWASP SAMM o equivalente para medir y mejorar la madurez<br>OS<br>y<br>del proceso de desarrollo seguro, con evaluación inicial y reevaluación anual.|Deseable|



Bases Técnicas Transversales TFEP-01/2026 24/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### 11.5 Certificaciones y estándares de seguridad exigidos 

|Sistema de gestión de seguridad|ISO/IEC 27001 e ISO/IEC 27002|
|---|---|
|Servicios en nube|ISO/IEC 27017|
|Datos personales en nube|ISO/IEC 27018|
|Marco de ciberseguridad|NIST Cybersecurity Framework 2.0|
|Arquitectura de confianza cero|NIST SP 800-207|
|Seguridad de aplicaciones|OWASP ASVS 4.0 nivel 2 como mínimo; OWASP Top 10 y OWASP API Security<br>Top10|
|Endurecimiento de sistemas|CIS Benchmarks del producto correspondiente|
|Cadena de suministro de software||SLSA nivel 3 o superior|
|Continuidad|ISO 22301 e ISO/IEC 27031|
|Normativa nacional|Leyes N* 21.719, N” 21.663, N* 21.459 y N* 19.799, según aplicabilidad al caso|



###### CAPÍTULO 12 - IDENTIDAD, ACCESO Y GESTIÓN DE SESIONES 

|RT-12.01|La gestión de identidad será centralizada, con federación mediante OpenID Connect y<br>OAuth 2.1, o SAML 2.0 cuando la integración con el CLIENTE lo requiera, e integración<br>con el directorio corporativo del CLIENTE por LDAP o su equivalente en la nube.|Obligatorio|
|---|---|---|
|RT-12.02|Existirá inicio de sesión único para todos los módulos de la solución, con cierre de<br>a<br>sesión propagado a todos ellos.|Obligatorio|
|RT-12.03|La autenticación multifactor será obligatoria para personas usuarias administradoras,<br>para todo acceso privilegiado y para todo acceso originado fuera de la red<br>corporativa.|Obligatorio|
|RT-12.04|Se soportarán factores resistentes a la suplantación de identidad, tipo FIDO2 o claves<br>:<br>ER<br>de acceso, al menos para los perfiles administradores.|Deseable|
|RT-12.05|El control de acceso será basado en roles, complementado con control basado en<br>atributos donde el proceso lo exija, con matriz de segregación de funciones<br>documentaday verificable.|Obligatorio|
|RT-12.06|Los accesos privilegiados se gestionarán con elevación temporal a demanda,<br>Es<br>E<br>a<br>SY<br>.<br>:<br>aprobación previa y grabación de sesión para las operaciones de mayor riesgo.|Obligatorio|
|RT-12.07|La política de sesión declarará duración máxima, caducidad por inactividad,<br>renovación de la credencial de sesión tras la autenticación, revocación inmediata y<br>control de sesiones concurrentes.|Obligatorio|
|RT-12.08|Las credenciales de sesión serán firmadas y de vida breve, con credencial de refresco<br>rotatoria. Queda prohibido transportar identificadores de sesión en la ruta de la<br>dirección web.|Obligatorio|
|RT-12.09|Se registrará auditoría completa del ciclo de vida de la identidad: creación,<br>modificación, elevación, bloqueo y baja de cuentas, con no repudio y retención<br>declarada.|Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 25/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-12.10|El aprovisionamiento y el desaprovisionamiento estarán automatizados y ligados al<br>ciclo de vida laboral, con baja efectiva en un plazo no superior a 24 horas desde la<br>desvinculación.|Obligatorio|
|---|---|---|
|RT-12.11|El mecanismo de autenticación se adecuará al perfil operacional real descrito en el<br>caso: entornos de terreno, uso con guantes, baja alfabetización digital, dispositivos<br>compartidos por turno y ausencia de correo electrónico personal.|Según caso|
|RT-12.12|Las personas usuarias externas del CLIENTE— clientes, proveedores, pacientes,<br>productores, según el caso— dispondrán de un mecanismo de registro, verificación<br>de identidad y recuperación de acceso autoservido y seguro.|Según caso|
|RT-12.13|El PROPONENTE declarará el procedimiento de acceso de emergencia( cuenta de<br>0<br>,<br>a<br>último recurso), su custodia, su control y su auditoría.|Obligatorio|



###### CAPÍTULO 13 - USABILIDAD, ACCESIBILIDAD Y EXPERIENCIA DE USUARIO 

|RT-13.01|Todas las interfaces destinadas a personas usuarias cumplirán WCAG 2.2 nivel AA,<br>verificado con herramientas automatizadas y con pruebas manuales, con informe de<br>conformidad entregable.|Obligatorio|
|---|---|---|
|RT-13.02|El diseño será responsivo y funcionará correctamente en escritorio, tableta y<br>teléfono, con puntos de quiebre coherentes y adaptación inteligente del contenido,<br>no simple reducción.|Obligatorio|
|RT-13.03|El PROPONENTE ejecutará investigación con personas usuarias reales del CLIENTE,<br>prototipado y pruebas de usabilidad antes de la construcción definitiva, y<br>documentará los hallazgos y los cambios de diseño que produjeron.|Obligatorio|
||Se comprometerán indicadores de usabilidad medibles: tiempo máximo de la||
|RT-13.04|transacción operacional crítica, número máximo de pasos, tasa de error tolerada y<br>tiempo de aprendizaje esperado por perfil.|Obligatorio|
|RT-13.05|Ninguna funcionalidad principal requerirá más de tres interacciones desde la pantalla<br>de inicio del perfil correspondiente.|Obligatorio|
|RT-13.06|La solución entregará retroalimentación visual clara ante cada acción, manejará los<br>errores de forma comprensible— indicando qué ocurrió y qué hacer— y evitará<br>mensajes técnicos dirigidos a la persona usuaria final.|Obligatorio|
|RT-13.07|La solución soportará a personas usuarias con baja alfabetización digital: alto<br>contraste, objetivos táctiles de al menos 44 x 44 píxeles, iconografía acompañada de<br>texto, y flujos guiados paso a paso.|Obligatorio|
|RT-13.08|Cuando el caso lo requiera, las interfaces de terreno operarán con guantes, a la<br>.<br>.<br>o<br>.<br>.<br>o,<br>intemperie, con luminosidad variable y sin conexión.|Según caso|
|RT-13.09|Existirá un sistema de diseño documentado con paleta de colores acotada, jerarquía<br>tipográfica de a lo más dos familias, iconografía coherente, retícula y componentes<br>reutilizables.|Obligatorio|
|RT-13.10|El PROPONENTE declarará la matriz de navegadores y de versiones soportadas y su<br>a<br>o,<br>política de actualización.|.<br>.<br>Obligatorio|
|RT-13.11|La solución será navegable integramente por teclado, con orden de foco lógico<br>8<br>E<br>P<br>!<br>gico<br>Y<br>atajos para las operaciones frecuentes.|z<br>;<br>Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 26/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

Se valorará el soporte de modo oscuro, de personalización de la interfaz por persona RT-13.12 Deseable usuaria y de múltiples idiomas cuando el caso lo justifique. 

###### CAPÍTULO 14 - OBSERVABILIDAD Y GESTIÓN DEL SERVICIO 

|RT-14.01|La observabilidad será unificada para nube y on-premise, con métricas, registros y<br>trazas distribuidas correlacionadas por un identificador único de transacción,<br>instrumentadas conforme a OpenTelemetry.|Obligatorio|
|---|---|---|
|RT-14.02|El CLIENTE dispondrá de acceso propio y permanente a los tableros operacionales y<br>de negocio, con datos en tiempo real y capacidad de exportación.|Obligatorio|
|RT-14.03|Los indicadores de nivel de servicio se medirán sobre la experiencia real de la<br>persona usuaria y no sobre pruebas sintéticas, sin perjuicio de que estas se empleen<br>como complemento.|Obligatorio|
|RT-14.04|El alertamiento se basará en síntomas de negocio y no sólo en umbrales de<br>infraestructura, con supresión de ruido, agrupación, escalamiento automático y<br>turnos de disponibilidad declarados.|Obligatorio|
|RT-14.05|Existirá un libro de operación y una guía de resolución documentados para cada<br>escenario de falla previsible, con automatización progresiva de las tareas repetitivas.|Obligatorio|
|RT-14.06|Todo incidente crítico dará lugar a un análisis de causa raíz obligatorio, con informe<br>entregable dentro de cinco días hábiles y seguimiento de las acciones correctivas<br>hasta su cierre.|Obligatorio|
|RT-14.07|Los registros de la solución no contendrán datos personales sensibles ni credenciales,<br>y su acceso estará controlado y auditado.|Obligatorio|
|RT-14.08|El PROPONENTE declarará la retención de métricas, registros y trazas, y su costo<br>asociado, distinguiendo el almacenamiento en línea del archivado.|Obligatorio|
|RT-14.09|Se valorará la detección proactiva de anomalías mediante análisis del<br>comportamiento histórico, con alerta antes de que el incidente afecte a la operación.|Deseable|



###### CAPÍTULO 15 - SOSTENIBILIDAD, EFICIENCIA Y CERTIFICACIONES 

###### 15.1 Sostenibilidad y eficiencia energética 

|RT-15.01|El PROPONENTE dimensionará la infraestructura ajustada a la demanda real,<br>evitando capacidad ociosa permanente, y declarará el factor de utilización<br>proyectado.|Obligatorio|
|---|---|---|
|RT-15.02|Los ambientes no productivos se apagarán o reducirán fuera del horario de uso.|Obligatorio|
|RT-15.03|El PROPONENTE estimará la huella de carbono anual de la operación de la solución y<br>declarará la metodología empleada.|Obligatorio|
|RT-15.04|Se declarará la eficiencia en el uso de la energía( PUE) del recinto on-premise y la<br>intensidad de carbono de la región de nube escogida.|Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 27/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-15.05|Se valorará la elección de regiones de nube con menor intensidad de carbono cuando<br>la latencia y la regulación lo permitan, con el análisis comparativo correspondiente.|Deseable|
|---|---|---|
|RT-15.06|Se valorará la definición de metas de reducción del consumo durante la Operación,<br>con medición y reporte anual.|Deseable|



###### 15.2 Certificaciones institucionales exigidas Certificaciones institucionales exigidas institucionales exigidas exigidas 

15.2 Certificaciones institucionales exigidas Certificaciones institucionales exigidas institucionales exigidas exigidas 

|ISO/IEC 27001— Seguridad de la<br>información|Obligatoria|Vigente a la fecha de la oferta o plan de certificación<br>con hitos verificables dentro de los primeros 12 meses<br>del Contrato.|
|---|---|---|
|ISO 9001— Gestión de la calidad|Obligatoria|Vigente a la fecha de la oferta.|
|ISO/IEC 20000-1— Gestión de<br>servicios de Tl|Deseable|Vigente o plan declarado.|
|ISO 22301— Continuidad del negocio|Deseable|Vigente o plan declarado.|
|ISO/IEC 42001— Gestión de<br>inteligencia artificial|Deseable|Exigible sólo si la solución incorpora componentes de lA.|
|Certificación sectorial específica|Según caso|La que identifiquen las Bases Técnicas del caso.|



###### 15.3 Certificaciones del personal 

El equipo propuesto acreditará, como mínimo, las siguientes certificaciones individuales vigentes. Una misma persona puede acreditar más de una, pero no puede contarse dos veces para el mismo requisito. 

|Certificación o competencia|Cantidad mínima|
|---|---|
|Gestión de proyectos( PMP, PRINCE2 o equivalente)|2 personas|
|Gestión de servicios( ITIL 4 Foundation o superior)|5 personas|
|Gobierno de TI( COBIT o equivalente)|2 personas|
|Arquitectura de nube del proveedor ofertado, nivel profesional o de<br>arquitecto|3 personas|
|Seguridad de la información( CISSP, CISM, CEH, OSCP o equivalente)|2 personas|
|Bases de datos del motor ofertado|2 personas|
|Calidad y pruebas de software( ISTQB o equivalente)|2 personas|



|RT-15.07|Las certificaciones se acreditarán con copia del certificado vigente y con el código de<br>oi<br>.<br>a<br>.<br>verificación del organismo emisor cuando exista.|Obligatorio|
|---|---|---|
||Las personas certificadas formarán parte del equipo efectivamente asignado al||
|RT-15.08|PROYECTO, con dedicación declarada. No se aceptará acreditar personal que no<br>participe.|Obligatorio|
||El ADJUDICATARIO mantendrá vigentes estas certificaciones durante todo el período||
|RT-15.09|contractual y las repondrá ante la salida de una persona certificada, conforme al<br>Artículo 76” de las Bases Administrativas.|Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 28/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### TÍTULO Y 

###### CAPACIDADES TRANSVERSALES DE LA SOLUCIÓN 

Los módulos y capacidades de este Título son exigibles en las trece industrias. No son el negocio del caso —eso lo definen las Bases Técnicas respectivas— sino la infraestructura funcional sin la cual ninguna plataforma de misión crítica es operable, auditable ni administrable. 

###### CAPÍTULO 16 - MÓDULOS TRANSVERSALES OBLIGATORIOS 

###### 16.1 Administración y parametrización 

|RT-16.01|La solución dispondrá de un módulo de administración que permita al CLIENTE, sin<br>intervención del ADJUDICATARIO, gestionar personas usuarias, roles, permisos,<br>unidades organizacionales y sus jerarquías.|Obligatorio|
|---|---|---|
|RT-16.02|Las reglas de negocio parametrizables— umbrales, plazos, montos, tolerancias,<br>catálogos, listas de valores, textos de notificación— serán configurables desde la<br>.<br>o<br>o,<br>.<br>.<br>o,<br>os<br>interfaz de administración, con control de versiones y registro de quién cambió qué y<br>cuándo.|.<br>.<br>Obligatorio|
|RT-16.03|Todo cambio de parámetro con impacto operacional requerirá aprobación de un<br>.<br>po<br>rr<br>segundo perfil y quedará registrado con su justificación.|.<br>.<br>Obligatorio|
|RT-16.04|El PROPONENTE declarará expresamente qué elementos son parametrizables y<br>cuáles requieren desarrollo. Presentar como parametrizable lo que exige desarrollo<br>se evaluará como observación grave.|Obligatorio|
|RT-16.05<br>6.2 Auditor|Existirá un ambiente de simulación que permita probar el efecto de un cambio de<br>;<br>:<br>o<br>parámetro antes de aplicarlo a producción.<br>ía y trazabilidad|Deseable|
|RT-16.06|Toda operación que cree, modifique o elimine información quedará registrada con<br>identificación de la persona o del sistema que la ejecutó, fecha y hora con zona<br>horaria, origen, valores anteriores y valores posteriores.|Obligatorio|
|RT-16.07|El registro de auditoría será inalterable y no podrá ser modificado ni eliminado por<br>ningún perfil, incluido el administrador de la plataforma.|Obligatorio|
|RT-16.08|El CLIENTE podrá consultar y exportar la auditoría desde la interfaz, con filtros por<br>,<br>É<br>.<br>A<br>.<br>persona, período, entidad y tipo de operación, sin requerir acceso a la base de datos.|.<br>.<br>Obligatorio|
|RT-16.09|Las consultas a información sensible quedarán registradas, no sólo las<br>o<br>a<br>8<br>!<br>modificaciones.|,<br>Según caso|
|RT-16.10|El período de retención de la auditoría será el que fije el caso y, en su defecto, no<br>.<br>.<br>.<br>mn<br>inferior a cinco años.|Según caso|



###### 16.2 Auditoría y trazabilidad 

Bases Técnicas Transversales TFEP-01/2026 29/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### 16.3 Flujos de trabajo y motor de reglas 

|RT-16.11|La solución soportará flujos de trabajo con estados, transiciones, responsables,<br>.<br>E<br>o<br>2<br>.<br>plazos, escalamiento automático por vencimiento y delegación por ausencia.|Obligatorio|
|---|---|---|
|RT-16.12|Los flujos serán configurables por el CLIENTE sin desarrollo, al menos en lo relativo a<br>responsables, plazos y niveles de aprobación.|Obligatorio|
|RT-16.13|Toda solicitud pendiente será visible para su responsable en una bandeja de tareas<br>unificada, con priorización y alerta de vencimiento.|Gbiistoia<br>8|
|RT-16.14|El motor de reglas permitirá definir condiciones de negocio evaluables sin<br>recompilación, con trazabilidad de qué regla se aplicó a cada transacción.|D<br>bl<br>eseable|
|6.4 Gestió<br>RT-16.15|n documental y firma electrónica<br>La solución gestionará documentos con versionado, metadatos, control de acceso,<br>z<br>.<br>.o<br>búsqueda por contenido y por metadato, y previsualización sin descarga.|Obligatorio|
|RT-16.16|Los documentos se almacenarán cifrados, con verificación de integridad y retención<br>ae<br>conformea la política del caso.|Obligatorio<br>-|
|RT-16.17|La solución soportará firma electrónica conforme a la Ley N* 19.799, con firma<br>avanzada para los actos que el caso lo requiera, y verificación de validez del<br>certificado al momento de la firma.|Según caso|
|RT-16.18|Se generará el sello de tiempo y se conservará la evidencia de firma que permita<br>ce<br>o<br>e<br>q<br>verificar el documento con posterioridad al vencimiento del certificado.|Según caso|
|RT-16.19|La solución generará documentosa partir de plantillas administrables por el CLIENTE,<br>z<br>.<br>.<br>con datos de la transacción y salida en formato abierto.|Obligatorio<br>8|



###### 16.4 Gestión documental y firma electrónica 

###### 16.5 Notificaciones y mensajería multicanal 

|RT-16.20|La solución enviará notificaciones por al menos tres canales: correo electrónico,<br>notificación en la aplicación y mensajería instantánea o SMS, según lo que el caso<br>requiera.|Obligatorio|
|---|---|---|
|RT-16.21|Las plantillas de notificación serán administrables por el CLIENTE, con variables de la<br>transacción, y versionadas.|Obligatorio|
|RT-16.22|Cada persona usuaria podrá configurar sus preferencias de canal y de frecuencia,<br>e<br>]<br>.<br>:<br>respetando las notificaciones que el CLIENTE defina como obligatorias.|AMES<br>igatorio<br>8|
|RT-16.23|El envío será asíncrono, con reintento ante falla, control de duplicados y registro de<br>entrega, apertura y error por cada mensaje.|Obligatorio|
|RT-16.24|El PROPONENTE declarará el proveedor de cada canal, su costo unitario, su volumen<br>proyectado y el tratamiento del costo variable en la Oferta Económica.|óblitodo<br>8|
|RT-16.25|Las notificaciones respetarán la normativa de comunicaciones comerciales y<br>e<br>.<br>permitirán la baja cuando corresponda.|Obligatori<br>igatorio<br>8|
|RT-16.26|Se valorará la integración con canales conversacionales que permitan a la persona<br>usuaria responder y ejecutar acciones desde el propio canal.|esauBra|



Bases Técnicas Transversales TFEP-01/2026 30/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### 16.6 Búsqueda, reportería y exportación 

|RT-16.27|La solución dispondrá de búsqueda global con indexación de texto completo,<br>tolerancia a errores de escritura, filtros facetados y respeto del control de acceso de<br>la persona que busca.|Obligatorio|
|---|---|---|
|RT-16.28|Los listados serán ordenables, filtrables, paginados y exportables en formatos<br>z<br>abiertos, con el filtro aplicado reflejado en la exportación.|Obligatorio<br>8|
|RT-16.29|Las exportaciones de gran volumen se procesarán de forma asíncrona, con<br>AL<br>Ea<br>.<br>o,<br>notificación al completarse y sin bloquear la sesión.|,<br>]<br>Obligatorio|
|RT-16.30<br>6.7 Portal|Toda exportación de información sensible quedará registrada en la auditoría, con<br>P<br>q<br>8<br>!<br>identificación de quién exportó qué y cuándo.<br>público y canales de autoatención|.<br>.<br>Obligatorio|
|RT-16.31|La solución dispondrá de un portal público con la información que el caso determine,<br>accesible sin autenticación, con los mismos estándares de accesibilidad y desempeño<br>que el resto de la plataforma.|Según caso|
|RT-16.32|Las personas usuarias externas dispondrán de autoatención para las consultas de<br>.<br>.<br>AA<br>.<br>.<br>mayor frecuencia, evitando el contacto telefónico para operaciones simples.|Obligatorio|
|RT-16.33|El PROPONENTE estimará la reducción esperada del volumen de atención asistida por<br>a<br>peraca<br>e<br>P<br>efecto de la autoatención y comprometerá el indicador.|Obligatorio|
|RT-16.34|El<br>portal público resistirá picos de tráfico sin degradar los servicios transaccionales<br>P<br>P<br>P<br>8<br>internos, mediante aislamiento de recursos y caché.|.<br>.<br>Obligatorio|



###### 16.7 Portal público y canales de autoatención 

###### CAPÍTULO 17 - CANALES DIGITALES Y MOVILIDAD 

|RT-17.01|La solución proveerá una aplicación móvil para los perfiles operacionales que el caso<br>identifique, con funcionamiento sin conexión y sincronización diferida cuando la<br>operación en terreno lo requiera.|Según caso|
|---|---|---|
|RT-17.02|El PROPONENTE declarará si la aplicación es nativa, híbrida o web progresiva, y<br>justificará la decisión frente al requisito de operación desconectada, al acceso a<br>periféricos y al costo de mantención.|Obligatorio|
|RT-17.03|La aplicación soportará las versiones de sistema operativo móvil vigentes y las dos<br>.<br>te<br>2.”<br>anteriores, con política de actualización declarada.|Obligatorio|
|RT-17.04|La aplicación se distribuirá por las tiendas oficiales o mediante gestión de flota<br>P<br>.<br>.<br>Po,<br>e<br>.<br>.g<br>corporativa, con firma de la aplicación y verificación de integridad.|.<br>.<br>Obligatorio|
|RT-17.05|La información almacenada en el dispositivo estará cifrada, con borrado remoto y<br>eo<br>.<br>o<br>.<br>bloqueo ante pérdida o desvinculación de la persona usuaria.|,<br>.<br>Obligatorio|
|RT-17.06|La aplicación integrará los periféricos que el caso requiera: cámara, lector de códigos<br>P<br>.<br>8<br>bl<br>q<br>:<br>A<br>!<br>q<br>NFC, GPS, impresora de etiquetas, balanza o báscula.|Según caso|
|RT-17.07|El consumo de datos móviles y de batería se optimizará y se declarará el consumo<br>Y<br>P<br>y<br>estimado por turno de trabajo.|.<br>.<br>Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 31/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-17.08|Se valorará la disponibilidad de una versión de la interfaz para dispositivos de bajo<br>.<br>.<br>:<br>.<br>costo o de generaciones anteriores, ampliando la cobertura de personas usuarias.|Deseable|
|---|---|---|



###### CAPÍTULO 18 - INTELIGENCIA ARTIFICIAL Y AUTOMATIZACIÓN 

La incorporación de inteligencia artificial no es obligatoria. Sí lo es, cuando el PROPONENTE la incorpore, cumplir íntegramente los requisitos de este capítulo. Una capacidad de inteligencia artificial mal gobernada es un riesgo, no una ventaja competitiva. 

|RT-18.01|El PROPONENTE declarará cada componente de inteligencia artificial: propósito,<br>modelo o servicio empleado, proveedor, versión y ubicación de procesamiento de los<br>datos.|Obligatorio|
|---|---|---|
|RT-18.02|Se garantizará contractualmente que los datos del CLIENTE no serán utilizados para<br>8<br>q<br>o,<br>.<br>P<br>entrenar modelos de terceros, salvo autorización expresa y escrita.|.<br>.<br>Obligatorio|
|RT-18.03|Se documentarán los límites de uso, los casos en que el resultado requiere validación<br>]<br>q<br>q<br>humana previa y el procedimiento de supervisión.|A<br>3<br>Obligatorio|
|RT-18.04|Los riesgos de sesgo, alucinación, fuga de información y uso indebido se evaluarán y<br>mitigarán conforme al NIST Al Risk Management Framework 1.0 y a la norma ISO/IEC<br>42001.|Obligatorio|
|RT-18.05|Toda interacción relevante con un componente de inteligencia artificial quedará<br>registrada para efectos de auditoría y trazabilidad, incluyendo la entrada, la salida y<br>la decisión humana posterior.|Obligatorio|
|RT-18.06|El componente podrá desactivarse sin comprometer la operación del resto de la<br>solución, y existirá un procedimiento manual de respaldo para la función que<br>automatiza.|Obligatorio|
|RT-18.07|Cuando el resultado se presente a una persona usuaria, se indicará expresamente<br>que fue generado o sugerido de forma automática, y su nivel de confianza cuando el<br>modelo lo provea.|Obligatorio|
|RT-18.08|Los modelos predictivos declararán sus variables de entrada, su métrica de<br>2<br>Z<br>.<br>do<br>:<br>desempeño, su línea base y su plan de reentrenamiento y de detección de deriva.|Obligatorio|
|RT-18.09|La responsabilidad por los resultados de los componentes de inteligencia artificial<br>recae integramente en el ADJUDICATARIO, conforme al Artículo 86” de las Bases<br>Administrativas.|Obligatorio|
|RT-18.10|Se valorará el uso de automatización robótica de procesos o de agentes para tareas<br>repetitivas de back office, con el ahorro de horas cuantificado y reflejado en la Oferta<br>Económica.|Deseable|



Incorporar un modelo de lenguaje a la solución sin declarar dónde se procesan los datos, sin control de acceso a la información que consulta y sin validación humana de sus resultados será evaluado como incumplimiento de los requisitos de seguridad, no como innovación. 

Bases Técnicas Transversales TFEP-01/2026 32/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### TÍTULO VI PROYECTO, IMPLANTACIÓN Y OPERACIÓN 

###### CAPÍTULO 19 - ESTRUCTURA Y GOBIERNO DEL PROYECTO 

###### 19.1 Oficina de gestión y metodología 

|RT-19.01|El ADJUDICATARIO constituirá una oficina de gestión del proyecto con metodología<br>declarada, basada en el PMBOK del Project Management Institute e integrando<br>prácticas ágiles donde el PROPONENTElo justifique.|Obligatorio|
|---|---|---|
|RT-19.02|El Jefe de Proyecto tendrá dedicación exclusiva durante toda la fase de<br>implementación y facultades para comprometer al ADJUDICATARIO en materias de<br>ejecución.|Obligatorio|
|RT-19.03|Existirá un procedimiento formal de control de cambios conforme al Artículo 72* de<br>las Bases Administrativas, con registro de cambios, análisis de impacto y aprobación<br>previa a la ejecución.|Obligatorio|
|RT-19.04|La gestión del riesgo seguirá la norma ISO 31000, con registro de riesgos vivo,<br>revisión en cada Comité de Proyecto y planes de mitigación con responsable, plazo y<br>disparador.|Obligatorio|
|RT-19.05|El ADJUDICATARIO habilitará un espacio colaborativo accesible al CLIENTE, con la<br>documentación del proyecto, los entregables, las actas, el registro de riesgos y el<br>registro de cambios siempre actualizados.|Obligatorio|



###### 19.2 Roles mínimos del equipo Roles mínimos del equipo mínimos del equipo del equipo equipo 

# CO 19.2 Roles mínimos del equipo Roles mínimos del equipo mínimos del equipo del equipo equipo 

|Jefe de Proyecto|100% en implementación|Certificación en gestión de proyectos y<br>experiencia comprobable en proyectos de<br>escala equivalente.|
|---|---|---|
|.<br>o<br>Arquitecto de Solución|Alta en diseño, permanente en<br>a<br>.<br>el Comité de Arquitectura|Certificación de arquitectura del proveedor<br>de nube ofertado.|
|Encargado de Seguridad de la<br>8o<br>8<br>Información|Permanente|,<br>.<br>.<br>Certificación en seguridad vigente.|
|.<br>Líder de Datos|.<br>o<br>Permanente en implementación|Experiencia en modelado y migración de<br>datos.|
|Líder de Desarrollo|100% en implementación|Experiencia en la tecnología ofertada.|
|Líder Funcional|100% en implementación|Experiencia en la industria del caso.|
|Líder de Calidad y Pruebas|Permanente|Certificación en pruebas de software.|
|,<br>Líder de Integración|.<br>Permanente en implementación|Experiencia en integración de sistemas<br>heredados.|
|az<br>Líder de Operación/ SRE|Desde el mes 6, permanente en<br>P<br>Operación|O<br>o,<br>E<br>Certificación en gestión de servicios.|



Bases Técnicas Transversales TFEP-01/2026 33/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|C||O|
|---|---|---|
|<br>Líder de Implantación y Gestión del<br>.<br>Cambio|<br>Desde el mes 8|<br>Experiencia en implantación con usuarios<br>.<br>operacionales.|



El PROPONENTE podrá agregar los roles que su propuesta requiera. La dotación total del equipo deberá ser coherente con las horas hombre del Formulario T-15 y con la curva de recursos de la Oferta Económica. 

###### 19.3 Control y reporte del proyecto 

|RT-19.06|El ADJUDICATARIO entregará un informe mensual de avance con estado del<br>cronograma, avance físico y financiero, entregables del período, desviaciones,<br>riesgos, incidencias y compromisos del período siguiente.|Obligatorio|
|---|---|---|
|RT-19.07|El avance se medirá con valor ganado, reportando el índice de desempeño del<br>cronograma y del costo, y no mediante declaración cualitativa de porcentaje de<br>avance.|Obligatorio|
|RT-19.08|El CLIENTE dispondrá de un tablero de estado del proyecto actualizado, accesible en<br>.<br>cualquier momento.|Obligatorio|
|RT-19.09|Las actas de todos los comités del Artículo 71” de las Bases Administrativas se<br>levantarán dentro de los dos días hábiles siguientes y registrarán acuerdos,<br>responsables y plazos.|Obligatorio|
|RT-19.10|Toda desviación superior al 10% en un hito se comunicará dentro de los cinco días<br>..<br>cuz<br>hábiles de detectada, con plan de recuperación.|Obligatorio|



###### CAPÍTULO 20 - IMPLANTACIÓN, PRUEBAS Y CRITERIOS DE ACEPTACIÓN 

###### 20.1 Estrategia de pruebas 

|Unitarias y de componente||Continuo, en el flujo de integración|Cobertura mínima de 70% en lógica de<br>A<br>negocio; sin pruebas en falla.|
|---|---|---|
|Integración|Continuo, tras cada despliegue a QA|Todos los flujos de integración del caso<br>.<br>Ñ<br>ejecutados sin error.|
|.<br>y<br>Sistema y regresión|Antes de cada promoción a<br>2d<br>Preproducción|Batería de regresión automatizada<br>.<br>.<br>completa sin regresiones.|
|o<br>.<br>Aceptación de usuario|Le<br>Antes de cada certificación de etapa|Casos de aceptación del caso aprobados<br>.<br>P<br>AÑ.<br>y<br>firmados por la Contraparte Técnica.|
|y<br>Carga y estrés|o<br>Antes de cada paso a producción|Umbrales del Capítulo 9 cumplidos a 1,5<br>P<br>P<br>veces el peak declarado.|
|Resiliencia|Antes de cada paso a producción y<br>semestral en Operación|La solución degrada de forma controlada y<br>se recupera sin intervención.|
|Recuperación ante<br>desastres|Antes del paso a producción y semestral|RTO y RPO comprometidos alcanzados en<br>conmutación real.|
|Seguridad ofensiva|Antes de cada paso a producción y anual||Sin hallazgos críticos ni altos abiertos.|
|nte<br>Accesibilidad|o,<br>Antes de cada paso a producción|Conformidad WCAG 2.2 AA verificada<br>y<br>documentada.|



Bases Técnicas Transversales TFEP-01/2026 34/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|Migración de datos|Dos ensayos previos a la migración<br>as<br>definitiva|Conciliación sin diferencias no explicadas.|
|---|---|---|



###### 20.2 Requisitos de implantación 

|RT-20.01|El PROPONENTE presentará un plan de implantación por sitio y por perfil, coherente<br>A<br>2<br>a<br>con el cronograma obligatorio del Artículo 17” de las Bases Administrativas.|Obligatorio<br>8|
|---|---|---|
|RT-20.02|La estrategia de paso a producción será gradual y reversible. Se declarará el criterio<br>o<br>o,<br>.<br>.<br>o,<br>de avance entre olas y el procedimiento de reversión, con su tiempo de ejecución.|.<br>.<br>Obligatorio|
|RT-20.03|Durante la marcha blanca, la solución convivirá con la operación vigente del CLIENTE<br>?<br>P<br>8<br>!<br>con conciliación diaria y sin doble digitación no declarada.|"<br>a<br>Obligatorio|
|RT-20.04|El PROPONENTE definirá los indicadores diarios que se medirán durante la marcha<br>blanca y sus umbrales de avance, conforme al Artículo 17.3 de las Bases<br>Administrativas.|Obligatorio|
|RT-20.05|Se dispondrá de acompañamiento en terreno durante las primeras semanas de cada<br>.<br>.<br>,<br>Ep<br>ola, con dotación declarada y decreciente según la curva de adopción.|Obligatorio<br>8|
|RT-20.06|Se establecerá un período de estabilización con atención reforzada tras cada paso a<br>"e<br>perio:<br>10<br>ze<br>P<br>producción, con dotación y duración declaradas y sin costo adicional.|Obligatorio|
|RT-20.07|Existirá una definición de terminado acordada con el CLIENTE, aplicable a cada<br>to<br>A<br>entregable, que incluya código, pruebas, documentación, seguridad y despliegue.|Obligatorio|
|RT-20.08|El protocolo de aceptación de cada hito se formalizará conforme al Formulario T-17,<br>con criterios objetivos y verificables.|z<br>Ñ<br>Obligatorio|



###### CAPÍTULO 21 - MODELO DE OPERACIÓN, MANTENCIÓN Y SOPORTE 

###### 21.1 Estructura operativa 

|RT-21.01|El ADJUDICATARIO dispondrá de un centro de operaciones de red con cobertura<br>24x7x365, propio o subcontratado, y declarará su ubicación, dotación por turno y<br>procedimientos.|Obligatorio|
|---|---|---|
|RT-21.02|Se designará un gerente de servicio dedicado como contraparte permanente del<br>-<br>CLIENTE durante la fase de Operación.|Obligatori<br>eono|
|RT-21.03|El EQUIEo de operación contará con especialistas por tecnología, nominados y con<br>dedicación declarada.|Obligatorio|
|RT-21.04|Los procedimientos de operación estarán documentados y serán ejecutables por el<br>personal del CLIENTE tras la transferencia de conocimiento.|.<br>.<br>Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 35/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### 21.2 Centro de atención telefónica 

Este ámbito es central para dar continuidad y seguimiento al esfuerzo de incorporación y adopción de la solución. 

|RT-21.05|El PROPONENTE dispondrá de un centro de atención adecuado para soportar<br>integralmente las consultas, propio o subcontratado con un operador de nivel<br>acreditado.|Obligatorio|
|---|---|---|
|RT-21.06|El centro de atención cumplirá un tiempo de atención al usuario final de 80% antes<br>de 20 segundos y una resolución al primer contacto de al menos 70%. La tasa de<br>abandono no superará el 5%.|Obligatorio|
|RT-21.07|El horario mínimo de atención será de 8:00 a 20:00 en días hábiles, ampliado a 24x7<br>para los incidentes de severidad crítica y para la ventana operacional que defina el<br>caso.|Según caso|
|RT-21.08|La atención cubrirá orientación funcional de distintos grados de complejidad, desde<br>preguntas simples hasta situaciones complejas, y las preguntas técnicas más<br>frecuentes sobre la aplicación y su entorno de uso.|Obligatorio|
|RT-21.09|Se mantendrá un registro histórico de las actividades de soporte que permita<br>monitorear y gestionar los principales requerimientos, con análisis de tendencia<br>mensual.|Obligatorio|
|RT-21.10|Existirá un proceso de aprendizaje del centro de soporte que acumule conocimiento<br>sobre las complejidades de la operación y las necesidades de las personas usuarias,<br>reflejado en la base de conocimiento.|Obligatorio|
|RT-21.11|Se proveerán servicios de capacitación en línea en modalidad de autoformación, con<br>j<br>.<br>registro de avance para efectos de monitoreo.|Obligatorio|
|RT-21.12|Se habilitarán espacios de interacción entre las entidades y personas usuarias del<br>sistema, que permitan compartir experiencias de uso.|Deseable|
|RT-21.13|Los indicadores clave del proceso de soporte estarán abiertos al CLIENTE, y los<br>indicadores específicos serán accesibles según nivel de autorización.|.<br>.<br>Obligatorio|
|RT-21.14|El PROPONENTE dimensionará la dotación del centro de atención con fundamento<br>cuantitativo, empleando teoría de colas o el modelo Erlang C, a partir del volumen de<br>contactos proyectado del caso.|Obligatorio|



###### 21.3 Mesa de ayuda por niveles 

## CI E 

|Nivel1|Recibe los contactos de las personas usuarias<br>internas y externas sobre cualquier requerimiento<br>de la plataforma.|Recepción, registro del ticket, clasificación,<br>soluciones básicas y derivación.|
|---|---|---|
|Nivel2|Agentes con mayores conocimientos o especialistas<br>en el sistema y en las aplicaciones provistas por el<br>ADJUDICATARIO. Resuelven los incidentes derivados <br>del nivel 1 apoyándose en manuales y guías.|Soporte especializado, configuraciones y<br>diagnóstico. Los incidentes relativos a<br>procedimientos propios de la operación o a<br>|aplicaciones del CLIENTE no provistas por el<br>ADJUDICATARIO son de responsabilidad del<br>CLIENTEy no se derivan a la mesa.|



Bases Técnicas Transversales TFEP-01/2026 36/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

### Pd pr 

|Nivel3|Métodos de solución a nivel experto y análisis<br>avanzado de la solución y de las aplicaciones<br>provistas.|Resolución de problemas nuevos o<br>desconocidos, apoyo a los niveles 1 y 2, e<br>investigación y desarrollo de soluciones. Incluye<br>el traslado a sitio cuando el problema lo<br>requiera.|
|---|---|---|
|||Es responsabilidad del ADJUDICATARIO gestionar|
|Nivel4|Soporte del fabricante de los componentes de<br>software o hardware utilizados.|y obtener este soporte cuando se requiera, sin<br>que ello lo exima de responsabilidad frente al<br>CLIENTE.|



|RT-21.15|Existirá un canal único de registro de incidentes y solicitudes, con número de ticket,<br>clasificación por severidad y seguimiento del ciclo de vida completo hasta el cierre<br>conforme.|Obligatorio|
|---|---|---|
|RT-21.16|Cuando el caso comprenda sitios alejados, los especialistas de niveles 2 y 3 deberán<br>trasladarse cuando la resolución lo requiera, por el medio más rápido disponible y<br>.<br>ae<br>.<br>o.<br>.<br>o,<br>con disponibilidad de tiempo suficiente, sin alterar la atención normal del resto de<br>los sitios. El costo del traslado está incluido en la oferta.|'<br>Según caso|
|RT-21.17|El cierre de un ticket requerirá confirmación de la persona usuaria o transcurso del<br>,<br>dun<br>plazo de confirmación automática declarado.|Obligatorio|
|RT-21.18|El ADJUDICATARIO reportará mensualmente el cumplimiento de los niveles de<br>o<br>o,<br>.<br>o<br>.<br>o<br>servicio de atención, con el detalle por severidad y el análisis de los incumplimientos.|.<br>A<br>Obligatorio|



###### 21.4 CO Mantención 

|Preventiva|Revisiones programadas, actualizaciones<br>planificadas, optimización continua y auditorías<br>técnicas.|Calendario anual acordado con el CLIENTE.<br>Auditorías al menos trimestrales, con<br>informe.|
|---|---|---|
|Correctiva|Corrección de defectos de la solución.|Sin costo adicional. Sujeta a los tiempos de<br>resolución del Artículo 78” de las Bases<br>Administrativas.|
|Evolutiva|Mejoras funcionales, nuevas características y<br>optimización del desempeño solicitadas por el<br>CLIENTE.|Bolsa anual de horas comprometida en la<br>:<br>oferta, con tarifa declarada para el<br>e<br>o<br>excedente. La bolsa no utilizada en un año<br>no se pierde y se acumula al siguiente.|
|N<br>Í<br>ormativa|Adecuación de la solución ante cambios legales o<br>regulatorios aplicables al caso.|Incluida en el valor de la Operación, sin<br>costo adicional. Plazo de adecuación<br>coherente con la entrada en vigencia de la<br>norma.|



||El PROPONENTE declarará el tamaño de la bolsa anual de horas de mantención||
|---|---|---|
|RT-21.19|evolutiva, su composición por perfil y el procedimiento de solicitud, estimación,|Obligatorio|
||aprobacióny liquidación.||



Bases Técnicas Transversales TFEP-01/2026 37/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-21.20|La mantención evolutiva se someterá al mismo estándar de calidad, pruebas y<br>seguridad que el desarrollo original.|Obligatorio<br>8|
|---|---|---|
|RT-21.21|El PROPONENTE mantendrá un registro de deuda técnica cuantificado y destinará<br>o,<br>Ñ<br>o,<br>.<br>una fracción declarada de la capacidad de la Operación a reducirla.|s<br>E<br>Obligatorio|
|RT-21.22|Las actualizaciones de versión de los componentes de base se planificarán<br>anualmente, con ventana acordada y plan de reversión.|.<br>.<br>Obligatorio|



###### CAPÍTULO 22 - CAPACITACIÓN Y TRANSFERENCIA DE CONOCIMIENTO 

|RT-22.01|El plan de capacitación se estructurará por perfil: personas usuarias finales, usuarias<br>po<br>.<br>avanzadas, administradoras, equipo técnico y soporte de niveles 1 y 2.|Obligatorio<br>8|
|---|---|---|
|RT-22.02|Las modalidades incluirán capacitación presencial en cada sitio de operación,<br>sesiones en línea sincrónicas, autoformación y acompañamiento en puesto de<br>trabajo durante la marcha blanca.|Obligatorio|
|RT-22.03|Todo el material de capacitación se entregará en español, en formato editable y de<br>propiedad del CLIENTE: manuales por perfil, guías rápidas, preguntas frecuentes,<br>videos tutoriales y base de conocimiento consultable.|Obligatorio|
|RT-22.04|La capacitación no podrá afectar la operación del CLIENTE: se programará por turnos<br>y en horarios acordados, considerando la estacionalidad y la ventana operacional del<br>caso.|Según caso|
|RT-22.05|Las personas usuarias administradoras y el equipo técnico del CLIENTE serán<br>0<br>Ade<br>.<br>evaluadosy certificados como condición para el cierre de cada marcha blanca.|:<br>A<br>Obligatorio|
|RT-22.06|Durante la Operación se ejecutarán al menos dos jornadas anuales de actualización y<br>se capacitará al personal nuevo del CLIENTE sin costo adicional.|Oblizatorio<br>E|
|RT-22.07|El ADJUDICATARIO proveerá acompañamiento y mentoría al equipo técnico del<br>CLIENTE durante al menos seis meses posteriores al paso a producción de la Etapa 2.|Oniatano<br>a|
|RT-22.08|La base de conocimiento será mantenida y actualizada durante todo el Contrato, con<br>0<br>a<br>a<br>métricas de uso y de utilidad percibida.|.<br>.<br>Obligatorio|
|RT-22.09|Se valorará la existencia de un ambiente permanente de entrenamiento, con datos<br>ficticios, disponible para la práctica sin riesgo.|Deseable|



Bases Técnicas Transversales TFEP-01/2026 38/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### TÍTULO VII 

###### EXIGENCIAS DE PRESENTACIÓN DE LA PROPUESTA 

Este Título establece entregables de la propuesta que no son documentos escritos: la presencia digital del proponente, un video de presentación y un prototipo interactivo. Los tres se evalúan y los tres tienen causales de descalificación propias. 

###### CAPÍTULO 23 - INFORMACIÓN CORPORATIVA Y PRESENCIA DIGITAL 

###### 23.1 Página web corporativa 

El PROPONENTE deberá disponer de una página web corporativa activa y actualizada que contenga, como mínimo, la siguiente información claramente identificable y de fácil acceso. 

|RT-23.01|Información institucional: descripción detallada del giro principal, historia y<br>trayectoria de la empresa con al menos tres años de antigúedad comprobable,<br>misión, visión y valores, certificaciones y acreditaciones vigentes, y presencia<br>geográfica y oficinas.|Obligatorio|
|---|---|---|
|RT-23.02|Experiencia y casos de éxito: portafolio de proyectos similares de los últimos cinco<br>años, casos documentados con métricas verificables, testimonios de clientes con<br>autorización de publicación, industrias atendidas con énfasis en la del caso asignado,<br>y volumen de transacciones o de personas usuarias gestionadas.|Obligatorio|
|RT-23.03|Equipo profesional: organigrama del equipo directivo, perfiles de socios y directores,<br>currículos resumidos del equipo técnico clave y certificaciones profesionales del<br>personal.|Obligatorio|
|RT-23.04|Capacidades técnicas: servicios y soluciones ofrecidas, conjunto tecnológico<br>dominado, alianzas tecnológicas con proveedores de nube y de plataforma,<br>metodologías de trabajo certificadas, e infraestructura y capacidad instalada.|Obligatorio|
|RT-23.05|El sitio será accesible conforme a WCAG 2.2 nivel AA, responsivo y con certificado TLS<br>23<br>;<br>válido y vigente.|Obligatorio|
|RT-23.06|El sitio se mantendrá activo y disponible durante todo el proceso de licitación, desde<br>.<br>o<br>o,<br>el registro del participante hasta la adjudicación.|.<br>.<br>Obligatorio|
|RT-23.07|Material educativo digital: seminarios en línea, artículos técnicos o centro de<br>un<br>recursos y documentación.|Deseable|
|RT-23.08|Demostración en línea, recorrido virtual de la solución o portal de soporte para<br>y<br>cliente s.|Deseable|
|RT-23.09|Métricas de disponibilidad y desempeño de los servicios del proponente publicadas<br>en tiempo real.|Nesaaklá|
|RT-23.10|Calculadora de retorno de la inversión o herramienta de estimación pertinente a la<br>.<br>.<br>industria del caso.|Deseable|



###### 23.2 Verificación y validación 

El CLIENTE verificará el sitio durante el proceso de evaluación. Constituyen causal de descalificación: 

- e Sitio web no disponible o con caídas recurrentes durante el período de evaluación. 

Bases Técnicas Transversales TFEP-01/2026 39/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

- e Información falsa o engañosa comprobada. 

- e Ausencia de la información crítica exigida en el numeral 23.1. 

- e Casos de éxito no verificables o cuyas contrapartes desmientan lo declarado. 

- e Plagio de contenido de otros sitios. 

###### 23.3 Declaración de veracidad 

El PROPONENTE deberá incluir en el Sobre N* 1 una declaración jurada simple que indique: 

- La dirección oficial del sitio web de la empresa. 

- Que toda la información publicada en el sitio es verídica y se encuentra actualizada. 

- La autorización para que la Comisión Evaluadora contacte a las referencias declaradas. 

- El compromiso de mantener el sitio activo durante todo el proceso. 

- La aceptación de la descalificación en caso de información falsa. 

###### CAPÍTULO 24 - VIDEO DE PRESENTACIÓN DE LA PROPUESTA 

###### 24.1 Especificaciones técnicas 

|Duración|Máximo 5 minutos( 300 segundos). Excederlo produce descalificación automática.|
|---|---|
|Resolución|Full HD, 1920 x 1080 píxeles como mínimo.|
|Formato de archivo|MP4 con códec H.264.|
|Cuadros por segundo|30 fps como mínimo.|
|Tasa de bits de video|5 Mbps como mínimo.|
|Tamaño máximo del<br>archivo|500MB.|
|Audio|44,1 kHz y 16 bits como mínimo, en AAC o MP3, con niveles normalizados, sin<br>distorsión ni ruido de fondo excesivo.|
|Música|Opcional, con licencia acreditable.|
|Orientación|Horizontal( apaisada).|
|Aspectos visuales|Iluminación profesional adecuada, fondo neutro o corporativo, sin efectos que<br>distraigan del mensaje y con transiciones suaves.|



###### 24.2 Estructura y contenido 

El video deberá contener los siguientes segmentos, en este orden: 

1. Introducción corporativa: logotipo animado, nombre del proyecto y del caso, fecha de la propuesta y 

   - nombre del proponente. 

2. Comprensión del problema: análisis de la problemática actual, impacto en las personas afectadas, riesgos de no implementar la solución, métricas del problema identificado y demostración de comprensión del sector. 

3. Solución propuesta: visión general, beneficios para cada grupo de interés, diferenciadores clave, innovaciones incluidas y resultados esperados con métricas. 

Bases Técnicas Transversales TFEP-01/2026 40/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

4. Propuesta tecnológica: conjunto tecnológico completo, arquitectura de alto nivel, servicios de nube 

   - utilizados, y seguridad y cumplimiento normativo. 

5. Ventajas competitivas: por qué el proponente es la mejor opción, experiencia específica, casos de éxito relevantes, garantías y compromisos, y valor agregado único. 

6. Cierre y compromiso: compromiso con el proyecto, datos de contacto e identidad corporativa final. 

###### 24.3 Participación del equipo 

|RT-24.01|Todos los integrantes clave del equipo deberán aparecer individualmente<br>presentándose, en toma de medio cuerpo, mirando directamente a la cámara, con<br>.<br>o<br>.,<br>o.<br>a<br>vestimenta formal o de negocio informal, y con una duración mínima de aparición de<br>10 segundos por persona.|Obligatorio|
|---|---|---|
|RT-24.02|Cada vez que aparezca un integrante deberá mostrarse en pantalla su nombre<br>completo, su cargo en el proyecto, sus años de experiencia y su especialización<br>relevante.|Obligatorio|
|RT-24.03|Las certificaciones principales de cada integrante podrán mostrarse en pantalla.|Deseable|
|RT-24.04|El fondo será el mismo para todas las tomas de personas, con iluminación<br>consistente y encuadre similar para todos los participantes.|.<br>.<br>Obligatorio|
|RT-24.05|La paleta de colores corporativa, la tipografía y el uso de la marca serán consistentes<br>en todo el video, con logotipo visible en todas las escenas y datos de contacto en el<br>encabezado o pie.|Obligatorio|
|RT-24.06|Los niveles de volumen estarán normalizados, con la misma calidad de grabación y<br>.<br>o<br>.<br>sin variaciones bruscas de sonido.|Obligatorio|



###### 24.4 Evaluación, penalizaciones y descalificación 

|Audio con problemas menores|-5 puntos|
|---|---|
|Iluminación deficiente|-5 puntos|
|Transiciones bruscas|-5 puntos|
|Información poco clara|-5 puntos|
|Falta de un rol no crítico del equipo|-5 puntos|
|Duración superior a 5 minutos|Descalificación automática|
|No aparición del equipo clave completo|Descalificación automática|
|Calidad técnica inferior a la especificada en el numeral 24.1|Descalificación automática|
|Información falsa o engañosa|Descalificación automática|
|Uso de material con derechos de autor sin licencia|Descalificación automática|
|No entrega del video junto con la propuesta|Descalificación automática|



###### 24.5 Entrega, derechos y autorizaciones 

- e Entrega física: unidad de almacenamiento USB junto con la propuesta, etiquetada con el nombre de la empresa y del proyecto, incluyendo archivo de respaldo. 

Bases Técnicas Transversales TFEP-01/2026 41/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

- e Entrega digital: enlace de descarga con vigencia mínima de 60 días, sin restricciones de descarga y con la contraseña de acceso en documento separado. 

- e El PROPONENTE autoriza el uso del video para fines de evaluación y su proyección en las sesiones de evaluación. 

- e El PROPONENTE garantiza que posee todos los derechos necesarios sobre el material utilizado. 

- e La Comisión Evaluadora mantendrá la confidencialidad del contenido, no lo distribuirá sin autorización y eliminará las copias posteriores a la evaluación de las propuestas no seleccionadas. 

###### CAPÍTULO 25 - PROTOTIPO INTERACTIVO DE INTERFAZ Y DISEÑO UX/UI 

###### 25.1 Objetivo y momento de entrega 

El PROPONENTE deberá presentar, junto con el Informe 3, un prototipo interactivo de alta fidelidad que demuestre de manera clara y tangible la visión de diseño de interfaz propuesta para la solución del caso. El prototipo permite evaluar la comprensión del proponente sobre las necesidades reales de las personas usuarias y su capacidad de traducirlas en una experiencia de uso adecuada. 

El prototipo no requiere conexión con servicios de fondo ni con base de datos, pero debe simular de manera realista la navegación y los flujos de trabajo principales, permitiendo a los evaluadores experimentar la solución desde la perspectiva de los distintos perfiles de personas usuarias. 

###### 25.2 Alcance mínimo 

El prototipo deberá incluir, como mínimo, las siguientes vistas y funcionalidades navegables: 

|Portal principal|Página de inicio pública; página de inicio con sesión iniciada y personalizada por perfil;<br>tablero principal con componentes configurables; menú de navegación completo y<br>funcional; rastro de navegación y navegación contextual.|
|---|---|
|Autenticación e<br>incorporación|Pantalla de inicio de sesión unificada; registro de una nueva persona usuaria externa<br>en al menos cinco pasos; recuperación de acceso; segundo factor de autenticación; y<br>tablero de primer ingreso con recorrido guiado.|
|Proceso operacional<br>principal del caso|El flujo de negocio central de la industria asignada, de extremo a extremo, en al<br>menos seis pasos, desde su inicio hasta su cierre, incluyendo los estados intermedios<br>y el manejo de la excepción más frecuente.|
|Proceso operacional<br>secundario del caso|Un segundo flujo relevante, con su listado, su vista de detalle, su creación y su flujo de<br>aprobación visual.|
|Perfil de terreno o de<br>operación|La vista que utilizará la persona usuaria operacional en su puesto real, incluida su<br>versión móvil y su comportamiento sin conexión, cuando el caso lo requiera.|
|Gestión de terceros|Directorio de la contraparte externa del caso— clientes, proveedores, productores,<br>.<br>.<br>.<br>yz<br>a<br>pacientes, pasajeros—, su ficha completa, su evaluación y su historial.|
|Tablero analítico|Indicadores principales con visualizaciones; al menos seis tipos de gráfico distintos;<br>filtros por período y categoría; profundización desde el indicador hasta el detalle; y<br>exportación de informes.|
|Administración|Gestión de personas usuarias, roles y permisos; parametrización; y consulta de<br>os<br>auditoría.|
|Dos módulos adicionales|A elección del PROPONENTE, pertinentes al caso.|



Bases Técnicas Transversales TFEP-01/2026 42/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### 25.3 Principios de diseño exigidos 

|RT-25.01|Navegación intuitiva sin necesidad de manual, con un máximo de tres interacciones<br>para alcanzar cualquier funcionalidad principal.|Obligatorio<br>8|
|---|---|---|
|RT-25.02|Retroalimentación visual clara ante cada acción, estados de carga y transición fluidos,<br>y manejo elegante de los errores.|Obligatorio<br>-|
|RT-25.03|Cumplimiento de WCAG 2.2 nivel AA: contraste adecuado, tamaños de fuente<br>legibles, objetivos táctiles de al menos 44 x 44 píxeles, navegación completa por<br>teclado, y textos alternativos y etiquetas de accesibilidad.|Obligatorio|
|RT-25.04|Diseño responsivo demostrado en escritorio( 1920 x 1080 y 1366 x 768), tableta( 768<br>x 1024 en vertical y horizontal) y teléfono (375 x 812), con puntos de quiebre<br>coherentes.|Obligatorio|
|RT-25.05|Sistema de diseño documentado: paleta de a lo más cinco colores principales, a lo<br>más dos familias tipográficas jerarquizadas, iconografía coherente, retícula y<br>espaciado consistentes, y componentes reutilizables.|Obligatorio|



###### 25.4 Componentes de interfaz obligatorios 

||Componentes que el prototipo debe demostrar|
|---|---|
|Navegación|Menú principal, menú secundario contextual, rastro de navegación, paginación, pestañas y<br>acordeones, navegación por pasos y menú de acciones rápidas.|
|Formularios|Campos de texto con validación en tiempo real, selectores y desplegables, casillas y botones<br>de opción, selectores de fecha y hora, carga de archivos con arrastrar y soltar,<br>autocompletado y formularios de múltiples pasos.|
|Visualización de datos|Tablas con ordenamientoy filtrado, gráficos de barras, de líneas y circulares, tarjetas de<br>|información, líneas de tiempo, indicadores de progreso, distintivos y etiquetas, e<br>información contextual emergente.|
|Retroalimentación|Mensajes de éxito, error, advertencia e información; ventanas modales y diálogos;<br>notificaciones emergentes; esqueletos de carga; indicadores de progreso; y estados vacíos<br>ilustrados.|
|Acción|Botones primarios, secundarios y terciarios; botón de acción flotante; acciones en línea;<br>menús contextuales; acciones masivas; y confirmación de acciones críticas.|



###### 25.5 Entrega y nivel de interactividad 

|RT-25.06|El prototipo se entregará como enlace navegable en línea, sin instalación ni<br>.<br>.<br>complementos, compatible con los navegadores modernos vigentes.|Obligatorio|
|---|---|---|
|RT-25.07|El acceso al prototipo estará garantizado por un mínimo de seis meses desde su<br>entrega.|Obligatorio|
|RT-25.08|El prototipo permitirá navegación completa entre pantallas, simulación de ingreso de<br>datos, transiciones y animaciones básicas, estados de posadoy activo, simulación de<br>carga de archivos, elementos desplegables funcionales y simulación de validaciones.|Obligatorio|
|RT-25.09|Se entregará la arquitectura de información del prototipo: mapa del sitio completo,<br>diagrama de navegación, taxonomía y nomenclatura, estructura de menús y jerarquía<br>de la información.|Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 43/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

Se valorará la posibilidad de exportar el prototipo a un documento interactivo para RT-25.10 o os Deseable revisión sin conexión. 

###### 25.6 Restricciones y penalizaciones 

|No se requiere|Se penalizará|
|---|---|
|Funcionalidad real de servicios de fondo.|Prototipos estáticos, no navegables.|
|Conexión a base de datos.|Diseños genéricos sin personalización al caso.|
|Procesamiento real de datos.|Incumplimiento de los estándares de accesibilidad.|
|Integración con servicios externos.|Navegación confusa o enlaces rotos.|
|Autenticación real.|Inconsistencias visuales evidentes.|
|Persistencia de la información ingresada.|Falta de responsividad en los tamaños exigidos.|



###### 25.7 Propiedad intelectual del diseño 

- e El diseño propuesto será de propiedad del CLIENTE si la propuesta resulta adjudicada, conforme al Artículo 84” de las Bases Administrativas. 

- e El PROPONENTE mantiene los derechos sobre sus componentes genéricos y sobre su sistema de diseño preexistente. 

- e Se autoriza el uso del prototipo para fines de evaluación y para su proyección en las sesiones de evaluación. 

- e El CLIENTE mantendrá la confidencialidad de los diseños no seleccionados. 

###### CAPÍTULO 26 - INNOVACIONES 

La exigencia de innovación se establece en el Capítulo 5 de las Bases Administrativas: cinco innovaciones obligatorias, una por cada tipo, con los siete elementos del Artículo 29? documentados en el Formulario T-19. Este capítulo agrega las exigencias técnicas de su formulación. 

|RT-26.01|Cada innovación se ubicará explícitamente en la arquitectura: qué capa la contiene,<br>A<br>a<br>2<br>qué componentes la implementan y qué interfaces consume o expone.|Obligatorio|
|---|---|---|
|RT-26.02|Cada innovación identificará los paquetes de la estructura de descomposición del<br>trabajo que la ejecutan y el mes del cronograma en que se materializa.|Obligatorio<br>8|
|RT-26.03|Las innovaciones de base tecnológica declararán el nivel de madurez de la tecnología<br>8<br>dd<br>y<br>con la escala utilizada y citarán las fuentes en norma APA 7.2 edición.|OBlizato<br>igatorio<br>8|
|RT-26.04|Cada innovación declarará su riesgo de adopción, su probabilidad, su impacto, la<br>estrategia de mitigación y el plan de contingencia si no rinde lo esperado.|Obligatorio|
|RT-26.05|Cada innovación declarará su indicador de verificación con línea base, meta y<br>momento de medición, y su impacto en inversión, costo operacional y beneficio<br>esperado.|Obligatorio|
|RT-26.06|Las innovaciones que incorporen inteligencia artificial cumplirán integramente el<br>Capítulo 18 de este documento.|.<br>.<br>Obligatorio|



Bases Técnicas Transversales TFEP-01/2026 44/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|RT-26.07|Las innovaciones que modifiquen la arquitectura de seguridad requerirán su propio<br>modelado de amenazas.|Obligatorio|
|---|---|---|
|RT-26.08|Se valorará que al menos una innovación sea verificable durante la marcha blanca de<br>la Etapa 1, es decir, que su beneficio pueda medirse antes del mes 16.|Deseable|



No se aceptará como innovación la sola adopción de una tecnología que ya constituye estándar de la industria, la mención de una tendencia sin diseño de incorporación, ni una funcionalidad exigida por las Bases Técnicas presentada como innovación. La pertinencia al caso pesa más que la novedad tecnológica en abstracto. 

Bases Técnicas Transversales TFEP-01/2026 45/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

###### TÍTULO VIII ANEXOS 

###### CAPÍTULO A - ÍNDICE DE REQUISITOS TRANSVERSALES 

Resumen de los requisitos codificados de este documento. El PROPONENTE deberá pronunciarse sobre la totalidad de ellos en el Formulario T-12. 

A estos requisitos se suman los del Capítulo 4 de las Bases Administrativas y la totalidad de los requerimientos funcionales, volúmenes y criterios de aceptación de las Bases Técnicas del caso asignado. 

||Modelo de arquitectura de referencia|RT-02.01<br>—RT-02.14||
|---|---|---|---|
|03|Modelo híbrido: nube y on-premise|RT-03.01— RT-03.24|24|
|04|Ambientes, entrega continua y configuración|RT-04,01— RT-04.14|14|
|05|Datos, integración e interoperabilidad|RT-05.01— RT-05.30|30|
|06|Site principal on-premise|RT-06.01— RT-06.34|34|
|07|Site secundario y recuperación ante desastres|RT-07.01— RT-07.14|14|
|08|Hardware, puestos de trabajo y terreno|RT-08.01— RT-08.19|19|
|09|Desempeño, capacidad y escalabilidad|RT-09.01— RT-09.10|10|
|10|Disponibilidad, continuidad y resiliencia|RT-10.01— RT-10.09|9|
|all|Seguridad de la información|RT-11.01— RT-11.28|28|
|12|Identidad, acceso y sesiones|RT-12.01— RT-12.13|13|
|13|Usabilidad, accesibilidad y experiencia de usuario|RT-13.01— RT-13.12|12|
|14|Observabilidad y gestión del servicio|RT-14,01— RT-14.09|9|
|15|Sostenibilidad, eficiencia y certificaciones|RT-15.01— RT-15.09|9|
|16|Módulos transversales obligatorios|RT-16.01— RT-16.34|34|
|17|Canales digitales y movilidad|RT-17.01— RT-17.08|8|
|18|Inteligencia artificial y automatización|RT-18.01— RT-18.10|10|
|19|Estructura y gobierno del proyecto|RT-19.01— RT-19.10|10|
|20|Implantación, pruebas y aceptación|RT-20.01— RT-20.08|8|
|21|Operación, mantención y soporte|RT-21.01— RT-21.22|22|
|22|Capacitación y transferencia de conocimiento|RT-22.01— RT-22.09|9|
|23|Información corporativa y presencia digital|RT-23.01— RT-23.10|10|
|24|Video de presentación de la propuesta|RT-24.01— RT-24.06|6|
|25|Prototipo interactivo y diseño UX/UI|RT-25.01— RT-25.10|10|



Bases Técnicas Transversales TFEP-01/2026 46/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|Innovaciones|RT-26.01<br>— RT-26.08||
|---|---|---|
|TOTAL DE REQUISITOS CODIFICADOS||374|



###### CAPÍTULO B - PLANTILLA DE VOLUMETRÍA 

Las Bases Técnicas de cada caso entregan la volumetría real de la industria correspondiente, completando la siguiente plantilla. El PROPONENTE deberá dimensionar su solución sobre esos valores y declarar el margen de crecimiento considerado. 

|Transacciones de negocio anuales|
|---|
|Transacciones por segundo en régimen normal|
|Transacciones por segundo en peak|
|Personas usuarias registradas|
|Personas usuarias concurrentes|
|Contrapartes externas activas|
|Documentos procesados al año|
|Volumen de almacenamiento transaccional|
|Volumen de almacenamiento documental y<br>multimedia|
|Volumen de datos históricos a migrar|
|Dispositivos de terreno en operación|
|Sitios u operaciones a cubrir|
|Integraciones con sistemas internos|
|Integraciones con sistemas externos|
|Contactos mensuales al centro de atención|
|Ventana operacional crítica( horario y<br>estacionalidad)|



###### CAPÍTULO C - CHECKLIST DE ENTREGABLES DE LA OFERTA TÉCNICA 

Lista de verificación para el PROPONENTE. No reemplaza a los formularios del Anexo B de las Bases Administrativas ni altera sus exigencias. 

|Documento de arquitectura conforme a<br>ISO/IEC/IEEE 42010, con las cinco vistas|RT-02.03|SobreN*2|
|---|---|---|
|2<br>Registro de decisiones de arquitectura( ADR)|RT-02.04|SobreN*2|



Bases Técnicas Transversales TFEP-01/2026 47/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

||Tabla de emplazamiento de componentes en nube<br>y on-premise, justificada|Cap.3|SobreN*2|
|---|---|---|---|
||Declaración de funciones no disponibles en modo<br>desconectado|RT-03.13|SobreN*2|
||Modelo de datos y diccionario de datos|RT-05.01|SobreN*2|
||Plan de migración de datos|RT=05.11|SobreN*2|
||Documentación de interfaces en OpenAPlI y<br>AsyncAPl|RT-05.16|SobreN*2|
||Especificación del site principal y del site<br>secundario, con planos|Caps.6y7|SobreN*2|
||Plan de recuperación ante desastres y política de<br>respaldo|Cap.7|SobreN*2|
|10|Especificación del hardware y de los dispositivos<br>de terreno|Cap.8|SobreN*2|
|11|Cálculo de capacidad y dimensionamiento|RT-09.01|SobreN*2|
|12|Plan de continuidad del negocio conforme a ISO<br>22301|RT-10.03|SobreN*2|
|13|Modelado de amenazas y matriz de controles de<br>seguridad|RT-11.02 y RT-11.05|SobreN*2|
|14|Declaración de la superficie de exposición de la<br>solución|RT-11,13|SobreN*2|
|15|Plan de respuesta a incidentes de seguridad|RT-11.18|SobreN*2|
|16|Modelo de identidad, matriz de roles y segregación<br>de funciones|Cap.12|SobreN*2|
|17|Sistema de diseño e informe de conformidad de<br>accesibilidad|Cap.13|SobreN*2|
|18|Estrategia de observabilidad y catálogo de alertas|Cap.14|SobreN*2|
|19|Certificados institucionales y del personal|Cap.15|Sobre N* 1 y N* 2|
|20|Estrategia de pruebas y plan de pruebas<br>(Formulario T-13)|Cap.20|SobreN*2|
|21|Plan de implantación y de marcha blanca<br>(Formulario T-18)|RT-20.01|SobreN*2|
|22|Modelo de operación, soporte y<br>dimensionamiento del centro de atención|Cap.21|SobreN*2|
|23|Plan de capacitación y de transferencia de<br>conocimiento|Cap.22|SobreN*2|
|24|Matriz de cumplimiento técnico( Formulario T-12)<br>sobre todos los códigos RT|Numeral 1.5|SobreN*2|
|25|Sitio web corporativo activo y declaración jurada<br>de veracidad|Cap.23|SobreN*1|
|26|Video de presentación de la propuesta|Cap.24|Con la propuesta final|



Bases Técnicas Transversales TFEP-01/2026 48/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|Prototipo interactivo y arquitectura de información|Cap.25|Con el Informe 3|
|---|---|
|28|Fichas de las cinco innovaciones( Formulario T-19)|Cap.26|SobreN*2|



###### CAPÍTULO D - GLOSARIO Y DEFINICIONES 

Complementa el Artículo 3” de las Bases Administrativas. Ante discrepancia, prevalece la definición de dicho artículo. 

|Término|Definición|
|---|---|
|ADR|Architecture Decision Record. Registro fechado de una decisión de arquitectura, sus<br>:<br>alternativas y su fundamento.|
|AFIS|Automated Fingerprint Identification System. Sistema automatizado de identificación por<br>huella dactilar.|
|API|Application Programming Interface. Interfaz de programación que expone capacidades de<br>un sistema a otro.|
|ASVS|Application Security Verification Standard, de OWASP. Estándar de verificación de<br>seguridad de aplicaciones.|
|.<br>53<br>Capa anticorrupción|Componente que traduce el modelo de un sistema externo al modelo propio, impidiendo<br>.<br>que aquel contamine este.|
|CDN|Content Delivery Network. Red de distribución de contenidos.|
|CIS Benchmarks|Guías de configuración segura publicadas por el Center for Internet Security.|
|Cortacircuitos|Patrón que interrumpe las llamadas a una dependencia en falla para evitar la propagación<br>del error.|
|Despliegue azul-verde|Estrategia que mantiene dos entornos productivos y conmuta el tráfico entre ellos.|
|Despliegue canario|Estrategia que expone la nueva versión a una fracción creciente del tráfico.|
|DevSecOps|Integración de las prácticas de seguridad en el ciclo de desarrollo y operación.|
|ErlangC|Modelo de teoría de colas empleado para dimensionar centros de atención.|
|FCR|First Call Resolution. Resolución en el primer contacto.|
|FM-200|Agente limpio de extinción de incendios, apto para recintos con equipamiento electrónico.|
|laC|Infrastructure as Code. Infraestructura definida como código versionado.|
|.<br>Idempotencia|Propiedad de una operación que produce el mismo resultado aunque se ejecute varias<br>veces.|
|ITIL|Marco de buenas prácticas para la gestión de servicios de tecnologías de información.|
|Mamparo de<br>aislamiento|Patrón que separa recursos por grupo de consumo para que la falla de uno no agote los del<br>resto.|
|MTTR|Mean Time To Restore. Tiempo medio de restauración del servicio.|
|NOC|Network Operations Center. Centro de operaciones de red.|
|NCh<br>OpenTelemetry|Norma Chilena Oficial, emitida por el Instituto Nacional de Normalización.<br>Estándar abierto de instrumentación para métricas, registros y trazas.|



Bases Técnicas Transversales TFEP-01/2026 49/51 

Pontificia Universidad Católica de Valparaíso - Escuela de Informática 

Licitación N* TFEP-01/2026 - Bases Técnicas Transversales 

|Término<br>OWASP|Definición<br>Open Worldwide Application Security Project.|
|---|---|
|Percentil 95|Valor bajo el cual se encuentra el 95% de las mediciones. Refleja la experiencia de la cola<br>lenta, no el promedio.|
|PMBOK|Guía de fundamentos para la dirección de proyectos, del Project Management Institute.|
|PMO|Project Management Office. Oficina de gestión de proyectos.|
|Presupuesto de error|Fracción de indisponibilidad admitida por el objetivo de nivel de servicio, empleada para<br>regular el ritmo de cambios.|
|PUE|Power Usage Effectiveness. Relación entre la energía total consumida por un recinto y la<br>consumida por el equipamiento de Tl.|
|RAID|Redundant Array of Independent Disks. Arreglo redundante de discos.|
|RPO|Recovery Point Objective. Máxima pérdida de datos tolerada, expresada en tiempo.|
|RTO|Recovery Time Objective. Máximo tiempo tolerado para restituir el servicio.|
|sSBOM|Software Bill of Materials. Inventario de los componentes de un artefacto de software.|
|SIEM|Security Information and Event Management. Plataforma de correlación de eventos de<br>seguridad.|
|SLA/ SLO/ SLI|Acuerdo, objetivo e indicador de nivel de servicio.|
|SLSA|Supply-chain Levels for Software Artifacts. Marco de niveles de seguridad de la cadena de<br>suministro de software.|
|soc|Security Operations Center. Centro de operaciones de seguridad.|
|SRE|Site Reliability Engineering. Disciplina de operación de sistemas basada en ingeniería.|
|STRIDE|Metodología de modelado de amenazas: suplantación, manipulación, repudio, divulgación,<br>denegación y elevación de privilegios.|
|TPS|Transactions Per Second. Transacciones por segundo.|
|UAT|User Acceptance Testing. Pruebas de aceptación de usuario.|
|WAF|Web Application Firewall. Cortafuegos de aplicaciones web.|
|WCAG|Web Content Accessibility Guidelines. Pautas de accesibilidad para el contenido web.|
|Zero Trust|Modelo de seguridad en que ninguna red, dispositivo, identidad o carga de trabajo es<br>confiable por defecto.|



Bases Técnicas Transversales TFEP-01/2026 50/51 

