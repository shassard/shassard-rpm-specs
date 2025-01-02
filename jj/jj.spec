%global debug_package %{nil}

Name:       jj
Version:    0.25.0
Release:    1%{?dist}
Summary:    A Git-compatible VCS that is both simple and powerful

License:    Apache-2.0
URL:        https://github.com/jj-vcs/jj
Source0:    %{url}/releases/download/v%{version}/%{name}-v%{version}-x86_64-unknown-linux-musl.tar.gz

%description
A Git-compatible VCS that is both simple and powerful

%prep
%setup -q -c %{name}-%{version}

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 %{name} %{buildroot}%{_bindir}

%files
%doc LICENSE
%{_bindir}/%{name}
