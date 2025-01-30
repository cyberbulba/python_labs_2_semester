import pytest
from repeated_symbols import repeated_symbols


def test_repeated_symbols():
    """
    случаи без исключений
    """
    assert repeated_symbols('1234') == 0
    assert repeated_symbols('aaabb') == 2
    assert repeated_symbols('Aabc') == 0
    assert repeated_symbols('aBcbc') == 1


def test_exceptions_repeated_symbols():
    """
    случай с исключением (строка пустая)
    """
    with pytest.raises(ValueError):
        repeated_symbols('')
