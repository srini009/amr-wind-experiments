#!/bin/bash

#MAKE APPROPRIATE CHANGES WHEREVER IT SAYS 'CHANGE ME'
module load cmake
module swap PrgEnv-intel PrgEnv-gnu
module unload darshan
. $HOME/spack/share/spack/setup-env.sh #CHANGE ME
module swap cray-libsci/20.06.1 cray-libsci/20.03.1
export CRAYPE_LINK_TYPE=dynamic
export MPICH_GNI_NDREG_ENTRIES=1024
export PATH=$HOME/serviz/build/examples:$HOME/AMR_WIND_INSTALL/bin:$PATH #CHANGE ME
export PKG_CONFIG_PATH=/usr/lib64/pkgconfig:$HOME/serviz/build/lib/pkgconfig:$PKG_CONFIG_PATH #CHANGE ME
