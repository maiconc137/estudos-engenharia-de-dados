from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator, BranchPythonOperator
from datetime import datetime, timedelta
import random
    
with DAG('branchtest', description="branchtest",
        schedule_interval=None, start_date=datetime(2024,12,16),
        catchup=False, default_view='graph', tags=['branchtest']) as dag:

    def gera_numero_aleatorio():
        return random.randint(1, 100)

    def avalia_numero_aleatorio(**agrs):
        

    task1 = PythonOperator(task_id="gera_numero_aleatorio_task", python_callable="gera_numero_aleatorio")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 1")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 1")
    task4 = BashOperator(task_id="tsk4", bash_command="sleep 1")
    task5 = BashOperator(task_id="tsk5", bash_command="sleep 1")
    taskdummy = DummyOperator(task_id="taskdummy")


    [task1, task2, task3] >> taskdummy >> [task4, task5]