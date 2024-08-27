from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# Định nghĩa DAG
default_args = {
    'owner': 'airflow',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'start_date': datetime(2024, 8, 25),
}

with DAG(
    'extract_and_transform_dag',
    default_args=default_args,
    description='DAG để thực hiện extraction và transformation data',
    schedule_interval='@daily',
    catchup=False,
) as dag:

    # Tạo một BashOperator để chạy hàm main từ extract.py
    run_python_script = BashOperator(
        task_id='run_python_script',
        bash_command="python3 /spark/app/extract.py",
    )
    run_spark_job = BashOperator(
        task_id='run_spark_job',
        bash_command=(
            'docker exec e9392c7cc91a '
            '/opt/bitnami/spark/bin/spark-submit '
            '--master spark://spark:7077 '
            '--jars /opt/bitnami/spark/jars/snowflake-jdbc-3.16.1.jar,/opt/bitnami/spark/jars/spark-snowflake_2.12-2.16.0-spark_3.2.jar '
            '/app/transform.py'
        ),
    )



    # Định nghĩa thứ tự thực hiện các công việc
    run_python_script >> run_spark_job
