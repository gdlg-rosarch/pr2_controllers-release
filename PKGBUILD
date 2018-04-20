# Script generated with Bloom
pkgdesc="ROS - Contains the controllers that run in realtime on the PR2 and supporting packages."
url='http://ros.org/wiki/pr2_controllers'

pkgname='ros-kinetic-pr2-controllers'
pkgver='1.10.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-control-toolbox'
'ros-kinetic-ethercat-trigger-controllers'
'ros-kinetic-joint-trajectory-action'
'ros-kinetic-pr2-calibration-controllers'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-pr2-gripper-action'
'ros-kinetic-pr2-head-action'
'ros-kinetic-pr2-mechanism-controllers'
'ros-kinetic-robot-mechanism-controllers'
'ros-kinetic-single-joint-position-action'
)

conflicts=()
replaces=()

_dir=pr2_controllers
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_controllers $srcdir/pr2_controllers
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

