Summary:	Xxf86misc library
Summary(pl):	Biblioteka Xxf86misc
Name:		xorg-lib-libXxf86misc
Version:	0.99.2
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/lib/libXxf86misc-%{version}.tar.bz2
# Source0-md5:	6f293994d1b478dfb322ec9c7e182bdb
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xxf86misc library.

%description -l pl
Biblioteka Xxf86misc.

%package devel
Summary:	Header files for libXxf86misc development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXxf86misc
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
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
Summary:	Static libXxf86misc library
Summary(pl):	Biblioteka statyczna libXxf86misc
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

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
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/libXxf86misc.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXxf86misc.so
%{_libdir}/libXxf86misc.la
%{_pkgconfigdir}/xxf86misc.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXxf86misc.a
