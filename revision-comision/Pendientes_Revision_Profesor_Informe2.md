# Pendientes · Primera Revisión del Informe 2 (profesor)

Sólo lo que falta corregir de la Primera Revisión del Informe 2 (`revisiones-profesor/G01 - OVERFORE - Primera Revisión Informe 2.pdf`), según el contraste del 03-11-2026 con `main` (`f778818`). La lista completa, con lo ya corregido, está en [Checklist_Revision_Profesor_Informe2.md](Checklist_Revision_Profesor_Informe2.md). Los folios entre paréntesis son los de la entrega que revisó el profesor (1 a 1571).

**Total: 90 observaciones; 39 cerradas en LC-02 y 51 abiertas** (algunas abiertas ya tienen avance anotado en cursiva). Las figuras están en [Figuras_Pendientes.md](Figuras_Pendientes.md).

- **[Decisión]**: cambia contenido técnico, cifras o compromisos; lo acuerda el equipo antes de editar (AGENTS.md).
- 🔎: confirmar en el PDF antes de corregir; la búsqueda automática no basta.
- Prioridad: **Crítico** (marcado así por el profesor o ligado al 9.1), **Alta** (pedido en «Qué se espera en la Propuesta Final»), **Media**, **Forma**.
- Al cerrar un punto, marcar `[x]` y registrar el cambio en `TAREAS.md`.

**Resumen por peso (T-21, propuesta final)** — conteo inicial, antes de LC-02; el estado actual está en las casillas.

| Subdoc | Peso final | Pendientes | Lo que más pesa |
|---|---|---|---|
| S7 Plan de trabajo | 12 % | 15 | EDT por entregables, Gantt con dependencias, ruta crítica real, reserva |
| S3 Esquema y alcance | 10 % | 6 | Registro de reglas de negocio, parciales del T-12, escalabilidad |
| S4.2 Arquitectura física | 10 % | 8 | Latencia y costo de Brazil South, LTE del rajo, figuras de nube |
| S8 Riesgos | 7 % | 11 | Sacar 11 riesgos internos, agregar externos, HH preventivas en T-14/T-15 |
| S13 Innovaciones | 8 % | 6 | Cuantificar la 3, valorizar la 1, defender la 3 ante el Art. 30 |
| S6 Metodologías | 6 % | 9 | Un solo registro de interesados, acreditación y traspaso a TI |
| S9 Calidad | 6 % | 11 | Modelo de madurez de pruebas, criterio 14, pruebas en detenciones |
| S4.1 Arquitectura lógica | 5 % | 6 | ADR de región y CIO, ADR fuera del formato Campo/Contenido |
| S5 Datos | 5 % | 5 | Frecuencia del histórico ambiental, SSO como imagen indexada |
| S2 Problema | 4 % | 5 | Investigación de dominio con contenido propio |
| General | 2 % | 4 | Dominio de correo y sitio, volumen, figuras bajo 9 pt |
| S1 Empresa | 1 % | 4 | Una sola cifra de dotación, ISO/IEC 42001 |

---

## General · Formalidad (2 %)

- [x] **Alta [Decisión]** Correo `overfore60@gmail.com` y sitio `lucasdzamora.github.io/FEP_Proyecto` (S1 Tabla 1.1; T-12 RT-23.01 a 23.04): usar un dominio de la empresa o quitar el sitio. → _Hecho (DEC-019): correo con dominio propio y sin sitio personal en el S1._
- [ ] **Alta** 8 figuras bajo 9 pt: 7.3 (5,5), 4.23 (5,8), 7.4 (6,7), 6.7 (7,7), 1.1, 6.9 y 9.3 (8,7), 4.36 (8,9). Medir con `python herramientas/medir_figuras.py`.
- [ ] **Media [Decisión]** Volumen: pasar listados del cuerpo a anexos o formularios (el profesor contó 1.035 páginas sólo en los ítems del Informe 1; el S4 no cumple la proporción cuerpo/detalle).
- [ ] **Alta** Lectura de cierre humana completa de todos los archivos, registrada con nombre y fecha.

## S1 · Presentación de la empresa (1 %)

