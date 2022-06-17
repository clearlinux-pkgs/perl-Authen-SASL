#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Authen-SASL
Version  : 2.16
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/G/GB/GBARR/Authen-SASL-2.16.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GB/GBARR/Authen-SASL-2.16.tar.gz
Summary  : 'SASL Authentication framework'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Authen-SASL-perl = %{version}-%{release}
Requires: perl(GSSAPI)
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)

%description
No detailed description available

%package dev
Summary: dev components for the perl-Authen-SASL package.
Group: Development
Provides: perl-Authen-SASL-devel = %{version}-%{release}
Requires: perl-Authen-SASL = %{version}-%{release}

%description dev
dev components for the perl-Authen-SASL package.


%package perl
Summary: perl components for the perl-Authen-SASL package.
Group: Default
Requires: perl-Authen-SASL = %{version}-%{release}

%description perl
perl components for the perl-Authen-SASL package.


%prep
%setup -q -n Authen-SASL-2.16
cd %{_builddir}/Authen-SASL-2.16

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
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
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

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
