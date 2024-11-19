from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler
import gspread
from oauth2client.service_account import ServiceAccountCredentials

secret = '/opt/airflow/dags/secret.json'

def fetch_from_gsheets(sheet_name):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(secret, scope)
    client = gspread.authorize(creds)
    sheet = client.open("ASI-Lab-2").worksheet(sheet_name)
    data = pd.DataFrame(sheet.get_all_records())
    return data

def save_to_gsheets(sheet_name, data):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name(secret, scope)
    client = gspread.authorize(creds)
    sheet = client.open("ASI-Lab-2").worksheet(sheet_name)
    df = pd.read_json(data)
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

def fetch_data(**kwargs):
    df = fetch_from_gsheets("train")
    kwargs['ti'].xcom_push(key='data', value=df.to_json())

def clean_data(**kwargs):
    data = kwargs['ti'].xcom_pull(key='data')
    df = pd.read_json(data)
    df.dropna(inplace=True)
    df.drop_duplicates(inplace=True)
    kwargs['ti'].xcom_push(key='clean_data', value=df.to_json())

def process_data(**kwargs):
    data = kwargs['ti'].xcom_pull(key='clean_data')
    df = pd.read_json(data)
    scaler = StandardScaler()
    df[df.columns] = scaler.fit_transform(df)
    kwargs['ti'].xcom_push(key='processed_data', value=df.to_json())

def save_processed_data(**kwargs):
    processed_data = kwargs['ti'].xcom_pull(key='processed_data')
    save_to_gsheets("processed", processed_data)

with DAG('dag_2_data_processing',
         default_args={'start_date': datetime(2024, 1, 1)},
         schedule_interval='@daily',
         catchup=False) as dag:
    fetch_task = PythonOperator(task_id='fetch_data', python_callable=fetch_data, provide_context=True)
    clean_task = PythonOperator(task_id='clean_data', python_callable=clean_data, provide_context=True)
    process_task = PythonOperator(task_id='process_data', python_callable=process_data, provide_context=True)
    save_task = PythonOperator(task_id='save_processed_data', python_callable=save_processed_data, provide_context=True)

    fetch_task >> clean_task >> process_task >> save_task
