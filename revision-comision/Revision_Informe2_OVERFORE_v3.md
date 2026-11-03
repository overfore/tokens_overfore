# Revisión Informe 2 · OVERFORE S.A. · Caso 01 Minería · v3

Revisión hecha con `Prompt_Revision_Subdocumentos.md` (Modo B, Informe 2) sobre los 31 PDF compilados el 03-11-2026 desde la rama `claude/kind-heisenberg-egckbe` (contenido igual a `a15efa3`), con folios del 1 al 1317. Los folios citados son los impresos en el pie («Folio N»). Se contrastó con la revisión v2 (`Revision_Informe2_OVERFORE_v2.md`, PDF del 20-10, 1273 folios) y con `Figuras_bajo_9pt.md` (22-10). Es una estimación del equipo, no la nota de la comisión.

**Cómo se compiló.** En modo normal, `python compilar.py` se detiene: la clase marca ERROR en 9 subdocumentos porque la tabla «Declaración de uso de IA por sección» no cabe en una página (ver O-G.0). Por eso los PDF revisados son los de `python compilar.py --borrador` (`latex/salida-borrador/`). Compilaron en 3 pasadas, sin errores y con folio estable. Entorno: TeX Live 2023 (XeLaTeX) en Linux, con Open Sans y Montserrat de Debian. El equipo compila con MiKTeX, y las métricas de las fuentes pueden diferir en algunas líneas; el desborde de la tabla de IA, en cambio, ocurre igual en ambos entornos (ver O-G.0).

**Método.**
- Texto extraído de los 31 PDF con búsquedas dirigidas: banderas del §5, forma del §6, matriz del §8 y recálculo del §9.
- Letra de las figuras medida con `herramientas/medir_figuras.py --carpeta salida-borrador`, sobre 161 figuras.
- Citas cruzadas revisadas con `herramientas/revisar_referencias.py` y verificadas a mano: se descartaron los falsos positivos de las figuras con sufijo «a/b» y de las tablas citadas en otro documento.
- Cada observación de la v2 se verificó en el PDF nuevo.
- No hubo una relectura humana completa de las 1317 páginas.

---

## Parte 1 · Estado por subdocumento

| Subdocumento | Estado | Puntaje estimado | Peso Informe 2 | Banderas rojas | Observaciones (bloq. / altas / medias / forma) |
|---|---|---|---|---|---|
| S7 · Plan de trabajo (T-14, T-15, T-18) | ⚠️ Cumple con observaciones | 60 | 15 % | 0 | 0 / 1 / 2 / 1 |
| S3 · Esquema de solución y alcance (T-12) | ⚠️ Cumple con observaciones | 60 | 12 % | 0 | 1 / 1 / 2 / 0 |
| S4.2 · Arquitectura física (T-11) | ⚠️ Cumple con observaciones | 70 | 12 % | 0 | 1 / 0 / 2 / 1 |
| S8 · Plan de riesgos (T-16) | ⚠️ Cumple con observaciones | 60 | 10 % | 0 | 1 / 1 / 1 / 0 |
| S13 · Innovaciones (T-19) | ✅ Cumple | 70 | 10 % | 0 | 1 / 0 / 0 / 1 |
| S6 · Metodologías (T-9, T-10) | ⚠️ Cumple con observaciones | 60 | 8 % | 0 | 1 / 1 / 2 / 0 |
| S9 · Plan de calidad (T-13, T-17) | ⚠️ Cumple con observaciones | 70 | 8 % | 0 | 1 / 0 / 1 / 0 |
| S4.1 · Arquitectura lógica | ⚠️ Cumple con observaciones | 70 | 7 % | 0 | (con S4.2) |
| S2 · Problema y necesidad | ⚠️ Cumple con observaciones | 70 | 6 % | 0 | 1 / 1 / 0 / 0 |
| S5 · Modelo y gestión de datos | ⚠️ Cumple con observaciones | 70 | 6 % | 0 | 1 / 0 / 1 / 0 |
| General · Formalidad | ❌ No cumple | 50 | 3 % | 0 | 1 / 2 / 2 / 1 |
| S1 · Presentación de la empresa | ⚠️ Cumple con observaciones | 60 | 3 % | 0 | 1 / 1 / 2 / 1 |

El bloqueante «1» de cada subdocumento es el mismo hallazgo, O-G.0: la tabla de la Declaración de uso de IA no cabe en una página. Se corrige una sola vez en el patrón, pero hay que aplicarlo en los nueve archivos.

**Cambios frente a la v2 (20-10):**
- **Figuras.** De 67 figuras bajo 9 pt se pasó a **8**, y 7 quedan en el límite. Están resueltas las 18 cartas Gantt del T-14, casi todo el S4 (partido en vista general y partes), el S3, el S5 y la 1.2. Siguen bajo el mínimo la ruta crítica 7.3 (5,5 pt) y el calendario 7.4 (6,7 pt).
- **Innovación 4.** Su beneficio ya está cuantificado: 948 HH y días hábiles (O-13.1 cerrada).
- **Rótulos de zona.** Las láminas físicas ya llevan el código de zona en el título (O-4.2 cerrada).
- **Nuevo bloqueante de forma.** La entrega no compila en modo normal (O-G.0).
- **Siguen abiertas:** 14 frente a 19 grupos de interés (S6/T-9), la leyenda de la RBS (S8), la «referencia de la industria» (S2), el sitio en github.io (S1) y los 97 «Cumple parcialmente» del T-12.

