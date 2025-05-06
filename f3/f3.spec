Name:		f3
Version:	9.0
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
