# Figuras pendientes de corregir

Figuras que hay que editar en su origen (draw.io o imagen) para cerrar la Primera Revisión del Informe 2 y la regla de 9 pt. Ya se corrigió el texto que las rodea y, cuando correspondía, se decidió la cifra que deben mostrar (ver [DECISIONES.md](../DECISIONES.md), DEC-017 a DEC-020). Lista armada el 03-11-2026 sobre `main` más las correcciones de la tarea LC-02.

**Cómo medir:** desde `latex/`, `python herramientas/medir_figuras.py` (o `--carpeta salida-borrador`). Mínimo 9 pt al tamaño impreso (Art. 40.4 y Comunicado 10, §4); la medida tiene ± 0,3 pt.

**Prioridad:** primero las que cambian contenido o contradicen el texto (A), después las que sólo están bajo 9 pt (B), y al final las que están en el límite (C).

---

## A. Cambiar contenido (hoy contradicen el texto o la revisión)

| Figura | Archivo | Qué cambiar | Cifra o criterio que ya fija el texto |
|---|---|---|---|
| **1.1** Estructura organizacional (S1) | `subdoc01/subdocumento/figuras/fig-1-1-estructura-organizacional-overfore-s.png` (sin draw.io) | «Asigna a Aranda 5 desarrolladores» → «8 desarrolladores en los meses 3 a 11 y 7 en los meses 13 a 17». «Asigna a Aranda 3 técnicos de terreno» → «hasta 10 técnicos de terreno (5 en régimen desde el mes 24)». Subir la letra a 9 pt o más (hoy ~8,7). | Anexo F del S1 y Formulario T-15 (DEC-017). |
| **1.2** Organización del proyecto (S1) | `subdoc01/subdocumento/figuras/fig-1-2-organizacion-proyecto-sitco-aranda.png` (sin draw.io) | Caja Líder de Desarrollo: «5 desarrolladores en tres equipos Scrum» → «8 desarrolladores en tres equipos Scrum (M3–M11)». Caja Líder de Operación: «3 técnicos de terreno 7x7» → «hasta 10 técnicos de terreno 7x7». | Igual que la 1.1. |
| **4.26 y 4.27** Nube principal (S4) | `subdoc04/subdocumento/figuras/drawio/fig-4-26-…drawio.xml` y `fig-4-27-…drawio.xml` | Dibujar las zonas de disponibilidad, los SKU y las subredes que hoy están sólo en el texto (4.2.2.2). Verificar 9 pt (hoy ~9,1, en el límite). | Texto de 4.2.2.2 y Formulario T-11. |
| **6.4** Ecosistema de actores (S6) | `subdoc06/subdocumento/figuras/fig-6-4-ecosistema-actores-interesados-sitco-aranda.png` | Mostrar los **19 grupos** del Subdocumento 2 (14 internos y 5 externos), no 14. | DEC-018: un solo registro de 19 grupos; el S6 y el T-9 ya dicen 19 y 171 canales. |
| **6.5** Matriz de poder e interés (S6) | `subdoc06/subdocumento/figuras/fig-6-5-matriz-poder-interes-grupos-interes.png` | Ubicar los **19 grupos** en la matriz. | DEC-018. Debe coincidir con las Figuras 2.11 y 2.12 del S2. |
| **8.3** RBS (S8) | `subdoc08/subdocumento/figuras/fig-8-3-estructura-desglose-riesgos-rbs-sitco.png` | Poner el identificador R-xx en cada caja y numerar la séptima rama («7. Equipo y acreditación»). Opcional: color de la zona inherente con su leyenda. Usar en el párrafo siguiente los mismos nombres de rama que la figura. | La leyenda ya no promete la zona inherente; si se agrega el color, se puede devolver a la leyenda. |
| **9.1** Estructura del plan de calidad (S9) | `subdoc09/subdocumento/figuras/fig-9-1-estructura-plan-calidad-conexion-demas.png` | Agregar los Anexos D y E del S9 entre los entregables (hoy sólo A, B y C). | Índice de OVERFORE-Subdocumento9-Anexos. |
| **Cartas Gantt C.1 a C.18** (T-14) y **7.3** Ruta crítica (S7) | `subdoc07/formulario-T-14/figuras/drawio/*.drawio.xml` y `subdoc07/subdocumento/figuras/fig-7-3-…png` | Lo que pide el profesor para el S6, S7 y S9: (1) dependencias entre paquetes, con flechas o columna de predecesoras; (2) los sprints, revisiones y liberaciones de los módulos en lugar de barras de 5 a 8 meses; (3) las puertas de calidad del S9 vinculadas al módulo que verifican y al paso a producción; (4) el paquete y la tarea del despliegue por anillos (botonera y tabletas); (5) la reserva de cronograma como barra visible antes de H7 y H12. La 7.3 debe salir de esa misma red. | Tarea F-03 en curso. Requiere además rehacer el CPM con duraciones estimadas (decisión del equipo; ver Pendientes). |

