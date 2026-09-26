# **FORMULACIÓN DE PROVECTOS** 

**BASES TÉCNICAS** PARA LA PREPARACIÓN DE LA PROPUESTA 

Versión 1.0 Fecha Documento: 18-08-2026 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

## **Bases Técnicas - Minería** 

Compañía Minera Altos de Aranda S.A. - trazabilidad, productividad y cumplimiento en una operación de cobre a rajo abierto 

|**Asignatura**|Taller de Formulación de Proyectos Informáticos -<br>ICl-5444|
|---|---|
|**Unidad académica**|Escuela de Informática, Pontificia Universidad Católica de Valparaíso|
|**Profesor**|Antonio Moya Villegas -<br>antonio.moya@pucv.cl|
|**Industria**|Minería -<br>extracción de recursos. Cobre a rajo abierto|
|**Mandante**|Compañía Minera Altos de Aranda S.A.( empresa ficticia)|
|**Faena**|Rajo Aranda, Sierra Gorda, Región de Antofagasta, 3.180 m s. n. m.|
|**Documentos que rigen**|Bases Administrativas FEP0l.26 y Bases Técnicas Transversales FEP02.26|
|**Duración del contrato**|56 meses: implementación en dos etapas y 36 meses de operación|
|**Versión**|1.0 -<br>agosto de 2026|



Este documento no es una especificación de requerimientos. Es la descripción de una operación real, con sus datos, sus dolores, sus contradicciones internas y sus vacíos. 

Identificar qué es funcional y qué no lo es, completar lo que falta con supuestos declarados y con reglas de negocio propias de la industria, investigar aquello que el documento no explica, y traducir todo ello en un alcance, una arquitectura, un plan y una estrategia de puesta en producción, es exactamente el trabajo que se está licitando y lo que será evaluado. 

Caso 01 · Minería · TFEP-01/2026 1 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

#### **CONTENIDO** 

||**Contenido**||
|---|---|---|
|**1**·** El mandante y el encargo**|Cómo llegamos a esta licitación, la compañía, sus cifras y los<br>sitios de la operación.|1-3|
|**11**·** La operación tal como es hoy**|El ciclo del mineral del banco al embarque, los sistemas<br>existentes, la conectividad y los indicadores del problema.|4-7|
|**111**·** Lo que dicen quienes operan**|Diez entrevistas de levantamiento, con sus contradicciones<br>intactas.|8|
|**IV· Lo que el mandante espera**|Expectativas de negocio, restricciones no negociables,<br>exclusiones, marco normativo y prioridades.|9-13|
|**V**·** Antecedentes para el**<br>**dimensionamiento**|Volumetría entregada y volumetría a estimar, parámetros del<br>caso y decisiones deliberadamente no resueltas.|14-16|
|**VI**·** Lo que debe producir el**<br>**proponente**|El trabajo de traducción exigido, los criterios de aceptación y<br>cómo se evaluará este caso.|17-19|
|**VII**·** Anexos del caso**|Mapa de sistemas y flujos actuales, calendario operacional y<br>glosario de la industria.|A-C|



###### **Cómo leer este documento** 

Los Títulos I y 11 describen la operación. Se entregan con detalle porque de ellos dependen todas las decisiones de diseño: no hay atajo que permita saltarlos. 

El Título 111 recoge las voces de quienes operan. No están de acuerdo entre sí, y esa discrepancia es información, no ruido: revela dónde el proyecto va a encontrar resistencia y qué tensiones habrá que arbitrar. 

El Título IV expresa lo que el mandante espera, deliberadamente en lenguaje de negocio y no de requerimientos. El Título V entrega los datos duros que la compañía conoce, señala cuáles debe estimar el proponente, fija los parámetros de los requisitos que las Bases Técnicas Transversales dejaron abiertos al caso, y enumera catorce decisiones que el cliente no ha tomado. 

El Título VI describe el trabajo exigido y los criterios con que se juzgará. Conviene leerlo primero y volver a él al final. 

Sobre la ausencia de una lista de requerimientos. 

En un proceso real, el cliente rara vez entrega un catálogo de requerimientos bien formado. Entrega su operación, sus problemas y sus expectativas, y espera que el proveedor sepa convertirlos en un proyecto. Ese es el ejercicio. 

Todo lo que este documento no dice está dicho en alguna parte: en la operación descrita, en lo que alguien mencionó al pasar en una entrevista, en un indicador que no cuadra, en una restricción que parece menor, o en la práctica habitual de la industria del cobre, que el proponente deberá estudiar. 

Caso 01 · Minería · TFEP-01/2026 2 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

##### **TÍTULO 1** 

### **EL MANDANTE Y EL ENCARGO** 

##### **CAPÍTULO 1 CÓMO LLEGAMOS A ESTA LICITACIÓN** 

El 14 de abril de 2026, a las once de la mañana, Rodrigo Palma Echeñique entró a la sala del directorio de Compañía Minera Altos de Aranda con una carpeta de nueve páginas y la certeza de que no iba a salir de ahí sin una decisión. 

Tres semanas antes, el comprador japonés que se lleva el 38 % del concentrado de Aranda había enviado una carta breve y cortés. Renovaría el contrato de largo plazo, pero a partir de 2029 exigiría trazabilidad verificable del origen del mineral, huella de carbono por tonelada de cobre fino calculada trimestralmente y auditada por un tercero, y evidencia documental de las condiciones laborales de la cadena de suministro. La carta terminaba con una frase que Rodrigo leyó en voz alta al directorio: «entendemos que esto puede requerir adecuaciones y estamos disponibles para acompañarlas». 

« Lo que están diciendo con mucha educación», explicó Rodrigo, «es que si en tres años no podemos demostrar de dónde viene cada tonelada, se van a comprar el cobre a otro lado. Y no son los únicos: el mismo requerimiento me llegó del comprador coreano en enero, con otras palabras.» 

El problema, y esto Rodrigo lo sabía mejor que nadie en esa sala, es que Altos de Aranda no puede responder esa pregunta hoy. No con precisión, no en un plazo razonable y no sin que tres áreas distintas entreguen tres números distintos. 

El año anterior, cuatro de los treinta y un embarques recibieron penalización por contenido de arsénico sobre el límite del contrato. Costó un millón novecientos mil dólares en menor ingreso. Cuando el directorio pidió saber de qué sector del rajo venía ese mineral -para dejar de mezclarlo, o para mezclarlo distinto-, la respuesta tomó cinco semanas y llegó con una advertencia de la Superintendencia de Planificación: «es una estimación; con los registros que tenemos no se puede afirmar más que eso». 

Sebastián Ortúzar, gerente de finanzas, agregó el segundo golpe de la mañana. La conciliación metalúrgica del mes -el ejercicio de cuadrar cuánto cobre salió de la mina, cuánto entró a la planta, cuánto se recuperó y cuánto se embarcó- cierra dieciocho días hábiles después del cierre contable, con diferencias que en los últimos doce meses oscilaron entre 3,1 % y 6,8 %. «En una operación de cien mil toneladas de cobre fino al año», dijo, «cada punto porcentual de diferencia son diez millones de dólares que no sabemos si perdimos, si nunca existieron o si están en un stock que nadie contó bien.» 

Carolina Vidal Ossandón, gerenta de operaciones mina, planteó el asunto desde el otro extremo. «Yo tengo treinta y ocho camiones, cinco palas y nueve perforadoras. Tengo un sistema de despacho que funciona bien y me dice dónde está cada camión. Tengo tres portales web distintos, uno por cada fabricante, con la telemetría de los equipos. Tengo el mantenimiento en SAP. Y no tengo una sola pantalla donde eso se cruce. Cuando un camión se detiene, mi supervisor abre cuatro sistemas para entender qué pasó, y en el intertanto el camión sigue detenido.» 

Paula Guerrero Liza na, gerenta de sustentabilidad y asuntos regulatorios, cerró el cuadro. « Nosotros reportamos a la Superintendencia del Medio Ambiente con planillas que armo a mano con datos que me llegan por correo de cinco áreas distintas. El año pasado nos hicieron una observación por inconsistencia entre dos 

Caso 01 · Minería · TFEP-01/2026 3 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

reportes. La observación era correcta: los datos no cuadraban, y no cuadraban porque los saqué de fuentes distintas en momentos distintos. Si esto sigue así, la próxima observación no va a ser una observación.» 

Fue Ignacio Bustos Carvajal, jefe de mantenimiento, quien puso la nota discordante, y el directorio agradeció después que lo hiciera. «Antes de que aprueben otro proyecto», dijo, «quiero recordar que en 2018 compramos una plataforma de mantenimiento predictivo. Costó ochocientos mil dólares. La usamos catorce meses. Hoy está apagada. El problema no fue el software: el problema fue que nadie de nosotros participó en definir qué necesitábamos, nos entregaron un sistema hecho para otra faena y los alertas eran tantas que dejamos de mirarlas. Si vamos a hacer esto de nuevo, háganlo bien.» 

El directorio aprobó, por unanimidad, licitar el proyecto. En el acta quedó consignada una condición que Rodrigo pidió incorporar textualmente: «el proyecto se adjudicará a quien demuestre que entendió la operación de Aranda, no a quien ofrezca la tecnología más avanzada». 

Este documento es el resultado de nueve meses de levantamiento, más de cuarenta entrevistas en faena y en oficina, y tres talleres con las gerencias involucradas. No es una especificación. Es la descripción, lo más honesta que el CLIENTE ha sido capaz de hacer, de una operación real con sus datos, sus dolores, sus contradicciones internas y sus vacíos. Traducir esto en requerimientos es el trabajo del PROPONENTE, y es precisamente lo que se evalúa. 

#### **CAPÍTULO 2 LA COMPAÑÍA** 

###### **2.1 Identificación** 

|**Antecedente**|.<br>- -<br>-|
|---|---|
|**Razón social**|Compañía Minera Altos de Aranda S.A.|
|**Giro**|Extracción, procesamiento y comercialización de minerales de cobre.|
|**Producto**|Concentrado de cobre con contenido de oro y plata como subproductos.|
|**Faena**|Rajo Aranda, comuna de Sierra Gorda, Región de Antofagasta.|
|**Emplazamiento**|3.180 metros sobre el nivel del mar, a 145 km de Antofagasta por Ruta 25 y 26 km<br>de camino privado.|
|**Inicio de operaciones**|2009.|
|**Vida útil remanente del plan**<br>**minero**|14 años.<br>~<br>-|
|**Oficina corporativa**|<br>Santiago, comuna de Las Condes.|
|**Centro Integrado de**<br>**Operaciones**|Antofagasta, inaugurado en 2022, con 24 posiciones de operación.|
|**Propiedad**|Sociedad anónima cerrada. Controlador internacional con 70%; grupo inversor<br>1 nacional con 30%.|



###### **2.2 Cifras de la operación** 

Caso 01 · Minería · TFEP-01/2026 4 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

|**Indicador**||
|---|---|
|**Mineral enviado a planta**|21,5 millones de toneladas al año|
|**Razón estéril/ mineral**|2,8:1|
|**Capacidad nominal de la concentradora**|59.000 toneladas por día|
|**Ley media de cabeza**|0,54 % de cobre|
|**Recuperación metalúrgica**|86,5%|
|**Producción de cobre fino**|:::100.000 toneladas al año|
|**Producción de concentrado**|:::372.000 toneladas al año, base seca, con ley de 27 % de<br>cobre|
|**Embarques anuales**<br>-|31, de aproximadamente 12.000 toneladas cada uno<br>-<br>-|
|**Transporte a puerto**|:::34 viajes diarios de camión, con 30 toneladas netas por<br>viaje|
|**Costo directo de operación**|1,92 dólares por libra de cobre fino|



###### **2.3 Equipamiento principal** 

|||**Observación**<br>1|
|---|---|---|
|**Camiones de extracción de 240**<br>**toneladas**|38|Tres generaciones distintas, dos fabricantes. Antigüedad<br>promedio 7,4 años.|
|**Palas eléctricas de cable**|5|Un fabricante. La más antigua tiene 16 años.|
|**Cargadores frontales**<br>-|3<br>~<br>-<br>-|ayo y carguío en stocks.<br>-|
|**Perforadoras**|9|Dos fabricantes, con niveles distintos de instrumentación.|
|**Equipos de apoyo**|62|Motoniveladoras, bulldozers, camiones aljibe,<br>camionetas de operación.|
|**Flota liviana de faena**|310 vehículos|Mayoritariamente de contratistas.|



###### **2.4 Las personas** 

|-:.|**Dotación**|**Régimen**<br>1|
|---|---|---|
|**Personal propio**|1.780|Turno 7x7 en faena; jornada ordinaria en<br>Antofagasta y Santiago.|
|**Contratistas permanentes**|2.400|Turno 7x7. Alrededor de 90 empresas<br>contratistas activas.|
|**Contratistas en detención mayor de**<br>**planta**|hasta 4.300 adicionales<br>-<br>-|Dos veces al año, seis días cada vez, en marzo y<br>septiembre.<br>-|
|**Personal en el Centro Integrado de**<br>**Operaciones**|115|Turnos rotativos en Antofagasta.|
|**Capacidad del campamento**|1.900 camas|A 9 km de la faena.|



La faena opera de forma continua, veinticuatro horas al día, los trescientos sesenta y cinco días del año, en dos turnos de doce horas: día de 08:00 a 20:00 y noche de 20:00 a 08:00. El cambio de turno se realiza en el Centro Integrado de Operaciones para el personal de sala de control y en los puntos de encuentro del rajo para el personal de operación de equipos. 

Caso 01 · Minería · TFEP-01/2026 5 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

##### **CAPÍTULO 3 LOS SITIOS DE LA OPERACIÓN** 

El PROPONENTE deberá considerar que la operación se distribuye en seis emplazamientos con condiciones muy distintas entre sí. El diseño de la solución tiene que hacerse cargo de esa heterogeneidad. 

