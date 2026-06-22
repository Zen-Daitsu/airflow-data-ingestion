# Airflow Data Ingestion & Orchestration Workflow

An Apache Airflow-based orchestration pipeline engineered for modular daily data collection, execution logging, and automated workflow validation.

## 1. Architectural Overview
The pipeline executes a synchronous 4-stage orchestration graph running on a daily interval:

1. **Task Initialization:** Triggers the operational start sequence for data collection via Bash execution.
2. **Data Ingestion/Processing:** Leverages Python-based operator logic to iterate and process predefined data lists.
3. **Pipeline Validation:** Executes logical success checks to ensure the pipeline integrity remains within expected parameters.
4. **Collection Termination:** Performs final system logging and cleanup protocols to signal the successful end of the daily ingestion cycle.

## 2. Engineering Highlights & Trade-offs
* **Modular Task Decoupling:** Isolated task logic within a dedicated `tasks/` directory, decoupling core execution from the DAG definition to enforce maintainability and code clarity.
* **Package-Based Architecture:** Utilized Python `__init__.py` modules to standardize imports, ensuring the workflow environment is scalable and clean.
* **Test-Driven Development (TDD):** Integrated a `tests/` suite using `pytest` to validate both task infrastructure and business logic, ensuring robust CI/CD integration.
* **Standardized Coding Environment:** Enforced consistent style guides using `.editorconfig` to ensure code uniformity across collaborative environments.

## 3. Technical Stack
* **Orchestration:** Apache Airflow
* **Core Language:** Python 3.x
* **Task Execution:** BashOperator, PythonOperator
* **Testing Framework:** Pytest
* **CI/CD:** GitHub Actions

## 4. Project Architecture
```text
.
├── .github/
│   └── workflows/          # CI/CD automation pipelines
├── dags/
│   └── daily_data_collection_pipeline.py
├── tasks/
│   ├── __init__.py         # Modular task package definitions
│   ├── task_end_collect.py
│   ├── task_print_list.py
│   ├── task_print_success.py
│   └── task_start_collect.py
├── tests/
│   └── test_tasks.py       # Unit & integration testing suite
├── .editorconfig
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## 5. Local Deployment & Setup

### Prerequisites
Ensure your local machine has Python 3.x and a functional Apache Airflow environment installed.

### Installation
1. Clone the project locally:
   ```bash
   git clone git@github.com:Zen-Daitsu/airflow-data-ingestion.git
   cd airflow-data-ingestion
