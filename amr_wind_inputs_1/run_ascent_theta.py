import os
from random import randint

import radical.pilot as rp

# All pre-set resource configs:
#   https://github.com/radical-cybertools/radical.pilot/tree/devel/src/radical/pilot/configs

RESOURCE_LABEL = 'anl.theta'
PROJECT_NAME = 'HEP_on_HPC'   # appropriate project name should be used
QUEUE_NAME = 'debug-flat-quad'  # if not set then the default one is used
ACCESS_SCHEMA = 'local'
NUM_CORES_PER_NODE = 64

NUM_TASKS = 1
NUM_NODES = 8
RUN_TIME = 15  # in min

# Get executable:
#   wget https://raw.githubusercontent.com/radical-cybertools/radical.pilot/devel/examples/hello_rp.sh
#   chmod +x hello_rp.sh


input_staging_arr = [
        {'source': 'pilot:///damBreak.i', 
            'target': 'task:///damBreak.i', 
            'action': rp.LINK},
        {'source': 'pilot:///ascent_actions.yaml', 
            'target': 'task:///ascent_actions.yaml', 
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
            'input_staging': ['/home/sramesh/VIZ_SERVICE/experiments/amr_wind_inputs_1/damBreak.i', '/home/sramesh/VIZ_SERVICE/experiments/ascent_actions.yaml']})))
        tds = []
        for _num in range(1):
            tds.append(rp.TaskDescription({
                'cpu_processes': 240,
                'cpu_threads': 1,
                'cpu_process_type': rp.MPI,
                'pre_exec': ['source /home/sramesh/VIZ_SERVICE/experiments/cleanup.sh', 'module unload darshan', 'source /home/sramesh/VIZ_SERVICE/theta_sourceme.sh', 'source /home/sramesh/VIZ_SERVICE/experiments/amr_wind_inputs_1/sourceme.sh'],
                'executable': '/home/sramesh/VIZ_SERVICE/ascent_microservice/build/examples/example-server',
                'stdout': 'STDOUT',
                'arguments': ['-a', 'ofi+gni'],
                'input_staging': input_staging_arr}))
        for _num in range(NUM_TASKS):
            task_id = 'export AMS_TASK_ID='+str(_num+1)
            tds.append(rp.TaskDescription({
                'cpu_processes': 240, 
                'cpu_threads': 1,
                'cpu_process_type': rp.MPI,
                'pre_exec': ['source ~/VIZ_SERVICE/theta_sourceme.sh', 'module unload darshan', 'source ~/VIZ_SERVICE/experiments/amr_wind_inputs_1/sourceme.sh',task_id],
                'executable': '/home/sramesh/VIZ_SERVICE/AMR_WIND_INSTALL/bin/amr_wind',
                'stdout': 'STDOUT',
                'arguments': ['damBreak.i'],
                'input_staging': input_staging_arr}))
        tmgr.submit_tasks(tds)
        tmgr.wait_tasks()
    finally:
        session.close(download=True)
