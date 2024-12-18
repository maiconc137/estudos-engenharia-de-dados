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

    gera_numero_aleatorio = PythonOperator(
        task_id = 'gera_numero_aleatorio',
        python_callable=gera_numero_aleatorio
    )
 
    def avalia_numero_aleatorio(**agrs):
        number = agrs['task_instance'].xcom_pull(task_ids='gera_numero_aleatorio')
        if number % 2 ==0:
            return 'par_task'
        else:
            return 'impar_task'
        

    branch_task = BranchPythonOperator(
        task_id = 'branch_task',
        python_callable = avalia_numero_aleatorio,
        provide_context = True
    )

    par_task = BashOperator(task_id="par_task", bash_command='echo "Número Par"')
    impar_task = BashOperator(task_id="impar_task", bash_command='echo "Número Impar"')

    gera_numero_aleatorio >> branch_task
    branch_task >> par_task
    branch_task >> impar_task