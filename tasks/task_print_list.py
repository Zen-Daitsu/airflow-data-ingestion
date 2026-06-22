#Développé par : Kraiem
#Date : 05/02/2025
#Examen final - Collecte de données

from airflow.operators.python import PythonOperator

def print_list():
    items = ['Flouflou', 'Flouclair', 'CLAiCLAIR']
    for item in items:
        print(item)

def create_print_list_task(dag):
    return PythonOperator(
        task_id='print_list',
        python_callable=print_list,
        dag=dag
    )