- [ ] **Alta [Decisión]** Una sola cifra de desarrolladores y técnicos de terreno: Figura 1.1 y 1.2 dicen 5 desarrolladores, el texto dice ocho (meses 3–11), el Anexo F llega a 10 técnicos (folios 7, 12, 13, 33). Debe coincidir con el T-15 (DEC-013 / R-05).
- [x] **Alta** Reescribir el párrafo de ISO/IEC 42001 en una sola idea: qué se certifica, cuándo y qué alcance tiene sobre la verificación facial (folio 11). → _Hecho._
- [x] **Alta** Analizar en 1.4 por qué proyectos de hasta USD 800.000 respaldan un contrato de la escala de Aranda (alcance, plazo, sitios, 24x7), no sólo por camiones y personas (folio 10). → _Hecho._
- [x] **Media** Anexo E: dice que la persona ejerce los dos roles «sólo desde la primera ola del paso de la Etapa 2 hasta el acta de H12», mientras la Tabla E.1 la pone como JP en M1–M21 y Gerente de Servicio en M21–M56 (folios 28–29). → _Hecho._

## S2 · Problema y necesidad (4 %)

- [x] **Alta** Desarrollar en 2.2 la investigación de dominio con contenido propio: cálculo de la conciliación metalúrgica y sus factores, IEC 62443 aplicada a la lectura del historiador (zonas y conductos), fórmula de liquidación con ley pagable, cargos y penalidad por arsénico. → _Hecho: nueva subsección «Conceptos de la industria que condicionan la solución»._
- [ ] **Alta** Llevar al cuerpo el análisis de las particularidades operacionales, regulatorias y estacionales; dejar en el Anexo C sólo el listado (hoy el 2.2 remite a C.3–C.9).
- [x] **Media** Tabla 2.5: la columna «Consultados al cliente» dice «SUP-30» en lugar de «1» (folio 75). → _Hecho._
- [ ] **Media** Figura 2.1 titulada «Faena (Antofagasta Norte)»; la faena está en Sierra Gorda (folio 50). Las Figuras 2.1–2.3 son renders sobre capturas satelitales que no aportan al problema. → _Leyenda corregida; reemplazar los renders es opcional._
- [x] **Forma** Citas de las Bases con un solo estilo y con entrada «CMAA» en la lista; distinguir las tres capturas de Google como «s. f.-a, -b, -c» (folios 50–52, 77). 🔎 → _Hecho para Google (s. f.-a, -b, -c); el estilo CMAA ya es uniforme._

## S3 · Esquema de solución y alcance (10 %)

- [ ] **Crítico [Decisión]** Restituir el registro de reglas de negocio de la industria (conciliación, liquidación, mezcla, clasificación de detenciones, habilitación), trazado a su origen, como exige el Cap. 17.1 del caso. Era OK en el Informe 1 y desapareció (regresión).
- [ ] **Alta [Decisión]** Cerrar o justificar los requisitos obligatorios del T-12 en «Cumple parcialmente» o «Por cumplir» (hoy 97 y 8 en el resumen), empezando por sala técnica, hardware y desempeño (por ejemplo, RT-06.27 y RF-TRZ-004).
- [x] **Alta** Agregar al 3.2 un análisis breve de escalabilidad y desempeño: qué se satura primero y con qué volumen, coherente con el S4 (Tabla 4.33). → _Hecho (3.2.4.3)._
- [ ] **Media** Declaración de IA: niveles de diagrama inconsistentes entre sección y subsecciones (3.3 «Ninguno», 3.3.1 a 3.3.6 «Alto»); el profesor también nota la herramienta sin versión.
- [ ] **Forma** La fuente de la Figura 3.13 queda en la página siguiente, separada de la figura. 🔎
- [ ] **Forma** La portada de los anexos del S3 pone bajo el representante el RUT de la empresa (folio 284). 🔎

## S4.1 · Arquitectura lógica (5 %)

- [ ] **Alta [Decisión]** Llevar a ADR la región de recuperación (Brazil South) y el descarte del CIO como sitio de recuperación.
- [ ] **Alta** Convertir los ADR del cuerpo en texto con una tabla de síntesis y dejar el registro completo en anexo (las Tablas ADR usan «Campo | Contenido», que la Aclaración no acepta; son los 9 avisos de R-08).
- [x] **Media** Los ocho ADR citan como fuente «análisis de decisiones con múltiples criterios (PMI, 2017)»: el PMBOK no es fuente de un ADR. → _Hecho._
- [ ] **Media** Matriz RF → componente: la Tabla 4.17 da totales y ejemplos; el mapeo completo está sólo en el T-12 y el Anexo B.
- [ ] **Media** Figuras 4.6 a 4.9: un solo párrafo de tres líneas que repite la figura sin conclusiones; la frase «se desarrollan en el Subdocumento 5» se repite en párrafos seguidos.
- [x] **Forma** Verificar la fecha de fin de soporte de Angular 22 («Junio de 2028», Tabla de componentes) contra la política de 18 meses de Angular. → _Hecho: noviembre de 2027._

