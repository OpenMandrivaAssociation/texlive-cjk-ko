%global tl_name cjk-ko
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.5
Release:	%{tl_revision}.1
Summary:	Extension of the CJK package for Korean typesetting
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/language/korean/cjk-ko
License:	gpl lppl1.3c pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk-ko.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/cjk-ko.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(cjk)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package supports typesetting UTF-8-encoded modern Korean documents
with the help of the LaTeX2e CJK package. It provides some enhanced
features focused on Korean typesetting culture, one of them being
allowing line-break between Latin and CJK characters. The package
requires nanumtype1 fonts.

