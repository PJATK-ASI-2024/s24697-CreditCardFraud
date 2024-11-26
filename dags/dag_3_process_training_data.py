from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import os

file_path ="/opt/airflow/dags/data.csv"

def process_data():
    file_path ="/opt/airflow/dags/data.csv"
    processed_data_path = '/opt/airflow/data/processed_data/processed_data.csv'
    os.makedirs('/opt/airflow/data/processed_data/', exist_ok=True)

    df = pd.read_csv(file_path)
    df.fillna(df.mean(), inplace=True)
    df.to_csv(processed_data_path, index=False)

with DAG('dag_3_process_training_data',
         default_args={'start_date': datetime(2024, 1, 1)},
         schedule_interval='@daily',
         catchup=False) as dag:
    process_data_task = PythonOperator(
        task_id="process_data",
        python_callable=process_data
    )

    process_data_task
