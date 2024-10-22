%global debug_package %{nil}

Name:       ripgrep
Version:    14.1.1
Release:    1%{?dist}
Summary:    ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern.
License:    MIT
URL:        https://github.com/BurntSushi/ripgrep
Source0:    %{url}/releases/download/%{version}/%{name}-%{version}-x86_64-unknown-linux-musl.tar.gz

%description
ripgrep is a line-oriented search tool that recursively searches the current directory for a regex pattern. By default, ripgrep will respect gitignore rules and automatically skip hidden files/directories and binary files. ripgrep has first class support on Windows, macOS and Linux, with binary downloads available for every release. ripgrep is similar to other popular search tools like The Silver Searcher, ack and grep.

%prep
%autosetup -n %{name}-%{version}-x86_64-unknown-linux-musl

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 rg %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_docdir}/ripgrep
install -m 0644 doc/*.md %{buildroot}%{_docdir}/ripgrep
mkdir -p %{buildroot}%{_mandir}/man1
install -m 0644 doc/rg.1 %{buildroot}%{_mandir}/man1
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
install -m 0644 complete/rg.bash %{buildroot}%{_datadir}/bash-completion/completions
mkdir -p %{buildroot}%{_datadir}/zsh/site-functions
install -m 0644 complete/_rg %{buildroot}%{_datadir}/zsh/site-functions
mkdir -p %{buildroot}%{_datadir}/fish/vendor_completions.d
install -m 0644 complete/rg.fish %{buildroot}%{_datadir}/fish/vendor_completions.d

%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/rg
%{_mandir}/*
%{_docdir}/*
%{_datadir}/*
