Summary:	xlogo application - X Window System logo
Summary(pl.UTF-8):	Aplikacja xlogo - logo X Window System
Name:		xorg-app-xlogo
Version:	1.0.6
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	https://xorg.freedesktop.org/releases/individual/app/xlogo-%{version}.tar.xz
# Source0-md5:	5b74069cab9e1247dfff4336b21956ab
URL:		https://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXaw-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXft-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel >= 1.0.0
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xz
Requires:	xorg-lib-libXt >= 1.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The xlogo application simply displays the X Window System logo.

%description -l pl.UTF-8
Aplikacja xlogo po prostu wyświetla logo X Window System.

%prep
%setup -q -n xlogo-%{version}

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
%doc COPYING ChangeLog README.md
%attr(755,root,root) %{_bindir}/xlogo
%{_datadir}/X11/app-defaults/XLogo*
%{_mandir}/man1/xlogo.1*
