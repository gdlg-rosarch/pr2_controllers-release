# Script generated with Bloom
pkgdesc="ROS - The pr2_gripper_action provides an action interface for using the gripper. Users can specify what position to move to (while limiting the force) and the action will report success when the position is reached or failure when the gripper cannot move any longer."
url='http://ros.org/wiki/pr2_gripper_action'

pkgname='ros-kinetic-pr2-gripper-action'
pkgver='1.10.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-pr2-mechanism-controllers'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-robot-mechanism-controllers'
'ros-kinetic-roscpp'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-pr2-mechanism-controllers'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-robot-mechanism-controllers'
'ros-kinetic-roscpp'
)

conflicts=()
replaces=()

_dir=pr2_gripper_action
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_gripper_action $srcdir/pr2_gripper_action
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