||.<br>-.|**Condiciones relevantes**|
|---|---|---|
|**Rajo Aranda**|Perforación, tronadura, carguío y<br>transporte de mineral y estéril. Botaderos y<br>stocks intermedios.|A la intemperie, entre- 6º C y 34º C, con viento,<br>polvo en suspensión y radiación solar extrema.<br>El fondo del rajo está 340 metros bajo el nivel<br>de la plataforma. Cobertura de red desigual.|
|**Planta concentradora**|Chancado, molienda, flotación,<br>espesamiento y filtrado. Sala de control de<br>proceso.|Operación continua. Ambiente industrial con<br>ruido, vibración y humedad en algunos<br>sectores. Red de control de proceso segregada.|
|**Depósito de relaves**|Disposición de relaves espesados.<br>Monitoreo geotécnico y de aguas.|A 6 km de la planta. Instrumentación existente<br>con transmisión intermitente. Obligaciones de<br>monitoreo ante la autoridad.|
|**Área de servicios y **<br>**portería**|Acceso a faena, acreditación, control de<br>contratistas, policlínica, bodegas, talleres<br>de mantenimiento.|Concentra el flujo de personas. Es el punto<br>donde hoy se producen los rechazos de<br>ingreso.|
|**Acopio y embarque**<br>**en Antofagasta**|Recepción del concentrado desde faena,<br>acopio de 25.000 toneladas y embarque en<br>terminal de terceros.|Recinto portuario administrado por un tercero.<br>Interacción con nave, agente de aduana y<br>organismo fiscalizador.|
|**Centro Integrado de**<br>**Operaciones**|Sala de control integrada de mina y planta,<br>planificación de corto plazo, despacho y<br>análisis.|En Antofagasta, a 145 km de la faena. Depende<br>íntegramente del enlace de comunicaciones.|
|**Oficina corporativa**|Finanzas, comercial, sustentabilidad,<br>abastecimiento y tecnologías de<br>información.|En Santiago. Trabajo mixto, con tres días<br>presenciales y dos desde el hogar.|



El Centro Integrado de Operaciones fue construido en 2022 con la expectativa de trasladar allí buena parte de la operación de la mina. Hoy se utiliza cerca del 40 % de su capacidad instalada, porque varias funciones no pudieron trasladarse: dependían de información que sólo existe en la faena o en la cabeza de quien está en la faena. Revertir esa situación es uno de los resultados que el CLIENTE espera del proyecto, aunque no está declarado como requerimiento. 

Caso 01 · Minería · TFEP-01/2026 6 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

##### **TÍTULO 11** 

### **LA OPERACIÓN TAL COMO ES HOY** 

##### **CAPÍTULO 4 · EL CICLO DEL MINERAL, DEL BANCO AL EMBARQUE** 

Lo que sigue es la descripción del proceso tal como ocurre, no como debería ocurrir. Se entrega con este nivel de detalle porque de él dependen las decisiones de alcance, de arquitectura y de trazabilidad que el PROPONENTE deberá tomar. 

###### **4.1 Planificación y diseño** 

El plan minero de largo plazo se construye sobre el modelo de bloques del yacimiento, en un software especializado de planificación que la compañía mantiene y que no forma parte de esta licitación. De ese plan se derivan un plan anual, un plan trimestral y un plan semanal. El plan semanal se traduce en polígonos de extracción: sectores acotados de un banco, con una ley estimada, un destino asignado -planta, stock de baja ley o botadero- y un tonelaje planificado. 

Los polígonos se dibujan en el software de planificación y se comunican a la operación mediante un archivo que el planificador exporta cada domingo y publica en una carpeta compartida. La operación los carga manualmente en el sistema de despacho de flota. Los cambios que ocurren durante la semana -y ocurren todas las semanas- se comunican por radio y por el grupo de mensajería del turno. 

Nadie lleva un registro consolidado de cuántas veces se modificó el plan semanal ni por qué. El cumplimiento del plan se calcula al cierre del mes, comparando el tonelaje planificado con el tonelaje registrado por el sistema de despacho, con un desfase de entre diez y quince días. 

###### **4.2 Perforación y tronadura** 

Las perforadoras ejecutan las mallas de perforación diseñadas por el área de perforación y tronadura. Dos de las nueve perforadoras registran automáticamente la posición, la profundidad y los parámetros de perforación de cada pozo; las siete restantes no, y su avance se registra en una planilla que el operador entrega al final del turno. 

Los datos de perforación contienen información valiosa sobre la dureza del macizo rocoso, que hoy no se aprovecha. El área de geología los pidió tres veces; en dos ocasiones se los entregaron en un formato que no pudieron procesar. 

Tras la tronadura, el sector queda disponible para carguío. La coordinación entre el momento en que se libera un sector y el momento en que la operación lo sabe se realiza por radio. 

###### **4.3 Carguío y transporte** 

Cinco palas cargan camiones de 240 toneladas. El sistema de despacho de flota, provisto por el fabricante de la mayor parte de los camiones, asigna cada camión a una pala y a un destino, registra los tiempos de ciclo y estima el tonelaje transportado a partir del peso registrado por el sistema de pesaje de a bordo del camión. 

Ese sistema funciona bien y la compañía está conforme con él. Tiene contrato vigente hasta 2031 y no se reemplaza. El problema es que su información vive dentro de él: se puede consultar en sus propias pantallas y se puede exportar en informes, pero no se cruza con nada más de forma automática. 

Caso 01 · Minería · TFEP-01/2026 7 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

El operador de la pala identifica visualmente el material que está cargando y, cuando estima que el material no corresponde al del polígono planificado -porque cambió la mineralización o porque la tronadura desplazó el contacto-, lo informa por radio al despachador, quien puede reasignar el destino del camión. Ese cambio queda registrado en el sistema de despacho, pero la razón del cambio no. 

Los camiones descargan en el chancador primario, en los stocks de mineral, en el stock de baja ley o en los botaderos. En la salida del área de descarga hay una báscula de camiones que pesa una muestra de los viajes, no todos, para calibrar el pesaje de a bordo. Los tres números -el peso de a bordo, el peso de la báscula y el tonelaje que la planta declara haber procesado- no coinciden, y cada área utiliza el que le resulta más conveniente para su informe. 

###### **4.4 Stocks intermedios** 

Entre la mina y la planta existen stocks de mineral que operan como pulmón. El mineral se acopia y se retoma con cargadores frontales según lo requiera la mezcla que la planta necesita. Cada stock recibe material de distintos polígonos a lo largo de semanas. 

El control de qué hay en cada stock se lleva en una planilla que actualiza el supervisor de turno. Cuando se retoma material de un stock, se asume que la ley del material retomado corresponde al promedio ponderado de lo que se acopió. Nadie ha verificado ese supuesto. 

**El tratamiento de los stocks intermedios es uno de los puntos donde la trazabilidad se rompe hoy. El CLIENTE no tiene una respuesta definida sobre cómo debería resolverse. Es una decisión de diseño que el PROPONENTE deberá tomar, justificar y declarar como supuesto.** 

###### **4.5 Procesamiento** 

El mineral pasa por chancado primario, secundario y terciario, molienda, flotación colectiva y selectiva, espesamiento y filtrado. El proceso está controlado por un sistema de control distribuido con su historiador de proceso, en una red segregada de la red administrativa. Esa red es intocable: la compañía autoriza leer de ella, no escribir en ella. 

El laboratorio químico analiza muestras de alimentación, de concentrado y de relave, con una frecuencia definida por procedimiento. Los resultados se registran en un sistema de gestión de laboratorio que la compañía mantiene y que no se reemplaza. El tiempo entre la toma de la muestra y la disponibilidad del resultado es de entre cuatro y treinta y seis horas, según el tipo de análisis. 

El balance metalúrgico del turno lo calcula el metalurgista de turno en una planilla. El balance del mes lo calcula el área de metalurgia en otra planilla, más completa, que consolida los turnos y aplica factores de ajuste que se han ido incorporando a lo largo de los años y que hoy sólo dos personas saben explicar. 

###### **4.6 Despacho, transporte a puerto y embarque** 

El concentrado filtrado se acopia en la faena y se carga en camiones para su transporte a Antofagasta. Cada camión sale con una guía de despacho y una planilla de pesaje. En el acopio del recinto portuario el concentrado se descarga y se acopia por lotes. 

Cuando se programa un embarque, se conforma el lote comercial mezclando material del acopio. Se toman muestras conforme al protocolo acordado con el comprador, se determinan la humedad y la ley, y se emiten los documentos de embarque. La liquidación con el comprador se realiza meses después, sobre la base del análisis de una muestra que se dirime entre el laboratorio del vendedor, el del comprador y, si hay discrepancia, un tercer laboratorio árbitro. 

Caso 01 · Minería · TFEP-01/2026 8 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

Reconstruir de qué polígonos del rajo proviene el mineral de un lote embarcado es, hoy, un ejercicio de arqueología documental que toma entre cuatro y seis semanas y cuyo resultado es una estimación. 

###### **4.7 Mantenimiento** 

El mantenimiento se planifica en el módulo correspondiente de SAP, con pautas preventivas basadas en horas de operación y en calendario. El mantenimiento correctivo se gestiona con avisos que el operador levanta por radio y que un planificador transcribe al sistema. 

Los fabricantes de los camiones, de las palas y de las perforadoras entregan telemetría de sus equipos a través de tres portales web distintos. Cada portal muestra alarmas, horas de operación, consumos y códigos de falla. Ninguno de los tres está integrado con SAP ni con el sistema de despacho. Nadie mira los tres portales de forma sistemática: el jefe de mantenimiento revisa uno, el planificador revisa otro cuando tiene tiempo, y el tercero prácticamente no se abre. 

La compañía no tiene claridad contractual sobre quién es dueño de los datos de telemetría que generan sus propios equipos ni sobre si puede extraerlos por vía programática. El asunto se planteó una vez a un fabricante y la respuesta fue que existía un servicio adicional para ello. 

###### **4.8 Seguridad, salud ocupacional y control de acceso** 

Para ingresar a la faena, toda persona debe estar acreditada: contrato vigente, exámenes preocupacionales al día, cursos de inducción y de riesgos específicos aprobados, y credencial emitida. La acreditación de un trabajador contratista nuevo demora en promedio nueve días. 

El control se realiza en portería con torniquetes y lectura de credencial. La validación documental se apoya en una planilla que mantiene el área de seguridad y salud ocupacional y que se actualiza manualmente. El catorce por ciento de los rechazos en portería corresponde a documentos vencidos que nadie advirtió con anticipación; el trabajador viaja seiscientos kilómetros para que le nieguen el ingreso. 

Los incidentes, los cuasi accidentes, las observaciones de conducta y las inspecciones planificadas se registran en formularios de papel que después alguien digita. La Superintendencia de Seguridad exige poder mostrar esos registros ante fiscalización, y en la última auditoría de la autoridad seis de las once observaciones tuvieron relación con la trazabilidad de esos registros. 

El control de fatiga y somnolencia opera con cámaras instaladas en las cabinas de los camiones, provistas por un tercero, con su propia plataforma. Las alertas llegan a un correo y a un teléfono de turno. No hay registro consolidado de qué se hizo ante cada alerta. 

###### **4.9 Medio ambiente y comunidades** 

La Resolución de Calificación Ambiental de la faena establece compromisos de monitoreo y de reporte: consumo de agua, calidad del aire, ruido, monitoreo geotécnico y de aguas subterráneas en el depósito de relaves, y control de emisiones. Cada compromiso tiene su frecuencia, su punto de medición y su destinatario. 

La información proviene de instrumentos propios, de laboratorios externos y de planillas de operación. Se consolida manualmente en el área de sustentabilidad. La huella de carbono se calcula una vez al año con apoyo de una consultora externa. 

Existe además un convenio con la comunidad más próxima que compromete indicadores de empleo local y de compras locales, hoy reportados semestralmente y construidos a mano desde información de abastecimiento y de recursos humanos. 

Caso 01 · Minería · TFEP-01/2026 9 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

##### **CAPÍTULO 5 · LOS SISTEMAS QUE EXISTEN HOY** 

El PROPONENTE deberá integrarse a este panorama, no reemplazarlo. La columna de destino indica la decisión ya tomada por el CLIENTE respecto de cada sistema. 

|||**Destino**|
|---|---|---|
|**ERP corporativo( SAP**<br>**S/4HANA)**|Finanzas, abastecimiento, inventarios,<br>recursos humanos y planificación de<br>mantenimiento.|Se mantiene. Es el sistema de registro<br>contable y de gestión. La solución le entrega<br>datos; no lo reemplaza ni lo modifica.|
|**Sistema de despacho de**<br>**flota**|Asignación de camiones, tiempos de<br>ciclo, pesaje de a bordo,<br>posicionamiento.|Se mantiene. Contrato vigente hasta 2031.<br>Debe integrarse.|
|**Sistema de control**<br>**distribuido e historiador**<br>**de proceso**|Control y registro del proceso de la<br>planta.|Se mantiene, en red segregada. Sólo lectura.<br>No se escribe en la red de control.|
|**Sistema de gestión de**<br>**laboratorio**|Registro de muestras, análisis y<br>resultados.|Se mantiene. Debe integrarse en ambos<br>sentidos.|
|**Software de planificación**<br>**minera**<br>-|Modelo de bloques, diseño,<br>secuenciamiento y plan minero.<br>-|Se mantiene. La solución consume sus<br>salidas.<br>-|
|**Sistema de pesaje de**<br>**báscula de camiones**|Pesaje de control en la salida del área de<br>descarga y en el despacho a puerto.|Se mantiene el equ ipamiento. Su software<br>local puede reemplazarse si el PROPONENTE<br>lo justifica.|
|**Portales de telemetría de**<br>**fabricantes (tres)**|Alarmas, horas, consumos y códigos de<br>falla por marca de equipo.|Se mantienen como fuente. La integración y<br>la negociación técnica con los fabricantes<br>son parte del alcance del PROYECTO.|
|**Plataforma de control de**<br>**fatiga y somnolencia**|Cámaras en cabina y alertas de un<br>tercero.|Se mantiene. Debe integrarse.|
|**Control de acceso de**<br>**portería**|Torniquetes y lectura de credencial.|El equipamiento se mantiene o se amplía. La<br>gestión de acreditación es parte del alcance.|
|**Planillas de cálculo y **<br>**carpetas compartidas**|Acreditación, balance metalúrgico,<br>control de stocks, reporte ambiental,<br>cumplimiento del plan, indicadores de<br>comunidad.|Deben desaparecer como sistema de<br>registro. Ese es, en buena medida, el objeto<br>de esta licitación.|