### General · Formalidad y cumplimiento de instrucciones — ❌ No cumple (50)

No cumple
- [O-G.0] La tabla «Declaración de uso de IA por sección» no cabe en una página: compilación normal detenida en 9 subdocumentos y filas finales fuera de la página — S1 f. 15, S2 f. 63, S3 f. 230, S4 f. 538, S5 f. 686, S6 f. 823, S8 f. 1066, S9 f. 1172, S13 f. 1266
- [O-G.1] 8 figuras bajo 9 pt y 7 en el límite — S1, S4, S6, S7, S9 y S13-Anexos (lista en O-G.1)
- [O-G.2] Referencias listadas sin cita en el texto — T-14 (Gans et al., 2003, y otras), Subdocumento8-Anexos (Overfore 2026a–g, CMAA 2026b y 2026c), T-16 (Overfore 2026a, b y d–g)
- [O-G.3] Citas a tablas que no existen — T-12, f. 315: «(Tabla 6.2)» y «(Tabla 6.2 del Subdoc. 6)»; el S6 sólo tiene la Tabla 6.1
- [O-G.4] Erratas de fusión — S4 f. 426 «persona.La Figura 4.5»; T-14 f. 954 «solo.La reversión»; S13 f. 1256 «licencias.El esfuerzo»
- [O-G.5] Páginas casi vacías con 1 a 3 líneas arrastradas — T-11 f. 632, T-15 f. 1022, T-18 f. 1039, S8-Anexos f. 1081, T-16 f. 1145

OK
- Folio único y correlativo del 1 al 1317 en los 31 archivos, sin saltos ni repeticiones; media firma en el 100 % de las páginas.
- Nomenclatura `OVERFORE-…` correcta; un formulario por archivo.
- Sin marcadores, sin «pendiente de verificar», sin PUCV, curso, docente ni «simulado» o «ficticio» en sentido de ejercicio. «Simulador» aparece sólo como herramienta de prueba, y «ficticios» sólo en la cita literal del RT-22.09 (T-12, f. 324).
- Sin «Terraform»: OpenTofu es coherente en S3, S4-Anexos, S6, T-10, T-11, T-12 y T-13.
- Sin precios de la oferta. Los «USD» son los rangos de monto de proyectos anteriores (T-6, f. 32) y la penalización del caso (USD 1,9 millones: S2-Anexos f. 112, S13 f. 1239 y T-19 f. 1304).
- Referencias y Declaración de uso de IA al cierre de los diez subdocumentos, en ese orden.

### S1 · Presentación de la empresa — ⚠️ Cumple con observaciones (60)

No cumple
- [O-1.1] Figura 1.1 bajo 9 pt — f. 6 (~8,7 pt)
- [O-1.2] Sitio web en dominio gratuito con nombre de un integrante — Tabla 1.1, f. 4; arrastre a T-12, RT-23.01 a RT-23.04
- [O-1.3] Dotación de apoyo que no explica el máximo de 45 personas — 1.2, f. 7; arrastre a S7 y T-15
- [O-1.4] Meses del máximo de apoyo distintos entre cuerpo y anexo — S1 f. 7 («meses 14 y 15») frente a S1-Anexos f. 28 («meses 13 a 15»)
- [O-1.5] Declaración de IA con la herramienta escrita de forma dispar («Claude», «claude», «claude y chatGPT») — Tabla de declaración, f. 14–15

OK
- Organigrama del proyecto (Figura 1.2) ya en 9 pt o más.
- Cartas de referencia en una página cada una, con nombre, cargo, correo y teléfono (S1-Anexos f. 20–23).
- Equipo clave de nueve personas coherente con S1-Anexos, T-14 y T-16.

### S2 · Problema y necesidad — ⚠️ Cumple con observaciones (70)

No cumple
- [O-2.1] Sigue una meta interna llamada «referencia de la industria» — 2.2.3, f. 49

OK
- Las 12 figuras cumplen 9 pt.
- El comprador del 38 % es el japonés y el coreano se menciona como en el caso (cap. 1).
- Diecinueve grupos de actores: catorce internos y cinco externos (2.4, f. 53).

### S3 · Esquema de solución y alcance — ⚠️ Cumple con observaciones (60)

No cumple
- [O-3.1] T-12 con 97 requisitos «Cumple parcialmente» y 8 «Por cumplir» — Tabla de resumen, f. 244
- [O-3.2] Descripciones del catálogo del T-12 cortadas con «…» (unas 245) — B.2
- [O-3.3] Remisión a una Tabla 6.2 inexistente — T-12, RT-19.08 y RT-19.10, f. 315
- [O-3.4] Declaración de IA con «Alto» en 7 filas — f. 229–230

OK
- Las 14 figuras del S3 cumplen 9 pt, incluidas 3.4 y 3.5 de alcance por etapa (antes entre 5 y 6 pt).
- RTO 4 h / RPO 15 min y Brazil South coherentes con S4, S5, S9, T-11 y T-12.

