import pytest
import internal_unit_testing


def test_dag_import():
    from . import stock_data_dag as module

    internal_unit_testing.assert_has_valid_dag(module)