El CLIENTE no dispone de un inventario técnico completo de estos sistemas: no tiene documentadas todas sus interfaces, ni sus versiones exactas, ni las condiciones contractuales de acceso a sus datos. Levantar esa información es parte del trabajo del ADJUDICATARIO durante los primeros meses del PROYECTO, y el riesgo asociado debe estar reflejado en la propuesta. 

Caso 01 · Minería · TFEP-01/2026 10 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

###### **CAPÍTULO 6 · CONECTIVIDAD Y CONDICIONES DEL SITIO** 

||**Situación actual**|
|---|---|
|**Enlace faena**-<br>**Antofagasta**|Fibra óptica de un único proveedor, con respaldo satelital de capacidad reducida. Se<br>registran entre tres y seis cortes de fibra al año, con duraciones de cuatro a veinte horas.<br>Durante el corte, el enlace satelital sostiene la telefonía y el correo, pero no soporta la<br>operación de sistemas transaccionales.|
|**Red interna de faena**|Fibra propia entre la portería, la planta, los talleres y el edificio de administración.<br>Cableado estructurado en buen estado en administración y planta; deficiente en talleres.|
|**Red inalámbrica del rajo**|Red LTE privada instalada en 2021, con cobertura en la plataforma principal, las rampas<br>superiores y los accesos. Existen zonas de sombra permanentes en el fondo del rajo, en el<br>botadero norte y en dos sectores de rampa. La cobertura se degrada con el avance del<br>rajo y no ha sido reevaluada desde su instalación.|
|**Depósito de relaves**|Instrumentación geotécnica con transmisión por radioenlace, con interrupciones<br>frecuentes. Sin cobertura de datos continua.|
|**Acopio y embarque en**<br>**Antofagasta**|Recinto de terceros. Conectividad provista por el operador portuario, sin acuerdo de nivel<br>de servicio con la compañía.|
|**Energía en faena**|Suministro desde el sistema eléctrico nacional con respaldo de generación propia para las<br>instalaciones críticas. La sala de servidores actual cuenta con energía respaldada y<br>climatización, pero sin redundancia.|
|**Sala de servidores de**<br>**faena**|Recinto de 40 metros cuadrados en el edificio de administración, habilitado en 2014, con<br>climatización simple, alimentación ininterrumpida de 15 minutos y control de acceso por<br>llave. No cumple los estándares del Capítulo 6 de las Bases Técnicas Transversales.|
|**Condiciones ambientales**<br>**del rajo**|Temperaturas entre- 6º C y 34º C, viento con ráfagas sobre 70 km/h, polvo en suspensión<br>permanente y radiación solar extrema. El personal opera con guantes y lentes de<br>seguridad.|



**La compañía ha sido explícita en un punto: la operación de la mina y de la planta no puede quedar detenida por un corte del enlace con Antofagasta. Cualquier arquitectura que suponga conectividad permanente hacia la nube para sostener la operación en terreno será rechazada.** 

###### **CAPÍTULO 7 · LO QUE DUELE: INDICADORES DEL PROBLEMA** 

Los siguientes datos corresponden al ejercicio 2025 y provienen de los registros de la compañía. Se entregan porque dimensionan el problema y porque el PROPONENTE deberá comprometer mejoras verificables sobre ellos. 

**7 .1 Trazabilidad y conciliación** 

|||**Referencia de industria**<br>----------|
|---|---|---|
|**Diferencia de conciliación metalúrgica mina-**<br>**planta-embarque**|entre 3,1% y 6,8% mensual|bajo 2%|
|**Días hábiles para cerrar la conciliación del mes**|18|1<br>3a5|
|**Tiempo para reconstruir el origen de un lote**|4 a 6 semanas, con resultado|horas, con resultado|
|**embarcado**|estimado|verificable|



Caso 01 · Minería · TFEP-01/2026 11 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

|**Indicador**|**Valor 2025**|**Referencia de industria**|
|---|---|---|
|**Embarques con penalización por arsénico**|4de31|1<br>-|
|**Menor ingreso por penalizaciones**|USD 1,9 millones|1<br>-|
|**Verificación del supuesto de ley en retoma de**<br>**stocks**|nunca realizada|1<br>-|



###### **7 .2 Productividad de la operación** 

|**Utilización efectiva de la flota**|71%|80%|
|---|---|---|
|**Demoras operacionales sin clasificar**|23% del tiempo registrado|bajo 5%|
|**Horas de detención no programada de planta**|214 horas en el año|bajo 120|
|**Detenciones sin causa raíz documentada**|61%|bajo 10%|
|**Tiempo medio entre falla y diagnóstico en equipo mina**|4,2 horas|1 hora|
|**Pérdida efectiva por cambio de turno**|47 minutos por turno|25 minutos|
|**Cumplimiento del plan semanal medido con desfase**|10 a 15 días|el turno siguiente|



###### **7.3 Personas, seguridad y cumplimiento** 

|**Días promedio para acreditar a un trabajador contratista nuevo**||
|---|---|
|**Rechazos en portería por documentación vencida no advertida**|14% de los rechazos|
|**Observaciones en la última auditoría de la autoridad minera**|**11,** de las cuales 6 por trazabilidad<br>de registros|
|**Registros de seguridad en papel digitados con posterioridad**|prácticamente la totalidad|
|**Alertas de fatiga con acción documentada**|sin registro consolidado|
|**Observación de la autoridad ambiental por inconsistencia de reportes**|1|
|**Frecuencia de cálculo de la huella de carbono**|anual, con consultora externa|
|**Frecuencia exigida por los compradores a partir de 2029**|trimestral y auditada|



Ninguno de estos indicadores se resuelve comprando software. Se resuelven cambiando la forma en que se captura el dato en el punto donde ocurre el hecho, y asegurando que ese dato viaje sin transformarse a mano. El PROPONENTE que entienda esto y lo demuestre en su propuesta tendrá una ventaja evidente sobre quien ofrezca módulos. 

Caso 01 · Minería · TFEP-01/2026 12 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

##### **TÍTULO 111** 

### **LO QUE DICEN QUIENES OPERAN** 

###### **CAPÍTULO 8 · ENTREVISTAS DE LEVANTAMIENTO** 

Las siguientes son transcripciones editadas de las entrevistas de levantamiento sostenidas entre agosto y diciembre de 2025. Se entregan con sus contradicciones intactas, porque las contradicciones son parte del problema. 

El PROPONENTE debe leerlas como lo que son: la palabra de personas que conocen muy bien su parte de la operación y que no tienen por qué conocer la de los demás, ni tienen por qué saber de sistemas. Distinguir el hecho de la opinión, la necesidad del capricho y el problema de la solución que la persona ya se imaginó es parte del trabajo profesional que se está licitando. 

**Rodrigo Palma Echeñique** · Gerente General 

Yo llevo cuatro años en Aranda y voy a ser franco con ustedes: esta compañía opera bien. Producimos lo que prometemos, tenemos buen costo, la gente es competente. Lo que no tenemos es la capacidad de demostrarlo con datos. 

Cuando el directorio me pregunta por qué el costo por tonelada subió tres por ciento el mes pasado, yo tengo una explicación, pero es una explicación construida a mano por cuatro personas durante tres días. Cuando el comprador me pregunta de dónde viene el mineral de un embarque, tengo una estimación. Cuando la autoridad me pide los registros de una fiscalización, mando a alguien a buscar carpetas. 

Lo que necesito es que la operación deje huella. Que cada cosa que pasa quede registrada donde pasa, en el momento en que pasa, y que después esa huella se pueda seguir hacia adelante y hacia atrás. Suena simple dicho así. Sé que no lo es. 

Y le voy a pedir una cosa más, porque de esto depende que el proyecto sirva. No quiero un sistema que le agregue trabajo al que está operando. Si para que yo tenga mi trazabilidad el operador de la pala tiene que llenar tres pantallas más, esto va a fracasar. La huella tiene que salir de lo que la gente ya hace, no de lo que le vamos a pedir que haga. 

**Carolina Vidal Ossandón** · Gerenta de Operaciones Mina 

Mi trabajo es mover ochenta y dos millones de toneladas al año. Todo lo que me haga mover menos toneladas es un problema, por muy buena que sea la intención. 

Yo tengo un sistema de despacho que funciona. Está bien implementado, la gente lo usa, me entrega los tiempos de ciclo y me dice dónde está cada camión. Si vienen a decirme que lo van a reemplazar, la conversación se termina ahí. 

Lo que sí necesito es que la información salga de ahí y se cruce. Hoy, si un camión se detiene, mi supervisor tiene que abrir el despacho para ver dónde está, el portal del fabricante para ver si tiró alguna alarma, SAP para ver si tenía una pauta pendiente, y llamar por radio para preguntar qué pasó. Cuatro sistemas y una radio. Eso son quince o veinte minutos con un camión de doscientas cuarenta toneladas parado. 

Caso 01 · Minería · TFEP-01/2026 13 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

Del tema de la trazabilidad les voy a decir algo que a lo mejor no les gusta. Yo entiendo por qué el gerente general la quiere. Pero cuando la pala está cargando y el operador ve que el material cambió, lo que hace es avisar por radio y seguir cargando. Si ahora le vamos a pedir que además clasifique el material en una pantalla, que declare por qué cambió y que espere una confirmación, me van a bajar el rendimiento de la pala. Y el rendimiento de la pala es el rendimiento de la mina. 

Ah, y sobre las zonas de sombra. Nos dijeron cuando instalaron la red LTE que iba a cubrir todo. No cubre todo. En el fondo del rajo no hay señal, y el rajo va bajando todos los años. Cualquier cosa que ustedes diseñen tiene que funcionar sin señal, porque va a haber sectores sin señal siempre. 

**Héctor Sanhueza Molina** · Superintendente de Planta Concentradora 

Con todo respeto por mis colegas de la mina: yo no confío en el tonelaje que me declaran. Y no es un problema de honestidad, es un problema de medición. Ellos me dicen que me mandaron un tonelaje. Mi balanza de alimentación me dice otro. La diferencia mensual anda entre tres y siete por ciento. Alguien está equivocado y hasta hoy nadie ha querido resolver cuál de las dos mediciones es la buena. 

Lo mismo con la ley. El plan dice que el polígono tenía cero coma cincuenta y ocho. Mi cabeza dice cero coma cincuenta y uno. ¿Se perdió cobre? ¿La estimación del bloque estaba mala? ¿Me mandaron material de otro lado? No lo sé, y ese no saber me cuesta plata todos los meses. 

Yo quiero muestreo obligatorio. En cada punto de transferencia, sin excepción y sin que nadie pueda saltárselo porque va apurado. Sé que eso incomoda a la mina. Me da igual: sin muestreo no hay conciliación y sin conciliación estamos administrando a ciegas. 

El balance metalúrgico lo hace mi metalurgista de turno en una planilla que armó él. El del mes lo hace metalurgia en otra planilla que tiene factores de ajuste que se fueron agregando desde 2013. Hay dos personas en esta compañía que saben explicar de dónde salen esos factores, y una se jubila en marzo. 

Última cosa. La red de control de la planta no se toca. Ustedes pueden leer del historiador todo lo que quieran, pero nadie escribe en el control de proceso. Si eso está en discusión, mejor lo aclaramos ahora. 

**Ignacio Bustos Carvajal** · Jefe de Mantenimiento 

Ya nos vendieron mantenimiento predictivo dos veces. La primera vez fue en 2018, ochocientos mil dólares, catorce meses de uso, hoy apagado. La segunda fue un piloto de un fabricante en 2022 con seis camiones, que terminó cuando terminó el piloto. Así que discúlpenme el escepticismo, pero me lo gané. 

¿Por qué fracasaron? Por lo mismo las dos veces. El sistema tiraba alertas. Muchas. La mayoría no significaba nada. Al mes y medio mis planificadores dejaron de mirarlas, y con toda razón: si de veinte alertas diecinueve son ruido, la vigésima también la vas a ignorar. 

Lo que sí me sirve, y esto se los digo en serio, es que los datos de los tres portales de fabricante lleguen a un solo lugar y se junten con las horas de operación y con las pautas de SAP. Eso solo ya me cambia el día. Hoy tengo un camión con una alarma en un portal, con doscientas horas para la pauta en SAP y con un tiempo de ciclo que se degradó en el despacho, y esas tres cosas nunca se encuentran. 

Hay un tema contractual que nadie ha querido enfrentar. Los datos de telemetría los genera mi equipo, pero viven en el portal del fabricante. Cuando pregunté si me los podía bajar automáticamente, me dijeron que había un servicio adicional. No sé si somos dueños de esos datos. Alguien debería averiguarlo antes de prometer una integración. 

Caso 01 · Minería · TFEP-01/2026 14 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

Y si me van a proponer predictivo, quiero saber tres cosas: con qué datos lo van a entrenar, cuántas alertas por semana espero recibir y qué pasa cuando la alerta se equivoca. Si no me responden eso, no lo compro. 

**Paula Guerrero Lizana** · Gerenta de Sustentabilidad y Asuntos Regulatorios 

Mi problema es que trabajo con datos que no controlo. El consumo de agua me lo manda operaciones por correo. La calidad del aire viene de un laboratorio externo en un informe en PDF. El monitoreo del depósito de relaves llega de una empresa geotécnica. El combustible me lo da abastecimiento desde SAP, en litros comprados, no en litros consumidos por área, que es lo que yo necesito. 

