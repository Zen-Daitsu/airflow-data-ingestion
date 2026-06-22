#Développé par : Kraiem
#Date : 05/02/2025
#Examen final - Collecte de données

from airflow.models import DAG
from airflow.utils.dates import days_ago
from tasks.task_start_collect import create_start_collect_task
from tasks.task_print_list import create_print_list_task
from tasks.task_print_success import create_print_success_task
from tasks.task_end_collect import create_end_collect_task

default_args = {
    'owner': 'amink',
    'start_date': days_ago(1),
    'retries': 1,
}

# DAG
with DAG(
    'A53_Exercice2',
    default_args=default_args,
    description='Exercice 2',
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