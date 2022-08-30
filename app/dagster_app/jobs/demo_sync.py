import shutil
import time
from pathlib import Path
from uuid import uuid4

from dagster import (op, graph, ScheduleDefinition, DefaultScheduleStatus, In, Dict, Out, Output)

from dagster_app.schemas import main_config_schema, get_main_config


@op(
    description='Generate dummy files.',
    required_resource_keys={"main_config"},
    out=Out(Dict)
)
def generate_files(context):
    demo_conf = context.resources.main_config['demo_config_group']
    src_dir = demo_conf["source_dir"]
    context.log.info(f'Generating files in {src_dir} directory.')
    limit = demo_conf['limit']
    Path(src_dir).mkdir(exist_ok=True, parents=True)

    files_list = []
    for _ in range(limit):
        file_location = Path(src_dir).joinpath(f'{str(uuid4())}.txt')
        with open(str(file_location), 'w') as fl:
            fl.write(str(uuid4()))
        context.log.info(f'File has been generated {file_location}')
        files_list.append(str(file_location))
        time.sleep(0.5)

    return Output({
        'src_files': files_list
    })


@op(
    description='Move files',
    required_resource_keys={"main_config"},
    ins={'data': In(Dict)},
)
def move_files(context, data):
    demo_conf = context.resources.main_config['demo_config_group']
    dest_dir = demo_conf["destination_dir"]
    Path(dest_dir).mkdir(exist_ok=True, parents=True)
    src_files = data['src_files']
    for fl_src in src_files:
        new_location = shutil.move(fl_src, dest_dir)
        context.log.info(f'File moved from {fl_src} to {new_location}')
        time.sleep(0.5)


@graph(
    tags={'demo_job': '1'}
)
def demo_sync_graph():
    move_files(generate_files())


def execution_check(context):
    """Function returns True if pipeline can be executed."""
    return True


demo_sync_job = demo_sync_graph.to_job(
    name='demo_sync_job',
    resource_defs=main_config_schema(),
    config=get_main_config()
)

demo_sync_scheduled_job = ScheduleDefinition(
    job=demo_sync_job,
    cron_schedule="*/20 * * * *",
    run_config=get_main_config(),
    should_execute=execution_check,
    default_status=DefaultScheduleStatus.RUNNING
)

if __name__ == "__main__":
    demo_sync_job.execute_in_process(run_config=get_main_config())
