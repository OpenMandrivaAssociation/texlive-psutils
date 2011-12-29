# revision 23089
# category TLCore
# catalog-ctan /support/psutils
# catalog-date 2009-11-10 00:30:52 +0100
# catalog-license other-free
# catalog-version p17
Name:		texlive-psutils
Version:	p17
Release:	1
Summary:	PostScript utilities
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/support/psutils
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psutils.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/psutils.doc.tar.xz
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
%{_bindir}/extractres
%{_bindir}/fixdlsrps
%{_bindir}/fixfmps
%{_bindir}/fixpsditps
%{_bindir}/fixpspps
%{_bindir}/fixscribeps
%{_bindir}/fixtpps
%{_bindir}/fixwfwps
%{_bindir}/fixwpps
%{_bindir}/fixwwps
%{_bindir}/includeres
%{_bindir}/psmerge
%{_texmfdir}/scripts/psutils/extractres.pl
%{_texmfdir}/scripts/psutils/fixdlsrps.pl
%{_texmfdir}/scripts/psutils/fixfmps.pl
%{_texmfdir}/scripts/psutils/fixpsditps.pl
%{_texmfdir}/scripts/psutils/fixpspps.pl
%{_texmfdir}/scripts/psutils/fixscribeps.pl
%{_texmfdir}/scripts/psutils/fixtpps.pl
%{_texmfdir}/scripts/psutils/fixwfwps.pl
%{_texmfdir}/scripts/psutils/fixwpps.pl
%{_texmfdir}/scripts/psutils/fixwwps.pl
%{_texmfdir}/scripts/psutils/includeres.pl
%{_texmfdir}/scripts/psutils/psmerge.pl
%doc %{_mandir}/man1/epsffit.1*
%doc %{_texmfdir}/doc/man/man1/epsffit.man1.pdf
%doc %{_mandir}/man1/extractres.1*
%doc %{_texmfdir}/doc/man/man1/extractres.man1.pdf
%doc %{_mandir}/man1/fixdlsrps.1*
%doc %{_texmfdir}/doc/man/man1/fixdlsrps.man1.pdf
%doc %{_mandir}/man1/fixfmps.1*
%doc %{_texmfdir}/doc/man/man1/fixfmps.man1.pdf
%doc %{_mandir}/man1/fixpsditps.1*
%doc %{_texmfdir}/doc/man/man1/fixpsditps.man1.pdf
%doc %{_mandir}/man1/fixpspps.1*
%doc %{_texmfdir}/doc/man/man1/fixpspps.man1.pdf
%doc %{_mandir}/man1/fixscribeps.1*
%doc %{_texmfdir}/doc/man/man1/fixscribeps.man1.pdf
%doc %{_mandir}/man1/fixtpps.1*
%doc %{_texmfdir}/doc/man/man1/fixtpps.man1.pdf
%doc %{_mandir}/man1/fixwfwps.1*
%doc %{_texmfdir}/doc/man/man1/fixwfwps.man1.pdf
%doc %{_mandir}/man1/fixwpps.1*
%doc %{_texmfdir}/doc/man/man1/fixwpps.man1.pdf
%doc %{_mandir}/man1/fixwwps.1*
%doc %{_texmfdir}/doc/man/man1/fixwwps.man1.pdf
%doc %{_mandir}/man1/includeres.1*
%doc %{_texmfdir}/doc/man/man1/includeres.man1.pdf
%doc %{_mandir}/man1/psbook.1*
%doc %{_texmfdir}/doc/man/man1/psbook.man1.pdf
%doc %{_mandir}/man1/psmerge.1*
%doc %{_texmfdir}/doc/man/man1/psmerge.man1.pdf
%doc %{_mandir}/man1/psnup.1*
%doc %{_texmfdir}/doc/man/man1/psnup.man1.pdf
%doc %{_mandir}/man1/psresize.1*
%doc %{_texmfdir}/doc/man/man1/psresize.man1.pdf
%doc %{_mandir}/man1/psselect.1*
%doc %{_texmfdir}/doc/man/man1/psselect.man1.pdf
%doc %{_mandir}/man1/pstops.1*
%doc %{_texmfdir}/doc/man/man1/pstops.man1.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdir}/scripts/psutils/extractres.pl extractres
    ln -sf %{_texmfdir}/scripts/psutils/fixdlsrps.pl fixdlsrps
    ln -sf %{_texmfdir}/scripts/psutils/fixfmps.pl fixfmps
    ln -sf %{_texmfdir}/scripts/psutils/fixpsditps.pl fixpsditps
    ln -sf %{_texmfdir}/scripts/psutils/fixpspps.pl fixpspps
    ln -sf %{_texmfdir}/scripts/psutils/fixscribeps.pl fixscribeps
    ln -sf %{_texmfdir}/scripts/psutils/fixtpps.pl fixtpps
    ln -sf %{_texmfdir}/scripts/psutils/fixwfwps.pl fixwfwps
    ln -sf %{_texmfdir}/scripts/psutils/fixwpps.pl fixwpps
    ln -sf %{_texmfdir}/scripts/psutils/fixwwps.pl fixwwps
    ln -sf %{_texmfdir}/scripts/psutils/includeres.pl includeres
    ln -sf %{_texmfdir}/scripts/psutils/psmerge.pl psmerge
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_mandir}/man1
mv %{buildroot}%{_texmfdir}/doc/man/man1/*.1 %{buildroot}%{_mandir}/man1
