# Script generated with Bloom
pkgdesc="ROS - The pr2_mechanism_controllers package contains realtime controllers that are meant for specific mechanisms of the PR2."
url='http://ros.org/pr2_mechanism_controllers'

pkgname='ros-kinetic-pr2-mechanism-controllers'
pkgver='1.10.14_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-control-toolbox'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-filters'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-generation'
'ros-kinetic-nav-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-pr2-controller-interface'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-pr2-mechanism-msgs'
'ros-kinetic-pr2-msgs'
'ros-kinetic-realtime-tools'
'ros-kinetic-robot-mechanism-controllers'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
)

depends=('ros-kinetic-angles'
'ros-kinetic-control-toolbox'
'ros-kinetic-diagnostic-msgs'
'ros-kinetic-diagnostic-updater'
'ros-kinetic-filters'
'ros-kinetic-geometry-msgs'
'ros-kinetic-message-runtime'
'ros-kinetic-nav-msgs'
'ros-kinetic-pluginlib'
'ros-kinetic-pr2-controller-interface'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-pr2-mechanism-model'
'ros-kinetic-pr2-mechanism-msgs'
'ros-kinetic-pr2-msgs'
'ros-kinetic-realtime-tools'
'ros-kinetic-robot-mechanism-controllers'
'ros-kinetic-rosconsole'
'ros-kinetic-roscpp'
'ros-kinetic-rospy'
'ros-kinetic-std-msgs'
'ros-kinetic-tf'
'ros-kinetic-visualization-msgs'
)

conflicts=()
replaces=()

_dir=pr2_mechanism_controllers
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_mechanism_controllers $srcdir/pr2_mechanism_controllers
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

