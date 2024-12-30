from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime
from airflow.models import Variable

DOCKER_USERNAME = Variable.get("DOCKER_USERNAME")
DOCKER_PASSWORD = Variable.get("DOCKER_PASSWORD")

with DAG('dag_6_build_image',
         default_args={'start_date': datetime(2024, 1, 1)},
         schedule_interval='@daily',
         catchup=False) as dag:
    
    docker_login = BashOperator(
        task_id="docker_login",
        bash_command=f"echo $DOCKER_PASSWORD | docker login -u {DOCKER_USERNAME} --password-stdin",
        env={"DOCKER_PASSWORD": DOCKER_PASSWORD},
    )
    
    build_image = BashOperator(
        task_id='build_image',
        bash_command='docker build -t s24697/creditcardfraudapi -f /opt/airflow/api/Dockerfile /opt/airflow'
    )

    push_image = BashOperator(
        task_id='push_image',
        bash_command='docker push s24697/creditcardfraudapi'
    )

    docker_login >> build_image >> push_image