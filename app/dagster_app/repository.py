from dagster import repository
from dagster_app.jobs.demo_sync import demo_sync_scheduled_job, demo_sync_job


@repository(
    name='Dagster_Jobs',
    description='Demo jobs'
)
def main_repo():
    return [demo_sync_scheduled_job, demo_sync_job]
