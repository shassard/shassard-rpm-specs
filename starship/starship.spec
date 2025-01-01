%global debug_package %{nil}

Name:       starship
Version:    1.21.1
Release:    1%{?dist}
Summary:    The minimal, blazing-fast, and infinitely customizable prompt for any shell!

License:    ISC
URL:        https://github.com/starship/starship
Source0:    %{url}/releases/download/v%{version}/starship-x86_64-unknown-linux-gnu.tar.gz

%description
The minimal, blazing-fast, and infinitely customizable prompt for any shell!

%prep
%setup -q -c starship-%{version}

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 starship %{buildroot}%{_bindir}

%files
%{_bindir}/starship
