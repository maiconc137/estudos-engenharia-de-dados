from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

default_args = {
    "owner": "tester",
    "retries": 1,
    "retry_delay": timedelta(seconds=5),
}

with DAG(
    "test_generic_dag",
    default_args=default_args,
    description="Generic Test DAG",
    schedule_interval=None,
    start_date=datetime(2024, 12, 18),
    catchup=False,
) as dag:

    # Funções simuladas
    def simulate_task(task_id):
        print(f"Running task: {task_id}")
        if random.choice([True, False]):  # Simula falhas aleatórias
            raise Exception(f"Task {task_id} failed!")
        print(f"Task {task_id} completed successfully!")

    def simulate_delete_cluster():
        print("Cluster deleted successfully!")

    # Tarefas genéricas
    start_dag = DummyOperator(task_id="start_dag")
    end_dag = DummyOperator(task_id="end_dag")

    tasks = []
    for i in range(3):  # Simula 3 tarefas de transformação
        task = PythonOperator(
            task_id=f"transient_to_raw_{i}",
            python_callable=simulate_task,
            op_args=[f"transient_to_raw_{i}"],
        )
        tasks.append(task)
        start_dag >> task

    # Task para deletar cluster (executa após todas as anteriores)
    delete_cluster = PythonOperator(
        task_id="delete_cluster",
        python_callable=simulate_delete_cluster,
        trigger_rule="all_done",  # Garante execução mesmo com falhas
    )

    # Configuração das dependências
    for task in tasks:
        task >> delete_cluster

    delete_cluster >> end_dag
