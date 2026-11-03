%% overfore.cls — Formato único de OVERFORE S.A. · Licitación TFEP-01/2026
%%
%% Tres modos, y sólo tres:
%%   \documentclass[subdoc]{../../comun/overfore}
%%   \documentclass[anexo]{../../comun/overfore}
%%   \documentclass[formulario]{../../comun/overfore}
%%
%% Reglas que impiden compilar:
%%   1. No indicar un modo, o indicar uno distinto de subdoc, anexo o formulario.
%%      (Que el documento use esta clase y no otra lo verifica compilar.py.)
%%   2. Dar formato propio dentro del documento: colores, tamaños o tipos de
%%      letra, negritas o subrayado. Ese formato lo pone sólo esta clase.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{overfore}[2026/10/20 v1.0 Formato OVERFORE S.A.]

% ======================================================================= modos
\newif\ifov@subdoc \newif\ifov@anexo \newif\ifov@formulario
\newcount\ov@nmodos
\DeclareOption{subdoc}{\ov@subdoctrue\advance\ov@nmodos\@ne}
\DeclareOption{anexo}{\ov@anexotrue\advance\ov@nmodos\@ne}
\DeclareOption{formulario}{\ov@formulariotrue\advance\ov@nmodos\@ne}
\DeclareOption*{\ClassError{overfore}{Modo no permitido: '\CurrentOption'}%
  {Los unicos formatos permitidos son subdoc, anexo y formulario.}}
\ProcessOptions\relax
\ifnum\ov@nmodos=\@ne\else
  \ClassError{overfore}{Indique exactamente un modo: subdoc, anexo o formulario}%
  {Ejemplo: \string\documentclass[anexo]{../../comun/overfore}}
\fi

\LoadClass[11pt,letterpaper]{article}

% Borrador (python compilar.py --borrador): los errores pasan a avisos y cada página
% lleva la marca BORRADOR. Sirve sólo para revisar cómo queda; no se entrega.
\newif\ifov@borrador
\ifdefined\ovborrador\ov@borradortrue\fi

% ======================================================================= paquetes
\def\ov@comun{../../comun/}
\RequirePackage[spanish,es-noshorthands,es-nolists,es-tabla,es-noindentfirst]{babel}
\RequirePackage{amsmath}
\RequirePackage{fontspec}
\RequirePackage[table]{xcolor}
\RequirePackage{graphicx}
\graphicspath{{figuras/}{\ov@comun imagenes/}}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage{titletoc}
\RequirePackage{caption}
\RequirePackage{array,longtable,multirow,calc}
\RequirePackage{needspace}
\RequirePackage{environ}
\RequirePackage{enumitem}
\RequirePackage{ragged2e}
\RequirePackage{tikz}
\RequirePackage{xr}
\RequirePackage[hidelinks,bookmarksnumbered,unicode]{hyperref}
\urlstyle{same}

% ======================================================================= colores
\definecolor{ovnavy}{HTML}{071A34}
\definecolor{ovprofundo}{HTML}{0F2C52}
\definecolor{ovazul}{HTML}{0A7CFC}
\definecolor{ovcian}{HTML}{03CEFC}
\definecolor{ovtexto}{HTML}{1F2733}
\definecolor{ovgris}{HTML}{5B6676}
\definecolor{ovgris2}{HTML}{5A6B80}
\definecolor{ovlinea}{HTML}{D5DCE5}
\definecolor{ovcebra}{HTML}{F3F6FA}

% ======================================================================= fuentes
\setmainfont{OpenSans}[Extension=.ttf,UprightFont=*-Regular,BoldFont=*-Bold,
  ItalicFont=*-Italic,BoldItalicFont=*-BoldItalic]
