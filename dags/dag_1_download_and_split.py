from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from sklearn.model_selection import train_test_split
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
import kagglehub


def fetch_data(**kwargs):
    file_path ="/opt/airflow/dags/data.csv"

    path = kagglehub.dataset_download("dhanushnarayananr/credit-card-fraud", force_download=True)
    df = pd.read_csv( f'{path}/card_transdata.csv') 
    df = df.sample(n=50000, random_state=42)
    df.to_csv(file_path, index=False)

    kwargs['ti'].xcom_push(key='raw_data', value=df.to_json())

def split_data(**kwargs):
    raw_data = kwargs['ti'].xcom_pull(key='raw_data')
    df = pd.read_json(raw_data)
    train, test = train_test_split(df, test_size=0.3, random_state=42)
    kwargs['ti'].xcom_push(key='train_data', value=train.to_json())
    kwargs['ti'].xcom_push(key='test_data', value=test.to_json())

def save_to_gsheets(sheet_name, data):
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('/opt/airflow/dags/secret.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open("ASI-Lab-2").worksheet(sheet_name)
    df = pd.read_json(data)
    sheet.update([df.columns.values.tolist()] + df.values.tolist())

def upload_data(**kwargs):
    train_data = kwargs['ti'].xcom_pull(key='train_data')
    test_data = kwargs['ti'].xcom_pull(key='test_data')
    save_to_gsheets("train", train_data)
    save_to_gsheets("test", test_data)

with DAG('dag_1_data_split',
         default_args={'start_date': datetime(2024, 1, 1)},
         schedule_interval='@daily',
         catchup=False) as dag:
    fetch_task = PythonOperator(task_id='fetch_data', python_callable=fetch_data)
    split_task = PythonOperator(task_id='split_data', python_callable=split_data, provide_context=True)
    upload_task = PythonOperator(task_id='upload_data', python_callable=upload_data, provide_context=True)

    fetch_task >> split_task >> upload_task