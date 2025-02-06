%global debug_package %{nil}

Name:       asdf
Version:    0.16.1
Release:    %autorelease
Summary:    Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more 
License:    MIT
URL:        https://github.com/asdf-vm/asdf
ExclusiveArch: x86_64 aarch64
Source1:    %{url}/releases/download/v%{version}/%{name}-v%{version}-linux-amd64.tar.gz
Source2:    %{url}/releases/download/v%{version}/%{name}-v%{version}-linux-arm64.tar.gz

%description
Extendable version manager with support for Ruby, Node.js, Elixir, Erlang & more 

%prep
%ifarch x86_64
%setup -q -T -a 1 -c asdf-%{version}
%endif
%ifarch aarch64
%setup -q -T -a 2 -c asdf-%{version}
%endif

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 asdf %{buildroot}%{_bindir}

%files
%{_bindir}/asdf

%changelog
%autochangelog
