# Script generated with Bloom
pkgdesc="ROS - The PR2 head action is a node that provides an action interface for pointing the head of the PR2. It passes trajectory goals to the controller, and reports success when they have finished executing."
url='http://ros.org/wiki/pr2_head_action'

pkgname='ros-kinetic-pr2-head-action'
pkgver='1.10.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-catkin'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-parser'
'ros-kinetic-message-filters'
'ros-kinetic-orocos-kdl'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-trajectory-msgs'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-geometry-msgs'
'ros-kinetic-kdl-parser'
'ros-kinetic-message-filters'
'ros-kinetic-orocos-kdl'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-sensor-msgs'
'ros-kinetic-tf'
'ros-kinetic-tf-conversions'
'ros-kinetic-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=pr2_head_action
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_head_action $srcdir/pr2_head_action
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

