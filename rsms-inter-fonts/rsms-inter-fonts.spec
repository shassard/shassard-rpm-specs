Version:        4.0
Release:        1%{?dist}
URL:            https://rsms.me/inter/

%global foundry rsms
%global fontlicense OFL
%global fontlicenses LICENSE.txt
%global fontdocsex %{fontlicenses}

%global fontfamily Inter
%global fontsummary The Inter font family
%global fonts "Inter.ttc"
%global fontconfs %{SOURCE10}
%global fontdescription %{expand:Inter is a typeface specially designed for user interfaces with focus on high
legibility of small-to-medium sized text on computer screens.

The family features a tall x-height to aid in readability of mixed-case and
lower-case text. Several OpenType features are provided as well, like contextual
alternates that adjusts punctuation depending on the shape of surrounding
glyphs, slashed zero for when you need to disambiguate "0" from "o", tabular
numbers, etc.}

Source0:        https://github.com/rsms/inter/releases/download/v%{version}/Inter-%{version}.zip
Source10:       63-%{fontpkgname}.conf

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


%changelog
* Thu Nov 23 2023 Stephen Hassard <steve@hassard.net> - 4.0-1
- Update to 4.0

* Fri Jul 21 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Fri Jan 20 2023 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_38_Mass_Rebuild

* Tue Oct 04 2022 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.19-5
- Package hinted TrueType fonts instead of Type 1 OTF fonts (RHBZ #2122246)

* Sat Jul 23 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Fri Jul 23 2021 Fedora Release Engineering <releng@fedoraproject.org> - 3.19-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sat Jun 19 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.19-1
- Update to 3.19

* Thu Apr 01 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.18-1
- Update to 3.18

* Tue Mar 30 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.17-1
- Update to 3.17

* Mon Mar 29 2021 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.16-1
- Update to 3.16

* Thu Dec 24 2020 Mohamed El Morabity <melmorabity@fedoraproject.org> - 3.15-1
- Initial RPM release
