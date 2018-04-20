# Script generated with Bloom
pkgdesc="ROS - Controllers to operate the digital output of the motor controller boards and the projector board. This package has not been reviewed and should be considered unstable."
url='http://www.ros.org/wiki/ethercat_trigger_controllers'

pkgname='ros-kinetic-ethercat-trigger-controllers'
pkgver='1.10.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('libtool'
'ros-kinetic-catkin'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-message-generation'
'ros-kinetic-pluginlib'
'ros-kinetic-pr2-controller-interface'
'ros-kinetic-realtime-tools'
'ros-kinetic-roscpp'
'ros-kinetic-std-msgs'
)

depends=('libtool'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-pluginlib'
'ros-kinetic-pr2-controller-interface'
'ros-kinetic-realtime-tools'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
)

conflicts=()
replaces=()

_dir=ethercat_trigger_controllers
source=()
md5sums=()

prepare() {
    cp -R $startdir/ethercat_trigger_controllers $srcdir/ethercat_trigger_controllers
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

