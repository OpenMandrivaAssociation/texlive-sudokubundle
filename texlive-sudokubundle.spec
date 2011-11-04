# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sudokubundle
# catalog-date 2007-03-12 11:51:09 +0100
# catalog-license lppl
# catalog-version 1.0a
Name:		texlive-sudokubundle
Version:	1.0a
Release:	1
Summary:	A set of sudoku-related packages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sudokubundle
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudokubundle.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudokubundle.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sudokubundle.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The bundle provides three packages: - printsudoku, which
provides a command \sudoku whose argument is the name of a file
containing a puzzle specification; - solvesudoku, which
attempts to find a solution to the puzzle in the file named in
the argument; and - createsudoku, which uses the random package
to generate a puzzle according to a bunch of parameters that
the user sets via macros. The bundle comes with a set of ready-
prepared puzzle files.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