### S4.1 y S4.2 · Arquitectura lógica y física — ⚠️ Cumple con observaciones (70)

No cumple
- [O-4.1] Vista general de la topología física y lámina de Brazil South bajo 9 pt — Figura 4.23, f. 489 (~5,8 pt); Figura 4.36, f. 532 (~8,9 pt)
- [O-4.2] Frase de plantilla repetida tras cada figura partida — f. 428, 433 y 452: «Las Figuras 4.Xa, 4.Xb presentan este recorrido por partes»
- [O-4.3] Figuras 4.6, 4.8, 4.15 y 4.24 partidas en a/b sin vista general — f. 429–430, 434–435, 455–456 y 494–495
- [O-4.4] Figuras en el límite — 4.1 (f. 416), 4.16 (f. 463), 4.26 (f. 502) y 4.27 (f. 504), ~9,1 pt

OK
- 45 de las 51 figuras ya superan 9,3 pt, con las vistas densas partidas en vista general y partes (4.10, 4.21, 4.22 y 4.23).
- Láminas físicas con código de zona en el título («Figura 4.30 — Z04 · Sala técnica y Nodo de Faena», f. 512).
- Dimensionamiento derivado y recalculado sin error (Tabla 4.33, f. 522; ver §9).

### S5 · Modelo y gestión de datos — ⚠️ Cumple con observaciones (70)

No cumple
- [O-5.1] Declaración de IA con «Alto» en 12 de 13 filas — f. 685–686

OK
- Las 16 figuras del modelo cumplen 9 pt (antes 9 bajo el mínimo).
- RPO 15 min, TPS 135 y 200 coherentes con el S4.

### S6 · Metodologías — ⚠️ Cumple con observaciones (60)

No cumple
- [O-6.1] Catorce grupos de interés frente a los diecinueve del S2 — 6.1.4 y 6.1.5, f. 803; arrastre a T-9
- [O-6.2] Figuras 6.7 (f. 808, ~7,7 pt) y 6.9 (f. 813, ~8,7 pt) bajo 9 pt; 6.3 y 6.11 en el límite
- [O-6.3] Declaración de IA con «Alto» en 9 de 15 filas — f. 822–823

OK
- OpenTofu igual en texto, figuras y T-10.

### S7 · Plan de trabajo, EDT, cronograma e implantación — ⚠️ Cumple con observaciones (60)

No cumple
- [O-7.1] Ruta crítica y calendario de implantación bajo 9 pt — Figura 7.3, f. 864 (~5,5 pt); Figura 7.4, f. 866 (~6,7 pt)
- [O-7.2] Declaración de IA con «Alto» en 9 de 10 filas — f. 870–871
- [O-7.3] Referencias del T-14 sin cita (Gans et al., 2003, entre otras) — Referencias del T-14
- [O-7.4] Páginas con 1 a 3 líneas arrastradas en T-15 y T-18 — f. 1022 y 1039

OK
- Las 23 figuras del T-14, incluidas las cartas Gantt C.1 a C.18, cumplen 9 pt (antes 5,8–7,3).
- 183.066 HH coherentes en S7, T-14 y T-15; 60.394 + 122.672 y 56.886 + 126.180 cuadran.
- Máximo de 45 personas en el mes 14, coherente en S7, T-15 y T-16.

### S8 · Plan de riesgos — ⚠️ Cumple con observaciones (60)

No cumple
- [O-8.1] La leyenda de la RBS promete la «zona inherente de cada riesgo» y la figura no la muestra; las categorías del texto no coinciden con las de la figura — Figura 8.3, f. 1050
- [O-8.2] Referencias sin cita en el S8-Anexos y en el T-16 — Referencias de ambos documentos

OK
- 800 HH preventivas = 704 de las fichas + 96 de continuidad, declarado (f. 1059).
- La Figura 8.3 ya cumple 9 pt.

### S9 · Plan de calidad — ⚠️ Cumple con observaciones (70)

No cumple
- [O-9.1] Figura 9.3 bajo 9 pt — f. 1161 (~8,7 pt)

OK
- Conmutación planificada «2 h 50 min… estimados… se medirá» en S9 f. 1162 y T-13 f. 1208, coherente con T-11.

### S13 · Innovaciones — ✅ Cumple (70)

No cumple
- [O-13.1] Errata de fusión en el impacto económico de la innovación 4 — 13.4.4, f. 1256

OK
- Beneficio de la innovación 4 cuantificado: 948 HH transferidas y días hábiles por cambio funcional, con hipótesis declarada (13.4.4, f. 1256). Cierra la O-13.1 de la v2.
- Las 6 figuras del S13 cumplen 9 pt; sólo la A.1 de sus anexos queda en el límite (f. 1274, ~9,1 pt).

---

## Parte 2 · Revisión detallada

### GENERAL
Formalidad y contenido del documento / Cumplimiento de instrucciones (3 %)
Revisión: (50)
La entrega mejoró mucho en legibilidad: de 67 figuras bajo 9 pt quedan 8. Pierde porque, tal como está en el repositorio, no se puede generar la entrega con el compilador oficial: la Declaración de uso de IA desborda la página en nueve subdocumentos. Pierde además por citas a tablas inexistentes, referencias sin cita y tres erratas de fusión.

