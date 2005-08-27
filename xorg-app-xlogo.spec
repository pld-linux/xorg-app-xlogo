# $Rev: 3400 $, $Date: 2005-08-27 17:42:47 $
#
Summary:	xlogo application
Summary(pl):	Aplikacja xlogo
Name:		xorg-app-xlogo
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/app/xlogo-%{version}.tar.bz2
# Source0-md5:	d4aa73acb70b58cf162cad07d0521163
Patch0:		xlogo-man.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXprintUtil-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-util-util-macros
BuildRequires:	pkgconfig >= 0.19
BuildRoot:	%{tmpdir}/xlogo-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
xlogo application.

%description -l pl
Aplikacja xlogo.


%prep
%setup -q -n xlogo-%{version}
%patch0 -p1


%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%{_sysconfdir}/X11/app-defaults/*
%attr(755,root,wheel) %{_bindir}/*
%{_mandir}/man1/*.1*
