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
      image="aws-image/test-application:v1.4", # renovate: depName=testing-box/test-tap
      get_logs=True,
    )
    
    test_operator
  return dag
