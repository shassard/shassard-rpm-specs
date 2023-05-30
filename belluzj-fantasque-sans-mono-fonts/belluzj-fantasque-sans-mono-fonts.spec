Version: 1.8.0
Release: 3%{?dist}
URL:     https://github.com/belluzj/fantasque-sans

%global foundry           belluzj
%global fontlicense       OFL
%global fontlicenses      LICENSE.txt
%global fontdocs          README.md CHANGELOG.md

%global fontfamily        Fantasque Sans Mono
%global fontsummary       Fantasque monospaced font with programming ligatures
%global fonts             TTF/*.ttf
%global fontconfs         %{SOURCE10}
%global fontdescription   %{expand:
A programming font, designed with functionality in mind, and with some
wibbly-wobbly handwriting-like fuzziness that makes it unassumingly cool.

Previously known as Cosmic Sans Neue Mono.

Font designed by Jany Belluz
}

Source0:        https://github.com/belluzj/fantasque-sans/releases/download/v%{version}/FantasqueSansMono-Normal.tar.gz
Source10:       64-%{fontpkgname}.conf

%fontpkg

%prep
%setup -c

%build
%fontbuild

%install
%fontinstall

%check
%fontcheck

%fontfiles

%changelog
* Wed Aug 04 2021 Olivier Samyn <code@oleastre.be> - 1.8.0-3
- Correct generic font family

* Sun Jul 11 2021 Olivier Samyn <code@oleastre.be> - 1.8.0-2
- Switch to new font packaging spec format

* Mon Nov 18 2019 Olivier Samyn 🎻 <code@oleastre.be> - 1.8.0-1
- New upstream version with code ligatures.

* Fri Mar 02 2018 Olivier Samyn <code@oleastre.be> - 1.7.2-1
  - Added
    Font variant with a larger line height, especially for users of accented capitals. #23
    Numero sign (№) #23
    Perl 6 quotes (｢ and ｣) #82
    Black circle (●) #78
    Comparison operators (≤ and ≥) #69

  - Changed
    Fixed the curly tail on Cyrillic у #23
    Upgrade the build system to have a proper version of the font with a built-in stylistic set ss01 (no-loop k) #67
    Thanks to the Monoid project for open-sourcing their build scripts.

* Mon Apr 10 2017 Olivier Samyn <code@oleastre.be> - 1.7.1-3
- Updated spec filename to match package name

* Wed Nov 09 2016 Olivier Samyn <code@oleastre.be> - 1.7.1-2
- Use ttf fonts instead of otf one.

* Sun Nov 06 2016 Olivier Samyn <code@oleastre.be> - 1.7.1-1
- Initial rpm
