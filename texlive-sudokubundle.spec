Name:		texlive-sudokubundle
Version:	15878
Release:	2
Summary:	A set of sudoku-related packages
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sudokubundle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudokubundle.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudokubundle.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudokubundle.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides three packages: - printsudoku, which
provides a command \sudoku whose argument is the name of a file
containing a puzzle specification; - solvesudoku, which
attempts to find a solution to the puzzle in the file named in
the argument; and - createsudoku, which uses the random package
to generate a puzzle according to a bunch of parameters that
the user sets via macros. The bundle comes with a set of ready-
prepared puzzle files.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sudokubundle/createsudoku.sty
%{_texmfdistdir}/tex/latex/sudokubundle/printsudoku.sty
%{_texmfdistdir}/tex/latex/sudokubundle/solvesudoku.sty
%doc %{_texmfdistdir}/doc/latex/sudokubundle/README
%doc %{_texmfdistdir}/doc/latex/sudokubundle/somesudoku.tex
%doc %{_texmfdistdir}/doc/latex/sudokubundle/sudokubundle.pdf
#- source
%doc %{_texmfdistdir}/source/latex/sudokubundle/sudokubundle.dtx
%doc %{_texmfdistdir}/source/latex/sudokubundle/sudokubundle.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
