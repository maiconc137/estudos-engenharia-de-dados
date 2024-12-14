from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.email import EmailOperator
from datetime import datetime, timedelta

default_args = {
    'depends_on_past': False,
    'start_date': datetime(24, 12, 14),
    'email' : ['qumaicon@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(seconds=10)
}
    
with DAG('email_teste', description="Email",
        default_args=default_args,
        schedule_interval=None,
        catchup=False, default_view='graph', tags=['email']) as dag:

    task1 = BashOperator(task_id="tsk1", bash_command="sleep 1")
    task2 = BashOperator(task_id="tsk2", bash_command="sleep 1")
    task3 = BashOperator(task_id="tsk3", bash_command="sleep 1")
    task4 = BashOperator(task_id="tsk4", bash_command="sleep 1")
    task5 = BashOperator(task_id="tsk5", bash_command="sleep 1", trigger_rule='none_failed')
    task6 = BashOperator(task_id="tsk6", bash_command="sleep 1", trigger_rule='none_failed')
    

    send_email = EmailOperator(
        task_id="send_email",
        to="qumaicon@gmail.com",
        subject="Airflow Error",
        html_content="""
                    <h3>Ocorreu um erro na Dag</h3>   
                    <p> Vá lá ver </p>
                    """,
        trigger_rule="one_failed"
    )

    [task1 >> task2] >> task3 >> task4
    task4 >> [task5, task6, send_email]