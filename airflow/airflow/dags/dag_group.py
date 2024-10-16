from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

# Definindo o DAG dentro de um bloco 'with'
with DAG(
    'dag_group', 
    description="group",
    schedule_interval=None, 
    start_date=datetime(2024, 9, 26),
    catchup=False
) as dag:

    task1 = BashOperator(task_id="tsk1", bash_command="sleep 5")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 5")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 5")
    task4 = BashOperator(task_id="tsk4", bash_command="sleep 5")
    task5 = BashOperator(task_id="tsk5", bash_command="sleep 5")
    task6 = BashOperator(task_id="tsk6", bash_command="sleep 5")

    # Criando o TaskGroup dentro do contexto do DAG
    with TaskGroup(group_id="taks_group") as taskGroup:
        task7 = BashOperator(task_id="tsk7", bash_command="sleep 5")
        task8 = BashOperator(task_id="tsk8", bash_command="exit 1")
        task9 = BashOperator(
            task_id="tsk9", 
            bash_command="sleep 5", 
            trigger_rule='all_failed'
        )

    # Definindo as dependências
    task1 >> task2
    task3 >> task4
    [task2, task4] >> task5 >> task6
    task6 >> taskGroup
