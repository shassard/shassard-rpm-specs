%global debug_package %{nil}

Name:       lazyjj
Version:    0.4.2
Release:    1%{?dist}
Summary:    TUI for Jujutsu/jj

License:    Apache-2.0
URL:        https://github.com/Cretezy/lazyjj
Source0:    %{url}/releases/download/v%{version}/%{name}-v%{version}-x86_64-unknown-linux-musl.tar.gz

%description
TUI for Jujutsu/jj

%prep
%setup -q -c %{name}-%{version}

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 %{name} %{buildroot}%{_bindir}

%files
%{_bindir}/%{name}
