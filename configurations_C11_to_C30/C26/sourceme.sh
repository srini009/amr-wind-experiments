#!/bin/bash
export AMS_SERVER_ADDR_FILE=$HOME/serviz-experiments/configurations_C11_to_C30/C26/addr.mercury
export AMS_NODE_ADDR_FILE=$HOME/serviz-experiments/configurations_C11_to_C30/C26/nodes.mercury
export AMS_WORKING_DIR=`pwd`
export AMS_USE_LOCAL_ASCENT=0
export AMS_NUM_SERVERS=64
export AMS_NUM_SERVERS_PER_INSTANCE=64
export AMS_NUM_SERVER_INSTANCES=1
export MARGO_ENABLE_PROFILING=0
export AMS_SERVER_MODE=0
export MPICH_GNI_NDREG_ENTRIES=1024
