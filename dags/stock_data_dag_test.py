from internal_unit_testing import assert_has_valid_dag
from stock_data_dag import dag  # Import the DAG object directly

def test_dag_import():
    assert_has_valid_dag(dag)  # Pass the DAG object to the testing function
