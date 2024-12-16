from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta
    
with DAG('pool', description="pool",
        schedule_interval=None, start_date=datetime(2024,12,16),
        catchup=False, default_view='graph', tags=['Dummy']) as dag:

    task1 = BashOperator(task_id="tsk1", bash_command="sleep 1", pool="meupool")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 1", pool="meupool", priority_weight=5)
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 1", pool="meupool")
    task4 = BashOperator(task_id="tsk4", bash_command="sleep 1", pool="meupool")
    task5 = BashOperator(task_id="tsk5", bash_command="sleep 1", pool="meupool", priority_weight=10)