## S4.2 · Arquitectura física (10 %)

- [ ] **Alta [Decisión]** Cuantificar la latencia Chile Central → Brazil South y el costo de la región de recuperación frente al CIO, con fuente citada (hoy la comparación es cualitativa, folio 599). 🔎
- [ ] **Alta** Especificar qué faltaría en la LTE del rajo para las zonas de sombra según el estudio de cobertura (Cap. 11 del caso; T11-66).
- [ ] **Alta** Figuras 4.26 y 4.27 (nube) con zonas, SKU y subredes dibujadas, no sólo en el texto.
- [ ] **Alta** Figura 4.23 (vista general de la topología) bajo 9 pt (~5,8) y 4.36 (~8,9).
- [ ] **Media** Declarar contra qué requisito del Cap. 6 de las Transversales se dimensionan los 30 min de autonomía de las UPS de la sala técnica (los gabinetes tienen 60).
- [ ] **Media** T-11: numeración con huecos (faltaban T11-49, -52, -61, -62) y «67 ítems» con identificadores hasta T11-71. 🔎
- [x] **Forma** Referencias de la lista sin cita (ISO/IEC 27001, 27002, 27017, 27018; Microsoft s.f.-c y -k; Bases Transversales 2026c). 🔎 → _Verificado: ya no están en la lista._
- [ ] **Forma** Palabras cortadas por columnas angostas («Etap a» en la Tabla 4.22; «Herramient a» en la 4.33). 🔎

## S5 · Modelo y gestión de datos (5 %)

- [x] **Alta [Decisión]** Declarar y justificar la frecuencia del histórico de monitoreo ambiental que se migra: hoy «186 instrumentos × 365 × 10» (una lectura diaria) frente a 1.440 lecturas diarias del Anexo D del S4. → _Hecho (DEC-020)._
- [x] **Alta** Decir que los formularios de SSO se migran como imagen indexada (consulta por tipo, fecha, área, empresa y persona, no por contenido), no «completos». → _Hecho._
- [x] **Media** Digitalización: la figura la ubica desde el mes 9 y el texto en los meses 10 a 15 (folios 791–792). → _Verificado: la Figura 5.17 ya dice M10–M15._
- [x] **Media** Tabla 5.5: la celda de RTO del registro de terreno tiene nueve líneas de explicación; pasarla a texto. → _Hecho._
- [ ] **Forma** Páginas casi vacías antes de las figuras (folios 748, 755, 757, 759 de la entrega).

## S6 · Metodologías (6 %)

- [ ] **Alta [Decisión]** Un solo registro de interesados en S2, S3 y S6 (19 o 14) con su cálculo de canales (hoy S6 y T-9: 14 y 91 canales; S2 y S3: 19) — DEC-012 / R-04. → _Hecho en texto (DEC-018); faltan las Figuras 6.4 y 6.5._
- [x] **Alta** Declarar quién autoriza entre sesiones las intervenciones de la ventana de 03:00 a 05:00 (el Comité de Operación es mensual) y con qué registro. → _Hecho._
- [x] **Alta** Incorporar a la metodología la acreditación del personal de Overfore (tiempos, examen de altura; restricción 12 y RT-21.16) y el plan de traspaso al equipo de TI del cliente de once personas (restricción 10, Art. 77). → _Hecho._
- [ ] **Alta** Extender la estrategia de anillos a las 176 tabletas de camiones, supervisores, portería y SSO (hoy sólo botonera de palas) y darle paquete en el T-14 y tarea en la Gantt. → _Hecho en S6 y T-10; sin paquete propio en el T-14 (DEC-021)._
- [ ] **Alta** Llevar los sprints, demostraciones y liberaciones a la Gantt (ver S7).
- [ ] **Media** Explicar qué entra a pruebas en H4 (mes 10) y qué se termina en el mes 11.
- [ ] **Media** T-9 y T-10: agregar detalle operativo (matriz RACI, plantilla del informe mensual, registro de interesados) en lugar de repetir el S6.
- [ ] **Media** Figuras 6.7 (~7,7 pt) y 6.9 (~8,7 pt) bajo 9 pt.
- [ ] **Forma** El T-9 lista la referencia 2026c sin citarla. 🔎

## S7 · Plan de trabajo, EDT, cronograma (12 %)