**O-G.0 · Declaración de uso de IA que no cabe en una página** · Prioridad: Bloqueante (forma)
- Dónde: tabla «Declaración de uso de IA por sección» de S1 (f. 15, 15 filas), S2 (f. 63), S3 (f. 230), S4 (f. 538, 45 filas), S5 (f. 686), S6 (f. 823), S8 (f. 1066), S9 (f. 1172) y S13 (f. 1266).
  - En el S1 las filas «Anexo D del Subdocumento 1» a «T-6» quedan por debajo de «Media firma · Representante Legal» y fuera de la página (texto hasta y = 799 pt en una página de 792 pt).
  - La página siguiente lleva sólo «Fuente: elaboración propia.» (S1 f. 16, S2 f. 64, S3 f. 231, S4 f. 539, S5 f. 687, S6 f. 824, S8 f. 1067, S9 f. 1173, S13 f. 1267).
- Qué está mal y por qué: la clase (`overfore.cls`, entorno `tabla`) trata como ERROR toda tabla del subdocumento que pase de una página, así que `python compilar.py` no entrega PDF. Si se fuerza con `--borrador`, las páginas salen marcadas «BORRADOR · NO ENTREGAR» y la declaración queda cortada. Para la comisión, una Declaración de IA incompleta incumple el Comunicado 10, §7.2.
- Cambio directo: acortar la columna «Revisión humana» a una frase por fila (por ejemplo, «Kavon Kermani: validó cargos y dependencias.»). Si aun así no cabe, como en el S4, agrupar filas por sección de primer nivel («4.1.1 a 4.1.9»), manteniendo una fila por anexo y por formulario. Recompilar en modo normal hasta que no queden errores.

**O-G.1 · Figuras con texto bajo 9 pt** · Prioridad: Alta
- Dónde (percentil 5 de la altura de las minúsculas, medido al tamaño impreso):
  - Bajo 9 pt: S1 1.1 (f. 6, 8,7); S4 4.23 (f. 489, 5,8) y 4.36 (f. 532, 8,9); S6 6.7 (f. 808, 7,7) y 6.9 (f. 813, 8,7); S7 7.3 (f. 864, 5,5) y 7.4 (f. 866, 6,7); S9 9.3 (f. 1161, 8,7).
  - En el límite, de 9,0 a 9,3 pt: S4 4.1, 4.16, 4.26 y 4.27; S6 6.3 y 6.11; S13-Anexos A.1.
- Qué está mal y por qué: Art. 40.4 de las Bases administrativas y Comunicado 10, §4.
- Cambio directo:
  - 7.3 y 7.4: regenerar en página horizontal, partiendo por etapa si hace falta. Pesan el 15 %.
  - 4.23: como ya tiene partes legibles (4.23a, b y c), simplificar la vista general a sitios y enlaces sin rótulos de equipos.
  - 6.7, 1.1, 6.9, 9.3 y 4.36: subir 1 pt la letra en el origen.
- Nota: la medida tiene ± 0,3 pt y se hizo con las fuentes de Debian. Confirmar en la compilación del equipo las que quedan entre 8,7 y 9,3 pt.

**O-G.2 · Referencias listadas sin cita** · Prioridad: Media
- Dónde:
  - T-14: «Gans, N., Koole, G. y Mandelbaum, A. (2003)» sin cita. El cuerpo ya cita PMI, ISO/IEC, McConnell, OWASP y otras: mejoró frente a la v2.
  - Subdocumento8-Anexos: sólo cita «(Moya, 2026…)» y «(CMAA, 2026a…)»; Overfore S.A. 2026a–g y CMAA 2026b–c quedan sin cita.
  - T-16: cita CMAA 2026b, CMAA 2026c, ISO 2018 y Overfore 2026c; Overfore 2026a, b y d–g quedan sin cita.
- Qué está mal y por qué: Comunicado 10, §6: «toda referencia de la lista debe estar citada en el texto».
- Cambio directo: citar cada entrada donde se usa, por ejemplo «(Overfore S.A., 2026d, Tabla G.2)», o eliminarla.

**O-G.3 · Citas a una tabla inexistente** · Prioridad: Media
- Dónde: Formulario T-12, f. 315. RT-19.08: «Subdoc. 6, 6.1.5.1 y 6.1.5.2 (Tabla 6.2)». RT-19.10: «Aviso de desviación de hito con plan de recuperación (Tabla 6.2 del Subdoc. 6)».
- Qué está mal y por qué: el S6 tiene una sola tabla, la 6.1, que es la Declaración de IA. La comisión trata las referencias a elementos inexistentes como indicio del §7.1 d.
- Cambio directo: reemplazar «(Tabla 6.2)» por la sección o la tabla del T-9 o del T-10 que contiene el tablero y el aviso de desviación.

**O-G.4 · Erratas de fusión** · Prioridad: Media
- Dónde: S4 f. 426 «…decidir la habilitación de una persona.La Figura 4.5 muestra…»; T-14 f. 954 «…lo promueve y lo revierte solo.La reversión se completa…»; S13 f. 1256 «…no necesita hardware ni licencias.El esfuerzo…».
- Cambio directo: agregar el espacio después del punto en los tres lugares.

