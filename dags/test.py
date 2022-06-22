from airflow import DAG
from airflow.providers.cncf.kubernetes.operators.kubernetes_pod import (
    KubernetesPodOperator,
)

def test_dag() -> DAG:
  with DAG(
    dag_id="test",
  ):
    test_operator = KubernetesPodOperator(
      namespace="namespace",
      image=f"{config.AWS_ECR_URI}/tap-ukg-dimensions:v1.4.0", # renovate: depName=testing-box/test-tap
      get_logs=True,
    )
    
    test_operator
  return dag
