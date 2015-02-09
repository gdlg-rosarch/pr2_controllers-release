Name:           ros-indigo-ethercat-trigger-controllers
Version:        1.10.13
Release:        0%{?dist}
Summary:        ROS ethercat_trigger_controllers package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/ethercat_trigger_controllers
Source0:        %{name}-%{version}.tar.gz

Requires:       libtool
Requires:       libtool-ltdl-devel
Requires:       ros-indigo-diagnostic-msgs
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pluginlib
Requires:       ros-indigo-pr2-controller-interface
Requires:       ros-indigo-realtime-tools
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-rospy
Requires:       ros-indigo-std-msgs
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-diagnostic-msgs
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pluginlib
BuildRequires:  ros-indigo-pr2-controller-interface
BuildRequires:  ros-indigo-realtime-tools
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-std-msgs

%description
Controllers to operate the digital output of the motor controller boards and the
projector board. This package has not been reviewed and should be considered
unstable.

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
* Mon Feb 09 2015 Devon Ash <dash@clearpathrobotics.com> - 1.10.13-0
- Autogenerated by Bloom

* Tue Jan 13 2015 Austin Hendrix <ahendrix@willowgarage.com> - 1.10.12-0
- Autogenerated by Bloom
