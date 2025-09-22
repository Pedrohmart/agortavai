import pytest
from calc.calculator import add, sub, mul, div, powi

def test_add():
    assert add(2, 3) == 5

def test_sub():
    assert sub(10, 4) == 6

def test_mul():
    assert mul(7, -2) == -14

def test_div():
    assert div(10, 2) == 5

def test_div_by_zero():
    with pytest.raises(ZeroDivisionError):
        div(1, 0)

def test_powi_int_ok():
    assert powi(2, 5) == 32

def test_powi_type_error():
    with pytest.raises(TypeError):
        powi(2, 1.5)
