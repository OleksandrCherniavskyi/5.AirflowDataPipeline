from datetime import timedelta
from airflow import DAG

from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
import datetime
from justjoin_etl import run_justjoin_etl
import pandas

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime.datetime(2023, 4, 10),
    'email': ['oleksandr.cherniavskyi@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'dag_1',
    default_args=default_args,
    description='Our first DAG with ETL process!',
    schedule_interval=timedelta(days=1),
)


def just_a_function():
    print("I'm going to show you something :)")


run_etl = PythonOperator(
    task_id='whole_justjoin_etl',
    python_callable=run_justjoin_etl,
    dag=dag,
)

run_etl
