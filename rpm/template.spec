Name:           ros-indigo-stage
Version:        4.1.1
Release:        6%{?dist}
Summary:        ROS stage package

Group:          Development/Libraries
License:        GPL
URL:            http://rtv.github.com/Stage
Source0:        %{name}-%{version}.tar.gz

Requires:       fltk-devel
Requires:       gtk2-devel
Requires:       libjpeg-turbo-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       ros-indigo-catkin
BuildRequires:  cmake
BuildRequires:  fltk-devel
BuildRequires:  gtk2-devel
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  pkgconfig

%description
Mobile robot simulator http://rtv.github.com/Stage

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Sep 21 2015 William Woodall <william@osrfoundation.org> - 4.1.1-6
- Autogenerated by Bloom

* Wed Sep 16 2015 William Woodall <william@osrfoundation.org> - 4.1.1-5
- Autogenerated by Bloom

* Tue Mar 24 2015 William Woodall <william@osrfoundation.org> - 4.1.1-4
- Autogenerated by Bloom

* Fri Feb 27 2015 William Woodall <william@osrfoundation.org> - 4.1.1-3
- Autogenerated by Bloom

