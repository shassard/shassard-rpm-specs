%global debug_package %{nil}

Name:       babashka
Version:    1.12.196
Release:    1%{?dist}
Summary:    Native, fast starting Clojure interpreter for scripting

License:    EPL-1.0
URL:        https://github.com/babashka/babashka
Source0:    %{url}/releases/download/v%{version}/babashka-%{version}-linux-amd64.tar.gz

%description
Native, fast starting Clojure interpreter for scripting

%prep
%setup -q -c bb-%{version}

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 bb %{buildroot}%{_bindir}

%files
%{_bindir}/bb
