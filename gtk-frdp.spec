#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
#
Name     : gtk-frdp
Version  : 3.37.1
Release  : 7
URL      : https://gitlab.gnome.org/GNOME/gtk-frdp/-/archive/v3.37.1/gtk-frdp-v3.37.1.tar.gz
Source0  : https://gitlab.gnome.org/GNOME/gtk-frdp/-/archive/v3.37.1/gtk-frdp-v3.37.1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-3.0
Requires: gtk-frdp-data = %{version}-%{release}
Requires: gtk-frdp-lib = %{version}-%{release}
Requires: gtk-frdp-license = %{version}-%{release}
BuildRequires : FreeRDP-dev
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : fuse-dev
BuildRequires : pkgconfig(fuse3)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: update.patch

%description
No detailed description available

%package data
Summary: data components for the gtk-frdp package.
Group: Data

%description data
data components for the gtk-frdp package.


%package dev
Summary: dev components for the gtk-frdp package.
Group: Development
Requires: gtk-frdp-lib = %{version}-%{release}
Requires: gtk-frdp-data = %{version}-%{release}
Provides: gtk-frdp-devel = %{version}-%{release}
Requires: gtk-frdp = %{version}-%{release}

%description dev
dev components for the gtk-frdp package.


%package lib
Summary: lib components for the gtk-frdp package.
Group: Libraries
Requires: gtk-frdp-data = %{version}-%{release}
Requires: gtk-frdp-license = %{version}-%{release}

%description lib
lib components for the gtk-frdp package.


%package license
Summary: license components for the gtk-frdp package.
Group: Default

%description license
license components for the gtk-frdp package.


%prep
%setup -q -n gtk-frdp-v3.37.1
cd %{_builddir}/gtk-frdp-v3.37.1
%patch -P 1 -p1
pushd ..
cp -a gtk-frdp-v3.37.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695737030
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain   builddiravx2
ninja -v -C builddiravx2

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gtk-frdp
cp %{_builddir}/gtk-frdp-v%{version}/COPYING %{buildroot}/usr/share/package-licenses/gtk-frdp/a8a12e6867d7ee39c21d9b11a984066099b6fb6b || :
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/lib64/girepository-1.0/GtkFrdp-0.2.typelib
/usr/share/gir-1.0/*.gir
/usr/share/vala/vapi/gtk-frdp-0.2.deps
/usr/share/vala/vapi/gtk-frdp-0.2.vapi

%files dev
%defattr(-,root,root,-)
/usr/include/gtk-frdp/frdp-display.h
/usr/include/gtk-frdp/frdp-session.h
/usr/include/gtk-frdp/gtk-frdp-version.h
/usr/include/gtk-frdp/gtk-frdp.h
/usr/lib64/pkgconfig/gtk-frdp-0.2.pc

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libgtk-frdp-0.2.so
/usr/lib64/libgtk-frdp-0.2.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gtk-frdp/a8a12e6867d7ee39c21d9b11a984066099b6fb6b
