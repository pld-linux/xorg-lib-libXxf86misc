Summary:	XFree86-Misc X extension library
Summary(pl.UTF-8):	Biblioteka rozszerzenia X XFree86-Misc
Name:		xorg-lib-libXxf86misc
Version:	1.0.2
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXxf86misc-%{version}.tar.bz2
# Source0-md5:	51fed53e8de067d4b8666f75a0212400
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-proto-xf86miscproto-devel
BuildRequires:	xorg-util-util-macros >= 1.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
XFree86-Misc X extension library.

%description -l pl.UTF-8
Biblioteka rozszerzenia X XFree86-Misc.

%package devel
Summary:	Header files for libXxf86misc library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXxf86misc
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-proto-xf86miscproto-devel

%description devel
XFree86-Misc X extension library.

This package contains the header files needed to develop programs that
use libXxf86misc.

%description devel -l pl.UTF-8
Biblioteka rozszerzenia X XFree86-Misc.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXxf86misc.

%package static
Summary:	Static libXxf86misc library
Summary(pl.UTF-8):	Biblioteka statyczna libXxf86misc
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
XFree86-Misc X extension library.

This package contains the static libXxf86misc library.

%description static -l pl.UTF-8
Biblioteka rozszerzenia X XFree86-Misc.

Pakiet zawiera statyczną bibliotekę libXxf86misc.

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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXxf86misc.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libXxf86misc.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXxf86misc.so
%{_libdir}/libXxf86misc.la
%{_pkgconfigdir}/xxf86misc.pc
%{_mandir}/man3/XF86Misc*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXxf86misc.a
