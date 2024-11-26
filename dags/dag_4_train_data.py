from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib
import os

def train_gradient_boosting():
    data_path = '/opt/airflow/data/processed_data/processed_data.csv'
    tpot_data = pd.read_csv(data_path, sep=',', dtype=np.float64)
    
    features = tpot_data.drop('fraud', axis=1)
    target = tpot_data['fraud']
    training_features, testing_features, training_target, testing_target = train_test_split(
        features, target, random_state=42
    )
    
    exported_pipeline = GradientBoostingClassifier(
        learning_rate=0.1,
        max_depth=4,
        max_features=0.55,
        min_samples_leaf=3,
        min_samples_split=10,
        n_estimators=100,
        subsample=0.9500000000000001
    )
    
    if hasattr(exported_pipeline, 'random_state'):
        setattr(exported_pipeline, 'random_state', 42)
    
    exported_pipeline.fit(training_features, training_target)
    
    predictions = exported_pipeline.predict(testing_features)
    accuracy = accuracy_score(testing_target, predictions)
    report = classification_report(testing_target, predictions)
    
    os.makedirs('/opt/airflow/models', exist_ok=True)
    joblib.dump(exported_pipeline, '/opt/airflow/models/gradient_boosting_model.pkl')
    
    os.makedirs('/opt/airflow/reports', exist_ok=True)
    with open('/opt/airflow/reports/evaluation_report.txt', 'w') as f:
        f.write(f"Accuracy: {accuracy:.2f}\n\n")
        f.write(f"Classification Report:\n{report}")

with DAG('dag_4_train_data',
         default_args={'start_date': datetime(2024, 1, 1)},
         schedule_interval='@daily',
         catchup=False) as dag:
    train_model_task = PythonOperator(
        task_id="train_gradient_boosting",
        python_callable=train_gradient_boosting
    )

    train_model_task
