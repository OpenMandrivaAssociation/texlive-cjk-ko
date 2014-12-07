# revision 32342
# category Package
# catalog-ctan /language/korean/cjk-ko
# catalog-date 2013-12-06 13:41:45 +0100
# catalog-license other-free
# catalog-version 1.3
Name:		texlive-cjk-ko
Version:	1.3
Release:	4
Summary:	Extension of the CJK package for Korean typesetting
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/language/korean/cjk-ko
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk-ko.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk-ko.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package supports typesetting UTF-8-encoded modern Korean
documents with the help of the LaTeX2e CJK package. The package
requires nanumtype1 fonts.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cjk-ko/cjkutf8-josa.sty
%{_texmfdistdir}/tex/latex/cjk-ko/cjkutf8-ko.sty
%{_texmfdistdir}/tex/latex/cjk-ko/cjkutf8-nanummjhanja.sty
%{_texmfdistdir}/tex/latex/cjk-ko/kolabels-utf.sty
%{_texmfdistdir}/tex/latex/cjk-ko/konames-utf.sty
%{_texmfdistdir}/tex/latex/cjk-ko/kotex.sty
%doc %{_texmfdistdir}/doc/latex/cjk-ko/ChangeLog
%doc %{_texmfdistdir}/doc/latex/cjk-ko/README
%doc %{_texmfdistdir}/doc/latex/cjk-ko/cjk-ko-doc.pdf
%doc %{_texmfdistdir}/doc/latex/cjk-ko/cjk-ko-doc.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
