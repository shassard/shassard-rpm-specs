%global debug_package %{nil}

Name:       mise
Version:    2025.2.3
Release:    1%{?dist}
Summary:    dev tools, env vars, task runner

License:    MIT
URL:        https://github.com/jdx/mise
Source0:    %{url}/releases/download/v%{version}/mise-v%{version}-linux-x64.tar.xz

%description
dev tools, env vars, task runner

%prep
%setup -q -n mise

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 bin/mise bin/mise.d %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_mandir}/man1
install -p -m0755 man/man1/mise.1 %{buildroot}%{_mandir}/man1
install -d -m0755 %{buildroot}%{_datadir}/fish/vendor_conf.d
install -p -m0755 share/fish/vendor_conf.d/mise-activate.fish %{buildroot}%{_datadir}/fish/vendor_conf.d

%files
%license LICENSE
%{_bindir}/mise
%{_bindir}/mise.d
%{_mandir}/man1/mise.1.gz
%{_datadir}/fish/vendor_conf.d/mise-activate.fish
