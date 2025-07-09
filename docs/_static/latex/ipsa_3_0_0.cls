\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{ipsa_3_0_0}[2025/07/07 ipsa style class]

\LoadClass[openany,a4paper]{report}
% Loading in packages
\RequirePackage{xcolor}
\RequirePackage{listings}
\RequirePackage{geometry}
\RequirePackage{fancyhdr}
\RequirePackage{microtype}
\RequirePackage{setspace}
\RequirePackage{xkeyval}
\RequirePackage{fontspec}
\RequirePackage[nobottomtitles*]{titlesec}
\RequirePackage{hyperref}


\def\docversion{latest}
\define@key{ipsa_3_0_0.cls}{docversion}[latest]{
    \def\docversion{#1}
}
\def\docreference{latest}
\define@key{ipsa_3_0_0.cls}{docreference}[latest]{
    \def\docreference{#1}
}
\ExecuteOptionsX{docversion}
\ProcessOptionsX

% Pulling the colours from the docx file
\definecolor{pinkaccent}{HTML}{B84775}
\definecolor{purpleaccent}{HTML}{5F497A}
\definecolor{headeraccent}{HTML}{88456E}

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
\setlength{\topmargin}{-2.6cm}
\setlength{\headheight}{13pt}
\setlength{\headsep}{2.6cm}
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
    \fancyhfoffset[LO,RE]{2.55cm}
    \fancyhfoffset[LO,RE]{2.55cm}
    \fancyhfoffset[LE,RO]{1.8cm}
    \fancyhead[L]{\raisebox{0.35cm}{\includegraphics[width=1.32\textwidth]{header.png}}}
    \fancyhead[R]{\includegraphics[width=0.2\textwidth]{ipsalogo.png}}
    \fancyfoot{} % clear all footer fields
    \fancyfoot[L]{\raisebox{-0.8cm}{\includegraphics[width=1.32\textwidth]{footer.png}}}
    \fancyfoot[C] {{\bf \textcolor{white}{\small \thepage}}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
  }
  \fancypagestyle{normal}{
    \fancyhead{}
    \fancyhfoffset[LO,RE]{2.55cm}
    \fancyhfoffset[LO,RE]{2.55cm}
    \fancyhfoffset[LE,RO]{1.8cm}
    \fancyhead[L]{\raisebox{0.35cm}{\includegraphics[width=1.32\textwidth]{header.png}}}
    \fancyhead[R]{\includegraphics[width=0.2\textwidth]{ipsalogo.png}}
    \fancyfoot{} % clear all footer fields
    \fancyfoot[L]{\raisebox{-0.8cm}{\includegraphics[width=1.32\textwidth]{footer.png}}}
    \fancyfoot[C] {{\bf \textcolor{white}{\small \thepage}}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
  }
  \fancypagestyle{firstpage}{
    \fancyhead{}
    \fancyhfoffset[LO,RE]{2.5cm}
    \fancyhfoffset[LO,RE]{2.5cm}
    \fancyhfoffset[LE,RO]{1.8cm}
    \fancyhead[L]{\includegraphics[width=0.6\textwidth]{titlepage_topcorner.png}}
    \fancyfoot{} % clear all footer fields
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}  
  }
  \makeatother
}

% Formatting the title
\renewcommand{\maketitle}{
        {\raggedleft
        
        \hspace*{4.8cm}
        \includegraphics[width=0.8\textwidth]{ipsalogo.png}
        

        {\Large \bf \textcolor{pinkaccent}{IPSA Software}}
        \vspace{5mm}
        
        {\Large \bf \textcolor{pinkaccent}{PyIPSA Reference Manual (\docversion)}}
        \vfill

        {\large \textcolor{purpleaccent}{\docreference -- 000 -- R0}}
        \vspace{2mm}

        {\small \textcolor{purpleaccent}{\@date}}
        \vspace{10mm}
        
        {\Large \textcolor{pinkaccent}{PUBLISHED}}
        \vfill
        
        \raggedright
        \hspace*{-2.7cm}
        \makebox[0pt][l]{\raisebox{-6.75cm}[0pt][0pt]{            \includegraphics[width=1.315\textwidth]{titlepage_bottomimage.png}}}
        \vfill
        }
}

\AtBeginDocument{\thispagestyle{firstpage}}
\AtBeginDocument{\maketitle}

% Formatting the section headings
  
\AtBeginDocument{
    \titleformat{\chapter}[hang]
      {\huge\color{pinkaccent}}
      {\thechapter}{10pt}{\huge}[{\titlerule[0.8pt]}]
  
    \titleformat{\section}
      {\Large\bfseries\color{pinkaccent}}
      {\thesection}{1em}{}

    \titleformat{\subsection}
      {\large\bfseries\color{pinkaccent}}
      {\thesubsection}{1em}{}

    \titleformat{\subsubsection}
      {\large\color{pinkaccent}}
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