**O-G.5 · Páginas casi vacías** · Prioridad: Forma
- Dónde: T-11 f. 632; T-15 f. 1022; T-18 f. 1039; S8-Anexos f. 1081; T-16 f. 1145. Son páginas con 1 a 3 líneas que pasaron de la anterior.
- Cambio directo: ajustar caso a caso.

### SUBDOCUMENTO 1
1. Presentación de la empresa — Formulario T-6 (3 %)
Revisión: (60)

**O-1.1 · Figura 1.1 bajo 9 pt** · Prioridad: Media — f. 6, «Estructura organizacional de Overfore S.A.» (~8,7 pt). Cambio directo: subir 1 pt la letra en el origen o agrandar la figura al ancho de la página.

**O-1.2 · Sitio web en dominio gratuito** · Prioridad: Media
- Dónde: Tabla 1.1, f. 4: «https://lucasdzamora.github.io/FEP_Proyecto/».
- Arrastre a otros subdocumentos: T-12, RT-23.01 a RT-23.04.
- Cambio directo: publicar en un dominio corporativo y reemplazar la URL en la Tabla 1.1 y en el T-12. Si no es posible, registrarlo como decisión del equipo.

**O-1.3 · Dotación frente al máximo de 45 personas** · Prioridad: Media
- Dónde: 1.2, f. 7: «Ese apoyo llega a treinta personas en la implementación, en los meses 14 y 15… A ellos se agregan doce perfiles de especialistas externos».
- Arrastre a otros subdocumentos: S7 y T-15 («máximo de 45 personas del mes 14»).
- Qué está mal y por qué: 9 + 30 = 39. El S1 no muestra cómo se llega a 45 (DEC-013 / R-05 abiertas).
- Cambio directo: agregar «; con los especialistas externos y los digitalizadores, el proyecto llega a 45 personas distintas en el mes 14 (Formulario T-15)».

**O-1.4 · Meses del máximo distintos entre cuerpo y anexo** · Prioridad: Alta
- Dónde: S1, f. 7: «treinta personas en la implementación, en los meses 14 y 15». S1-Anexos, f. 28: «la implementación llega a treinta personas en los meses 13 a 15».
- Qué está mal y por qué: contradicción interna entre el cuerpo y su anexo (§7.1 c).
- Cambio directo: verificar el mes contra el T-15 y usar el mismo período en ambos lugares.

**O-1.5 · Herramienta escrita de forma dispar** · Prioridad: Forma — Declaración de IA, f. 14–15: «Claude», «claude», «claude y chatGPT». Cambio directo: «Claude (Anthropic)» y «ChatGPT (OpenAI)» en todas las filas y documentos.

### SUBDOCUMENTO 2
2. Resumen ejecutivo, comprensión del problema y de la necesidad (6 %)
Revisión: (70)

**O-2.1 · Meta interna llamada «referencia de la industria»** · Prioridad: Alta
- Dónde: 2.2.3, f. 49: «en cada cambio de turno se pierden 47 minutos efectivos, casi el doble de la referencia de la industria».
- Qué está mal y por qué: el cap. 7.2 del caso rotula esa columna «Meta interna». Es la observación 16 del Informe 1, y repetirla es «observación grave» (Art. 47.1). Ya estaba en la v2.
- Cambio directo: reemplazar «casi el doble de la referencia de la industria» por «casi el doble de la meta interna de 25 minutos».

### SUBDOCUMENTO 3
3. Esquema de solución y alcance — Formulario T-12 (12 %)
Revisión: (60)
El esquema y las figuras de alcance ya son legibles; con eso el ítem subiría a 70. Lo retiene en 60 el T-12, que sigue declarando parcial casi una quinta parte de los requisitos.

**O-3.1 · T-12 con requisitos parciales** · Prioridad: Alta
- Dónde: T-12, Tabla de resumen, f. 244: «Total 500 97 8 11 6». Requisitos transversales: 285 cumple, 64 parcial y 8 por cumplir.
- Qué está mal y por qué: numeral 1.4 de las Transversales: omitir un obligatorio vale cero en el ítem.
- Cambio directo: cerrar los parciales que se resuelven con un dato (por ejemplo, el modelo de procesador en el T-11, RT-08.01) y justificar por escrito los que dependen del Cliente.

**O-3.2 · Descripciones con «…»** · Prioridad: Media — T-12, B.2. Cambio directo: reemplazar el corte por una descripción breve que termine en punto, manteniendo la remisión al Anexo A del S2.

**O-3.3 · Tabla 6.2 inexistente** · Prioridad: Media — ver O-G.3.

**O-3.4 · Nivel «Alto» en la Declaración de IA** · Prioridad: Media — 7 filas en «Alto». Cambio directo: confirmar con cada redactor el nivel real, sin subdeclarar.

