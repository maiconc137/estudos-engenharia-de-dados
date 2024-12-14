from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG('dagrundag2', description="Dag run DAG",
          schedule_interval=None, start_date=datetime(2024, 9, 26),
          catchup=False) as dag:

    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")

    task1 >> task2
    