- [x] **Crítico [Decisión]** Justificar el primer nivel de la EDT o reorganizarlo por entregables de la solución, sin partir un mismo producto en paquetes de Etapa 1 y Etapa 2 (1.2.2/1.2.5, 1.4.3/1.4.4, 1.5.3/1.5.6…). → _Hecho: se justifica en 7.1 (se mantiene por fases, ligado a los hitos del E-25)._
- [x] **Crítico [Decisión]** Sacar de los paquetes las actividades de esfuerzo continuo (por ejemplo, 1.4.1.4 «Coordinación técnica», 21 meses). → _Hecho como paquetes de nivel de esfuerzo, declarados en 7.1._
- [ ] **Crítico** Carta Gantt con dependencias entre paquetes (predecesoras y flechas) y tareas de duración acotada (sprints o liberaciones), de modo que la ruta crítica salga de la Gantt y no de la red aparte de 35 actividades (tarea F-03 en curso).
- [ ] **Crítico [Decisión]** Rehacer el CPM con duraciones estimadas (PERT para terceros); hoy las duraciones llenan las ventanas entre hitos y 28 de 35 actividades quedan sin holgura.
- [ ] **Crítico [Decisión]** Reserva de cronograma explícita antes de H7 y H12, vinculada a las reservas del Cap. 8.
- [ ] **Crítico** Mostrar en la Gantt sprints, revisiones, liberaciones y puertas de calidad del S6 y el S9.
- [ ] **Alta [Decisión]** Contrastar la estimación con una medida de tamaño (Puntos de Casos de Uso u otra) y no despejar el PERT de una cifra fijada (el 77,5 % de las HH no tiene PERT) — R-01.
- [x] **Alta** Cuadrar la rama 1.7: 3.000 HH en T-14/T-15 y 2.920 en el T-19. → _Hecho: 3.000 HH en T-14, T-15 y T-19._
- [ ] **Alta** Cuadrar la dotación de desarrolladores con el S1 (ver S1). → _Hecho en texto (DEC-017); faltan las Figuras 1.1 y 1.2._
- [ ] **Alta** Figuras 7.3 (ruta crítica, ~5,5 pt) y 7.4 (calendario, ~6,7 pt) en 9 pt.
- [x] **Media** Criterio contradictorio del 1.4.6.2: «Sin errores en la muestra… con tasa de error bajo 1,5 %». → _Hecho: se explica con la regla del tres._
- [x] **Media** Tabla 7.1: mostrar la regla de imputación (la marcha blanca de la Etapa 1 incluye 2.360 HH de los meses 16–17). → _Hecho._
- [ ] **Media [Decisión]** T-18: justificar o reforzar una sola persona por turno en las semanas 1 y 2 de la marcha blanca de la Etapa 1, cuando entra portería.
- [x] **Media** Discutir en el cuerpo la holgura cero y qué se hace si se atrasa la cadena del núcleo. → _Hecho (7.3.1)._
- [ ] **Forma** Índice del T-14 con todas las secciones; fuentes del T-15 con páginas relativas («p. 45») en lugar de folio. 🔎 → _Fuentes del T-15 sin páginas relativas; índice del T-14 por verificar._

## S8 · Plan de riesgos (7 %)

- [x] **Crítico [Decisión]** Retirar del registro los 11 riesgos internos del proveedor (R-01 a R-04, R-13 a R-15, R-18, R-19, R-23, R-24) y resolverlos en la propuesta; reformular obsolescencia, bloqueo por proveedor, escalabilidad y ciberseguridad como exposición del cliente. → _Hecho en LC-03 (DEC-023): R-01 a R-04 y R-13 reformulados; seis retirados con su resolución en el T-16, sección F._
- [x] **Crítico [Decisión]** Agregar los riesgos externos que el caso anticipa: invierno altiplánico (enero–febrero, coincide con M13), auditoría y recertificación de 2029, exigencias de los compradores desde 2029 y emergencias. → _Hecho en LC-03: R-25 a R-28 con ficha completa._
- [x] **Alta [Decisión]** Incorporar las 704 HH preventivas y las 96 HH de continuidad a paquetes del T-14 y a la nivelación del T-15 (la regla de zona alta lo exige). → _Hecho en LC-03 (DEC-022): paquetes 1.1.3.3 y 1.1.3.4; total 183.866 HH; T-15, S7, S8 y figuras B.1/7.1, B.2, C.2, D.1/7.2 y D.2 actualizados._
- [ ] **Alta [Decisión]** Redefinir la reserva de gestión como reserva para lo no identificado; dejar la holgura de M11 y la incertidumbre de estimación como contingencia; mostrar la reserva de plazo en la Gantt.
- [x] **Alta** Justificar por escrito las respuestas con beneficio/costo bajo 1 (R-01 0,7; R-09 0,9; R-24 0,8) o cambiar la estrategia. → _Hecho._
- [x] **Alta** Descontar R-15 de la exposición agregada (se cuenta dos veces). → _Hecho: 5,06 → 2,01, reducción de 60 %._
- [x] **Alta** Rehacer la Figura 8.3 con identificadores R-xx, zonas y la séptima rama numerada; alinear los nombres del párrafo con las ramas dibujadas. → _Hecho en LC-03 (9,7 pt); texto y Anexo B usan los nombres de la figura._
- [ ] **Media** Si se mantiene la simulación de Montecarlo, modelar duraciones con distribución sobre la red del T-14 (hoy cinco eventos de Bernoulli).
- [x] **Media** Redondear la precisión espuria («0,4557375», «0,000528», «3.505,79845 HH»). → _Hecho en el texto, el anexo y la ficha de R-15; las tablas de cálculo del Anexo B conservan decimales._
- [x] **Media** Tabla 8.6: la indisponibilidad del personal clave del cliente está en R-10, no en R-07/R-18. → _Hecho._
- [x] **Forma** Fuentes de las tablas con «p. 4», «p. 15» de los anexos en lugar de folio. 🔎 → _Hecho._

