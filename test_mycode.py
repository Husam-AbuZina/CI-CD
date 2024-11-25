import pytest
from mycode import add_positive, add_zero, add_negative

def test_add_positive():
    assert add_positive(3, 5) == 8

def test_add_zero():
    assert add_zero(0, 5) == 5

def test_add_negative():
    assert add_negative(-3, -5) == -8

if __name__ == '__main__':
    pytest.main()
