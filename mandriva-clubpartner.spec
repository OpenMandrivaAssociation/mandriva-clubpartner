%define name mandriva-clubpartner
%define version 0.05
%define release %mkrel 3

Summary: Mandriva Club authentication system
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{name}-%{version}.tar.bz2
License: GPL
Group: System/Servers
Url: http://svn.mandriva.com/cgi-bin/viewvc.cgi/web/clubpartner/
Requires: apache-mod_authnz_external
%if %mdkversion < 201010
Requires(post):   rpm-helper
Requires(postun):   rpm-helper
%endif
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}

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
rm -rf %{buildroot}

%post
%if %mdkversion < 201010
%_post_webapp
%endif

%postun
%if %mdkversion < 201010
%_postun_webapp
%endif

%files
%defattr(-,root,root)
%doc README
%_bindir/*
%_mandir/man?/*
%dir %attr(0755, apache, apache) /var/cache/clubauth
%config(noreplace) %_webconfdir/webapps.d/*.conf
