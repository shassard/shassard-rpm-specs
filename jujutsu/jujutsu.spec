%global debug_package %{nil}
%global source_date_epoch_from_changelog false

Name:       jujutsu
Version:    0.25.0
Release:    2%{?dist}
Summary:    A Git-compatible VCS that is both simple and powerful

License:    Apache-2.0
URL:        https://github.com/jj-vcs/jj
Source0:    %{url}/releases/download/v%{version}/jj-v%{version}-%{_arch}-unknown-linux-musl.tar.gz

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
echo "source <(jj util completion bash)" > %{buildroot}%{_datadir}/bash-completion/completions/jj
echo "jj util completion fish | source" > %{buildroot}%{_datadir}/fish/vendor_completions.d/jj.fish
echo "source <(jj util completion zsh)" > %{buildroot}%{_datadir}/zsh/site-functions/_jj

%files
%doc LICENSE
%{_bindir}/jj
%{_datadir}/bash-completion/completions/jj
%{_datadir}/fish/vendor_completions.d/jj.fish
%{_datadir}/zsh/site-functions/_jj

%changelog
%autochangelog
