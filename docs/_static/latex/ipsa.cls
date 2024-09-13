\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipsa}[2023/10/27 ipsa style class]

\LoadClass[openany,a4paper]{report}
% Loading in packages
\RequirePackage{xcolor}
\RequirePackage{listings}
\RequirePackage{hyperref}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{microtype}
\RequirePackage{setspace}
\RequirePackage{xkeyval}
\RequirePackage{fontspec}
\RequirePackage[nobottomtitles*]{titlesec}


\def\docversion{latest}
\define@key{ipsa.cls}{docversion}[latest]{
    \def\docversion{#1}
}
\def\docreference{latest}
\define@key{ipsa.cls}{docreference}[latest]{
    \def\docreference{#1}
}
\ExecuteOptionsX{docversion}
\ProcessOptionsX

% Pulling the colours from the docx file
\definecolor{pinkaccent}{HTML}{b94775}
\definecolor{headeraccent}{HTML}{c76b90}
\definecolor{purpleaccent}{HTML}{534264}
\definecolor{linkcolour}{HTML}{2A567A}
\definecolor{code_comment}{HTML}{008000}
\definecolor{code_keyword}{HTML}{000080}
\definecolor{code_objects}{HTML}{0070C0}
\definecolor{code_error}{HTML}{800000}
\definecolor{grey_colour}{HTML}{808080}

% Setting the font
\setmainfont{NotoSans}[
    Path=./,
    Extension = .ttf,
    UprightFont=*-Regular,
    BoldFont=*-Bold,
    ItalicFont=*-Italic,
    BoldItalicFont=*-BoldItalic
    ]

% Setting the margins
\setlength{\paperwidth}{21cm}
\setlength{\paperheight}{29.7cm}
\setlength{\oddsidemargin}{0pt}
\setlength{\topmargin}{-1.27cm}
\setlength{\headheight}{13pt}
\setlength{\headsep}{1.27cm}
\addtolength{\headsep}{-13pt}
\setlength{\footskip }{2cm}
\setlength{\textwidth}{15.92cm}
\setlength{\textheight}{24.32cm}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{1pt}
\raggedbottom

% Setting the header and footer
\AtBeginDocument{
  \makeatletter
  \fancypagestyle{plain}{
    \fancyhead{}
    \fancyhead[R]{\textcolor{headeraccent}{\fontsize{7}{8}\selectfont \addfontfeature{LetterSpace=42.9} {\MakeUppercase{\rightmark}}}}
    \fancyhead[L]{\textcolor{headeraccent}{\fontsize{7}{8}\selectfont \thepage}}
    \fancyfoot{} % clear all footer fields
    \fancyfoot[L]{\includegraphics[width=0.2\textwidth]{ipsalogo_dimmed.pdf}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{1pt}
    \renewcommand{\footrule}{\hbox to\headwidth{%
        \color{grey_colour}\leaders\hrule height \footrulewidth\hfill}}
  }
  \fancypagestyle{normal}{
    \fancyhead{}
    \fancyhead[R]{\textcolor{headeraccent}{\fontsize{7}{8}\selectfont \addfontfeature{LetterSpace=42.9} {\MakeUppercase{\rightmark}}}}
    \fancyhead[L]{\textcolor{headeraccent}{\fontsize{7}{8}\selectfont \thepage}}
    \fancyfoot{} % clear all footer fields
    \fancyfoot[L]{\includegraphics[width=0.2\textwidth]{ipsalogo_dimmed.pdf}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{1pt}
    \renewcommand{\footrule}{\hbox to\headwidth{%
        \color{grey_colour}\leaders\hrule height \footrulewidth\hfill}}
  }
  \makeatother
}

% Formatting the title
\renewcommand{\maketitle}{
        {\vfill
        \centering
        {\huge \textcolor{purpleaccent}{{\bf IPSA} SOFTWARE} \hfill}
        \vspace{3mm}

        {\color{black}\hrule}
        \vspace{3mm}

        {\hfill \huge \textcolor{pinkaccent}{Simply Powerful.}}

        \includegraphics[width=0.9\textwidth]{IpsaBigLogo.png}
        \vspace{4mm}

        {\fontsize{34}{38}\selectfont {\bf \textcolor{purpleaccent}{PyIPSA Reference Manual}}}
        \vspace{3mm}

        {\Large \textcolor{purpleaccent}{Version:} \textcolor{pinkaccent}{IPSA \docversion} }

        {\Large \textcolor{purpleaccent}{Document Reference:} \textcolor{pinkaccent}{\docreference} }

        \textcolor{purpleaccent}{Date Modified:} \textcolor{pinkaccent}{ \@date }
        \vspace{2mm}

        {\color{grey_colour}\hrule}
        \vspace{2mm}

        \textcolor{grey_colour}{IPSA Power, Bainbridge House, 86-90 London Road, Manchester, M1 2PW}

        \hfill\textcolor{grey_colour}{Phone: +44 (0)161 233 4800 | Email: support@ipsa-power.com}\hfill
        }
}

\AtBeginDocument{\thispagestyle{empty}}
\AtBeginDocument{\maketitle}

% Formatting the section headings
\titleformat{\chapter}[display]
  {\huge\bfseries\color{purpleaccent}}
  {\chaptertitlename \thechapter}{10pt}{\Huge}[{\titlerule[0.8pt]}]

\AtBeginDocument{
    \titleformat{\section}
      {\huge\color{pinkaccent}}
      {\thesection}{1em}{}

    \titleformat{\subsection}
      {\Large\color{purpleaccent}}
      {\thesubsection}{1em}{}

    \titleformat{\subsubsection}
      {\Large\color{pinkaccent}}
      {\thesubsubsection}{1em}{}

    \renewcommand{\normalsize}{\fontsize{11}{13}\selectfont}
    \renewcommand{\linespread}{1.5}
    \setlength{\parindent}{0pt}

    \onehalfspacing

    \let\oldxcode\sphinxcode
    \renewcommand{\sphinxcode}[1]{\textit{\textcolor{pinkaccent}{{\textnormal\oldxcode{#1}}}}}

    \let\oldliteralstrong\sphinxstyleliteralstrong
    \renewcommand{\sphinxstyleliteralstrong}[1]{\textbf{\textcolor{pinkaccent}{{\textnormal \oldliteralstrong{#1}}}}}

    \let\oldliteralemphasis\sphinxstyleliteralemphasis
    \renewcommand{\sphinxstyleliteralemphasis}[1]{\textit{\textcolor{linkcolour}{{\textnormal \oldliteralemphasis{#1}}}}}
}

% Formatting hyperrefs
\hypersetup{
     colorlinks = true,
     linkcolor = pinkaccent,
     filecolor = blue,
     citecolor = black,
     urlcolor = linkcolour,
     }

\let\oldhref\href
\renewcommand{\href}[2]{\oldhref{#1}{\bfseries#2}}

\AtBeginDocument{
    \let\oldsphinxhref\sphinxhref
    \renewcommand{\sphinxhref}[2]{\oldsphinxhref{#1}{\textcolor{linkcolour}{#2}}}
}