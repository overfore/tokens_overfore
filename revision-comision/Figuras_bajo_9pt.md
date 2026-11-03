# Figuras con letra bajo 9 pt

Medición del 22-10-2026 sobre los PDF de `latex/salida/` (folios 1 a 1289), con `main` en `b6d2c0e`. La letra es el tamaño aproximado del texto más chico de cada figura, medido tal como se imprime en la página. Mínimo exigido: 9 pt (Art. 40.4 de las Bases administrativas y Comunicado 10, §4).

De las 67 figuras de la primera medición, 46 ya cumplen y quedan 21.

«En draw.io» indica si la figura está en el draw.io del equipo y en qué pestaña. Se buscó separando las pestañas con varios diagramas y comparando cada figura con el diagrama, por su texto y a la vista.

- Las pestañas marcadas «versión anterior» tienen el mismo contenido que la figura del informe; la marca venía de una comparación que fallaba porque draw.io no tiene instalada la letra Open Sans y dibuja con otra.
- Las del S5 y la 5.17 usan Open Sans: para exportarlas igual que en el informe hay que instalar esa letra.
- La 6.7 está en draw.io con otro orden de cajas y «51 funcionales» en vez de 52: es una versión distinta de la del informe.
- 1.1, 7.3, 7.4 y 9.3 no están en el draw.io ni en el repositorio.

## Pendientes

| Doc | Figura | Folio | Letra (pt) | En draw.io |
|---|---|---|---|---|
| S1 | 1.1 | 6 | 8,5 | No |
| S4 | 4.6 | 427 | 5,4 | Sí, igual al informe |
| S4 | 4.7 | 428 | 5,0 | Sí |
| S4 | 4.8 | 429 | 4,2 | Sí |
| S4 | 4.9 | 430 | 5,0 | Sí |
| S4 | 4.10 | 433 | 6,2 | Sí |
| S4 | 4.11 | 435 | 6,2 | Sí |
| S4 | 4.12 | 436 | 5,0 | Sí |
| S4 | 4.14 | 442 | 4,2 | Sí |
| S4 | 4.15 | 443 | 4,2 | Sí |
| S4 | 4.21 | 457 | 5,4 | Sí |
| S4 | 4.22 | 459 | 5,4 | Sí |
| S4 | 4.23 | 467 | 4,6 | Sí |
| S4 | 4.24 | 468 | 4,6 | Sí |
| S4 | 4.31 | 487 | 5,4 | Sí, igual al informe |

Las 14 del S4 con «Sí» dicen lo mismo que su pestaña del draw.io, pero no basta con subir la letra: al llevarlas a 9 pt el texto se monta, porque están entre 4,2 y 6,2 pt. Hay que reacomodarlas una por una y, las más densas, partirlas en vista general y partes (Comunicado 10, §4).
| S4 | 4.32 | 488 | 8,8 | Sí, en el repositorio |
| S4 | 4.36 | 504 | 8,8 | Sí, en el repositorio |
| S6 | 6.7 | 784 | 7,7 | Versión distinta, dentro de «Sin uso — Subdoc06 - varios» |
| S7 | 7.3 | 838 | 5,4 | No |
| S7 | 7.4 | 840 | 6,5 | No |
| S9 | 9.3 | 1134 | 8,5 | No |

## Ya cumplen

| Doc | Figuras | Quién |
|---|---|---|
| T-14 | C.1 a C.18 | Kavon (commit `4e345cb`) |
| S3 | 3.3, 3.4, 3.5, 3.7, 3.8 y 3.9 | commit `63a5678` |
| S1, S5, S6, S7, S8 | 1.2, 5.1, 5.5, 5.6, 5.8, 5.11, 5.12, 5.13, 5.14, 5.17, 6.2, 7.1 y 8.3 | commit `b6d2c0e` |
| S4 | 4.1, 4.16, 4.19, 4.26, 4.27, 4.28, 4.33, 4.34 y 4.35 | Kavon (commit `4e345cb`) |

## Resumen

| Doc | Antes | Ahora |
|---|---|---|
| T-14 | 18 | 0 |
| S1 | 2 | 1 |
| S3 | 6 | 0 |
| S4 | 25 | 16 |
| S5 | 9 | 0 |
| S6 | 2 | 1 |
| S7 | 3 | 2 |
| S8 | 1 | 0 |
| S9 | 1 | 1 |
| **Total** | **67** | **21** |
