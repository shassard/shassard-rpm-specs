%global debug_package %{nil}
%global source_date_epoch_from_changelog false

Name:       jujutsu
Version:    0.25.0
Release:    3%{?dist}
Summary:    A Git-compatible VCS that is both simple and powerful
License:    Apache-2.0
URL:        https://github.com/jj-vcs/jj
ExclusiveArch: x86_64 aarch64
%ifarch x86_64
Source10:    %{url}/releases/download/v%{version}/jj-v%{version}-x86_64-unknown-linux-musl.tar.gz
%endif
%ifarch aarm64
Source20:    %{url}/releases/download/v%{version}/jj-v%{version}-aarm64-unknown-linux-musl.tar.gz
%endif
Source31: jj.bash
Source32: jj.fish
Source33: jj.zsh

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
install -p -m0755 jj.bash %{buildroot}%{_datadir}/bash-completion/completions/jj
install -p -m0755 jj.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/jj.fish
install -p -m0755 jj.zsh %{buildroot}%{_datadir}/zsh/site-functions/_jj

%files
%doc LICENSE
%{_bindir}/jj
%{_datadir}/bash-completion/completions/jj
%{_datadir}/fish/vendor_completions.d/jj.fish
%{_datadir}/zsh/site-functions/_jj

%changelog
%autochangelog
