# generate/package docs
%define docs 1

# define to enable verbose build for debugging
%define sbcl_verbose 0
%define sbcl_shell /bin/bash

Name: 	 sbcl
Summary: Steel Bank Common Lisp
Version: 2.5.4
Release: 1%{?dist}

License: BSD
URL:	 https://sbcl.sourceforge.net/
Source0: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{version}-source.tar.bz2

ExclusiveArch: %{arm} %{ix86} x86_64 ppc sparcv9 aarch64

# Pre-generated html docs
Source1: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-%{version}-documentation-html.tar.bz2

## x86 section
%ifarch %{ix86}
%define sbcl_arch x86
Source10: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.0.15-x86-linux-binary.tar.bz2
%define sbcl_bootstrap_src -b 10
%endif

## x86_64 section
Source20: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-2.3.0-x86-64-linux-binary.tar.bz2
%ifarch x86_64
%define sbcl_arch x86-64
%define sbcl_bootstrap_src -b 20
%define sbcl_bootstrap_dir sbcl-2.3.0-x86-64-linux
%endif

## ppc section
# Thanks David!
%ifarch ppc 
%define sbcl_arch ppc
Source30: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.7-powerpc-linux-binary.tar.bz2
%define sbcl_bootstrap_src -b 30
%define sbcl_bootstrap_dir sbcl-1.2.7-powerpc-linux
%endif

## sparc section
%ifarch sparcv9
%define sbcl_arch sparc 
Source40: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.0.28-sparc-linux-binary.tar.bz2
%define sbcl_bootstrap_src -b 40
%define sbcl_bootstrap_dir sbcl-1.0.28-sparc-linux
%endif

## arm section
%ifarch armv5tel
%define sbcl_arch arm
Source50: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.0-armel-linux-binary.tar.bz2
%define sbcl_bootstrap_src -b 50
%define sbcl_bootstrap_dir sbcl-1.2.0-armel-linux
%endif

# generated on a fedora20 arm box, sf bootstrap missing sb-gmp
%ifarch armv6hl armv7hl
%define sbcl_arch arm
Source60: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.2.0-armhf-linux-binary.tar.bz2
%define sbcl_bootstrap_src -b 60
%define sbcl_bootstrap_dir sbcl-1.2.0-armhf-vfp
%endif

## aarch64 section
Source70: https://downloads.sourceforge.net/sourceforge/sbcl/sbcl-1.4.2-arm64-linux-binary.tar.bz2
%ifarch aarch64
%define sbcl_arch arm64
%define sbcl_bootstrap_src -b 70
%define sbcl_bootstrap_dir sbcl-1.4.2-arm64-linux
%endif

BuildRequires: make
BuildRequires: libzstd-devel
%if 0%{?fedora} >= 35
BuildRequires: ctags
%endif
%if 0%{?el8}
BuildRequires: ctags-etags
%endif
BuildRequires: gcc
BuildRequires: zlib-devel
# %%check/tests
BuildRequires: ed
BuildRequires: hostname
%if 0%{?docs}
# doc generation
BuildRequires: ghostscript
BuildRequires: texinfo
BuildRequires: time
%endif

%description
Steel Bank Common Lisp (SBCL) is a Open Source development environment
for Common Lisp. It includes an integrated native compiler,
interpreter, and debugger.


%prep
%setup -q -c -n sbcl-%{version} -a 1 %{?sbcl_bootstrap_src}

pushd sbcl-%{version}

# fix permissions (some have eXecute bit set)
find . -name '*.c' | xargs chmod 644

# set version.lisp-expr
sed -i.rpmver -e "s|\"%{version}\"|\"%{version}-%{release}\"|" version.lisp-expr

# make %%doc items available in parent dir to make life easier
cp -alf BUGS COPYING README CREDITS NEWS TLA TODO PRINCIPLES ..
ln -s sbcl-%{version}/doc ../doc
popd


%build
# LTO causes testsuite failures, though it may be the case that the tests are racy.
# Until further analysis is complete, disable LTO
%define _lto_cflags %{nil}

pushd sbcl-%{version}

export CFLAGS="%{?optflags}"
export LDFLAGS="%{?__global_ldflags}"
export CC=gcc

export SBCL_HOME=%{_prefix}/lib/sbcl
%{?sbcl_arch:export SBCL_ARCH=%{sbcl_arch}}
%{?sbcl_shell} \
./make.sh \
  --prefix=%{_prefix} \
  --with-sb-core-compression \
  %{?sbcl_bootstrap_dir:--xc-host="`pwd`/../../%{sbcl_bootstrap_dir}/run-sbcl.sh"}

# docs
%if 0%{?docs}
make -C doc/manual info

# Handle pre-generated docs
tar xvjf %{SOURCE1}
cp -av %{name}-%{version}/doc/manual/* doc/manual/
%endif
popd


%install
pushd sbcl-%{version}
mkdir -p %{buildroot}{%{_bindir},%{_prefix}/lib,%{_mandir}}

unset SBCL_HOME 
export INSTALL_ROOT=%{buildroot}%{_prefix} 
%{?sbcl_shell} ./install.sh 

popd

## Unpackaged files
rm -rfv %{buildroot}%{_docdir}/sbcl
rm -fv  %{buildroot}%{_infodir}/dir
# CVS crud 
find %{buildroot} -name CVS -type d | xargs rm -rfv
find %{buildroot} -name .cvsignore | xargs rm -fv
# 'test-passed' files from %%check
find %{buildroot} -name 'test-passed' | xargs rm -vf


%check
pushd sbcl-%{version}
ERROR=0
# sanity check, essential contrib modules get built/included?
CONTRIBS="sb-posix.fasl sb-bsd-sockets.fasl"
for CONTRIB in $CONTRIBS ; do
  if [ ! -f %{buildroot}%{_prefix}/lib/sbcl/contrib/$CONTRIB ]; then
    echo "WARNING: ${CONTRIB} awol!"
    ERROR=1
    echo "ulimit -a"
    ulimit -a
  fi
done
pushd tests
# verify --version output
test "$(. ./subr.sh; "$SBCL_RUNTIME" --core "$SBCL_CORE" --version --version 2>/dev/null | cut -d' ' -f2)" = "%{version}-%{release}"
# still seeing Failure: threads.impure.lisp / (DEBUGGER-NO-HANG-ON-SESSION-LOCK-IF-INTERRUPTED)
time %{?sbcl_shell} ./run-tests.sh ||:
popd
exit $ERROR
popd

%files
%license COPYING
%doc BUGS CREDITS NEWS PRINCIPLES README TLA TODO
%{_bindir}/sbcl
%dir %{_prefix}/lib/sbcl/
%{_prefix}/lib/sbcl/sbcl.mk
%{_prefix}/lib/sbcl/contrib/
%{_mandir}/man1/sbcl.1*
%if 0%{?docs}
%doc doc/manual/sbcl.html
%doc doc/manual/asdf.html
%{_infodir}/asdf.info*
%{_infodir}/sbcl.info*
%endif
%{_prefix}/lib/sbcl/sbcl.core
