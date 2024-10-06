from internal_unit_testing import assert_has_valid_dag
from stock_data_dag import stock_data_dag  # Import the specific DAG from stock_data_dag.py

def test_dag_import():
    assert_has_valid_dag(stock_data_dag)   

