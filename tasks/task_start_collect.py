#Développé par : Kraiem
#Date : 05/02/2025
#Examen final - Collecte de données

from airflow.operators.bash import BashOperator

def create_start_collect_task(dag):
    return BashOperator(
        task_id='start_collect',
        bash_command='echo "Démarrage de la collecte de données"',
        dag=dag,
    )