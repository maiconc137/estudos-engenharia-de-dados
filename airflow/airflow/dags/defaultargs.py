from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(24, 12, 14),
    'email' : ['teste@teste.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}
    
with DAG('defaultdag', description="Dag exemplo",
        default_args=default_args,
        schedule_interval='@hourly', start_date=datetime(2024, 9, 26),
        catchup=False, default_view='graph', tags=['Maicão']) as dag:

    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5", retries=3)
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")

    task1 >> task2 >> task3