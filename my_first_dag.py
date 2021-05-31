from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
import os

print(os.getcwd())


args = {'owner':'shankar'}

dag = DAG(
    dag_id = 'example_bash_operator',
    default_args= args,
    schedule_interval='0 0 * * *',
    start_date= days_ago(2),
    tags = ['example','eaxample2']
    )

run_this_first = DummyOperator(
    task_id = "run_this_first",
    dag = dag
)

run_this_second = BashOperator(
    task_id = 'run_this_second',
    bash_command = 'echo 1',
    dag = dag
)

run_this_third = BashOperator(
    task_id = 'run_this_third',
    bash_command = 'pwd',
    dag = dag
)

run_this_first >> run_this_second >> run_this_third
