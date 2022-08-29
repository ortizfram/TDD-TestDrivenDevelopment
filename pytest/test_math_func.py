import math_func
import pytest

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9 # +2
    assert math_func.add(5) == 7

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14

"""run test from terminal >>>
       . copy path
       . type: pytest + testFileName -v, or py.test
       . must say how many passed, how many fails"""