import pytest
from palindrom import is_palindrom


def test_is_palindrom():
    """
    тесты для случаев, кроме исключений
    """
    assert is_palindrom('aba')
    assert not is_palindrom('abc')
    assert is_palindrom('ghhg')
    assert is_palindrom('Aba')
    assert is_palindrom('Bfgfb')


def test_exceptions_is_palindrom():
    """
    тесты для исключений
    """
    with pytest.raises(ValueError):
        is_palindrom('')
        is_palindrom('ab')
