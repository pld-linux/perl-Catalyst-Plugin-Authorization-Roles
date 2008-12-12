#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Catalyst
%define	pnam	Plugin-Authorization-Roles
Summary:	Catalyst::Plugin::Authorization::Roles - Role based authorization for Catalyst based on Catalyst::Plugin::Authentication
#Summary(pl.UTF-8):	
Name:		perl-Catalyst-Plugin-Authorization-Roles
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Catalyst/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	afef214de7c8084c59fad8a07a640059
URL:		http://search.cpan.org/dist/Catalyst-Plugin-Authorization-Roles/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Catalyst >= 5.7
BuildRequires:	perl-Catalyst-Plugin-Authentication >= 0.10003
BuildRequires:	perl-Set-Object >= 1.14
BuildRequires:	perl-UNIVERSAL-isa >= 0.05
BuildRequires:	perl-Test-Exception
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Role based access control is very simple: every user has a list of roles,
which that user is allowed to assume, and every restricted part of the app
makes an assertion about the necessary roles.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Catalyst/Plugin/Authorization/*.pm
%{_mandir}/man3/*
