from airflow import DAG
# from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime

with DAG('xcom', description="Dag run DAG",
          schedule_interval=None, start_date=datetime(2024, 9, 26),
          catchup=False) as dag:

    def task_write(**kwarg):
        kwarg['ti'].xcom_push(key='valorxcom1', value=10200)

    task1 = PythonOperator(task_id="tsk1", python_callable=task_write)

    def task_read(**kargs):
        valor = kargs['ti'].xcom_pull(key='valorxcom1')
        print(f"Valor recuperado: {valor}")

    task2 = PythonOperator(task_id="tsk2", python_callable=task_read)

    task1 >> task2
    
