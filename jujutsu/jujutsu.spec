%global debug_package %{nil}

Name:       jujutsu
Version:    0.27.0
Release:    %autorelease
Summary:    A Git-compatible VCS that is both simple and powerful
License:    Apache-2.0
URL:        https://github.com/jj-vcs/jj
ExclusiveArch: x86_64 aarch64
Source1:    %{url}/releases/download/v%{version}/jj-v%{version}-x86_64-unknown-linux-musl.tar.gz
Source2:    %{url}/releases/download/v%{version}/jj-v%{version}-aarch64-unknown-linux-musl.tar.gz
Source10: jj.bash
Source11: jj.fish
Source12: jj.zsh

%description
A Git-compatible VCS that is both simple and powerful

%prep
%ifarch x86_64
%setup -q -T -a 1 -c jj-%{version}
%endif
%ifarch aarch64
%setup -q -T -a 2 -c jj-%{version}
%endif

%install
install -d -m0755 %{buildroot}%{_bindir}
install -p -m0755 jj %{buildroot}%{_bindir}
install -d -m0755 %{buildroot}%{_datadir}/bash-completion/completions
install -d -m0755 %{buildroot}%{_datadir}/fish/vendor_completions.d
install -d -m0755 %{buildroot}%{_datadir}/zsh/site-functions
install -p -m0644 %{SOURCE10} %{buildroot}%{_datadir}/bash-completion/completions/jj
install -p -m0644 %{SOURCE11} %{buildroot}%{_datadir}/fish/vendor_completions.d/jj.fish
install -p -m0644 %{SOURCE12} %{buildroot}%{_datadir}/zsh/site-functions/_jj

%files
%doc LICENSE
%{_bindir}/jj
%{_datadir}/bash-completion/completions/jj
%{_datadir}/fish/vendor_completions.d/jj.fish
%{_datadir}/zsh/site-functions/_jj

%changelog
%autochangelog