Con eso armo el reporte a la autoridad. A mano. El año pasado nos observaron por una inconsistencia entre dos reportes y la observación era correcta: los números no cuadraban porque los saqué de fuentes distintas en momentos distintos. 

Lo que viene es peor, y por eso estoy en esta conversación . Los compradores están pidiendo huella de carbono por tonelada de cobre fino, trimestral y verificada por un tercero. Yo la calculo una vez al año, con una consultora, y me demoro dos meses. Trimestral y auditable significa que el dato tiene que salir del sistema, no de mi planilla. 

Y necesito el consumo por área. Cuánta agua consume la planta, cuánta el campamento, cuánta la supresión de polvo en los caminos. Hoy tengo un solo medidor general y una regla de reparto que inventamos el 2019. 

También llevo el convenio con la comunidad: empleo local y compras locales. Eso lo reporto semestralmente y lo construyo pidiéndole planillas a recursos humanos y a abastecimiento. Si el sistema pudiera darme ese dato solo, me devolverían dos semanas de trabajo al año. 

**Marcelo Tapia Ríos** · Jefe de Seguridad y Salud Ocupacional 

Nueve días para acreditar a un trabajador nuevo. Nueve. Y el catorce por ciento de los rechazos en portería es porque a alguien se le venció un examen o un curso y nadie se dio cuenta. Ese trabajador viajó seiscientos kilómetros para que le digamos que no puede entrar. 

Lo que necesito es que el sistema sepa, antes que yo, que a fulano se le vence el examen en veinte días, y que le avise a él, a su empleador y a mí. No es complicado de imaginar. Lo complicado es que hoy esa información está en una planilla que mantiene una persona. 

El registro de incidentes es todo en papel. El supervisor llena un formulario, lo entrega, alguien lo digita tres días después. Cuando viene la autoridad y me pide los registros de las inspecciones del último trimestre, yo tengo que ir a buscar carpetas. En la última auditoría nos hicieron once observaciones y seis eran por eso. 

Del control de fatiga: las cámaras funcionan, las alertas llegan, pero llegan a un correo y a un teléfono de turno. Lo que se hizo con cada alerta no queda en ninguna parte. Si mañana tengo un accidente por somnolencia y me preguntan qué hice con las alertas previas, no tengo cómo responder. 

Un tema delicado. Yo quiero biometría en portería, porque hoy las credenciales se prestan y todos lo sabemos. El sindicato objetó formalmente esa idea el año pasado. No sé cómo se resuelve eso, pero ustedes tienen que saber que existe. 

**Sebastián Ortúzar Larraín** · Gerente de Finanzas 

Yo quiero el costo por tonelada movida y el costo por libra de cobre fino, todos los días, no dieciocho días después del cierre. Con eso puedo tomar decisiones. Sin eso administro mirando por el espejo retrovisor. 

Caso 01 · Minería · TFEP-01/2026 15 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

Me dicen que ese número no existe con esa granularidad. Puede ser. Pero si no existe, quiero saber exactamente qué falta para que exista, cuánto cuesta construirlo y en cuánto tiempo. 

La conciliación metalúrgica es mi mayor dolor de cabeza. Tres a siete por ciento de diferencia en una operación de cien mil toneladas de cobre fino son entre diez y treinta millones de dólares al año de incertidumbre. No estoy diciendo que se pierdan: estoy diciendo que no sé si se pierden. 

Y una advertencia sobre el presupuesto. El directorio aprobó un marco de inversión, pero yo voy a mirar con lupa la operación, no la implementación. Un proyecto que me cuesta poco construir y mucho operar durante tres años es peor negocio que uno que cuesta más al principio. Quiero ver el costo total, mes a mes, hasta el final del contrato. 

Ah, y todo lo que sea contable sale de SAP. El sistema nuevo le entrega datos a SAP, no al revés, y SAP emite. No quiero dos verdades. 

**Verónica Alcaíno Prat** · Jefa de Tecnologías de Información Corporativa 

Desde mi vereda esto es simple: nube. El estándar corporativo del grupo es nube pública, y llevamos tres años migrando todo lo que se puede migrar. No quiero más servidores en faena. La sala que tenemos en Aranda es de 2014, la climatización es simple, el respaldo eléctrico da quince minutos y la puerta se abre con llave. Es un riesgo, no un activo. 

Sé que operaciones va a decir que necesita algo en terreno. Lo entiendo, pero cada fierro que ponemos en faena es un fierro que alguien tiene que mantener a tres mil ciento ochenta metros de altura, y no tengo a esa persona. 

Mi equipo son once personas para toda la compañía. Cuatro en faena, siete en Santiago. Si el sistema que ustedes propongan requiere un especialista dedicado que yo no tengo, díganlo ahora y coticen el servicio, porque no voy a poder operarlo. 

Lo otro que me importa es la seguridad. Somos parte de un grupo internacional y me auditan todos los años. Necesito identidad federada con el directorio corporativo, doble factor, cero credenciales compartidas y registro de todo. Y necesito que la red de control de la planta quede aislada, porque si alguien entra por ahí, esto se convierte en un problema muy distinto. 

Sobre el enlace: el corte de fibra más largo del año pasado fue de veinte horas. Tenemos respaldo satelital, pero es para correo y teléfono, no para sostener sistemas. Sé que esto contradice lo que dije de la nube. Ese es el problema que ustedes tienen que resolver, no yo. 

**Eleodoro Painemal Curinao** · Operador de pala, 22 años en faena 

A mí me han puesto pantallas antes. La del despacho la uso todos los días y esa está bien, es grande y se ve. Pero nos pusieron una vez un aparato para reportar y no lo usó nadie. 

Le explico por qué. Yo estoy con guantes, de estos gruesos, porque en invierno acá arriba hace frío de verdad. El aparato ese había que tocarlo con el dedo y con guante no funcionaba. Sacarse el guante a las seis de la mañana en julio, a menos seis grados, para tocar una pantalla, es no conocer el trabajo. 

Y la pantalla no se veía. Con el sol de acá, a mediodía, esa pantalla era un espejo. El que la diseñó nunca se subió a una pala. 

Si me preguntan qué necesito, le digo dos cosas. Uno, que sea rápido, que no me pare la máquina. Cuando la pala está cargando, la pala tiene que estar cargando. Dos, que sea poco. Si tengo que apretar un botón, 

Caso 01 · Minería · TFEP-01/2026 16 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

aprieto un botón. Si tengo que llenar cinco casilleros, no lo voy a llenar y le voy a decir por radio al despachador como siempre. 

Yo lo que sí sé es cuándo el material cambió. Lo veo, lo escucho en la pala, lo siento. Eso lo sé mejor que cualquier planilla. Si el sistema me deja avisar eso con un botón, se lo aviso todas las veces. Si me hace escribir, no. 

**Francisca Ledermann Ruiz-Tagle** · Superintendenta de Planificación Minera 

El plan lo hago en el software de planificación, dibujo los polígonos y lo exporto los domingos a una carpeta compartida. Operaciones lo carga en el despacho. Hasta ahí bien. 

El problema es lo que pasa después. El lunes se cae una rampa, el martes la tronadura desplazó el contacto, el miércoles la planta pide más mineral oxidado. El plan cambia tres o cuatro veces por semana y esos cambios se comunican por radio y por el grupo de mensajería del turno . 

Al final del mes, cuando calculo el cumplimiento del plan, estoy comparando el plan que exporté el domingo con lo que efectivamente se movió. Y el cumplimiento sale mal, no porque la operación lo haya hecho mal, sino porque el plan que estoy comparando ya no era el plan. Nadie registra la versión del plan que estaba vigente en cada momento. 

Si yo tuviera el cumplimiento real del turno anterior, cada mañana, podría replanificar. Hoy replanifico con información de hace dos semanas. 

Y una advertencia sobre los polígonos. Un polígono no es una unidad limpia. Un camión puede cargar material de dos polígonos si la pala está en el borde. Cuando eso pasa, hoy el sistema asigna todo al polígono donde está la pala. Es una simplificación y todos la sabemos, pero nadie ha decidido si está bien o si hay que camb iarla. 

###### Sobre las contradicciones. 

El PROPONENTE habrá advertido que estas entrevistas no son consistentes entre sí. La gerenta de operaciones mina quiere menos registros en terreno y el superintendente de planta quiere muestreo obligatorio sin excepciones. La jefa de tecnologías de información quiere todo en la nube y ella misma describe por qué la operación no puede depender de la nube. El jefe de mantenimiento rechaza el mantenimiento predictivo que el gerente general ya considera parte del proyecto. El jefe de seguridad quiere biometría y el sindicato la objetó. 

Estas tensiones son reales y no se resolverán antes de la adjudicación. Resolverlas -o, cuando no sea posible, proponer una arquitectura que permita convivir con ellas y dejar constancia de la decisión y de su costo- es parte de lo que se está licitando. 

Caso 01 · Minería · TFEP-01/2026 17 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

##### **TÍTULO IV** 

### **LO QUE EL MANDANTE ESPERA** 

##### **CAPÍTULO 9 · EXPECTATIVAS DE NEGOCIO** 

Las siguientes son las expectativas del CLIENTE expresadas como resultados de negocio. Deliberadamente no están escritas como requerimientos. Traducirlas en requerimientos funcionales y no funcionales, priorizarlos, asignarlos a una etapa y hacerlos verificables es trabajo del PROPONENTE. 

###### **9.1 Saber de dónde viene cada tonelada** 

El CLIENTE espera poder tomar cualquier lote embarcado y reconstruir, con evidencia y no con estimación, de qué sectores del rajo proviene el mineral que lo compone, en qué fechas se extrajo, por qué stocks pasó, cuándo se procesó y qué análisis lo respaldan. Y espera poder recorrer esa cadena también en sentido inverso: desde un polígono extraído hace ocho meses, saber en qué embarques terminó. 

Esta expectativa tiene tres destinatarios distintos y conviene no confundirlos: el comprador, que exige cadena de custodia verificable; la operación, que necesita saber qué mezcla produjo qué resultado; y la autoridad, que fiscaliza el cumplimiento de compromisos ambientales y de seguridad. 

###### **9.2 Cerrar el mes en días, no en semanas** 

El CLIENTE espera que la conciliación metalúrgica del mes se cierre en pocos días hábiles, que la diferencia converja hacia los estándares de la industria y, sobre todo, que cuando exista una diferencia se pueda explicar dónde se produjo en lugar de aceptarla como un misterio recurrente. 

Esto supone resolver, antes que nada, una pregunta que la compañía ha evitado durante años: cuál es la fuente de verdad del tonelaje cuando el pesaje de a bordo, la báscula de control y la balanza de alimentación de la planta entregan cifras distintas. 

###### **9.3 Convertir el dato disperso en una sola vista de la operación** 

El CLIENTE espera que un supervisor, ante un equipo detenido, tenga en una sola pantalla el estado del equipo, su historial reciente, sus alarmas de telemetría, sus pautas de mantenimiento pendientes y su desempeño comparado. No espera adivinar el futuro: espera dejar de perder veinte minutos reuniendo información que ya existe. 

La compañía es escéptica respecto del mantenimiento predictivo, y con razones. Espera que quien lo proponga se haga cargo explícitamente de por qué esta vez sería distinto, con qué datos, con qué tasa de falsos positivos esperada y con qué mecanismo de mejora del modelo. 

###### **9.4 Que el registro nazca donde ocurre el hecho** 

El CLIENTE espera terminar con la digitación diferida. Que el incidente se registre en el lugar del incidente, que la inspección quede firmada en terreno, que el cambio de destino de un camión quede con su razón asociada y que el resultado del laboratorio fluya sin transcripción. 

Y espera que ese registro le cueste al operador el menor esfuerzo posible. La compañía ha sido explícita: un sistema que agregue pasos al ciclo productivo será rechazado por la operación aunque sea técnicamente impecable. 

Caso 01 · Minería · TFEP-01/2026 18 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

###### **9.5 Acreditar y controlar personas sin fricción** 

El CLIENTE espera que ninguna persona viaje a la faena para que se le niegue el ingreso por un documento vencido que el sistema podía haber advertido con semanas de anticipación, y que el estado de habilitación de cada persona en faena sea consultable y auditable en cualquier momento. 

###### **9.6 Reportar cumplimiento sin planillas** 

El CLIENTE espera que los reportes a la autoridad ambiental, los indicadores del convenio con la comunidad y la huella de carbono por tonelada de cobre fino se generen desde el sistema, con trazabilidad hasta la medición de origen, con la periodicidad que exijan la norma y los compradores, y en condiciones de ser auditados por un tercero. 

###### **9.7 Usar el Centro Integrado de Operaciones para lo que se construyó** 

El CLIENTE espera que las funciones que hoy no pudieron trasladarse a Antofagasta -porque dependían de información que sólo existe en la faena- puedan trasladarse. No es un requerimiento de software: es la consecuencia esperada de que la información deje de vivir en las cabezas y en las planillas. 

###### **9.8 Sostener la operación cuando se corta la fibra** 

El CLIENTE espera que un corte del enlace con Antofagasta, de la duración que se ha observado históricamente, no detenga la extracción, el transporte, el procesamiento ni el registro de lo que ocurre. Espera que la información se sincronice sola cuando el enlace vuelva y que nadie tenga que reconstruir a mano lo que pasó durante el corte. 

##### **CAPÍTULO 10 · RESTRICCIONES NO NEGOCIABLES** 

Las siguientes condiciones no están en discusión. Una propuesta que no las respete será evaluada como falta de comprensión del caso. 

