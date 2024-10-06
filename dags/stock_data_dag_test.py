import internal_unit_testing
from stock_data_dag import stock_data_dag  # Import the specific DAG from stock_data_dag.py

def test_dag_import():
    internal_unit_testing.assert_has_valid_dag(stock_data_dag)
    
