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
\definecolor{purpleaccent}{HTML}{534264}
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
  \newcommand{\doctitle}{PyIPSA Reference Manual}    
  \newcommand*{\shifttext}[2]{%
    \settowidth{\@tempdima}{#2}%
    \makebox[\@tempdima]{\hspace*{#1}#2}%
  }

  \fancypagestyle{plain}{
    \fancyhead{}
    \fancyhfoffset[LO,RE]{2.56cm}
    \fancyhfoffset[LO,RE]{2.56cm}
    \fancyhfoffset[LE,RO]{1.8cm}
    \fancyhead[L]{\raisebox{-0.8cm}{\includegraphics[width=1.32\textwidth]{header.png}}}
    \fancyhead[R]{\raisebox{-1cm}{\includegraphics[width=0.2\textwidth]{ipsalogo.png}}}
    \fancyhead[C]{\shifttext{-0.65\textwidth}{\textcolor{white}{\scriptsize {\bf \MakeUppercase{\rightmark}}}}}
    \fancyfoot{} % clear all footer fields
    \fancyfoot[L]{\raisebox{-0.81cm}{\includegraphics[width=1.322\textwidth]{footer.png}}}
    \fancyfoot[C] {{\bf \textcolor{white}{\small \thepage}}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
  }
  \fancypagestyle{normal}{
    \fancyhead{}
    \fancyhfoffset[LO,RE]{2.56cm}
    \fancyhfoffset[LO,RE]{2.56cm}
    \fancyhfoffset[LE,RO]{1.8cm}
    \fancyhead[L]{\raisebox{-0.8cm}{\includegraphics[width=1.32\textwidth]{header.png}}}
    \fancyhead[R]{\raisebox{-1cm}{\includegraphics[width=0.2\textwidth]{ipsalogo.png}}}
    \fancyhead[C]{\shifttext{-0.65\textwidth}{\textcolor{white}{\scriptsize {\bf \MakeUppercase{\rightmark}}}}}
    \fancyfoot{} % clear all footer fields
    \fancyfoot[L]{\raisebox{-0.81cm}{\includegraphics[width=1.322\textwidth]{footer.png}}}
    \fancyfoot[C] {{\bf \textcolor{white}{\small \thepage}}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
  }
  \fancypagestyle{firstpage}{
    \fancyhead{}
    \fancyhfoffset[LO,RE]{2.52cm}
    \fancyhfoffset[LO,RE]{2.52cm}
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
        
        
        {\fontsize{48}{56}\selectfont \textcolor{pinkaccent}{\doctitle}}
        \vfill

        {Version: \textcolor{pinkaccent}{IPSA \docversion}}
        \vspace{2mm}

        {Document Reference: \textcolor{pinkaccent}{\docreference}}
        \vspace{2mm}
        
        {\textcolor{pinkaccent}{\@date\:}}
        \vfill
        
        \raggedright
        \hspace*{-2.71cm}
        \makebox[0pt][l]{\raisebox{-6.75cm}[0pt][0pt]{            \includegraphics[width=1.317\textwidth]{titlepage_bottomimage.png}}}
        \vfill
        }
}

\AtBeginDocument{\thispagestyle{firstpage}}
\AtBeginDocument{\maketitle}

% Formatting the section headings
  
\AtBeginDocument{
   \titleformat{\chapter}[hang]
      {\huge\color{pinkaccent}}
      {\thechapter}{10pt}{\huge}[{\titlerule[0pt]}]
  
    \titleformat{\section}
      {\Large\color{pinkaccent}}
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

    \renewcommand*{\sphinxstyletheadfamily}{\bfseries\leavevmode\color{white}}
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