||**Restricción**<br>-----------------------------------------|
|---|---|
|1<br>-<br>-|La mina y la planta no se detienen. La operación es continua, 24 horas al día, los 365 días del año. Las únicas<br>ventanas de intervención mayor son las dos detenciones programadas de planta, de seis días cada una, en<br>marzo y septiembre.<br>-<br>-|
|<br>2|<br>La operación no puede depender del enlace con Antofagasta. Todo lo que sostiene la extracción, el transporte,<br>el procesamiento y el registro en terreno debe seguir funcionando durante un corte de fibra prolongado.|
|3|La red de control de proceso de la planta es de sólo lectura. Se puede leer del historiador; no se escribe en el<br>control de proceso, ni se instalan componentes en esa red sin la segregación que la compañía apruebe.|
|4|SAP no se reemplaza ni se modifica. Es el sistema de registro contable y de gestión. La solución le entrega<br>datos; SAP emite. No habrá dos verdades contables.|
|5|El sistema de despacho de flota se mantiene. Contrato vigente hasta 2031. Se integra, no se sustituye.<br>-|
|6|El sistema de gestión de laboratorio se mantiene y debe integrarse en ambos sentidos.|
|7<br>-|El software de planificación minera se mantiene. La solución consume sus salidas.<br>-<br>-|
|8|No se agregan pasos al ciclo productivo. Todo registro adicional que se pida al operador de un equipo debe<br>justificarse en términos de segundos y demostrarse en la marcha blanca.|
|9|La identidad se federa con el directorio corporativo del grupo. Doble factor obligatorio, sin credenciales<br>compartidas y con registro completo de accesos.|



Caso 01 · Minería · TFEP-01/2026 19 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

###### **Restricción** 

- El equipo de tecnologías de información de la compañía son once personas. Toda función que requiera un 

- 10 especialista dedicado que la compañía no tiene debe ofrecerse como servicio y estar costeada. 

- El personal clave de operaciones -planta y mina- tiene disponibilidad limitada durante las detenciones 

- 11 programadas de marzo y septiembre. Las validaciones que los requieran deben planificarse fuera de esas ventanas. 

Toda intervención en faena está sujeta al Reglamento de Seguridad Minera y a los procedimientos internos de 12 la compañía. El personal del ADJUDICATARIO debe acreditarse como cualquier contratista, con los tiempos 1 que ello implica. 

###### **CAPÍTULO 11 EXCLUSIONES EXPLÍCITAS** 

Para evitar sorpresas, el CLIENTE declara expresamente qué NO está pidiendo: 

- No se pide reemplazar el ERP corporativo ni ninguno de sus módulos. 

- No se pide reemplazar el sistema de despacho de flota, el sistema de gestión de laboratorio ni el software de planificación minera. 

- No se pide intervenir el control de proceso de la planta ni modificar la lógica de control. 

- No se pide automatizar equipos mineros: la operación autónoma de camiones o de perforadoras no forma parte de este proyecto. 

- No se pide el diseño del plan minero ni la estimación de recursos y reservas. 

- No se pide la gestión de remuneraciones ni la administración de personal, que residen en el ERP. 

- No se pide la operación del terminal portuario, que administra un tercero, sin perjuicio de la integración necesaria con él. 

- No se pide construir la red de comunicaciones del rajo, aunque sí evaluar si la cobertura actual es suficiente para la solución propuesta y especificar qué faltaría. 

- El hardware de terreno -dispositivos, lectores, etiquetas, instrumentación adicional- lo adquiere el CLIENTE; el PROPONENTE debe especificar exactamente qué comprar, cuánto y con qué características, conforme al Capítulo 8 de las Bases Técnicas Transversales. 

Que algo esté excluido del alcance no significa que pueda ignorarse en el diseño. La solución debe convivir con todo lo excluido, y las dependencias que ello genera deben estar identificadas, documentadas y consideradas en el plan y en el riesgo. 

###### **CAPÍTULO 12 · MARCO NORMATIVO Y COMPROMISOS CON TERCEROS** 

El PROPONENTE deberá identificar, investigar y considerar en su propuesta el marco que aplica a esta industria. El CLIENTE entrega la orientación inicial; la profundización es parte del trabajo. 

|.. .||**Por qué importa aquí**|
|---|---|---|
|**Seguridad minera**|Reglamento de Seguridad Minera y la<br>fiscalización del organismo sectorial<br>competente.|Obligaciones de registro, de reporte de<br>incidentes y de acreditación de personas. Es la<br>fuente de seis de las once observaciones de la<br>última auditoría.|



Caso 01 · Minería · TFEP-01/2026 20 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

|**Ámbito**|**Referencia**|**Por qué importa aquí**|
|---|---|---|
|**Cierre de faenas**|Normativa de cierre de faenas mineras y<br>sus obligaciones de información periódica.|Exige información trazable sobre el avance de<br>la operación y sobre las obras comprometidas.|
|**Medio ambiente**|Resolución de Calificación Ambiental de la<br>faena y fiscalización de la autoridad<br>ambiental.|Fija compromisos de monitoreo y de reporte<br>con frecuencia, punto de medición y<br>destinatario definidos.|
|**Salud ocupacional**|Normativa de condiciones sanitarias y<br>ambientales básicas en los lugares de<br>trabajo y protocolos de vigilancia aplicables<br>a la altura geográfica y a la exposición a<br>sílice.|Determina exámenes, periodicidades y<br>registros asociados a la habilitación de las<br>personas.|
|**Datos personales**|Ley N° 21.719 sobre protección de datos<br>personales.|Datos de salud ocupacional, resultados de<br>control de fatiga y controles de alcohol y drogas<br>son categorías sensibles.|
|**Seguridad de redes**<br>**industriales**|IEC 62443 y las prácticas de segregación<br>entre tecnología de información y<br>tecnología de operación.|Condición para cualquier lectura desde la red<br>de control de proceso.|
|**Trazabilidad y cobre**<br>**responsable**|Esquemas de aseguramiento de cobre<br>producido responsablemente y exigencias<br>de cadena de custodia de los compradores.|Es el origen de esta licitación. El PROPONENTE<br>deberá investigar qué exigen concretamente<br>estos esquemas.|
|**Huella de carbono**|Protocolo de gases de efecto invernadero,<br>alcances 1, 2 y 3, y su verificación por<br>tercero.|El comprador exige cálculo trimestral audita ble<br>a partir de 2029.|
|**Comercialización de**<br>**concentrado s**|Prácticas contractuales de liquidación: ley<br>pagable, deducciones, cargos de<br>tratamiento y refinación, y penalidades por<br>elementos deletéreos.|Determina el valor económico de la trazabilidad<br>y de la mezcla. El PROPONENTE deberá<br>investigarlas.|
|**lnteroperabilidad**<br>**industria l**|OPC UA, ISA-95 y estándares de<br>intercambio de datos de equipos mineros.|Definen cómo integrarse con la planta y con los<br>equipos sin inventar protocolos propios.|



**Este listado es orientador, no exhaustivo. El PROPONENTE es responsable de identificar la normativa aplicable completa y de acreditar en su propuesta cómo la solución la satisface. Invocar una norma sin explicar qué control concreto la implementa se evaluará como no acreditada.** 

###### **CAPÍTULO 13 · HORIZONTE, PRIORIDADES Y ETAPAS** 

###### **13.1 Lo que el directorio quiere primero** 

El directorio expresó, sin transformarlo en instrucción técnica, un orden de urgencia: primero la trazabilidad del mineral y la conciliación, porque de ellas depende el contrato con los compradores a partir de 2029; luego el registro en terreno y la acreditación de personas, porque de ellas depende la exposición ante la autoridad; y por último la analítica avanzada de mantenimiento, que el directorio considera valiosa pero no urgente. 

Ese orden es una preferencia del mandante, no una definición de alcance. La distribución concreta entre la Etapa 1 y la Etapa 2 la propone el PROPON ENTE y debe justificarla en función de las dependencias técnicas, del 

Caso 01 · Minería · TFEP-01/2026 21 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

riesgo, de la capacidad de absorción del CLIENTE y del cronograma contractual obligatorio del Artículo 17° de las Bases Administrativas. 

Una propuesta que se limite a repetir el orden de preferencia del directorio sin analizarlo será evaluada como falta de criterio profesional. Si el PROPONENTE considera que hay una dependencia técnica que obliga a alterar ese orden, debe decirlo y fundamentarlo. El CLIENTE contrata ingeniería, no obediencia. 

###### **13.2 Hitos externos que condicionan el proyecto** 

