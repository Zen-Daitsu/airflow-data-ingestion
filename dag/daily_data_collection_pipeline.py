#Développé par : Kraiem
#Date : 05/02/2025
#Examen final - Collecte de données

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime
from tasks import (
    create_start_collect_task,
    create_print_list_task,
    create_print_success_task,
    create_end_collect_task
)

default_args = {
    'owner': 'amink',
    'start_date': datetime(2026, 1, 1),
    'retries': 1,
}

# DAG
with DAG(
    'daily_data_collection',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=False,
) as dag:
    
    # Tâches
    t1 = create_start_collect_task(dag)
    t2 = create_print_list_task(dag)
    t3 = create_print_success_task(dag)
    t4 = create_end_collect_task(dag)

    # Séquence
    t1 >> t2 >> t3 >> t4
