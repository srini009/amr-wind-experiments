#!/bin/bash
export AMS_SERVER_ADDR_FILE=/home/sramesh/VIZ_SERVICE/experiments/addr.mercury
export AMS_NODE_ADDR_FILE=/home/sramesh/VIZ_SERVICE/experiments/nodes.mercury
export AMS_ACTIONS_FILE=/home/sramesh/VIZ_SERVICE/experiments/amr_wind_inputs_1/ascent_action_files/default.yaml
export AMS_WORKING_DIR=`pwd`
export AMS_USE_LOCAL_ASCENT=0
export AMS_NUM_SERVERS=60
export AMS_NUM_SERVERS_PER_INSTANCE=60
export AMS_NUM_SERVER_INSTANCES=1
export MARGO_ENABLE_PROFILING=0
export AMS_SERVER_MODE=1
export AMS_USE_LOCAL_ASCENT=0
export MPICH_GNI_NDREG_ENTRIES=1024
export AMS_MAX_STEP=50
export AMS_NUM_CLIENTS_PER_SERVER=60
