# Guía rápida: propuesta OVERFORE en LaTeX

## 1. Qué descargar (una sola vez)

| Programa | Para qué | Dónde |
|---|---|---|
| **MiKTeX** | Compila LaTeX | https://miktex.org/download (o `winget install MiKTeX.MiKTeX`) |
| **Python 3** | Corre `compilar.py` y las reglas | https://www.python.org/downloads (marcar *Add python to PATH*) |
| **VS Code** | Editor | https://code.visualstudio.com |
| Extensión **LaTeX Workshop** | Compilar y ver el PDF dentro de VS Code | VS Code → Extensiones → «LaTeX Workshop» |
| Extensión **Live Share** (opcional) | Editar entre varios | VS Code → Extensiones → «Live Share» |

Después de instalar MiKTeX, una vez:

```bash
initexmf --set-config-value "[MPM]AutoInstall=1"
```

Así MiKTeX baja solo los paquetes que falten (las fuentes Montserrat y Open Sans,
entre otros). La primera compilación tarda unos minutos por eso; las siguientes no.

No hay que instalar nada más: `compilar.py` y las reglas sólo usan Python estándar.

## 2. Paso a paso

1. **Abrir** la carpeta `latex` en VS Code (*Archivo → Abrir carpeta*). Tiene que ser
   esa carpeta, no la de arriba, para que VS Code tome las recetas de OVERFORE.
2. **Abrir** el documento, por ejemplo `subdoc04/subdocumento/OVERFORE-Subdocumento4.tex`.
3. **Escribir y guardar** (`Ctrl+S`). Al guardar:
   - se revisan las reglas;
   - si no hay errores, compila y actualiza índice y listados;
   - si hay errores, **no compila** y muestra la lista.
4. **Ver el PDF:** `Ctrl+Alt+V` (o el ícono de vista previa arriba a la derecha).
5. **Ver los errores:** pestaña *Salida* → *LaTeX Workshop*. Cada línea dice archivo,
   línea, regla y qué hacer, por ejemplo:
   `subdoc02\subdocumento\OVERFORE-Subdocumento2.tex:60: ERROR [sin-cita] La figura «Oficina corporativa en Santiago.» no se cita en el texto antes de aparecer`
6. **Ver cómo queda aunque haya errores:** `Ctrl+Shift+P` → *LaTeX Workshop: Build with
   recipe* → *OVERFORE borrador (compila aunque haya errores)*. Cada página sale
   marcada **BORRADOR · NO ENTREGAR**.
7. **Compilar todo para entregar** (folio continuo entre los 31 archivos), en la
   terminal de VS Code (`Ctrl+ñ`):

   ```bash
   python compilar.py
   ```

   Tarda unos 45 minutos. Los PDF quedan en `salida/` con su nombre oficial, listos
   para el ZIP. Si hay un solo error de reglas en cualquier documento, no compila.

## 3. Comandos

| Comando | Qué hace |
|---|---|
| `python compilar.py` | Todo, con folio continuo → `salida/` |
| `python compilar.py ruta/doc.tex` | Un documento (lo mismo que guardar en VS Code) |
| `python compilar.py --reglas` | Sólo revisa las reglas de los 31 documentos, sin compilar |
| `python compilar.py --borrador` | Todo, aunque haya errores → `salida-borrador/` (marca BORRADOR) |
| `python compilar.py --borrador ruta/doc.tex` | Un documento en borrador |

## 4. Cómo se escribe

```latex
\seccion{Arquitectura lógica}
La Tabla~\ref{tab:capas} resume las capas de la solución.

\begin{tabla}{I{0.3}I{0.5}D{0.2}}{Capas de la solución.}{tab:capas}
  {\cab{Capa} & \cab{Función} & \cab{Componentes}}
  {Fuente: elaboración propia.}
Presentación & Canales de uso & 6 \\
Integración & Bus de eventos & 4 \\
\end{tabla}
De la tabla se desprende que la integración concentra...

\figura{15}{fig-4-1-vista-general}{Vista general.}{fig:vista}{Fuente: elaboración propia.}
```

- Títulos: `\capitulo{}` (subdoc), `\anexo{}` (anexo), `\apartado{}` (formulario);
  luego `\seccion{}`, `\subseccion{}`, `\subsubseccion{}`. Los números los pone la clase.
- Columnas de tabla: `I{f}` izquierda, `C{f}` centro, `D{f}` derecha; `f` es la fracción del ancho.
- Las imágenes van en la carpeta `figuras/` del mismo documento.
- Celda sin dato: `—` o `No aplica`. Nunca vacía.
- Cursiva: `\emph{...}`. Negrita, colores, tamaños y tipos de letra **no** (los pone la clase).

## 5. Reglas

**No compila si:**

- la primera línea no es `\documentclass[subdoc|anexo|formulario]{../../comun/overfore}`;
- se usa formato propio (`\textbf`, `\color`, `\large`, `\underline`, `\texttt`…);
- quedan marcadores: `[Título]`, `[XX]`, «INSERTAR», «borrador»;
- aparece «OVERFORE» en mayúsculas en el texto (se escribe «Overfore»), la universidad o el
  curso, «Terraform» (es OpenTofu), «con apoyo de Claude» o un nombre de archivo `.md`;
- hay una celda vacía;
- en el **subdoc**:
  - un título va seguido de una tabla, una figura u otro título;
  - una tabla tiene más de 5 columnas o mide más de una página;
  - una celda tiene más de una frase;
  - una tabla o figura no tiene título o fuente, no se cita con `\ref` antes de aparecer,
    o no tiene texto que la explique después;
  - falta un título del índice obligatorio, está renombrado, en otro orden o nivel,
    o se agregó uno del mismo nivel (por ejemplo, un 2.6).

**Sólo avisa (compila igual):** tabla con forma «Concepto / Descripción» y capítulo
técnico sin figuras.

El detalle está en `LEEME.md` y en `comun/reglas.py`.

## 6. Live Share

El anfitrión (quien comparte) necesita todo lo de la sección 1 y es quien compila.
Los invitados sólo necesitan VS Code con Live Share: editan y ven el PDF del anfitrión.
