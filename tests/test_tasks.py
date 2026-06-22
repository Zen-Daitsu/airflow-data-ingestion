import pytest
import datetime
from airflow.models import DAG
from airflow.utils import timezone
from tasks.task_start_collect import create_start_collect_task
from tasks.task_print_list import create_print_list_task, print_list
from tasks.task_print_success import create_print_success_task, print_success_message
from tasks.task_end_collect import create_end_collect_task

# Fixture to provide a DAG object for task creation
@pytest.fixture
def dag():
    return DAG('test_dag', start_date=timezone.utcnow() - datetime.timedelta(days=1))

# 1. Infrastructure Tests
def test_task_initialization(dag):
    t1 = create_start_collect_task(dag)
    assert t1.task_id == 'start_collect'

    t2 = create_print_list_task(dag)
    assert t2.task_id == 'print_list'
    assert t2.python_callable == print_list

    t3 = create_print_success_task(dag)
    assert t3.task_id == 'print_success_message'
    assert t3.python_callable == print_success_message

    t4 = create_end_collect_task(dag)
    assert t4.task_id == 'end_collect'

# 2. Logic Tests
def test_print_list_logic(capsys):
    print_list()
    captured = capsys.readouterr()
    assert 'Flouflou' in captured.out
    assert 'Flouclair' in captured.out
    assert 'CLAiCLAIR' in captured.out

def test_print_success_logic(capsys):
    print_success_message()
    captured = capsys.readouterr()
    assert "Le pipeline fonctionne correctement" in captured.out
