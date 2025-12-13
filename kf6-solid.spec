%define major %(echo %{version} |cut -d. -f1-2)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)

%define libname %mklibname KF6Solid
%define devname %mklibname KF6Solid -d
#define git 20240217

Name: kf6-solid
Version: 6.21.0
Release: %{?git:0.%{git}.}1
%if 0%{?git:1}
Source0: https://invent.kde.org/frameworks/solid/-/archive/master/solid-master.tar.bz2#/solid-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/frameworks/%{major}/solid-%{version}.tar.xz
%endif
Summary: Desktop hardware abstraction
URL: https://invent.kde.org/frameworks/solid
License: CC0-1.0 LGPL-2.0+ LGPL-2.1 LGPL-3.0
Group: System/Libraries
BuildRequires: cmake
BuildRequires: cmake(ECM)
BuildRequires: python
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Network)
BuildRequires: cmake(Qt6Test)
BuildRequires: cmake(Qt6QmlTools)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(Qt6GuiTools)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6DBusTools)
BuildRequires: cmake(Qt6Xml)
BuildRequires: doxygen
BuildRequires: cmake(Qt6ToolsTools)
BuildRequires: cmake(Qt6)
BuildRequires: cmake(Qt6QuickTest)
BuildRequires: cmake(Qt6Concurrent)
BuildRequires: flex
BuildRequires: bison
BuildRequires: pkgconfig(libimobiledevice-1.0)
BuildRequires: pkgconfig(libplist-2.0)
BuildRequires: pkgconfig(mount)
BuildRequires: pkgconfig(libudev)
Requires: %{libname} = %{EVRD}

%description
Desktop hardware abstraction

%package -n %{libname}
Summary: Desktop hardware abstraction
Group: System/Libraries
Requires: %{name} = %{EVRD}
# DBus services accessed by solid
Requires: udev
Requires: udisks
Requires: media-player-info

%description -n %{libname}
Desktop hardware abstraction

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

Desktop hardware abstraction

%prep
%autosetup -p1 -n solid-%{?git:master}%{!?git:%{version}}
%cmake \
	-DBUILD_QCH:BOOL=ON \
	-DBUILD_WITH_QT6:BOOL=ON \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%find_lang %{name} --all-name --with-qt --with-html

%files -f %{name}.lang
%{_datadir}/qlogging-categories6/solid.*
%{_bindir}/solid-hardware6

%files -n %{devname}
%{_includedir}/KF6/Solid
%{_libdir}/cmake/KF6Solid

%files -n %{libname}
%{_libdir}/libKF6Solid.so*