### SUBDOCUMENTO 4.1 y 4.2
4.1 Arquitectura lógica (7 %) · 4.2 Arquitectura física — Formulario T-11 (12 %)
Revisión: (70)
La corrección de las figuras fue de fondo: 45 de las 51 figuras ya cumplen, las vistas densas están partidas y las láminas físicas llevan su zona en el título. Queda la vista general de la topología, una frase de plantilla repetida y cuatro figuras partidas sin vista general.

**O-4.1 · Figuras 4.23 y 4.36** · Prioridad: Media — ver O-G.1.

**O-4.2 · Frase de plantilla repetida** · Prioridad: Media
- Dónde:
  - f. 428: «Las Figuras 4.6a y 4.6b muestran dónde corre cada componente… Las Figuras 4.6a, 4.6b presentan este recorrido por partes.»
  - f. 433: la misma frase con 4.8a y 4.8b, en seguridad.
  - f. 452: la misma frase con 4.15a y 4.15b, en conectores.
  - Fuente: `OVERFORE-Subdocumento4.tex`, líneas 397, 439 y 611.
- Qué está mal y por qué: repite lo que dice la oración anterior y habla de «recorrido» en figuras de seguridad y de conectores. Es una frase de plantilla repetida casi textual, indicio del §7.1 que la comisión anota.
- Cambio directo: eliminar las tres oraciones «Las Figuras 4.Xa, 4.Xb presentan este recorrido por partes.».

**O-4.3 · Partes sin vista general** · Prioridad: Media
- Dónde: Figuras 4.6a/b, 4.8a/b, 4.15a/b y 4.24a/b. No existe una Figura 4.6, 4.8, 4.15 ni 4.24.
- Qué está mal y por qué: el Comunicado 10, §4 pide «primero vista general, luego partes». Las Figuras 4.10, 4.21, 4.22 y 4.23 sí lo cumplen.
- Cambio directo: agregar una vista general simple antes de cada par, o explicar en el texto que las dos partes son vistas complementarias de la vista general de la capa (Figura 4.1).

**O-4.4 · Figuras en el límite** · Prioridad: Forma — 4.1, 4.16, 4.26 y 4.27 (~9,1 pt). Cambio directo: confirmar en el origen.

### SUBDOCUMENTO 5
5. Modelo y gestión de datos (6 %)
Revisión: (70)

**O-5.1 · Declaración de IA en «Alto»** · Prioridad: Media — 12 de 13 filas en «Alto». Cambio directo: declarar el nivel real por sección. Con esa proporción y la regla del §7.1, la comisión puede leerlo como capítulo generado.

### SUBDOCUMENTO 6
6. Metodologías — Formularios T-9 y T-10 (8 %)
Revisión: (60)

**O-6.1 · Catorce frente a diecinueve grupos de interés** · Prioridad: Alta
- Dónde: 6.1.5, f. 803: «…entre los catorce grupos de interés del ecosistema. Entre ellos existen 91 canales potenciales, según n(n −1)/2 = 14 × 13 / 2»; 6.1.4: «los catorce grupos de interés representados en la Figura 6.4».
- Arrastre a otros subdocumentos: T-9, «Se aplica a los catorce grupos principales…» y «Para 14 grupos… 91 canales posibles»; S2, f. 53: «diecinueve grupos de actores: catorce internos y cinco externos».
- Qué está mal y por qué: contradicción entre subdocumentos (§7.1 c), ya señalada en la v2 (DEC-012 / R-04).
- Cambio directo: en 6.1.4, decir que se gestionan los diecinueve grupos del S2 y que la Figura 6.4 muestra los catorce internos. Recalcular los canales (19 × 18 / 2 = 171) o justificar el uso de 14. Aplicar lo mismo en el T-9.

**O-6.2 · Figuras 6.7 y 6.9 bajo 9 pt** · Prioridad: Media — ver O-G.1.

**O-6.3 · Declaración de IA en «Alto»** · Prioridad: Media — 9 de 15 filas.

### SUBDOCUMENTO 7
7. Plan de trabajo, EDT, cronograma e implantación — Formularios T-14, T-15 y T-18 (15 %)
Revisión: (60)
Las cartas Gantt ya son legibles y los totales cuadran en los tres documentos. Lo retiene en 60 la ruta crítica: es lo primero que verifica la comisión (Cap. 19: «que la ruta crítica sea creíble») y sigue en 5,5 pt.

**O-7.1 · Ruta crítica y calendario bajo 9 pt** · Prioridad: Alta
- Dónde: Figura 7.3 «Ruta crítica de la implementación sobre el cronograma contractual», f. 864 (~5,5 pt); Figura 7.4 «Calendario de implantación de las dos etapas, meses 12 a 23», f. 866 (~6,7 pt).
- Cambio directo: regenerar ambas en página horizontal, con la 7.3 partida por etapa (M1–M12 y M13–M20) si no cabe.

**O-7.2 · Declaración de IA en «Alto»** · Prioridad: Media — 9 de 10 filas.

**O-7.3 · Gans et al. (2003) sin cita en el T-14** · Prioridad: Media — citarlo donde se dimensiona la mesa de ayuda o eliminarlo.

**O-7.4 · Páginas casi vacías** · Prioridad: Forma — T-15 f. 1022 y T-18 f. 1039.

