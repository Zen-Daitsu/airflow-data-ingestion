#Développé par : Kraiem
#Date : 05/02/2025
#Examen final - Collecte de données

from airflow.operators.python_operator import PythonOperator

def print_success_message():
    print("Le pipeline fonctionne correctement")

def create_print_success_task(dag):
    return PythonOperator(
        task_id='print_success_message',
        python_callable=print_success_message,
        dag=dag,
    )