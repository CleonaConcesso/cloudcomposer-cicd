import internal_unit_testing

def test_dag_import():
    from . import stock_data

    internal_unit_testing.assert_has_valid_dag(stock_data)
