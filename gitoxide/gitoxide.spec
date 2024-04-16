%global debug_package %{nil}

Name:       gitoxide
Version:    0.62
Release:    1%{?dist}
Summary:    An idiomatic, lean, fast & safe pure Rust implementation of Git

License:    MIT
URL:        https://github.com/Byron/gitoxide
Source0:    %{url}/archive/refs/tags/gix-v%{version}.tar.gz

%if 0%{?el8}
%else
BuildRequires: cargo >= 1.39
BuildRequires: rust >= 1.39
%endif
BuildRequires: cmake
BuildRequires: openssl-devel
Requires: zlib

%description
gitoxide is an implementation of git written in Rust for developing future-proof applications which strive for correctness and performance while providing a pleasant and unsurprising developer experience.

%prep
%setup -n gitoxide-gix-v%{version}

%if 0%{?el8}
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
%endif


%install
export CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_OPT_LEVEL=3
%if 0%{?el8}
  $HOME/.cargo/bin/cargo install --root=%{buildroot}%{_prefix} --path=.
%else
  cargo install --root=%{buildroot}%{_prefix} --path=.
%endif

rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json
strip --strip-all %{buildroot}%{_bindir}/*


%files
%license LICENSE-MIT
%doc README.md
%{_bindir}/ein
%{_bindir}/gix
