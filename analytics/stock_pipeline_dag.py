from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    "stock_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    run_etl = BashOperator(
        task_id="run_etl",
        bash_command="cd ~/canada-intel/canada-intel && source venv/bin/activate && python etl.py"
    )

    run_etl
