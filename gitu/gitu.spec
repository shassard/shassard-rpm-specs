%global debug_package %{nil}

Name:       gitu
Version:    0.28.0
Release:    1%{?dist}
Summary:    A TUI Git client inspired by Magit

License:    MIT
URL:        https://github.com/altsem/gitu
Source0:    %{url}/releases/download/v%{version}/%{name}-v%{version}-x86_64-unknown-linux-gnu.tar.gz

%description
A TUI Git client inspired by Magit

%prep
%setup -q -n %{name}-v%{version}-x86_64-unknown-linux-gnu

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 gitu %{buildroot}%{_bindir}

%files
%license LICENSE
%{_bindir}/gitu