### SUBDOCUMENTO 8
8. Plan de riesgos — Formulario T-16 (10 %)
Revisión: (60)

**O-8.1 · La RBS no muestra lo que promete su leyenda** · Prioridad: Alta
- Dónde: Figura 8.3, f. 1050. Leyenda: «Estructura de desglose de riesgos (RBS) de SITCO Aranda, con la zona inherente de cada riesgo».
  - La figura muestra cajas sin color de zona y sin R-xx, y la rama «Equipo y acreditación» no lleva número.
  - El texto que sigue habla de «Solución y tecnología», «Operación del cliente» y «personas y adopción», pero las ramas de la figura se llaman «1. Tecnología y seguridad», «3. Operación e infraestructura» y «4. Adopción y uso».
- Qué está mal y por qué: la comisión verifica que cada leyenda corresponda a la figura; en el Informe 1 anotó «tres de las cuatro láminas del S4 no corresponden a su leyenda». Ya estaba en la v2.
- Cambio directo: rehacer la 8.3 con R-xx y el color de la zona inherente en cada caja, la rama 7 numerada y las categorías con los mismos nombres del texto. Alternativa mínima: cambiar la leyenda a «Estructura de desglose de riesgos (RBS) de SITCO Aranda» y alinear los nombres del párrafo con los de la figura.

**O-8.2 · Referencias sin cita** · Prioridad: Media — ver O-G.2.

### SUBDOCUMENTO 9
9. Plan de calidad — Formularios T-13 y T-17 (8 %)
Revisión: (70)

**O-9.1 · Figura 9.3 bajo 9 pt** · Prioridad: Media — f. 1161 (~8,7 pt). Cambio directo: subir 1 pt la letra en el origen.

### SUBDOCUMENTO 13
13. Innovaciones — Formulario T-19 (10 %)
Revisión: (70)
Corrige la principal falta de la v2: la innovación 4 ahora cuantifica su beneficio en horas y días hábiles, con la hipótesis de carga declarada como tal (DEC-016, propuesta pendiente de validación del equipo).

**O-13.1 · Errata** · Prioridad: Forma — 13.4.4, f. 1256: «licencias.El esfuerzo». Ver O-G.4.

### CONSIDERACIONES TRANSVERSALES
- **Consistencia técnica:** coherente en las cifras que sostienen la propuesta. Quedan dos contradicciones: 14 frente a 19 grupos de interés (S6/T-9 frente a S2) y los meses del máximo de apoyo (S1 frente a S1-Anexos).
- **Trazabilidad:** completa del caso al requerimiento, al componente y a la EDT. La debilitan el T-12, que se declara parcial en 97 requisitos, y su cita a una Tabla 6.2 inexistente.
- **Fundamentación ingenieril:** los recálculos del §9 cuadran.
- **Uso de IA generativa:** sin indicios graves del §7.1. El riesgo está en tres frentes:
  - la frase de plantilla repetida del S4 (O-4.2);
  - las declaraciones con «Alto» mayoritario (S5 12/13, S7 9/10, S6 9/15);
  - las tablas de declaración que hoy no caben en la página (O-G.0).

### Matriz de consistencia (§8)

| Elemento | Dónde se comparó | Resultado |
|---|---|---|
| HH totales | S7 · T-14 · T-15 | Coherente: 183.066 HH (8 menciones); 60.394 + 122.672 y 56.886 + 126.180 |
| Máximo de personas | S7 · T-15 · T-16 · S4 · S1 | 45 en el mes 14, coherente en S7, T-15 y T-16; el S1 no lo explica y su anexo da otro período (O-1.3, O-1.4) |
| HH preventivas | S8 f. 1059 · S8-Anexos · T-14 · T-16 | Coherente: 800 = 704 + 96 |
| TPS de régimen, punta y diseño | S4 f. 521–522 · S4-Anexos · S5 · T-11 · T-12 · T-13 · T-16 | Coherente: 40 / 135 / 200 |
| RTO / RPO | S3 · S4 · S5 · S7 · S9 · T-11 · T-12 · T-13 · T-16 | Coherente: 4 h / 15 min central; 1 h y 0 eventos en terreno |
| Región secundaria | S4 · S5 · S9 · S13 · T-11 · T-12 · T-16 · T-19 | Coherente: Brazil South |
| Infraestructura como código | S3 · S4-Anexos · S6 · T-10 · T-11 · T-12 · T-13 | Coherente: OpenTofu |
| Grupos de interés | S2 f. 53 · S3-Anexos · S6 f. 803 · T-9 | **Contradictorio**: 19 frente a 14 (O-6.1) |
| Requerimientos | S2 · S3 · S6 · S9 · T-9 · T-12 · T-13 | Coherente: 248 |
| Equipo clave | S1 · S1-Anexos · T-12 · T-14 · T-16 | Coherente: nueve personas |
| Comprador del 38 % | S2 f. 37, 53 y 55 | Coherente con el caso: japonés; el coreano, como en el cap. 1 |

### Recálculo de cifras (§9)

