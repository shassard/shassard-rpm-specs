%global debug_package %{nil}

Name:       fzf
Version:    0.57.0
Release:    1%{?dist}
Summary:    A command-line fuzzy finder
License:    MIT
URL:        https://github.com/junegunn/fzf
Source0:    %{url}/releases/download/v%{version}/%{name}-%{version}-linux_amd64.tar.gz

%description
fzf is a general-purpose command-line fuzzy finder.
It's an interactive Unix filter for command-line that can be used with any list; files, command history, processes, hostnames, bookmarks, git commits, etc.

%prep
%setup -c fzf

%install
mkdir -p %{buildroot}%{_bindir}
install -m 0755 fzf %{buildroot}%{_bindir}

%files
%{_bindir}/fzf
