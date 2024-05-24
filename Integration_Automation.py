from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
    'retries': 1,
}

dag = DAG(
    'genetic_analysis_pipeline',
    default_args=default_args,
    description='A simple genetic analysis pipeline',
    schedule_interval='@daily',
)

t1 = BashOperator(
    task_id='download_sra_data',
    bash_command='python /path/to/download_script.py',
    dag=dag,
)

t2 = BashOperator(
    task_id='quality_control',
    bash_command='python /path/to/quality_control_script.py',
    dag=dag,
)

t3 = BashOperator(
    task_id='align_reads',
    bash_command='python /path/to/alignment_script.py',
    dag=dag,
)

t4 = BashOperator(
    task_id='variant_calling',
    bash_command='python /path/to/variant_calling_script.py',
    dag=dag,
)

t5 = BashOperator(
    task_id='machine_learning',
    bash_command='python /path/to/machine_learning_script.py',
    dag=dag,
)

t1 >> t2 >> t3 >> t4 >> t5
