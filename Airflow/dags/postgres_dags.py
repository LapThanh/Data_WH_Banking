from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Định nghĩa các tham số mặc định cho DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

# Khởi tạo DAG
with DAG(
    'data_generation_dag',
    default_args=default_args,
    description='DAG to run the data generation script',
    schedule_interval=None,
    catchup=False,
) as dag:

    # Định nghĩa task để chạy script Python
    run_data_generation_script = BashOperator(
        task_id='run_data_generation_script',
        bash_command='python3 /opt/airflow/fake/Fake.py',
        dag=dag
    )

    # Xác định task order (nếu cần)
    run_data_generation_script
