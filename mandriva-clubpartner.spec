%define name mandriva-clubpartner
%define version 0.03
%define release %mkrel 1

Summary: Mandriva Club authentication system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Servers
Url: http://club.mandriva.com
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildArch: noarch
Requires: apache-mod_authnz_external

%description
This package contains script and config files to perform a direct
mandriva club member authentication 

%prep
%setup -q

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %buildroot
%makeinstall_std

mkdir -p %buildroot/var/cache/clubauth

mkdir -p %buildroot/%_webconfdir/webapps.d

cp httpd/*.conf %buildroot/%_webconfdir/webapps.d/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_bindir/*
%dir %attr(0755, apache, apache) /var/cache/clubauth
%_webconfdir/webapps.d/*.conf

%post
%_post_webapp

%postun
%_postun_webapp



