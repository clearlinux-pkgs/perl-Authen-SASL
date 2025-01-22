#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Authen-SASL
Version  : 2.1700
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/E/EH/EHUELS/Authen-SASL-2.1700.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/EH/EHUELS/Authen-SASL-2.1700.tar.gz
Summary  : 'SASL Authentication framework'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Authen-SASL-license = %{version}-%{release}
Requires: perl-Authen-SASL-perl = %{version}-%{release}
Requires: perl(GSSAPI)
BuildRequires : buildreq-cpan
BuildRequires : perl(Test::Pod)
BuildRequires : perl(Test::Pod::Coverage)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Authen::SASL - SASL Authentication framework
DESCRIPTION
-----------
SASL is a generic mechanism for authentication used by several network
protocols. Authen::SASL provides an implementation framework that all
protocols should be able to share.

%package dev
Summary: dev components for the perl-Authen-SASL package.
Group: Development
Provides: perl-Authen-SASL-devel = %{version}-%{release}
Requires: perl-Authen-SASL = %{version}-%{release}

%description dev
dev components for the perl-Authen-SASL package.


%package license
Summary: license components for the perl-Authen-SASL package.
Group: Default

%description license
license components for the perl-Authen-SASL package.


%package perl
Summary: perl components for the perl-Authen-SASL package.
Group: Default
Requires: perl-Authen-SASL = %{version}-%{release}

%description perl
perl components for the perl-Authen-SASL package.


%prep
%setup -q -n Authen-SASL-2.1700
cd %{_builddir}/Authen-SASL-2.1700

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
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
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Authen-SASL
cp %{_builddir}/Authen-SASL-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Authen-SASL/fe8bab1412f3f983e990e8ecabd74a1e786846b0 || :
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
/usr/share/man/man3/Authen::SASL.3
/usr/share/man/man3/Authen::SASL::Perl.3
/usr/share/man/man3/Authen::SASL::Perl::ANONYMOUS.3
/usr/share/man/man3/Authen::SASL::Perl::CRAM_MD5.3
/usr/share/man/man3/Authen::SASL::Perl::DIGEST_MD5.3
/usr/share/man/man3/Authen::SASL::Perl::EXTERNAL.3
/usr/share/man/man3/Authen::SASL::Perl::GSSAPI.3
/usr/share/man/man3/Authen::SASL::Perl::LOGIN.3
/usr/share/man/man3/Authen::SASL::Perl::PLAIN.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Authen-SASL/fe8bab1412f3f983e990e8ecabd74a1e786846b0

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
