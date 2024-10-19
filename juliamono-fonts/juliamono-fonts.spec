Version:        0.058
Release:        1%{?dist}
URL:            https://juliamono.netlify.app/

%global foundry Cormullion
%global fontlicense OFL
%global fontlicenses LICENSE.txt
%global fontdocsex %{fontlicenses}

%global fontfamily JuliaMono
%global fontsummary JuliaMono monospaced font
%global fonts JuliaMono-*.ttf
%global fontconfs %{SOURCE10}
%global fontdescription JuliaMono is a monospaced typeface designed for programming and in other text editing environments that require a wide range of specialist and technical Unicode characters.

Source0:        https://github.com/cormullion/juliamono/releases/download/v%{version}/JuliaMono-ttf.zip
Source10:       63-%{fontpkgname}.conf

BuildRequires:              fonts-rpm-macros
BuildRequires:              fonts-srpm-macros

%fontpkg

%prep
%autosetup -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles
