%global tl_name psutils
%global tl_revision 61719

Name:		texlive-%{tl_name}
Epoch:		1
Version:	p17
Release:	%{tl_revision}.1
Summary:	PostScript utilities
Group:		Publishing
URL:		https://www.ctan.org/pkg/psutils
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psutils.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/psutils.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(psutils.bin)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A bundle of utilities for manipulating PostScript documents, including
page selection and rearrangement, resizing the page, arrangement into
signatures for booklet printing, and page merging for n-up printing.
Utilities include psbook, psselect, pstops, psnup, psresize, epsffit.

