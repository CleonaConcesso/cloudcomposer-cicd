import internal_unit_testing

print("start")
def test_dag_import():
    print("hello")
    from . import stock_data_dag as module
    print("bye")
    internal_unit_testing.assert_has_valid_dag(module)  # Pass the DAG object to the testing function
