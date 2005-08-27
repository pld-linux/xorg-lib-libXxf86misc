# $Rev: 3323 $, $Date: 2005-08-27 17:42:48 $
#
Summary:	Xxf86misc library
Summary(pl):	Biblioteka Xxf86misc
Name:		xorg-lib-libXxf86misc
Version:	0.99.0
Release:	0.02
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXxf86misc-%{version}.tar.bz2
# Source0-md5:	a8f6eec4acc821b022fdfed89af1deee
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-util-util-macros
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRoot:	%{tmpdir}/libXxf86misc-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xxf86misc library.

%description -l pl
Biblioteka Xxf86misc.


%package devel
Summary:	Header files libXxf86misc development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXxf86misc
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXxf86misc = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-xf86miscproto-devel

%description devel
Xxf86misc library.

This package contains the header files needed to develop programs that
use these libXxf86misc.

%description devel -l pl
Biblioteka Xxf86misc.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXxf86misc.


%package static
Summary:	Static libXxf86misc libraries
Summary(pl):	Biblioteki statyczne libXxf86misc
Group:		Development/Libraries
Requires:	xorg-lib-libXxf86misc-devel = %{version}-%{release}

%description static
Xxf86misc library.

This package contains the static libXxf86misc library.

%description static -l pl
Biblioteka Xxf86misc.

Pakiet zawiera statyczn± bibliotekê libXxf86misc.


%prep
%setup -q -n libXxf86misc-%{version}


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}


%clean
rm -rf $RPM_BUILD_ROOT


%post	-p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,wheel) %{_libdir}/libXxf86misc.so.*


%files devel
%defattr(644,root,root,755)
%{_libdir}/libXxf86misc.la
%attr(755,root,wheel) %{_libdir}/libXxf86misc.so
%{_pkgconfigdir}/xxf86misc.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXxf86misc.a