## B. Sólo letra bajo 9 pt

| Figura | Archivo | Letra hoy | Sugerencia |
|---|---|---|---|
| **7.3** Ruta crítica (S7) | `subdoc07/subdocumento/figuras/fig-7-3-ruta-critica-implementacion-sobre-cronograma.png` | ~5,5 pt | Página horizontal y partir por etapa (M1–M12 y M13–M21). Hacerlo junto con el punto A. |
| **4.23** Topología física, vista general (S4) | `subdoc04/subdocumento/figuras/drawio/s4-revision-23.drawio.xml` | ~5,8 pt | Las partes 4.23a, b y c ya son legibles: dejar en la vista general sólo sitios y enlaces, sin rótulos de equipos. |
| **7.4** Calendario de implantación (S7) | `subdoc07/subdocumento/figuras/fig-7-4-calendario-implantacion-dos-etapas-meses.png` | ~6,7 pt | Página horizontal o partir por etapa. |
| **6.7** Equipos de desarrollo y módulos (S6) | `subdoc06/subdocumento/figuras/fig-6-7-equipos-desarrollo-modulos-construyen.png` | ~7,7 pt | Agrandar al ancho de la página y subir la letra. |
| **1.1** Estructura organizacional (S1) | ver A | ~8,7 pt | Junto con el cambio de cifras. |
| **6.9** Flujo desde el cambio de código (S6) | `subdoc06/subdocumento/figuras/fig-6-9-flujo-trabajo-desde-cambio-codigo.png` | ~8,7 pt | Subir 1 pt la letra en el origen. |
| **9.3** Niveles y tipos de prueba (S9) | `subdoc09/subdocumento/figuras/fig-9-3-niveles-tipos-prueba-segun-ambiente.png` | ~8,7 pt | Subir 1 pt la letra en el origen. |
| **4.36** Recuperación en Brazil South (S4) | `subdoc04/subdocumento/figuras/drawio/fig-4-36-recuperacion-brazil-south.drawio.xml` | ~8,9 pt | Subir 1 pt la letra en el origen. |

## C. En el límite (9,0 a 9,3 pt): confirmar en el origen

| Figura | Documento | Letra hoy |
|---|---|---|
| 4.1 Vista general en ocho capas | S4 | ~9,1 pt |
| 4.16 Parte 1 del recorrido | S4 | ~9,1 pt |
| 4.26 y 4.27 Nube principal | S4 | ~9,1 pt (ver también A) |
| 6.3 Tratamiento de una solicitud de cambio | S6 | ~9,1 pt |
| 6.11 Flujo de entrega continua | S6 | ~9,1 pt |
| A.1 Recorrido del control del arsénico | S13-Anexos | ~9,1 pt |

---

## Ya resuelto (no requiere cambio)

- **5.17** Ventanas de corte de la migración (S5): ya ubica la digitalización en los meses 10 a 15, igual que el texto y el paquete 1.4.6.3 del T-14.
- **2.1** Faena (S2): se corrigió la leyenda a «Faena de Aranda en Sierra Gorda, Región de Antofagasta». La imagen no lleva el nombre equivocado. El profesor observa además que las Figuras 2.1 a 2.3 son renders sobre capturas satelitales que no aportan al problema: reemplazarlas es opcional.
- **6.10** Integración continua (S6): ya dice OpenTofu.

Al corregir una figura, volver a medir con `medir_figuras.py`, marcarla aquí y en [Pendientes_Revision_Profesor_Informe2.md](Pendientes_Revision_Profesor_Informe2.md).
