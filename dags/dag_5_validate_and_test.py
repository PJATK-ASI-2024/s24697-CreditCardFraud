from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'email_on_failure': True,
    'email': ['s24697@pjwstk.edu.pl'],
    'retries': 1
}

def load_model_and_data():
    global model, test_data
    with open('/opt/airflow/models/gradient_boosting_model.pkl', 'rb') as f:
        model = pickle.load(f)
    test_data = pd.read_csv('/opt/airflow/data/processed_data/processed_data.csv')

def evaluate_model():
    global accuracy
    X = test_data.drop('fraud', axis=1)
    y_true = test_data['fraud']
    y_pred = model.predict(X)
    accuracy = accuracy_score(y_true, y_pred)
    if accuracy < 0.8:
        raise ValueError(f"Accuracy too low: {accuracy:.2f}")
    return accuracy

def run_unit_tests():
    failed_tests = []

    if test_data.empty:
        failed_tests.append("data is empty")

    predictions = model.predict(test_data.drop('fraud', axis=1))
    if len(predictions) != len(test_data):
        failed_tests.append("wrong output")


    if failed_tests:
        raise ValueError(f"fail: {', '.join(failed_tests)}")

    return "success"


with DAG('dag_5_validate_and_test',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    load_task = PythonOperator(
        task_id='load_model_and_data',
        python_callable=load_model_and_data
    )

    evaluate_task = PythonOperator(
        task_id='evaluate_model',
        python_callable=evaluate_model
    )

    test_task = PythonOperator(
        task_id='run_unit_tests',
        python_callable=run_unit_tests
    )

    load_task >> evaluate_task >> test_task
