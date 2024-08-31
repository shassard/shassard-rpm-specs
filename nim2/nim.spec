%undefine _debugsource_packages

Summary: A statically typed compiled systems programming language
Name: nim
Version: 2.0.8
Release: 1
License: MIT
Group: Development/Languages
Source: https://nim-lang.org/download/%{name}-%{version}.tar.xz
URL: https://nim-lang.org/
BuildRequires: gcc
BuildRequires: pcre2-devel
BuildRequires: openssl-devel
BuildRequires: git
Requires: gcc

%description
Nim is a statically typed compiled systems programming language.
It combines successful concepts from mature languages like Python,
Ada and Modula.

%prep
%setup -q

%build
sh ./build.sh
./bin/nim c koch
./koch boot -d:release
./koch tools

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 bin/* %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_datadir}/%{name}
sed -i '1i lib = "%{_datadir}/%{name}/lib"' config/nim.cfg
sed -i '1i path = "%{_datadir}/%{name}"' config/nim.cfg
cp -R config %{buildroot}/%{_datadir}/%{name}/config
cp -R compiler %{buildroot}/%{_datadir}/%{name}/compiler
cp -R doc %{buildroot}/%{_datadir}/%{name}/doc
cp -R lib %{buildroot}/%{_datadir}/%{name}/lib
cp -R nimpretty %{buildroot}/%{_datadir}/%{name}/nimpretty
cp -R nimsuggest %{buildroot}/%{_datadir}/%{name}/nimsuggest
cp -R testament %{buildroot}/%{_datadir}/%{name}/testament
mkdir -p %{buildroot}/%{_sysconfdir}/%{name}
ln -f -s -t %{buildroot}/%{_sysconfdir}/%{name} nim.cfg %{_datadir}/%{name}/config/nim.cfg

%files
%{_bindir}/atlas
%{_bindir}/nim
%{_bindir}/nimble
%{_bindir}/nim_dbg
%{_bindir}/nim-gdb
%{_bindir}/nimgrep
%{_bindir}/nimpretty
%{_bindir}/nimsuggest
%{_bindir}/testament
%{_datadir}/%{name}
%{_sysconfdir}/%{name}
