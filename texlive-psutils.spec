Name:		texlive-psutils
Version:	61719
Release:	2
Summary:	PostScript utilities
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/support/psutils
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psutils.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psutils.doc.r%{version}.tar.xz
BuildArch:	noarch
Provides:	texlive-psutils.bin = %{EVRD}
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A bundle of utilities for manipulating PostScript documents,
including page selection and rearrangement, resizing the page,
arrangement into signatures for booklet printing, and page
merging for n-up printing. Utilities include psbook, psselect,
pstops, psnup, psresize, epsffit.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_bindir}/*
%{_texmfdistdir}/scripts/psutils
%{_texmfdistdir}/dvips/getafm
%{_texmfdistdir}/psutils
%doc %{_mandir}/man1/*.1*
%doc %{_texmfdistdir}/doc/man/man1/*

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
ln -sf %{_texmfdistdir}/scripts/psutils/extractres.pl extractres
ln -sf %{_texmfdistdir}/scripts/psutils/fixdlsrps.pl fixdlsrps
ln -sf %{_texmfdistdir}/scripts/psutils/fixfmps.pl fixfmps
ln -sf %{_texmfdistdir}/scripts/psutils/fixpsditps.pl fixpsditps
ln -sf %{_texmfdistdir}/scripts/psutils/fixpspps.pl fixpspps
ln -sf %{_texmfdistdir}/scripts/psutils/fixscribeps.pl fixscribeps
ln -sf %{_texmfdistdir}/scripts/psutils/fixtpps.pl fixtpps
ln -sf %{_texmfdistdir}/scripts/psutils/fixwfwps.pl fixwfwps
ln -sf %{_texmfdistdir}/scripts/psutils/fixwpps.pl fixwpps
ln -sf %{_texmfdistdir}/scripts/psutils/fixwwps.pl fixwwps
ln -sf %{_texmfdistdir}/scripts/psutils/includeres.pl includeres
ln -sf %{_texmfdistdir}/scripts/psutils/psmerge.pl psmerge
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdistdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
