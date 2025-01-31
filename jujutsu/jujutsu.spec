%global debug_package %{nil}

Name:       jujutsu
Version:    0.25.0
Release:    %autorelease
Summary:    A Git-compatible VCS that is both simple and powerful
License:    Apache-2.0
URL:        https://github.com/jj-vcs/jj
ExclusiveArch: x86_64 aarch64
Source0:    %{url}/releases/download/v%{version}/jj-v%{version}-%{_arch}-unknown-linux-musl.tar.gz
Source10: jj.bash
Source11: jj.fish
Source12: jj.zsh

%description
A Git-compatible VCS that is both simple and powerful

%prep
%setup -q -c jj-%{version}

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 jj %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_datadir}/bash-completion/completions
install -d -m0755 %{buildroot}%{_datadir}/fish/vendor_completions.d
install -d -m0755 %{buildroot}%{_datadir}/zsh/site-functions
install -p -m0755 %{SOURCE10} %{buildroot}%{_datadir}/bash-completion/completions/jj
install -p -m0755 %{SOURCE11} %{buildroot}%{_datadir}/fish/vendor_completions.d/jj.fish
install -p -m0755 %{SOURCE12} %{buildroot}%{_datadir}/zsh/site-functions/_jj

%files
%doc LICENSE
%{_bindir}/jj
%{_datadir}/bash-completion/completions/jj
%{_datadir}/fish/vendor_completions.d/jj.fish
%{_datadir}/zsh/site-functions/_jj

%changelog
%autochangelog