## S9 · Plan de calidad (6 %)

- [x] **Alta [Decisión]** Agregar un modelo de madurez del proceso de calidad y pruebas (TMMi o CMMI) junto a SAMM, con línea base y meta. → _Hecho: TMMi (DEC-021)._
- [x] **Alta** Expresar el umbral de capacidad de interacción en segundos agregados al ciclo de la pala (restricción 8), no en «3 interacciones». → _Hecho._
- [x] **Alta [Decisión]** Justificar las pruebas de corte de 48 h y de recuperación dentro de las detenciones de planta frente a la restricción 11 y al peak de 8.500 personas, o moverlas; agregar a la puerta 5 la prohibición de pasar a producción durante una detención. → _Hecho, con la puerta 5._
- [x] **Alta** Incluir el criterio 14 del caso (adopción por decisión propia del operador de pala) en las condiciones de H7 y H12 del T-17. → _Hecho._
- [ ] **Alta** Vincular en la Gantt la certificación y las puertas con los módulos que verifican y con el paso a producción (ver S7).
- [x] **Media** Declarar qué campaña de calidad se sacrifica primero si se atrasa el mes 21. → _Hecho: escalamiento al Comité con criterio fijo._
- [x] **Media** El 9.3.3 remite los paquetes a «Subdocumento 7, 7.1», que no los lista: remitir al T-14. → _Hecho._
- [ ] **Media** Citar las Bases con el mismo autor en todos los subdocumentos.
- [ ] **Media** Figura 9.3 bajo 9 pt (~8,7).
- [ ] **Forma** La Figura 9.1 omite los Anexos D y E; el listado de tablas de los anexos omite A.1 y A.2. 🔎
- [ ] **Forma** Nomenclatura de tablas del T-13 idéntica entre el S9 y el formulario. 🔎

## S13 · Innovaciones (8 %)

- [x] **Alta [Decisión]** Cuantificar el beneficio de la innovación 3 en toneladas o en días de cierre. → _Hecho: toneladas de cobre fino por punto de diferencia y días de producción afectados._
- [x] **Alta** Valorizar en la innovación 1 el embarque penalizado evitado con la cifra del caso (USD 1,9 millones / 4 embarques). → _Hecho: USD 0,95 a 1,4 millones al año._
- [x] **Alta [Decisión]** Defender la innovación 3 frente a los códigos de práctica de contabilidad metalúrgica (VDI 2048, Narasimhan y Jordache) o reforzar su delta propio (Art. 30). → _Hecho: frecuencia por turno y sesgo por camión como delta._
- [x] **Alta** Cuadrar las horas de la rama 1.7: el T-19 declara 2.920 y la tabla suma 3.000 con el paquete 1.7.2.4. → _Hecho._
- [x] **Media** Incoherencia: la introducción dice que la innovación 5 usa datos «de otros tres módulos» y la 13.5.3 que «usa cinco módulos». → _Hecho._
- [ ] **Forma** Listado de tablas del T-19 (omitía T-19.5 y T-19.6) y fuentes con páginas relativas («sección 13.1, p. 7»). 🔎 → _Páginas relativas retiradas; listado por verificar._
