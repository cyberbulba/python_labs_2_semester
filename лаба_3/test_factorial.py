import pytest
from factorial import factorial


def test_factorial():
    """
    тесты для нуля, единицы, положительных значений
    """
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(5) == 120


def test_exceptions_factorial():
    """
    тест для отрицательных значений
    """
    with pytest.raises(ValueError):
        factorial(-100)
        factorial(4.59)
        factorial('abc')
