from unittest import result
import math_func
import pytest

@pytest.mark.number
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9 # +2
    assert math_func.add(5) == 7

@pytest.mark.number
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10
    assert math_func.product(7) == 14

"""run test from terminal >>>
       . copy path
       . type: pytest + testFileName -v, or py.test
       . must say how many passed, how many fails"""

@pytest.mark.string
def test_add_strings():
    result = math_func.add('Hello',' Im Franco')
    assert result == 'Hello Im Franco'
    assert type(result) is str

@pytest.mark.string
def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    result = math_func.product('Hello ')
    assert result == 'Hello Hello '
    assert type(result) is str
    assert 'Hello' in result

""" run just 1 of tests >>>
                type: pytest fileName.py::test_name or,
    run specific ones >>>
                type: pytest -v -k "add or string"  """ #will test all add's or string tests
""" run given tags to test modules >>>>:
                give tag: @pytest.mark.number
                test w tags: pytest -v -m number  
    run just failed >>>
                pytest -v -x
    don't see failed details >>>
                pytest -v -x --tb=no       """            