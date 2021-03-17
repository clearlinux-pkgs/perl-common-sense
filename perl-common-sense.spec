#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-common-sense
Version  : 3.75
Release  : 14
URL      : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/common-sense-3.75.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/M/ML/MLEHMANN/common-sense-3.75.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0 GPL-1.0
Requires: perl-common-sense-license = %{version}-%{release}
Requires: perl-common-sense-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
NAME
common::sense - save a tree AND a kitten, use common::sense!
SYNOPSIS
use common::sense;

%package dev
Summary: dev components for the perl-common-sense package.
Group: Development
Provides: perl-common-sense-devel = %{version}-%{release}
Requires: perl-common-sense = %{version}-%{release}

%description dev
dev components for the perl-common-sense package.


%package license
Summary: license components for the perl-common-sense package.
Group: Default

%description license
license components for the perl-common-sense package.


%package perl
Summary: perl components for the perl-common-sense package.
Group: Default
Requires: perl-common-sense = %{version}-%{release}

%description perl
perl components for the perl-common-sense package.


%prep
%setup -q -n common-sense-3.75
cd %{_builddir}/common-sense-3.75

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-common-sense
cp %{_builddir}/common-sense-3.75/LICENSE %{buildroot}/usr/share/package-licenses/perl-common-sense/9a56f3b919dfc8fced3803e165a2e38de62646e5
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/common::sense.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-common-sense/9a56f3b919dfc8fced3803e165a2e38de62646e5

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/common/sense.pm
/usr/lib/perl5/vendor_perl/5.32.1/x86_64-linux-thread-multi/common/sense.pod
