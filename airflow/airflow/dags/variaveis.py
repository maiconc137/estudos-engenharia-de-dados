from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.models import Variable
from datetime import datetime

with DAG('variable', description="variable",
          schedule_interval=None, start_date=datetime(2024, 9, 26),
          catchup=False) as dag:

    def print_variable(**context):
        minha_var = Variable.get('minhavar')
        print(f'O valor da variável é: {minha_var}')

    task1 = PythonOperator(task_id="tsk1", python_callable=print_variable)

    task1
    
