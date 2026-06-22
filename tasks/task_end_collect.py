#Développé par : Kraiem
#Date : 05/02/2025
#Examen final - Collecte de données

from airflow.operators.bash import BashOperator

def create_end_collect_task(dag):
    return BashOperator(
        task_id='end_collect',
        bash_command='echo "Fin de la collecte de données"',
        dag=dag,
    )