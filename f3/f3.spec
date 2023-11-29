Name:		f3
Version:	8.0
Release:	1%{?dist}
Summary:	Utility to test for fake flash drives and cards
Group:		Applications/System
License:	GPLv3
URL:		http://oss.digirati.com.br/%{name}/
Source0:    https://github.com/AltraMayor/f3/archive/v%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

%description
F3 is a utility to test for fake flash drives and cards. It is a Free
Software alternative to h2testw.  f3write will fill the unused part of
a filesystem with files NNNN.fff with known content, and f3read will
analyze the files to determine whether the contents are corrupted, as
happens with fake flash.

%prep
%setup -q
sed -i -e 's/gcc/gcc $(CFLAGS)/' Makefile

%build
make %{?_smp_mflags} CFLAGS="%{optflags}"

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 f3read f3write %{buildroot}%{_bindir}

%files
%doc LICENSE
%{_bindir}/f3read
%{_bindir}/f3write

%changelog
* Thu Dec 23 2021 Stephen Hassard <steve@hassard.net> - 8.0-1
- Update to 8.0

* Sun Feb 15 2015 Stephen Hassard <steve@hassard.net> - 5.0-1
- Update to 5.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jun 22 2012 Eric Smith <eric@brouhaha.com>  2-2
- Updated based on package review comments

* Wed Apr 25 2012 Eric Smith <eric@brouhaha.com>  2-1
- Initial version