|[**Fecha**|**Hito externo**|**Consecuencia**|
|---|---|---|
|**Marzo y septiembre**<br>**de cada año**|Detenciones programadas de planta, seis<br>días.|Únicas ventanas de intervención mayor.<br>También los períodos de menor disponibilidad<br>del personal clave de planta.|
|**Enero de 2029**|Entrada en vigor de las exigencias de<br>trazabilidad y huella de carbono del<br>principal comprador.|La capacidad de responder esas exigencias<br>debe estar en producción y con datos históricos<br>suficientes antes de esa fecha.|
|**Segundo semestre de**<br>**2029**|Auditoría de recertificación de los sistemas<br>de gestión de la compañía.|Los registros de seguridad y ambientales<br>deberían provenir del sistema para esa fecha.|
|**2030**|Evaluación de adquisición de una<br>operación en el extranjero.|No es seguro. Si ocurre, el CLIENTE espera<br>poder replicar la solución sin rehacerla.|
|**Permanente**|Avance del rajo.|Las zonas de sombra de la red inalámbrica<br>cambian con el avance. La solución no puede<br>suponer una cobertura fija.|



###### **13.3 Estrategia de puesta en producción esperada** 

El CLIENTE no impone una estrategia de implantación, pero sí declara las condiciones que cualquier estrategia debe respetar: 

- l. Nada entra en producción sin haber convivido con la forma actual de trabajar durante la marcha blanca correspondiente, con conciliación entre ambas y con la posibilidad de volver atrás. 

2. El paso a producción no puede coincidir con una detención programada de planta ni con el cierre contable del mes. 

3. El despliegue debe poder hacerse por área o por sitio, y no como un único evento que afecte simultáneamente a la mina, la planta, la portería y el puerto. 

4. Toda ola de despliegue debe contemplar acompañamiento en terreno, en turno de día y de noche, porque la faena opera de forma continua y la mitad de las personas trabaja de noche. 

- S. El régimen de turnos 7x7 implica que capacitar a la totalidad del personal de un área toma al menos dos ciclos completos. La planificación debe reflejarlo. 

6. La estabilización posterior a cada paso a producción debe tener dotación y duración declaradas, y ocurrir en faena, no de forma remota. 

El CLIENTE ha visto fracasar dos iniciativas tecnológicas por la misma causa: se implantaron correctamente y la gente dejó de usarlas. La estrategia de puesta en producción y de adopción pesa, en la evaluación de este caso, tanto como la arquitectura. 

Caso 01 · Minería · TFEP-01/2026 22 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

##### **TÍTULO V** 

#### **ANTECEDENTES PARA EL DIMENSIONAMIENTO** 

##### **CAPÍTULO 14 VOLUMETRÍA: LO QUE SE ENTREGA Y LO QUE SE DEBE ESTIMAR** 

El CLIENTE entrega los volúmenes que efectivamente conoce, porque son los que gobierna su operación. Los volúmenes propios del dimensionamiento de un sistema -concurrencia, transacciones por segundo, almacenamiento, integraciones- no los conoce, y no tiene por qué conocerlos: derivarlos es trabajo de ingeniería del PROPONENTE. 

**Las celdas marcadas como «a estimar» deben completarse en la propuesta con el valor estimado, el método de estimación y los supuestos empleados. Entregar la propuesta con esas celdas vacías, o con valores sin derivación, se evaluará como dimensionamiento no realizado.** 

**14.1 Volumetría operacional entregada por el CLIENTE** 

|||**Proyección a 3 años**|
|---|---|---|
|**Movimiento total mina**|82Mt/año|1<br>88Mt/año|
|**Mineral a planta**|21,5 Mt/año|22,4 Mt/año|
|**Viajes de camión de extracción**<br>-<br>-|:::342.000 al año<br>-<br>|:::367.000 al año<br>-<br>-<br>-|
|<br>**Ciclos de carguío de pala**|<br>:::1,37 millones al año|:::1,47 millones al año|
|**Pozos de perforación**<br>-<br>-|:::46.000 al año<br>-<br>|:::49.000 al año<br>-<br>-<br>-|
|<br>**Tronad u ras**|<br>:::340 al año|:::365 al año|
|**Polígonos de extracción activos simultáneamente**|12 a 18|hasta 22|
|**Muestras analizadas en laboratorio**|:::71.000 al año|:::78.000 al año|
|**Viajes de concentrado a puerto**|:::12.400 al año|:::13.000 al año|
|**Embarques**|31alaño|33alaño|
|**Órdenes de trabajo de mantenimiento**|:::34.000 al año|:::36.000 al año|
|**Equipos con telemetría de fabricante**|52|70|
|**Señales de proceso en el historiador de planta**<br>-|:::14.500 etiquetas<br>-<br>|:::16.000 etiquetas<br>--<br>-|
|**Instrumentos de monitoreo ambiental y geotécnico**|186|230|
|**Personas con acceso a faena en régimen**|4.180|4.400|
|**Personas con acceso en detención mayor de planta**|hasta 8.500|hasta 9.000|
|**Empresas contratistas activas**|:::90|:::100|
|**Ingresos y salidas de portería**|:::2.900 diarios|:::3.100 diarios|
|**Incidentes, cuasi accidentes y observaciones**<br>**registrados**<br>-|:::11.500 al año<br>-|:::12.000 al año<br>-|
|**Inspecciones planificadas de seguridad**|:::7.800 al año|:::8.200 al año|
|**Alertas de fatiga y somnolencia**|:::4.600 al año|:::5.000 al año|



Caso 01 · Minería · TFEP-01/2026 23 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

> 8 ~~~~~ 

**Proyección a 3 año ~·il::11:iifl:---sitiosacu~** 7 ~~1~~ 8 

###### **14.2 Volumetría de sistema que el proponente debe estimar** 

|**Dimensión**<br>-------------------------------||
|---|---|
|**Transacciones por segundo en régimen normal**<br>-|_A estimar y declarar como supuesto_<br>-|
|**Transacciones por segundo en peak**|_A estimar y declarar como supuesto_|
|**Momento del día y del mes en que se produce el peak**|_A estimar y declarar como supuesto_|
|**Personas usuarias registradas**|_A estimar y declarar como supuesto_|
|**Personas usuarias concurrentes en peak**|_A estimar y declarar como supuesto_|
|**Dispositivos de terreno en operación simultánea**|_A estimar y declarar como supuesto_|
|**Volumen anual de almacenamiento transaccional**|_A estimar y declarar como supuesto_|
|**Volumen anual de almacenamiento de telemetría y series de tiempo**|_A estimar y declarar como supuesto_|
|**Volumen anual de almacenamiento documental y multimedia**|_A estimar y declarar como supuesto_|
|**Volumen total de datos históricos a migrar**|_A estimar y declarar como supuesto_|
|**Número de integraciones y volumen de mensajes por integración**|_A estimar y declarar como supuesto_|
|**Ancho de banda requerido por sitio, en régimen y en peak**|_A estimar y declarar como supuesto_|
|**Volumen de datos generado en faena durante un corte de enlace de 20 horas**|_A estimar y declarar como supuesto_|
|**Tiempo de sincronización al restablecerse el enlace tras 20 horas**|_A estimar y declarar como supuesto_|
|**Contactos mensuales a la mesa de ayuda**|_A estimar y declarar como supuesto_|
|**Dotación de la mesa de ayuda y del centro de operaciones**|_A estimar y declarar como supuesto_|



La estimación de estas dimensiones no admite una única respuesta correcta. Lo que se evalúa es el método: de qué dato operacional se parte, qué supuesto se aplica, qué margen se considera y qué ocurre si el supuesto resulta equivocado. Dos propuestas con cifras distintas pueden estar ambas bien; una propuesta con cifras sin derivación está mal, aunque acierte. 

##### **CAPÍTULO 15 PARÁMETROS DEL CASO PARA LOS REQUISITOS «SEGÚN CASO»** 

Las Bases Técnicas Transversales marcan un conjunto de requisitos como «Según caso»: son obligatorios, pero su valor concreto lo fija cada industria. Los valores para el Caso 01 son los siguientes. Cuando este capítulo endurece un umbral del documento transversal, prevalece el más exigente. 

||**Materia**|**Valor para el Caso 01**<br>------------------------------|
|---|---|---|
|**RT-02.12**|Replicación a nuevas<br>unidades|Exigible. La compañía evalúa incorpora r una operación en el extranjero hacia<br>2030. La solución debe admitir su replicación por parametrización, con<br>catálogos, unidades organizacionales y reglas de negocio independientes.|
|**RT-03.10**|Operación desconectada<br>del componente on-<br>premise|Mínimo 48 horas continuas. El corte de fibra más prolongado regist rado fue de<br>20 horas; el CLIENTE exige más del doble de margen.|



Caso 01 · Minería · TFEP-01/2026 24 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

|**RT-03.13**|Sincronización tras la<br>re conexión|**Valor para el Caso 01**<br>La sincronización de 48 horas de operación desconectada debe completarse en<br>un plazo no superior a 4 horas, sin intervención manual y sin degradar la<br>operación en curso.|
|---|---|---|
|**RT-03.24**|Red inalámbrica de los<br>sitios operacionales|Exigible un estudio de cobertura del rajo actualizado, con identificación de las<br>zonas de sombra y proyección de su evolución con el avance del rajo a tres años.|
|**RT-05.10**|Retención de datos<br>históricos y de auditoría|Registros de seguridad y salud ocupacional: 10 años. Registros ambientales y de<br>monitoreo: 10 años. Registros de trazabilidad de mineral y de embarques: 10<br>años. Registros operacionales: 5 años. Registros tributarios: 7 años.|
|**RT-05.15**|Datos históricos a migrar|Producción y trazabilidad: 5 años. Mantenimiento: 3 años. Seguridad y salud<br>ocupacional: 10 años. Monitoreo ambiental: 10 años. Laboratorio: 5 años.|
|**RT-05.23**|Estándares sectoriales de<br>intercambio|OPC UA para la lectu ra del historiador de proceso. ISA-95 como modelo de<br>referencia de la integración entre operación y gestión. Estánda r abierto de<br>intercambio de datos de equipos mineros para la telemetría, cuando el<br>fabricante lo soporte. Protocolo de gases de efecto invernadero para la huella<br>de carbono.|
|**RT-05.29**|-<br>Latencia de la capa<br>analítica|-<br>-<br>Indicadores operacionales de turno: no superior a 15 minutos. Indicadores de<br>gestión y de cumplimiento: no superior a 4 horas. Conciliación metalúrgica:<br>cierre en no más de 3 días hábiles.|
|**RT-06.01**|Tipología del<br>emplazamiento on-<br>premise|Sala técnica principal en faena. La sala actual de 40 m<sup>2</sup>no cumple el Capítulo 6<br>del documento transversal y debe ser habilitada o reemplazada, con la obra civil<br>de cargo del CLIENTE y la especificación de cargo del PROPONENTE. Gabinetes<br>de borde en portería, planta, depósito de relaves y acopio de puerto.|
|**RT-09.02**|Concurrencia y volumen<br>de transacciones|El PROPONENTE lo deriva de la volumetría del numeral 14.1 y lo declara<br>conforme al numeral 14.2.|
|**RT-09.01**|Transacción operacional<br>crítica|El registro de un movimiento de material desde el equipo en terreno no debe<br>superar 2 segundos en el percentil 95, medido desde la acción de la persona<br>operadora hasta la confirmación en pantalla. El registro en báscula no debe<br>superar 3 segundos. La consulta de habilitación en portería no debe superar 1,5<br>segundos.|
|**RT-10.05**|Ventana operacional<br>protegida<br>1|Operación continua 24x7x365. Intervenciones mayores sólo en las detenciones<br>programadas de planta de marzo y septiembre. Intervenciones menores, previa<br>aprobación, en la ventana de baja actividad de 03:00 a 05:00. Prohibidas<br>durante el cierre contable del mes y durante las 48 horas previas a un<br>embarque.|
|**RT-11.10**|Cifrado a nivel de campo<br>-|Exigible para datos de salud ocupacional, exámenes preocupacionales,<br>resultados de control de fatiga y resultados de control de alcohol y drogas.|
|**RT-12.11**|Autenticación en el perfil<br>operacional|Operación con guantes de invierno, a la intemperie, con radiación solar directa y<br>temperaturas de hasta- 6º C. Dispositivos compartidos entre turnos. Personas<br>usuarias sin correo corporativo. La solución no puede exigir contraseña<br>alfanumérica escrita en terreno.|
|**RT-12.12**|Personas usuarias<br>externas|Empresas contratistas y sus trabajadores; el operador del terminal portuario; los<br>laboratorios externos; y los compradores, para la consulta de la trazabilidad de<br>sus lotes.|
|**RT-13.08**|Interfaces de terreno|Exigible operación con guantes, legibilidad bajo radiación solar directa,<br>funcionamiento entre- 6º C y 34 ºC, resistencia a polvo y a vibración, y operación<br>sin conexión.|
|**RT-15.02**|Certificaciones sectoriales<br>del adjudicatario|ISO 45001 e ISO 14001 vigentes. Conocimiento acreditado del Reglamento de<br>Seguridad Minera. Experiencia comprobable en faena minera en operación.|



Caso 01 · Minería · TFEP-01/2026 25 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

||**Materia**|**Valor para el Caso 01**|
|---|---|---|
|**RT-16.09**|Registro de consultas a<br>información sensible|Exigible para datos de salud ocupacional, control de fatiga y control de alcohol y<br>drogas, además del registro de modificaciones.|
|**RT-16.14**|Firma electrónica|Avanzada para los registros de seguridad exigidos por la autoridad, para las<br>actas de aceptación de embarque y para los informes de monitoreo ambiental<br>que se remitan a la autoridad.|
|**RT-16.21**|Canales de notificación|Correo electrónico, notificación en aplicación, mensajería instantánea para<br>contratistas, mensaje de texto para alertas críticas y alertas de seguridad, e<br>integración con el sistema de radio y megafonía de faena para las alertas de<br>evacuación.|
|**RT-16.30**|Portal público|No aplica portal abierto a la ciudadanía. Sí se exige un portal para empresas<br>contratistas y un portal de trazabilidad de lote para los compradores, ambos<br>autenticados.|
|**RT-17.01**|Aplicación móvil|Exigible, con operación desconectada, para el registro en terreno de la mina, las<br>inspecciones de seguridad, el registro de incidentes y el control de acceso.|
|**RT-17.06**|Periféricos a integrar|Lectores de código y de radiofrecuencia para identificación de camiones y de<br>personas, posicionamiento satelital de precisión, básculas de camiones, pesaje<br>de a bordo, cámaras de control de fatiga, torniquetes de portería, e<br>instrumentación geotécnica y ambiental.|
|**RT-21.06**|Horario del centro de<br>atención|24x7x365, con atención en español y con capacidad de respuesta presencial en<br>faena para los incidentes de severidad crítica.|
|**RT-21.16**|Traslado a sitios alejados|Exigible. Faena a 145 km de Antofagasta por Ruta 25 y camino privado, a 3.180<br>metros de altura. El personal que asista en faena debe estar acreditado y contar<br>con examen de altura geográfica vigente.|
|**RT-22.04**|Restricción de la<br>capacitación|Régimen de turnos 7x7 en faena. Capacitar a la totalidad del personal de un área<br>requiere al menos dos ciclos completos. La mitad del personal trabaja en turno<br>de noche y debe capacitarse en su turno.|



##### **CAPÍTULO 16 · LO QUE ESTE DOCUMENTO DELIBERADAMENTE NO RESUELVE** 

Las decisiones que siguen son necesarias para que la solución sea coherente. El CLIENTE no las ha tomado, y no las va a tomar por el PROPONENTE. Resolverlas, dejarlas escritas como supuesto y hacerse cargo de sus consecuencias en la arquitectura, en el alcance y en el costo forma parte del trabajo profesional que se licita. 

###### **16.1 Decisiones de diseño pendientes** 

||.<br>-|**Por qué importa**|
|---|---|---|
|1|Cuál es la unidad mínima de trazabilidad del<br>mineral: el polígono, el viaje de camión, el lote de<br>chancado, el turno o alguna otra.|Determina el volumen de datos, la complejidad del modelo, el<br>esfuerzo pedido al operador y la calidad de la respuesta que se<br>le podrá dar al comprador.|
|2|Cuál es la fuente de verdad del tonelaje ante la<br>discrepancia entre pesaje de a bordo, báscula de<br>control y balanza de alimentación de planta.|Sin esta definición la conciliación no converge. Es una decisión<br>de negocio que ninguna de las tres áreas involucradas ha<br>querido tomar.|
|3|Cómo se trata la mezcla en los stocks intermedios y<br>qué se asume sobre la ley del material retomado.|Es donde hoy se rompe la trazabilidad. Cualquier respuesta<br>implica un supuesto; el supuesto debe ser explícito y<br>verificable.|
|4|Cómo se identifica a la persona operadora cuando<br>el equipo se comparte entre turnos y la cabina no<br>se abandona en el relevo.|Sin esto no hay trazabilidad de quién registró qué, y los<br>registros de seguridad pierden valor probatorio.|



Caso 01 · Minería · TFEP-01/2026 26 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

||~~.~~<br>-|**Por qué importa**|
|---|---|---|
|5|Qué es exactamente una detención operacional,<br>cómo se clasifica y quién la clasifica.|El 23% del tiempo registrado hoy queda sin clasificar. Definir<br>la taxonomía y el responsable es condición para medir<br>productividad.|
|6|Qué ocurre con las muestras rechazadas o<br>invalidadas en el laboratorio y cómo afectan la<br>trazabilidad del lote.|Un lote sin análisis vá lido no puede embarcarse; la solución<br>debe saber qué hacer con él.|
|7|Qué ocurre con el concentrado devuelto o<br>rechazado por el comprador y cómo se reincorpora<br>a la cadena.|Es infrecuente pero ocurre, y hoy no existe procedimiento.|
|8|Cómo se autentica una persona contratista que no<br>tiene correo corporativo ni dispositivo propio.|Son 2.400 personas en régimen y hasta 8.500 en detención<br>mayor de planta.|
|9<br>-<br>-|Qué pasa con el registro cuando el equipo opera<br>en una zona de sombra prolongada y el operador<br>cambia de turno sin recuperar señal.<br>-|Determina el diseño del almacenamiento local, de la identidad<br>en modo desconectado y de la reconciliación.<br>-<br>-|
|10|Quién es dueño de los datos de telemetría que<br>generan los equipos de la compañía y bajo qué<br>condiciones contractuales pueden extraerse.|Condiciona por completo la factibilidad de la integración con<br>los tres portales de fabricante. Debe resolverse antes de<br>comprometer la.|
|11|Cómo se maneja el hecho de que un camión pueda<br>cargar material de dos polígonos cuando la pala<br>está en el borde.|Hoy se asigna todo al polígono de la pala. Es una simplificación<br>conocida que nadie ha decidido mantener o corregir.|
|12|Cómo se resuelve la tensión entre la exigencia de<br>muestreo obligatorio de la planta y la exigencia de<br>no agregar pasos al ciclo de la mina.|Son dos requerimientos legítimos y contradictorios. Alguien<br>tiene que proponer el equilibrio y justificarlo.|
|13<br>-|Cómo se aborda la objeción sindical a la biometría<br>en portería.<br>-~|Determina el mecanismo de control de acceso que puede<br>proponerse y su plan de gestión del cambio.<br>|
|14|<br>Con qué versión del plan minero se compara el<br>cumplimiento, dado que el plan cambia tres o<br>cuatro veces por semana.|<br>Sin versionado del plan, el indicador de cumplimiento seguirá<br>siendo inútil.|



Esta lista no es exhaustiva. Encontrar los demás vacíos es parte del ejercicio, y el PROPONENTE que identifique vacíos no listados aquí será evaluado favorablemente por ello. 

###### **16.2 Materias que el proponente deberá investigar** 

El CLIENTE no espera que el PROPONENTE conozca la industria minera de antemano. Sí espera que la estudie. Las siguientes materias son necesarias para formular una propuesta competente y no se explican en este documento: 

- Conciliación metalúrgica: qué es, cómo se calcula, qué factores de ajuste se emplean y qué rangos de diferencia se consideran aceptables en la industria. 

- Cadena de custodia del cobre y esquemas de aseguramiento de producción responsable: qué exigen concretamente y qué evidencia requieren. 

- Fórmulas de liquidación de concentrado: ley pagable, deducciones por humedad, cargos de tratamiento y refinación, y penalidades por elementos deletéreos como el arsénico. 

- Obligaciones de registro del Reglamento de Seguridad Minera y de la fiscalización sectorial. 

- Estructura y contenido de una Resolución de Calificación Ambiental y las obligaciones de reporte que genera. 

Caso 01 · Minería · TFEP-01/2026 27 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

- Cálculo de huella de carbono en operaciones mineras: alcances 1, 2 y 3, factores de emisión y requisitos de verificación por tercero. 

- Segregación entre tecnología de información y tecnología de operación conforme a IEC 62443, y qué significa en la práctica leer de un historiador de proceso. 

- Redes inalámbricas privadas en minería a rajo abierto: alcances, limitaciones, comportamiento en pendiente y efecto del avance del rajo. 

- Telemetría de equipos mineros: qué entregan los fabricantes, en qué formato, con qué latencia y bajo qué condiciones comerciales. 

- Gestión de fatiga y somnolencia en faenas mineras: tecnologías, protocolos de respuesta y consideraciones laborales. 

- Modelo de bloques, polígonos de extracción y secuenciamiento minero: lo suficiente para modelar correctamente la trazabilidad. 

- Condiciones de trabajo en altura geográfica y su efecto en la disponibilidad de personal y en la operación de equipamiento electrónico. 

La calidad de esta investigación se hará evidente en el Informe 1 y en la defensa técnica. Una propuesta que hable de «trazabilidad» sin usar el vocabulario de la industria, o que proponga integrar telemetría sin saber qué entregan realmente los fabricantes, quedará en evidencia frente a la Comisión de Expertos. 

Caso 01 · Minería · TFEP-01/2026 28 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

##### **TÍTULO VI** 

### **LO QUE DEBE PRODUCIR EL PROPONENTE** 

##### **CAPÍTULO 17 EL TRABAJO DE TRADUCCIÓN EXIGIDO** 

Este documento describe una operac1on y sus problemas. No contiene un catálogo de requerimientos. Construirlo es la primera tarea del PROPONENTE y la que condiciona todas las demás. 

###### **17.1 De la necesidad al requerimiento** 

El PROPONENTE deberá recorrer este documento y producir un catálogo de requerimientos trazable a su origen. Cada requerimiento debe indicar de qué párrafo, entrevista, indicador o restricción proviene, de modo que el CLIENTE pueda verificar que nada quedó fuera y que nada se inventó. 

|...|**Contenido esperado**|
|---|---|
|**Catálogo de requerimientos**<br>**funcionales**|Qué debe hacer la solución, expresado en términos verificables, con<br>identificador, descripción, actor, precondición, resultado esperado, prioridad y<br>origen en este documento.|
|**Catálogo de requerimientos no**<br>**funcionales**|Desempeño, disponibilidad, seguridad, usabilidad, operabilidad, mantenibilidad,<br>portabilidad y cumplimiento, con umbral numérico y método de verificación.<br>Deben incorporar los parámetros del Capítulo 15 y los requisitos del documento<br>transversal.|
|**Registro de supuestos**|Toda decisión que el PROPONENTE tomó por el CLIENTE, con su fundamento, su<br>impacto si resulta equivocada y la instancia en que se validará. Incluye<br>obligatoriamente las catorce decisiones del numeral 16.1.|
|**Registro de reglas de negocio**|Las reglas propias de la industria que la solución debe respetar y que este<br>documento no explicita: conciliación, liquidación, mezcla, clasificación de<br>detenciones, habilitación de personas, entre otras.|
|**Matriz de trazabilidad**|Correspondencia entre origen, requerimiento, componente de la arquitectura,<br>paquete de la EDT, prueba de verificación y criterio de aceptación.|
|**Registro de vacíos y consultas**|Aquello que el PROPONENTE no puede resolver por sí solo y que someterá al<br>CLIENTE durante el período de consultas.|



**Un requerimiento no es una frase copiada de este documento. «Debe haber trazabilidad» no es un requerimiento: es una necesidad. El requerimiento indica qué se registra, en qué momento, por quién, con qué dato, con qué tiempo de respuesta y cómo se verifica que se cumplió.** 

###### **17.2 Distinguir lo funcional de lo no funcional** 

Buena parte de lo que este documento describe puede leerse de las dos maneras, y la clasificación no es indiferente: determina quién lo verifica, cómo se prueba y en qué momento del proyecto se comprueba. Se ofrecen deliberadamente sin resolver algunos casos limítrofes: 

- «El registro no debe superar dos segundos»: ¿es un requerimiento no funcional de desempeño, o es funcional porque sin él el operador no lo usa y el proceso no ocurre? 

Caso 01 · Minería · TFEP-01/2026 29 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

- «Debe operar con guantes»: ¿es usabilidad, es una restricción de diseño de la interfaz, o es un requerimiento funcional del registro en terreno? 

- «Debe funcionar 48 horas sin enlace»: ¿es disponibilidad, es una decisión de arquitectura, o es un conjunto de requerimientos funcionales sobre qué se puede hacer y qué no en modo desconectado? 

- «El sistema debe avisar que a un trabajador se le vence un examen»: ¿es una funcionalidad de notificación o una regla de negocio de habilitación? 

- «La huella de carbono debe ser auditable»: ¿es trazabilidad, es cumplimiento normativo, o es un requerimiento funcional de cálculo y de conservación de evidencia? 

Se evaluará el criterio con que el PROPONENTE resuelve estos casos y la consistencia con que aplica su propio criterio a lo largo de la propuesta, no la coincidencia con una respuesta preestablecida. 

###### **17.3 Definir el alcance y su reparto entre etapas** 

A partir del catálogo, el PROPONENTE deberá delimitar el alcance de la Etapa 1 y de la Etapa 2, declarar las exclusiones y justificar el reparto en función de las dependencias técnicas, del riesgo, de los hitos externos del numeral 13.2 y de la capacidad de absorción del CLIENTE. 

La justificación debe hacerse cargo explícitamente de la preferencia del directorio expresada en el numeral 13.1, ya sea acogiéndola o apartándose de ella con fundamento técnico. 

###### **17.4 Diseñar la arquitectura** 

La arquitectura lógica y física debe ser propia de este caso y reconocible como tal. Debe hacerse cargo, como mínimo, de los siguientes asuntos, todos ellos derivados de lo descrito en este documento: 

- l. Qué se ejecuta en la faena y qué en la nube, y por qué, componente por componente, conforme al Capítulo 3 de las Bases Técnicas Transversales. 

2. Cómo se sostiene la operación durante 48 horas sin enlace y cómo se reconcilia después, incluyendo la identidad y la autorización en modo desconectado. 

3. Cómo se lee del historiador de proceso sin comprometer la segregación de la red de control. 

4. Cómo se captura el dato en el rajo, incluidas las zonas sin cobertura, y cómo se comporta el dispositivo cuando no hay señal durante un turno completo. 

- S. Cómo se integra el sistema de despacho de flota, el sistema de gestión de laboratorio, el ERP, el software de planificación y los tres portales de telemetría, con qué protocolo, en qué sentido y con qué frecuencia. 

6. Cómo se modela la trazabilidad del mineral y qué estructura de datos la sostiene desde el polígono hasta el lote embarcado. 

7. Cómo se separa el almacenamiento transaccional del analítico y cómo se sirven los indicadores de turno con la latencia comprometida. 

8. Cómo se protege la información sensible de salud ocupacional y de control de fatiga. 

9. Qué se hace con la sala de servidores actual, que no cumple el estándar exigido. 

10. Qué crecimiento admite el diseño y qué componente se satura primero. 

Caso 01 · Minería · TFEP-01/2026 30 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

###### **17.5 Planificar de forma realista** 

El plan de trabajo debe ser específico de esta faena. Un cronograma que podría servir para cualquier proyecto será evaluado como deficiente. En particular deberá reflejar: 

- El cronograma contractual obligatorio de 56 meses del Artículo 17° de las Bases Administrativas, sin proponer plazos alternativos. 

- Las dos detenciones programadas de planta al año como únicas ventanas de intervención mayor, y como períodos de baja disponibilidad del personal clave. 

- El régimen de turnos 7x7 y su efecto en la capacitación, en las validaciones y en el acompañamiento en terreno. 

- El tiempo de acreditación del propio personal del ADJUDICATARIO para ingresar a faena, y los exámenes de altura geográfica. 

- El tiempo real de las integraciones con terceros: la negociación técnica y comercial con los tres fabricantes de equipos no es una tarea de dos semanas. 

- La incertidumbre sobre el inventario técnico de los sistemas actuales, que el CLIENTE reconoce no tener documentado. 

- La solapa de los meses 13 a 15 y 19 a 20, con la dotación efectivamente necesaria para sostener dos frentes simultáneos. 

- El costo y la logística de mantener personal en faena a 3.180 metros, con turnos, traslados y alojamiento. 

###### **17.6 Proponer una estrategia de puesta en producción y de operación** 

El CLIENTE ha declarado que este es el punto donde ha fracasado antes. La propuesta deberá contener una estrategia explícita y no una declaración de intenciones: 

- l. Qué entra en producción primero, en qué sitio, con qué población de personas usuarias y con qué criterio de avance a la ola siguiente. 

2. Cómo conviven la solución y la forma actual de trabajar durante cada marcha blanca, cómo se concilian ambas y en qué momento se apaga la anterior. 

3. Qué indicadores se medirán diariamente durante la marcha blanca y con qué umbral se declara cerrada, conforme al Artículo 17.3 de las Bases Administrativas. 

4. Cómo se revierte un paso a producción fallido, en cuánto tiempo y qué se pierde al hacerlo. 

5. Qué dotación de acompañamiento habrá en faena, en qué turnos y por cuánto tiempo. 

6. Cómo se mide la adopción, con qué meta, y qué se hace si la adopción no alcanza la meta. 

7. Cómo se transfiere la operación al equipo del CLIENTE, que son once personas, y qué queda como servicio permanente del ADJUDICATARIO. 

8. Cómo se opera durante los 36 meses siguientes: dotación, ubicación, turnos, escalamiento y presencia en faena. 

Caso 01 · Minería · TFEP-01/2026 31 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

##### **CAPÍTULO 18 CRITERIOS DE ACEPTACIÓN DEL CASO** 

Los siguientes resultados de negocio son los que el CLIENTE utilizará para juzgar si el PROYECTO fue exitoso. El PROPONENTE deberá comprometerse con ellos, proponer la meta cuando este documento no la fije, indicar en qué momento del cronograma se alcanzará cada uno y cómo se medirá. 

|1|**Resultado esperado**<br>El origen del mineral de cualquier lote embarcado se reconstruye con<br>evidencia, en menos de dos horas, indicando polígonos, fechas de<br>extracción, stocks intermedios, fecha de procesamiento y análisis<br>asociados.|4 a 6 semanas, con resultado estimado.|
|---|---|---|
|2|La conciliación metalúrgica del mes cierra en no más de tres días<br>hábiles.|18 días hábiles.|
|3|La diferencia de conciliación converge y se sostiene bajo el umbral que<br>el PROPONENTE comprometa, y toda diferencia que persista queda<br>explicada por punto de la cadena.|Entre 3,1% y 6,8%, sin explicación.|
|4|El cumplimiento del plan minero se conoce al inicio del turno siguiente,<br>comparado contra la versión del plan efectivamente vigente.|10 a 15 días de desfase, contra un plan<br>desactualizado.|
|5<br>-|La totalidad de las detenciones de equipo y de planta queda clasificada<br>con causa dentro del turno siguiente.|23% del tiempo sin clasificar; 61% de las<br>detenciones sin causa raíz.|
|6|El supervisor dispone del estado, el historial, las alarmas de telemetría y<br>las pautas pendientes de un equipo en una sola vista.|Cuatro sistemas y una radio.|
|7|Ninguna persona es rechazada en portería por documentación vencida<br>que el sistema pudo advertir con anticipación.|14% de los rechazos.|
|8|Una persona contratista nueva se acredita en menos de 48 horas.|9 días.|
|9|Los registros de seguridad, las inspecciones y los incidentes nacen<br>digitales en el lugar del hecho y están disponibles para fiscalización sin<br>buscar carpetas.|Papel digitado con posterioridad.|
|10|Toda alerta de fatiga tiene acción documentada y trazable.|Sin registro consolidado.|
|11<br>-|Los reportes a la autoridad ambiental se generan desde el sistema, con<br>trazabilidad hasta la medición de origen.|Planillas construidas a mano.<br>-|
|12|La huella de carbono por tonelada de cobre fino se calcula<br>mensualmente y es auditable por un tercero.|Anual, con consultora externa.|
|13|La operación continúa y registra durante 48 horas sin enlace, y<br>sincroniza sin intervención manual al restablecerse.|El corte detiene el registro sistémico.|
|14|El operador de pala usa la solución en su turno, con guantes, y la usa<br>por decisión propia.|Dos iniciativas previas abandonadas.|



El criterio número 14 no es una nota de color. El CLIENTE ha visto fracasar dos proyectos correctamente implantados por falta de adopción. La propuesta deberá explicar cómo evitará el t ercero. 

Caso 01 · Minería · TFEP-01/2026 32 / 38 

Bases Técnicas del Caso 01 - Minería 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática 

##### **CAPÍTULO 19 CÓMO SE EVALUARÁ ESTE CASO** 

La evaluación se rige por el Título V de las Bases Administrativas y por la ponderación del Formulario T-21. Este capítulo precisa qué se buscará específicamente en el Caso 01 al aplicar esos criterios. 

||**Qué se buscará en este caso**|
|---|---|
|**Comprensión del problema**|Que el PROPONENTE distinga los tres problemas que están entrelazados -<br>trazabilidad comercial, productividad operacional y cumplimiento regulatorio- y no<br>los trate como uno solo. Que use el vocabulario de la industria con propiedad. Que<br>dimensione el problema con los datos entregados y con los que haya investigado.|
|**Esquema de solución y **<br>**alcance**|Que el alcance sea consecuencia del catálogo de requerimientos y no un listado de<br>módulos. Que las exclusiones sean explícitas. Que el reparto entre etapas esté<br>fundado en dependencias y no en preferencias.|
|**Arquitectura lógica y física**<br>-<br>-|Que resuelva de forma verificable la operación desconectada, la lectura del<br>historiador con segregación, la captura en zonas sin cobertura y la integración con los<br>cinco sistemas que se mantienen. Que sea propia de Aranda y no un diagrama de<br>referencia con el nombre cambiado.<br>-<br>-|
|<br>**Modelo y gestión de datos**|<br>Que el modelo de trazabilidad soporte la pregunta del comprador y la del regulador.<br>Que las catorce decisiones pendientes del numeral 16.1 estén resueltas y declaradas.|
|**Plan de trabajo, EDT y **<br>**cronograma**|Que refleje las detenciones de planta, los turnos 7x7, la acreditación del propio<br>personal, la negociación con fabricantes y el solapamiento de etapas. Que la ruta<br>crítica sea creíble.|
|**Plan de riesgos**|Que los riesgos sean de este proyecto: propiedad de los datos de telemetría,<br>cobertura de red que se degrada con el avance del rajo, objeción sindical a la<br>biometría, escepticismo del área de mantenimiento, indisponibilidad del personal<br>clave, ausencia de inventario técnico de los sistemas actuales.|
|**Servicios de operación y **<br>**niveles de servicio**|Que el modelo de soporte contemple presencia en faena, altura geográfica, turnos<br>continuos y traslado de 145 km. Que la dotación esté dimensionada con método.|
|**Innovaciones**|Que las cinco innovaciones sean pertinentes a la minería del cobre a rajo abierto y a<br>los problemas de Aranda, y no un catálogo de tecnologías de moda. Que la de<br>arquitectura cite fuentes.|
|**Consolidación**|Que la propuesta sea internamente coherente: que la arquitectura sostenga el<br>alcance, que la EDT contenga la arquitectura, que el cronograma refleje la EDT y que<br>el costo derive de todo lo anterior.|



Una advertencia final del mandante. 

En el acta del directorio del 14 de abril quedó consignado que el proyecto se adjudicará a quien demuestre que entendió la operación de Aranda, no a quien ofrezca la tecnología más avanzada. La Comisión Evaluadora aplicará ese criterio. 

Una propuesta técnicamente sofisticada que no resuelva las 48 horas sin enlace, que no diga qué hace con los stocks intermedios o que le pida cinco campos al operador de pala será superada por una propuesta más sobria que sí lo resuelva. 

Caso 01 · Minería · TFEP-01/2026 33 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

#### **TÍTULO VII** 

### **ANEXOS DEL CASO** 

##### **CAPÍTULO A MAPA DE SISTEMAS Y FLUJOS DE INFORMACIÓN ACTUALES** 

Descripción de los flujos de información tal como ocurren hoy. La columna «cómo viaja» es la que explica buena parte de los problemas descritos en el Capítulo 7. 

|planificación minera|**Destino**<br>Sistema de<br>despacho de flota|**Qué información**<br>-------------<br>Polígonos, leyes estimadas,<br>destinos y tonelajes planificados|Archivo exportado los domingos a carpeta<br>compartida y cargado a mano|
|---|---|---|---|
|Sistema de<br>despacho|Planillas de<br>operación|Tiempos de ciclo, tonelaje de a<br>bordo, posición de equipos|Informes exportados a mano|
|Operador de pala|Despachador|Cambio de material respecto de<br>lo planificado|Radio. La razón del cambio no queda<br>registrada|
|Báscula de<br>camiones|Nadie de forma<br>sistemática|Peso de control de una muestra<br>de viajes|Software local del fabricante, sin<br>integración|
|Balanza de<br>alimentación de<br>planta|Metalurgia|Tonelaje procesado|Historiador de proceso, consultado a<br>mano|
|Laboratorio|Metalurgia y<br>planificación|Leyes de alimentación,<br>concentrado y relave|Sistema de gestión de laboratorio;<br>transcripción manual a planillas|
|Metalurgista de<br>turno|Superintendencia<br>de planta|Balance metalúrgico del turno|Planilla de cálculo propia del metalurgista|
|Metalurgia|Finanzas|Balance metalúrgico del mes con<br>factores de ajuste|Planilla consolidada, 18 días hábiles<br>después del cierre|
|Portales de<br>fabricantes (tres)|Mantenimiento|Alarmas, horas, consumos,<br>códigos de falla|Consulta manual en tres portales web<br>separados|
|Operador de equipo|Planificación de<br>mantenimiento|Aviso de falla|Radio, transcrito después al ERP|
|ERP|Mantenimiento|Pautas preventivas y órdenes de<br>trabajo|Sistema, sin cruce con telemetría ni con<br>despacho|
|Supervisor de<br>terreno|Seguridad y salud<br>ocupacional|Incidentes, cuasi accidentes,<br>inspecciones|Formulario de papel, digitado días<br>después|
|Empresas<br>contratistas|Seguridad y salud<br>ocupacional|Contratos, exámenes, cursos,<br>documentación de habilitación|Correo electrónico y planil la mantenida a<br>mano|
|Plataforma de fatiga<br>de tercero|Turno|Alertas de somnolencia|Correo y teléfono de turno; la acción no<br>se registra|
|Instrumentación<br>ambiental y<br>geotécnica|Sustentabilidad|Consumo de agua, calidad de<br>aire, ruido, monitoreo de relaves|Instrumentos propios, informes de<br>laboratorios externos y correos|
|Abastecimiento y<br>recursos humanos|Sustentabilidad|Compras locales y empleo local|Planillas solicitadas semestralmente|



Caso 01 · Minería · TFEP-01/2026 34 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

|~~.~~<br>.-|~~.~~<br>-|~~.~~<br>-|**Cómo viaja hoy**|
|---|---|---|---|
|Sustenta bilidad|Autoridad<br>ambiental|Reportes de cumplimiento de la<br>Resolución de Calificación<br>Ambiental|Planilla consolidada a mano y correo|
|Faena|Terminal portuario|Guías de despacho y planillas de<br>pesaje del concentrado|Documento en papel que acompaña al<br>camión|
|Terminal portuario|Comercial|Conformación de lote, muestreo,<br>humedad y ley|Informes en documento; sin trazabilidad<br>al origen del mineral|
|Comercial|Comprador|Documentos de embarque y<br>certificados de análisis|Correo electrónico|



##### **CAPÍTULO B · CALENDARIO OPERACIONAL DE REFERENCIA** 

Elementos del calendario de la faena que condicionan la planificación del PROYECTO. Los meses se expresan en relación con el mes 1 del cronograma contractual del Artículo 17° de las Bases Administrativas. 

|||.-.|**Efecto sobre el proyecto**|
|---|---|---|---|
|**Detención programada**<br>**de planta**|Dos veces al año, en<br>marzo y septiembre|6 días|Única ventana de intervención mayor. Hasta 8.500<br>personas en faena. Personal clave de planta no<br>disponible para validaciones.|
|**Cierre contable del mes**|Mensual|Primeros 5 días<br>hábiles|Prohibido pasar a producción o intervenir<br>sistemas con impacto contable.|
|**Ventana de baja**<br>**actividad**|Diaria|03:00 a 05:00|Intervenciones menores, previa aprobación del<br>Comité de Operación.|
|**Embarque de**<br>**concentrado**|::::31alaño|36 a 48 horas|Prohibidas las intervenciones en las 48 horas<br>previas y durante el embarque.|
|**Cambio de turno**|Dos veces al día, 08:00<br>y 20:00|45 a 60 minutos|Peak de carga en registro, acceso y<br>comunicaciones. Es el momento crítico para la<br>solución.|
|**Tronadura**|Casi diaria|Ventana de 30 a<br>45 minutos|Evacuación del sector, pérdida transitoria de<br>cobertura y detención de equipos en el área.|
|**Ciclo de turno 7x7**|Permanente|14 días|Capacitar a la totalidad de un área requiere al<br>menos dos ciclos completos.|
|**Auditoría de la**<br>**autoridad minera**|Al menos anual|3 a 5 días|Los registros de seguridad deben estar disponibles<br>y trazables.|
|**Reporte a la autoridad**<br>**ambiental**|Según Resolución de<br>Calificación Ambiental<br>-|Variable|Frecuencias mensuales, trimestrales y anuales<br>según el compromiso.<br>~|
|**Invierno altiplánico**|Enero y febrero|Episodios de 1 a 3<br>días|<br>Lluvia y tormenta eléctrica. Riesgo de corte de<br>energía y de suspensión de faena.|



Caso 01 · Minería · TFEP-01/2026 35 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

##### **CAPÍTULO C · GLOSARIO DE LA INDUSTRIA** 

Vocabulario mínimo para leer este documento. No sustituye la investigación exigida en el numeral 16.2. 

|**Banco**|**Significado**<br>Nivel horizontal en que se divide un rajo para su explotación. Se extrae banco por banco,<br>de arriba hacia abajo.|
|---|---|
|**Botadero**|Depósito donde se acumula el material estéril extraído del rajo.|
|**CAEX**|Camión de extracción. Camión minero de gran tonelaje que transporta mineral y estéril<br>dentro de la faena.|
|**Cabeza**|Mineral que ingresa al proceso de concentración. La« ley de cabeza» es su contenido de<br>cobre.|
|**Chancado**<br>~<br>-|ducción de tamaño del mineral por fragmentación mecánica, previa a la molienda.|
|**Concentrado**|Producto de la concentración: polvo húmedo con alto contenido de cobre, en el orden del<br>25% al 30%, que se comercializa y se embarca.|
|**Conciliación**<br>**metalúrgica**<br>-<br>-|Ejercicio de cuadrar el cobre estimado en el modelo de bloques, el extraído de la mina, el<br>alimentado a la planta, el recuperado y el embarcado. Su diferencia mide la calidad del<br>control de la operación.<br>~<br>-|
|<br>**Detención operacional**|<br>Tiempo en que un equipo disponible no produce por causas de la operación: espera de<br>carguío, cambio de turno, tronadura, colación, congestión.|
|**Disponibilidad física**|Proporción del tiempo en que un equipo está en condiciones de operar, es decir, no está<br>en mantenimiento.|
|**Elemento deletéreo**|Impureza del concentrado que perjudica su procesamiento posterior y genera penalidades<br>comerciales. En Aranda el crítico es el arsénico.|
|**Estéril**<br>-<br>|Material sin valor económico que debe extraerse para acceder al mineral.<br>--<br>-|
|**Flotación**|Proceso fisicoquímico que separa las partículas de mineral de cobre del resto de la roca<br>molida.|
|**Historiador de proceso**|Sistema que registra en el tiempo las señales del control de proceso de la planta.|
|**Ley**|Contenido de un metal en el material, expresado como porcentaje o como gramos por<br>tonelada.|
|**Ley pagable**<br>-|Porción del contenido metálico del concentrado que el comprador efectivamente paga,<br>tras aplicar las deducciones del contrato.<br>~<br>-|
|**LOM**|<br>Life of Mine. Vida útil remanente del plan minero.|
|**Macizo rocoso**|Conjunto de roca in situ con sus discontinuidades. Su dureza condiciona la perforación y la<br>molienda.|
|**Malla de perforación**|Patrón geométrico de los pozos que se perforan para una tronadura.|
|**Modelo de bloques**|Representación tridimensional del yacimiento dividido en bloques, cada uno con su ley<br>estimada y sus atributos geológicos.|
|**Molienda**|Reducción del mineral a tamaño de partícula fina, previa a la flotación.|
|**Polígono de extracción**|Sector acotado de un banco, definido en el plan, con ley estimada, tonelaje y destino<br>asignado.|
|**Rajo**|Excavación a cielo abierto desde la que se extrae el mineral.|



Caso 01 · Minería · TFEP-01/2026 36 / 38 

Pontificia Universidad Católica de Valparaíso · Escuela de Informática Bases Técnicas del Caso 01 - Minería 

||**Significado**<br>------------------------------------|
|---|---|
|**Razón estéril/ mineral**|Toneladas de estéril que deben moverse por cada tonelada de mineral. En Aranda es 2,8 a<br>l.|
|**RCA**|Resolución de Cal ificación Ambiental. Acto administrativo que aprueba un proyecto y fija<br>sus compromisos ambientales.|
|**Recuperación**<br>**metalúrgica**|Porcentaje del cobre contenido en el mineral que efectivamente se recupera en el<br>concentrado.|
|**Relave**|Residuo del proceso de concentración, compuesto por roca molida y agua, que se dispone<br>en un depósito diseñado para ello.|
|**Retoma**|Operación de cargar material previamente acopiado en un stock para enviarlo a proceso.|
|**Sistema de despacho**|Sistema que asigna camiones a palas y destinos, y que registra los tiempos de ciclo y el<br>tonelaje transportado.|
|**Stock**|Acopio de mineral que opera como pulmón entre la mina y la planta, o que almacena<br>material de baja ley para su procesamiento futuro.|
|**Tiempo de ciclo**|Tiempo total que toma un camión en cargar, transportar, descargar y regresar.|
|**Tronadura**|Fragmentación de la roca mediante explosivos, previa al carguío.|
|**Utilización efectiva**|Proporción del tiempo disponible en que el equipo efectivamente produce.|



Caso 01 · Minería · TFEP-01/2026 37 / 38 

