import internal_unit_testing
from . import stock_data_dag as module  # Import the DAG object directly

def test_dag_import():
    internal_unit_testing.assert_has_valid_dag(module)  # Pass the DAG object to the testing function
