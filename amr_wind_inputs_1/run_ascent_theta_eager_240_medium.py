import os
from random import randint

import radical.pilot as rp

# All pre-set resource configs:
#   https://github.com/radical-cybertools/radical.pilot/tree/devel/src/radical/pilot/configs

RESOURCE_LABEL = 'anl.theta'
PROJECT_NAME = 'radix-io'   # appropriate project name should be used
QUEUE_NAME = 'default'  # if not set then the default one is used
ACCESS_SCHEMA = 'local'
NUM_CORES_PER_NODE = 64

NUM_TASKS = 64
NUM_NODES = 257
RUN_TIME = 50  # in min

# Get executable:
#   wget https://raw.githubusercontent.com/radical-cybertools/radical.pilot/devel/examples/hello_rp.sh
#   chmod +x hello_rp.sh


input_staging_arr = [
        {'source': 'pilot:///mediumlarge240.damBreak.i', 
            'target': 'task:///mediumlarge240.damBreak.i', 
            'action': rp.LINK},
        {'source': 'pilot:///default.yaml', 
            'target': 'task:///default.yaml', 
            'action': rp.LINK}]

if __name__ == '__main__':
    session = rp.Session()
    try:
        pmgr = rp.PilotManager(session=session)
        tmgr = rp.TaskManager(session=session)
        tmgr.add_pilots(pmgr.submit_pilots(rp.PilotDescription({
            'resource': RESOURCE_LABEL,
            'queue': QUEUE_NAME,
            'project': PROJECT_NAME,
            'access_schema': ACCESS_SCHEMA,
            'cores': NUM_NODES * NUM_CORES_PER_NODE,
            'runtime': RUN_TIME,
            'input_staging': ['/home/sramesh/VIZ_SERVICE/experiments/amr_wind_inputs_1/mediumlarge240.damBreak.i',
                '/home/sramesh/VIZ_SERVICE/experiments/amr_wind_inputs_1/ascent_action_files/default.yaml']})))
        tds = []
        for _num in range(1):
            tds.append(rp.TaskDescription({
                'cpu_processes': 60,
                'cpu_threads': 1,
                'cpu_process_type': rp.MPI,
                'pre_exec': ['source /home/sramesh/VIZ_SERVICE/theta_sourceme.sh', 'source /home/sramesh/VIZ_SERVICE/experiments/amr_wind_inputs_1/sourcemeeager240.sh'],
                'executable': '/home/sramesh/VIZ_SERVICE/ascent_microservice/build/examples/example-server',
                'stdout': 'STDOUT',
                'arguments': ['-a', 'ofi+gni'],
                'input_staging': input_staging_arr}))
        for _num in range(NUM_TASKS):
            task_id = 'export AMS_TASK_ID='+str(_num+1)
            server_instance_id = 'export AMS_SERVER_INSTANCE_ID=' + str(_num % 2)
            tds.append(rp.TaskDescription({
                'cpu_processes': 240, 
                'cpu_threads': 1,
                'cpu_process_type': rp.MPI,
                'pre_exec': ['source ~/VIZ_SERVICE/theta_sourceme.sh', 'source ~/VIZ_SERVICE/experiments/amr_wind_inputs_1/sourcemeeager240.sh', 'source ~/VIZ_SERVICE/experiments/amr_wind_inputs_1/checkserver.sh', task_id, server_instance_id],
                'executable': '/home/sramesh/VIZ_SERVICE/AMR_WIND_INSTALL/bin/amr_wind',
                'stdout': 'STDOUT',
                'arguments': ['mediumlarge240.damBreak.i'],
                'input_staging': input_staging_arr}))
        tmgr.submit_tasks(tds)
        tmgr.wait_tasks()
    finally:
        session.close(download=True)