% caracteres que Open Sans o Montserrat no tienen: se dibujan con la fuente matemática
\RequirePackage{newunicodechar}
\newunicodechar{→}{\ensuremath{\rightarrow}}
\newunicodechar{←}{\ensuremath{\leftarrow}}
\newunicodechar{↔}{\ensuremath{\leftrightarrow}}
\newunicodechar{σ}{\ensuremath{\sigma}}
\newunicodechar{μ}{\ensuremath{\mu}}
\newunicodechar{Σ}{\ensuremath{\Sigma}}
% los subíndices los compone la clase (\textsubscript usa \fontsize, que está bloqueado)
\newcommand\ov@sub[1]{{\ov@internotrue\textsubscript{#1}}}
\newunicodechar{₀}{\ov@sub{0}}\newunicodechar{₁}{\ov@sub{1}}
\newunicodechar{₂}{\ov@sub{2}}\newunicodechar{₃}{\ov@sub{3}}
\newunicodechar{₄}{\ov@sub{4}}\newunicodechar{ₚ}{\ov@sub{p}}
\newunicodechar{≈}{\ensuremath{\approx}}
\newunicodechar{≤}{\ensuremath{\leq}}
\newunicodechar{≥}{\ensuremath{\geq}}
\newunicodechar{✓}{\ensuremath{\checkmark}}
\newfontfamily\ov@mont{Montserrat}[Extension=.otf,UprightFont=*-Regular,
  BoldFont=*-Bold,ItalicFont=*-Italic,BoldItalicFont=*-BoldItalic]

% copias privadas de los comandos de formato: sólo la clase las usa
\let\ov@bfseries\bfseries
\let\ov@color\color
\let\ov@rowcolor\rowcolor
\let\ov@arrayrulecolor\arrayrulecolor
\let\ov@fontsize\fontsize
\def\@setfontsize#1#2#3{\@nomath#1\ifx\protect\@typeset@protect\let\@currsize#1\fi
  \ov@fontsize{#2}{#3}\selectfont}
\newcommand\ov@pt[2]{\ov@fontsize{#1}{#2}\selectfont}
\newcommand\ov@negrita{\ov@bfseries}
% el sombreado de filas de colortbl usa la copia privada del color
\def\CT@setup{\@tempdimb\col@sep\@tempdimc\col@sep
  \def\CT@color{\global\let\CT@do@color\CT@@do@color\ov@color}}
% cuerpo de 11 pt, interlineado 1,15
\renewcommand\normalsize{\@setfontsize\normalsize{11pt}{16.5pt}%
  \abovedisplayskip 8pt \belowdisplayskip 8pt
  \abovedisplayshortskip 4pt \belowdisplayshortskip 4pt}
\normalsize

% ======================================================================= página
\geometry{letterpaper,top=2.6cm,bottom=3.7cm,left=3cm,right=2.5cm,
  headheight=0.9cm,headsep=0.5cm,footskip=2.6cm}
\setlength\parindent{0pt}
\setlength\parskip{6pt plus 2pt}
\setlength\emergencystretch{3em}
\raggedbottom
\widowpenalty=10000 \clubpenalty=10000
\AtBeginDocument{\ov@color{ovtexto}}

% ======================================================================= datos
\def\ov@licitacion{Licitación TFEP-01/2026}
\def\ov@caso{Caso 01 Minería}
\newcommand\numsubdoc[1]{\def\ov@numsubdoc{#1}}
\newcommand\nombresubdoc[1]{\def\ov@nombresubdoc{#1}}
\newcommand\formulario[2]{\def\ov@numform{#1}\def\ov@nombreform{#2}}
\newcommand\informe[1]{\def\ov@informe{#1}}
\newcommand\fecha[1]{\def\ov@fecha{#1}}
\newcommand\lugar[1]{\def\ov@lugar{#1}}
\numsubdoc{N}\nombresubdoc{[Nombre del subdocumento]}
\formulario{T-[XX]}{[Nombre oficial del formulario]}
\informe{Informe Preparatorio N° n}\fecha{[día] de [mes] de 2026}\lugar{Valparaíso}
\newcommand\ov@iddoc{%
  \ifov@subdoc Subdocumento~\ov@numsubdoc\fi
  \ifov@anexo Anexos del Subdocumento~\ov@numsubdoc\fi
  \ifov@formulario Formulario~\ov@numform\fi}

% ======================================================================= referencias entre documentos
% comun/documentos.tex asocia una clave (S4, A4, T14...) a la ruta de cada documento.
% Se lee la copia <archivo>-ref.aux que deja compilar.py, no el .aux en uso.
\newcommand\ovdoc[2]{\expandafter\def\csname ov@ruta@#1\endcsname{#2}}
\InputIfFileExists{\ov@comun documentos.tex}{}{}
\newcommand\externos[1]{\@for\ov@x:=#1\do{%
  \ifcsname ov@ruta@\ov@x\endcsname
    \edef\ov@tmp{\noexpand\externaldocument[\ov@x-]{\ov@comun../\csname ov@ruta@\ov@x\endcsname-ref}}%
    \ov@tmp
  \else\ClassWarning{overfore}{Documento externo desconocido: \ov@x}\fi}}
\newcommand\refext[2]{{\ov@internotrue\ref*{#1-#2}}}

% ======================================================================= folio continuo
% compilar.py escribe comun/folios.tex con \folioinicial{<archivo>}{<primer folio>}
\newcommand\folioinicial[2]{\expandafter\def\csname ov@folio@#1\endcsname{#2}}
\InputIfFileExists{\ov@comun folios.tex}{}{}
\AtBeginDocument{\ifcsname ov@folio@\jobname\endcsname
    \setcounter{page}{\csname ov@folio@\jobname\endcsname}\fi}

% ======================================================================= encabezado y pie
\newcommand\ov@encabezado{{\ov@internotrue\ov@mont\ov@pt{9pt}{11pt}\ov@color{ovgris2}%
  OVERFORE S.A. · \ov@licitacion\ · \ov@caso\ · {\ov@negrita\ov@color{ovprofundo}\ov@iddoc}}}
\newcommand\ov@pie{{\ov@internotrue
  \begin{minipage}[b]{6.4cm}\raggedleft
    {\centering\includegraphics[height=1.25cm]{firma-recorte}\par}\vspace{-0.3cm}%
    {\ov@color{ovlinea}\rule{6.4cm}{0.5pt}}\par\vspace{1pt}%
    {\ov@pt{9pt}{11pt}\ov@color{ovgris2}Media firma · Representante Legal}\par\vspace{1pt}%
    {\ov@pt{9pt}{11pt}\ov@negrita\ov@color{ovnavy}Folio \thepage}%
  \end{minipage}}}
\fancypagestyle{overfore}{%
  \fancyhf{}%
  \fancyhead[L]{\ov@encabezado}%
  \fancyhead[R]{\raisebox{-0.12cm}{\includegraphics[height=0.72cm]{isotipo}}}%
  \fancyfoot[R]{\ov@pie}%
  \renewcommand\headrule{{\ov@color{ovlinea}\hrule height 0.5pt width\headwidth}}%
  \renewcommand\footrulewidth{0pt}}
\fancypagestyle{ovportada}{\fancyhf{}\fancyfoot[R]{\ov@pie}%
  \renewcommand\headrule{}\renewcommand\footrulewidth{0pt}}
\pagestyle{overfore}

% ======================================================================= títulos
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{3}
\ifov@subdoc
  \renewcommand\thesection{\ov@numsubdoc}
  \def\ov@etiq{Capítulo~\thesection\ ·}\def\ov@etiqtoc{Capítulo~\thecontentslabel\ ·\ }
\fi
\ifov@anexo
  \renewcommand\thesection{\Alph{section}}
  \def\ov@etiq{Anexo~\thesection\ —}\def\ov@etiqtoc{Anexo~\thecontentslabel\ —\ }
\fi
\ifov@formulario
  \renewcommand\thesection{\Alph{section}}
  \def\ov@etiq{\thesection.}\def\ov@etiqtoc{\thecontentslabel.\ }
\fi
\renewcommand\thesubsection{\thesection.\arabic{subsection}}
\renewcommand\thesubsubsection{\thesubsection.\arabic{subsubsection}}
\renewcommand\theparagraph{\thesubsubsection.\arabic{paragraph}}

\titleformat{\section}[block]{\ov@mont\ov@negrita\ov@pt{18pt}{22pt}\ov@color{ovnavy}\raggedright\hyphenpenalty=10000}
  {{\ov@color{ovcian}\ov@etiq}}{0.35em}{}[{\vspace{6pt}\ov@color{ovcian}\titlerule[1pt]}]
\titleformat{name=\section,numberless}[block]{\ov@mont\ov@negrita\ov@pt{18pt}{22pt}\ov@color{ovnavy}\raggedright}
  {}{0pt}{}[{\vspace{6pt}\ov@color{ovcian}\titlerule[1pt]}]
\titlespacing*{\section}{0pt}{0pt}{14pt}
\newcommand\sectionbreak{\clearpage}
\titleformat{\subsection}[hang]{\ov@mont\ov@negrita\ov@pt{14pt}{18pt}\ov@color{ovprofundo}\raggedright\hyphenpenalty=10000}
  {{\ov@color{ovcian}\thesubsection}}{0.6em}{}
\titlespacing*{\subsection}{0pt}{16pt}{6pt}
\titleformat{\subsubsection}[hang]{\ov@mont\ov@negrita\ov@pt{11.5pt}{15pt}\ov@color{ovazul}\raggedright}
  {\thesubsubsection}{0.6em}{}
\titlespacing*{\subsubsection}{0pt}{12pt}{5pt}
\titleformat{\paragraph}[hang]{\ov@mont\ov@negrita\ov@pt{11pt}{14pt}\ov@color{ovprofundo}\raggedright}
  {\theparagraph}{0.6em}{}
\titlespacing*{\paragraph}{0pt}{10pt}{4pt}

\newcommand\ov@solo[2]{\csname ifov@#1\endcsname\else
  \ClassError{overfore}{\string#2 no corresponde a este formato}%
  {Titulos de primer nivel: \string\capitulo\space(subdoc), \string\anexo\space(anexo), \string\apartado\space(formulario).}\fi}
\newcommand\capitulo{\ov@solo{subdoc}\capitulo\section}
\newcommand\anexo{\ov@solo{anexo}\anexo\section}
\newcommand\apartado{\ov@solo{formulario}\apartado\section}
\newcommand\seccion{\subsection}
\newcommand\subseccion{\subsubsection}
\newcommand\subsubseccion{\paragraph}
\newif\ifov@enIA
\newcommand\ov@textoIA{Declaración de uso de IA}
\newcommand\seccionsinnumero[1]{\def\ov@tmp{#1}\ifx\ov@tmp\ov@textoIA\global\ov@enIAtrue\else\global\ov@enIAfalse\fi
  \section*{#1}\phantomsection\addcontentsline{toc}{section}{#1}}

% ======================================================================= índice y listados
\newcommand\ov@puntos{\titlerule*[0.6pc]{.}}
\titlecontents{section}[0pt]{\addvspace{7pt}\ov@mont\ov@negrita\ov@pt{10pt}{13pt}\ov@color{ovnavy}}
  {\ov@etiqtoc}{}{\ov@puntos\contentspage}
\titlecontents{subsection}[1.2em]{\addvspace{1pt}\ov@mont\ov@pt{10pt}{13pt}\ov@color{ovtexto}}
  {\thecontentslabel\quad}{}{\ov@puntos\contentspage}
\titlecontents{subsubsection}[2.4em]{\ov@mont\ov@pt{9.5pt}{12pt}\ov@color{ovtexto}}
  {\thecontentslabel\quad}{}{\ov@puntos\contentspage}
\titlecontents{paragraph}[3.6em]{\ov@mont\ov@pt{9.5pt}{12pt}\ov@color{ovtexto}}
  {\thecontentslabel\quad}{}{\ov@puntos\contentspage}
\titlecontents{table}[0pt]{\addvspace{3pt}\ov@mont\ov@pt{9.5pt}{12.5pt}\ov@color{ovtexto}}
  {{\ov@negrita Tabla~\thecontentslabel}\ —\ }{}{\ov@puntos\contentspage}
\titlecontents{figure}[0pt]{\addvspace{3pt}\ov@mont\ov@pt{9.5pt}{12.5pt}\ov@color{ovtexto}}
  {{\ov@negrita Figura~\thecontentslabel}\ —\ }{}{\ov@puntos\contentspage}

\newcommand\ov@titulolista[2][0pt]{\par\vspace*{#1}%
  {\ov@mont\ov@negrita\ov@pt{18pt}{22pt}\ov@color{ovnavy}#2\par}%
  \vspace{3pt}{\ov@color{ovcian}\hrule height 0.8pt}\vspace{8pt}}
\newcounter{ov@ntab}\newcounter{ov@nfig}
\def\ov@totaltab{1}\def\ov@totalfig{1}
\AtEndDocument{\immediate\write\@auxout{%
  \gdef\string\ov@totaltab{\the\value{ov@ntab}}\gdef\string\ov@totalfig{\the\value{ov@nfig}}}}
\newcommand\ov@indices{{\ov@internotrue
  \clearpage
  \ov@titulolista{Índice}%
  Cada entrada está hipervinculada a su título. El folio indicado corresponde al número impreso en el pie de la página de destino.\par
  \vspace{4pt}\@starttoc{toc}%
  % los listados siguen al índice en la misma página si caben (no empiezan página nueva),
  % y se omiten cuando el documento no tiene tablas o figuras
  \ifnum\ov@totaltab>0
    \par\addvspace{18pt}\needspace{6\baselineskip}%
    \ov@titulolista{Listado de Tablas}\@starttoc{lot}\fi
  \ifnum\ov@totalfig>0
    \par\addvspace{18pt}\needspace{6\baselineskip}%
    \ov@titulolista{Listado de Figuras}\@starttoc{lof}\fi
  \clearpage}}

% ======================================================================= títulos de tabla y figura
\counterwithin*{table}{section}\counterwithin*{figure}{section}
\ifov@subdoc
  \renewcommand\thetable{\ov@numsubdoc.\arabic{table}}
  \renewcommand\thefigure{\ov@numsubdoc.\arabic{figure}}
\else
  \renewcommand\thetable{\ifnum\value{section}>0 \thesection.\fi\arabic{table}}
  \renewcommand\thefigure{\ifnum\value{section}>0 \thesection.\fi\arabic{figure}}
\fi
\addto\captionsspanish{\renewcommand\tablename{Tabla}\renewcommand\figurename{Figura}}
\DeclareCaptionFont{ovetiqueta}{\ov@mont\ov@negrita\ov@color{ovazul}}
\DeclareCaptionFont{ovtexto}{\normalfont\ov@color{ovtexto}}
\DeclareCaptionFont{ovnueve}{\ov@pt{9pt}{12pt}}
\DeclareCaptionLabelSeparator{ovguion}{{\normalfont\ov@color{ovtexto}\ —\ }}
\captionsetup{font=ovnueve,labelfont=ovetiqueta,textfont=ovtexto,labelsep=ovguion,skip=5pt}
\captionsetup[table]{justification=raggedright,singlelinecheck=false,position=top}
\captionsetup[figure]{justification=centering,position=bottom}

\newcommand\fuente[1]{\par{\centering\ov@pt{9pt}{12pt}\ov@color{ovgris}#1\par}\addvspace{4pt}}
\newcommand\nota[1]{\par{\raggedright\ov@pt{9pt}{12pt}\ov@color{ovgris}#1\par}}

% ======================================================================= tablas
% \begin{tabla}{columnas}{título}{etiqueta}{encabezado}{fuente}  filas  \end{tabla}
% Columnas: I{f} izquierda, C{f} centro, D{f} derecha (f = fracción del ancho útil).
% El encabezado se repite en cada página y ninguna fila se corta entre páginas.
\newcolumntype{I}[1]{>{\RaggedRight\arraybackslash}m{\dimexpr#1\linewidth-2\tabcolsep\relax}}
\newcolumntype{C}[1]{>{\Centering\arraybackslash}m{\dimexpr#1\linewidth-2\tabcolsep\relax}}
\newcolumntype{D}[1]{>{\RaggedLeft\arraybackslash}m{\dimexpr#1\linewidth-2\tabcolsep\relax}}
\newcommand\cab[1]{\leavevmode{\ov@internotrue\ov@mont\ov@negrita\ov@color{white}#1}}
\newcommand\ov@prepararTabla{\ov@pt{9pt}{12pt}%
  \setlength\tabcolsep{5pt}\renewcommand\arraystretch{1.3}%
  \setlength\LTpre{2pt}\setlength\LTleft{0pt}\setlength\LTright{0pt}%
  \def\CT@arc@{\ov@color{ovlinea}}\setlength\arrayrulewidth{0.5pt}%
  \rowcolors{2}{white}{ovcebra}}
% En anexos y formularios (y en la Declaración de uso de IA) la tabla puede seguir en
% la página siguiente. En el subdocumento es un bloque que no se corta: si no cabe en lo
% que queda de la página pasa entera a la siguiente, y si mide más de una página no compila.
\newsavebox\ov@tabcaja
\NewEnviron{tabla}[5]{%
  \par\addvspace{4pt}\stepcounter{ov@ntab}%
  \begingroup\ov@prepararTabla
  \ifov@subdoc\ifov@enIA\def\ov@modo{L}\else\def\ov@modo{C}\fi\else\def\ov@modo{L}\fi
  \if L\ov@modo
    \setlength\LTpost{0pt}%
    \begin{longtable}{#1}
    \caption{#2}\label{#3}\\[-1pt]
    \ov@rowcolor{ovnavy}#4\\*
    \endfirsthead
    \ov@rowcolor{ovnavy}#4\\*
    \endhead
    \hline
    \endfoot
    % la fuente va dentro del pie final: queda en la página de la última fila, nunca sola
    \hline
    \noalign{\vskip 6pt\hbox to\linewidth{\parbox{\linewidth}{\centering
      \ov@pt{9pt}{12pt}\ov@color{ovgris}#5}}\vskip 4pt}%
    \endlastfoot
    \BODY
    \end{longtable}%
  \else
    \sbox\ov@tabcaja{\begin{minipage}{\linewidth}%
      \captionof{table}{#2}\label{#3}\par\vspace{1pt}%
      \begin{tabular}{#1}
      \ov@rowcolor{ovnavy}#4\\
      \BODY
      \hline
      \end{tabular}\end{minipage}}%
    \ifdim\dimexpr\ht\ov@tabcaja+\dp\ov@tabcaja\relax>\textheight
      \ifov@borrador\ClassWarning{overfore}{BORRADOR: la tabla "#2" no cabe en una pagina}\else
      \ClassError{overfore}{La tabla "#2" no cabe en una pagina}%
        {En el subdocumento una tabla no se extiende mas de una pagina: deje el listado completo en el anexo y aqui una tabla de sintesis.}%
      \fi
    \fi
    \noindent\usebox\ov@tabcaja\par
    \vspace{-2pt}\fuente{#5}%
  \fi
  \endgroup\par}
\newcommand\ov@finTabla[3]{}
% tabla sin número (cartas y fichas que no llevaban título en el original)
\newenvironment{tablasintitulo}[2]{%
  \par\addvspace{4pt}\begingroup\ov@prepararTabla\setlength\LTpost{6pt}%
  \begin{longtable}{#1}
  \ifx\relax#2\relax\else\ov@rowcolor{ovnavy}#2\\* \endhead\fi}
 {\end{longtable}\endgroup}

% ======================================================================= figuras
% \figura{ancho en cm}{archivo}{título}{etiqueta}{fuente}
\newlength\ov@anchofig
% alto máximo de una figura: 70 % del alto útil; en página horizontal, 82 % (la figura
% ocupa la hoja y aún caben su título y su fuente)
\newcommand\ov@altofig{0.7}
\newcommand\ov@incluir[2]{\setlength\ov@anchofig{#1cm}%
  \ifdim\ov@anchofig>\linewidth\setlength\ov@anchofig{\linewidth}\fi
  \includegraphics[width=\ov@anchofig,height=\ov@altofig\textheight,keepaspectratio]{#2}}
\newcommand\figura[5]{\par\addvspace{6pt}\stepcounter{ov@nfig}%
  \noindent\begin{minipage}{\linewidth}\centering
    \ov@incluir{#1}{#2}\par
    \captionof{figure}{#3}\label{#4}\par
    \fuente{#5}%
  \end{minipage}\par\addvspace{4pt}}
\newcommand\imagen[2]{\par{\centering\ov@incluir{#1}{#2}\par}}

% ======================================================================= listas y referencias
\setlist{itemsep=2pt,topsep=2pt,parsep=0pt,leftmargin=1.4em}
\setlist[itemize,1]{label={{\ov@color{ovazul}\textbullet}}}
\setlist[itemize,2]{label={{\ov@color{ovazul}–}}}
\setlist[enumerate,1]{label=\arabic*.}
\setlist[enumerate,2]{label=\alph*)}
\newenvironment{referencias}{\par\begin{list}{}{\setlength\leftmargin{1.27cm}%
  \setlength\itemindent{-1.27cm}\setlength\itemsep{5pt}\setlength\parsep{0pt}%
  \setlength\topsep{2pt}}\RaggedRight}{\end{list}}

% ======================================================================= páginas horizontales
\newenvironment{horizontal}{%
  % hoja carta apaisada con los mismos márgenes: el texto, las tablas, el encabezado y el pie
  % usan todo el ancho de la página horizontal
  \clearpage
  \ov@hoja{279.4mm}{215.9mm}\def\ov@altofig{0.82}}
 {\clearpage
  \ov@hoja{215.9mm}{279.4mm}}
\newcommand\ov@hoja[2]{%
  \global\pdfpagewidth=#1 \global\pdfpageheight=#2
  \global\paperwidth=#1 \global\paperheight=#2
  \global\textwidth=\dimexpr#1-3cm-2.5cm\relax
  \global\textheight=\dimexpr#2-2.6cm-3.7cm\relax
  \global\oddsidemargin=\dimexpr3cm-1in\relax \global\evensidemargin=\oddsidemargin
  \global\topmargin=\dimexpr2.6cm-1in-\headheight-\headsep\relax
  \global\hsize=\textwidth \global\linewidth=\textwidth \global\columnwidth=\textwidth
  \global\@colht=\textheight \global\@colroom=\textheight \global\vsize=\textheight
  \global\headwidth=\textwidth}

% ======================================================================= portada
\newcommand\ov@lineacaso{\begin{tabular}{@{}l@{}}
  \ov@mont\ov@negrita\ov@pt{9pt}{12pt}\ov@color{ovazul}LICITACIÓN N° TFEP-01/2026\\[1pt]
  \ov@mont\ov@negrita\ov@pt{9pt}{12pt}\ov@color{ovnavy}CASO 01 · MINERÍA\end{tabular}}
% bloque de firma: misma posición en todas las portadas (20 cm desde el borde superior)
\newcommand\ov@bloquefirma{%
  \begin{tikzpicture}
    \fill[ovcebra] (0,0) rectangle (16.1,2.5);
    \fill[ovnavy] (0,0) rectangle (0.13,2.5);
    \draw[ovlinea,line width=0.5pt] (5.8,0.2) -- (5.8,2.3);
    % firma centrada en su casilla (entre la barra y la línea divisoria)
    \node[anchor=center,inner sep=0] at (2.965,1.25) {\includegraphics[height=1.85cm]{firma-recorte}};
    \node[anchor=west,align=left,inner sep=0] at (6.4,1.25) {%
      {\ov@mont\ov@negrita\ov@pt{10.5pt}{14pt}\ov@color{ovnavy}CLAUDIO IGNACIO CABELLO VASQUEZ}\\[3pt]
      {\ov@mont\ov@pt{9pt}{12pt}\ov@color{ovgris}RUT Empresa: 77.482.961-K}\\
      {\ov@mont\ov@pt{9pt}{12pt}\ov@color{ovgris}RUT Representante: 21.491.020-9}\\
      {\ov@mont\ov@pt{9pt}{12pt}\ov@color{ovgris}OVERFORE S.A.}};
  \end{tikzpicture}}
\newcommand\ov@filadato[2]{\leavevmode{\ov@mont\ov@negrita\ov@pt{9pt}{12pt}\ov@color{ovgris}#1} &
  \leavevmode{\ov@pt{10pt}{13pt}#2}\\ \hline}
\newcommand\ov@tablainfo{{\def\CT@arc@{\ov@color{ovlinea}}\renewcommand\arraystretch{1.6}%
  \begin{tabular}{@{}p{3.6cm}p{12.1cm}@{}}
    \ov@filadato{PROPONENTE}{OVERFORE S.A. · Consultoría y Desarrollo de Sistemas}
    \ov@filadato{MANDANTE}{Compañía Minera Altos de Aranda}
    \ov@filadato{DOCUMENTO}{\ov@informe\ · SITCO Aranda}
    \ov@filadato{FECHA Y LUGAR}{\ov@fecha, \ov@lugar}
  \end{tabular}}}
% espacio entre palabras fijo (sin estirar ni encoger) en los títulos de portada
\newcommand\ov@espacio{\spaceskip=0.27em\relax\xspaceskip=0.3em\relax}
\newcommand\ov@marcoportada[2]{{\ov@internotrue\hyphenpenalty=10000\exhyphenpenalty=10000\thispagestyle{ovportada}%
  \begin{tikzpicture}[remember picture,overlay]
    \node[anchor=north west,inner sep=0] at ([xshift=3cm,yshift=-2.2cm]current page.north west)
      {\includegraphics[width=4.8cm]{logo}};
    #1
    #2
  \end{tikzpicture}\null\clearpage}}
% firma de portada de anexos y formularios: recuadro a 20 cm del borde superior
\newcommand\ov@firmarecuadro{\node[anchor=north west,inner sep=0] at ([xshift=3cm,yshift=-20cm]current page.north west)
      {\ov@bloquefirma};}
\newcommand\ov@portadaanexoform[2]{\ov@marcoportada{%
    \begin{scope}[shift={([xshift=3cm,yshift=-5.05cm]current page.north west)}]
      \fill[ovcian] (0,0) rectangle (3.06,0.18); \fill[ovazul] (3.06,0) rectangle (7.89,0.18);
      \fill[ovnavy] (7.89,0) rectangle (16.1,0.18);
      \fill[ovnavy] (0,-0.18) rectangle (3.06,0); \fill[ovcian] (3.06,-0.18) rectangle (7.89,0);
      \fill[ovazul] (7.89,-0.18) rectangle (16.1,0);
    \end{scope}
    \node[anchor=north west,inner sep=0,align=left] at ([xshift=3cm,yshift=-5.75cm]current page.north west)
      {\ov@lineacaso};
    \node[anchor=north west,inner sep=0,text width=16.1cm,align=left] at ([xshift=3cm,yshift=-7.2cm]current page.north west)
      {{\ov@mont\ov@negrita\ov@pt{27pt}{32pt}\ov@espacio\RaggedRight{\ov@color{ovnavy}#1}\\{\ov@color{ovazul}#2}\par}%
       \vspace{8pt}{\ov@color{ovcian}\hrule height 1pt}\vspace{14pt}\ov@tablainfo};}{\ov@firmarecuadro}}
\newcommand\ov@portadasubdoc{\ov@marcoportada{%
    \fill[ovcian] ([xshift=3cm,yshift=-6cm]current page.north west) rectangle ++(6.3,0.07);
    \node[anchor=north east,inner sep=0,opacity=0.6] at ([xshift=0.2cm,yshift=-11.5cm]current page.north east)
      {\includegraphics[width=6.5cm]{arco}};
    \node[anchor=north west,inner sep=0,align=left] at ([xshift=3cm,yshift=-6.45cm]current page.north west)
      {\ov@lineacaso};
    \node[anchor=north west,inner sep=0,text width=15.6cm,align=left,
          font={\ov@mont\ov@negrita\ov@pt{28pt}{36pt}\ov@espacio},text=ovnavy] at ([xshift=3cm,yshift=-8.1cm]current page.north west)
      {Sistema Integrado de Trazabilidad, Conciliación y Cumplimiento Operacional SITCO Aranda};
    \node[anchor=north west,inner sep=0,text width=15.6cm,align=left,
          font={\ov@mont\ov@pt{13pt}{22pt}},text=ovgris] at ([xshift=3cm,yshift=-14.7cm]current page.north west)
      {\ov@informe\ · Subdocumento~\ov@numsubdoc\\
       \ov@nombresubdoc\\
       Compañía Minera Altos de Aranda\\
       OVERFORE S.A. · Consultoría y Desarrollo de Sistemas};}%
  {% firma centrada sobre su línea y datos del representante, sin recuadro
    \draw[ovlinea,line width=0.6pt] ([xshift=3cm,yshift=-21.3cm]current page.north west) -- ++(7.4,0);
    \node[anchor=south,inner sep=0] at ([xshift=6.7cm,yshift=-21.45cm]current page.north west)
      {\includegraphics[height=2.3cm]{firma-recorte}};
    \node[anchor=north west,inner sep=0,align=left,
          font={\ov@mont\ov@pt{9pt}{12.5pt}},text=ovgris] at ([xshift=3cm,yshift=-21.55cm]current page.north west)
      {RUT Empresa: 77.482.961-K\\
       RUT Representante: 21.491.020-9\\
       Claudio Ignacio Cabello Vasquez · Representante de Overfore S.A.\\
       \ov@lugar, \ov@fecha};}}
\newcommand\ov@portada{%
  \ifov@subdoc\ov@portadasubdoc\fi
  \ifov@anexo\ov@portadaanexoform{Anexos del}{Subdocumento \ov@numsubdoc}\fi
  \ifov@formulario\ov@portadaanexoform{Formulario \ov@numform}{\ov@nombreform}\fi}

% ======================================================================= bloqueo de formato propio
\newif\ifov@interno
\newcommand\ov@prohibido[1]{\ifov@borrador\ClassWarning{overfore}{BORRADOR: formato propio no permitido: \string#1}\else\ov@prohibidoerror{#1}\fi}
\newcommand\ov@prohibidoerror[1]{\ClassError{overfore}{Formato propio no permitido: \string#1}%
  {Colores, tamanos y tipos de letra, negritas y subrayado los pone la clase overfore. Quite \string#1 del documento.}}
\newcommand\ov@bloquear[1]{%
  \expandafter\let\csname ov@orig@\string#1\endcsname#1%
  \protected\edef#1{\noexpand\ifov@interno
    \noexpand\expandafter\noexpand\@firstoftwo
    \noexpand\else\noexpand\expandafter\noexpand\@secondoftwo\noexpand\fi
    {\expandafter\noexpand\csname ov@orig@\string#1\endcsname}%
    {\noexpand\ov@prohibido\noexpand#1\expandafter\noexpand\csname ov@orig@\string#1\endcsname}}}
\def\ov@listabloqueo{\textbf,\bfseries,\bf,\underline,\uline,\ul,%
  \textcolor,\color,\colorbox,\fcolorbox,\pagecolor,\rowcolor,\cellcolor,\columncolor,\arrayrulecolor,%
  \tiny,\scriptsize,\footnotesize,\small,\large,\Large,\LARGE,\huge,\Huge,\fontsize,%
  \textsf,\sffamily,\texttt,\ttfamily,\fontspec,\setmainfont,\setsansfont,\newfontfamily}
\def\ov@setref#1#2#3{{\ov@internotrue\ov@setref@orig{#1}{#2}{#3}}}
\AddToHook{begindocument/end}{%
  % LaTeX marca en negrita las referencias aún sin resolver (??): eso no es formato del documento
  \let\ov@setref@orig\@setref\let\@setref\ov@setref
  \@for\ov@c:=\ov@listabloqueo\do{\expandafter\ov@bloquear\ov@c}%
  \ov@internofalse
  \hypersetup{pdftitle={OVERFORE S.A. · \ov@iddoc},pdfauthor={OVERFORE S.A.}}%
  \ov@portada\ov@indices}
% marca de agua en los borradores
\AddToHook{shipout/background}{\ifov@borrador
  \put(0.5\paperwidth,-0.5\paperheight){\makebox(0,0){\rotatebox{50}{%
    \ov@mont\ov@negrita\ov@pt{64pt}{70pt}\ov@color{ovlinea}BORRADOR · NO ENTREGAR}}}\fi}
\endinput
