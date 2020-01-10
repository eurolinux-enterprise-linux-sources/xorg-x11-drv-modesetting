%global tarball xf86-video-modesetting
%global moduledir %(pkg-config xorg-server --variable=moduledir )
%global driverdir %{moduledir}/drivers

Summary:   Xorg X11 modesetting video driver
Name:      xorg-x11-drv-modesetting
Version:   0.5.0
Release:   1%{?dist}
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X Hardware Support

Source0:   ftp://ftp.x.org/pub/individual/driver/%{tarball}-%{version}.tar.bz2

# all X hw drivers aren't built on s390 - no need for separate bug
ExcludeArch: s390 s390x

BuildRequires: xorg-x11-server-sdk >= 1.10.99.902
BuildRequires: libX11-devel
BuildRequires: libdrm-devel
BuildRequires: libXext-devel

Requires: Xorg %(xserver-sdk-abi-requires ansic)
Requires: Xorg %(xserver-sdk-abi-requires videodrv)

%description 
X.Org X11 modesetting video driver - basic modesetting fallback driver.

%prep
%setup -q -n %{tarball}-%{version}

%build
%configure --disable-static
make

%install
make install DESTDIR=$RPM_BUILD_ROOT

# FIXME: Remove all libtool archives (*.la) from modules directory.  This
# should be fixed in upstream Makefile.am or whatever.
find $RPM_BUILD_ROOT -regex ".*\.la$" | xargs rm -f --

%files
%{driverdir}/modesetting_drv.so
%{_mandir}/man4/modesetting.4*
%doc COPYING README

%changelog
* Thu Sep 13 2012 Adam Jackson <ajax@redhat.com> 0.5.0-1
- modesetting 0.5.0
- Add ppc* to arches

* Mon Aug 20 2012 Daniel Mach <dmach@redhat.com> - 0.4.0-1
- Initial EL6 import.