| Cifra | Origen | Recálculo | Resultado |
|---|---|---|---|
| 40 TPS en régimen | S4, Tabla 4.33, f. 522 | 245 × 6 ÷ 60 = 24,5; + 9 + 6,5 = 40 | Cuadra |
| 135 TPS en el relevo | S4, f. 521 | 505 × 6 ÷ 30 = 101; + 34 = 135; 200 = 135 × 1,48 | Cuadra |
| 183.066 HH | S7, T-14, T-15 | 60.394 + 122.672 = 183.066; 56.886 + 126.180 = 183.066 | Cuadra |
| 800 HH preventivas | S8, f. 1059 | 704 + 96 = 800 | Cuadra |
| 948 HH transferidas (innovación 4) | S13, f. 1256 | 16 × 30 + 12 × 24 + 10 × 18 = 480 + 288 + 180 = 948; 38 h/mes ÷ 152 h = 25 % | Cuadra |
| 91 canales | S6, f. 803 | 14 × 13 ÷ 2 = 91 | Cuadra con 14; con los 19 del S2 serían 171 (O-6.1) |

## Parte 3 · Priorización

### A. Banderas rojas

No se detectaron banderas rojas del §7.1 ni causales de no presentado en el contenido. Se buscaron:
- marcadores y «pendiente de validar»;
- curso, PUCV y material docente;
- «simulado» y «ficticio» en sentido de ejercicio;
- precios de la oferta;
- «Terraform»;
- folio no correlativo y nomenclatura.

Lo más cercano a un indicio es la frase de plantilla repetida del S4 (O-4.2), y conviene quitarla. El bloqueante O-G.0 es de forma y de compilación, no de contenido, pero impide generar la entrega.

### B. Plan de corrección priorizado

| Prioridad | Observación | Subdocumento y sección | Cambio directo (resumen) | Arrastre | Regla | Puntaje en juego |
|---|---|---|---|---|---|---|
| Bloqueante | O-G.0 | Declaración de IA de S1, S2, S3, S4, S5, S6, S8, S9 y S13 | Acortar «Revisión humana» y agrupar filas hasta que quepa; recompilar en modo normal | 9 subdocumentos | Comunicado 10 §7.2; clase `tabla` | Toda la entrega |
| Alta | O-7.1 | S7, Figuras 7.3 y 7.4 | Horizontal, 9 pt, partir por etapa | — | Art. 40.4; Cap. 19 | 15 % |
| Alta | O-3.1 | T-12, resumen | Cerrar los parciales de un dato y justificar el resto | T-11 | Numeral 1.4 BTT | 12 % |
| Alta | O-8.1 | S8, Figura 8.3 | R-xx, zona y categorías iguales al texto | — | §4 | 10 % |
| Alta | O-6.1 | S6 6.1.4–6.1.5; T-9 | 19 grupos y 171 canales, o justificar 14 | S2 | §7.1 c | 8 % |
| Alta | O-2.1 | S2 2.2.3 | «meta interna de 25 minutos» | — | Art. 47.1 | 6 % |
| Alta | O-1.4 | S1 1.2 y S1-Anexos | Mismo período del máximo | T-15 | §7.1 c | 3 % |
| Media | O-4.2, O-4.3 | S4 | Quitar la frase de plantilla; vista general o explicación de las partes | — | §7.1; §4 | 19 % (protege) |
| Media | O-G.1 (resto) | 4.23, 4.36, 6.7, 6.9, 9.3, 1.1 | Subir letra o simplificar | — | Art. 40.4 | ~2 % |
| Media | O-G.3 | T-12 f. 315 | Corregir la cita a la Tabla 6.2 | S6 | §7.1 d | 12 % (protege) |
| Media | O-G.2 | T-14, S8-Anexos, T-16 | Citar o eliminar | — | §6 | ~0,5 % |
| Media | O-5.1, O-6.3, O-7.2, O-3.4 | Declaraciones de IA | Nivel real por sección | — | §7.2 | riesgo §7.1 |
| Media | O-1.2, O-1.3 | S1 | URL corporativa; explicar las 45 personas | T-12, S7, T-15 | Art. 47.1 | ~0,5 % |
| Forma | O-G.4, O-G.5, O-1.5, O-4.4 | Varios | Erratas, páginas casi vacías, nombre de herramienta | — | §6 | Transversal |

### C. Cierre
- **Puntaje ponderado estimado del Informe 2, una vez corregido O-G.0:** unos **65 / 100**. Desglose: Transversal 50; S1 60; S2 70; S3 60; S4.1 70; S4.2 70; S5 70; S6 60; S7 60; S8 60; S9 70; S13 70. La v2 estimaba 63. La mejora viene de las figuras del S4, del S5, de las Gantt del T-14 y de la innovación 4.
- **Sin corregir O-G.0** no hay entrega válida: el compilador oficial no produce los PDF y el borrador sale marcado «NO ENTREGAR».
- **Las tres correcciones que más puntos recuperan:**
  1. O-G.0: que la Declaración de IA quepa en una página en los nueve subdocumentos. Condición para entregar.
  2. O-7.1: ruta crítica 7.3 y calendario 7.4 legibles. Con eso S7 sube a 70: +1,5 puntos ponderados.
  3. O-3.1 y O-G.3: cerrar parciales del T-12 y corregir la Tabla 6.2. S3 sube a 70: +1,2 puntos.
