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

"""===============PARAMETRIZE=============================="""
@pytest.mark.parametrize('num1, num2, result',
                         [
                            (7, 3, 10),
                            ('Hello', ' World', 'Hello World'),
                            (10.5, 25.5, 36)  
                         ]
                        )
def test_simpadd(num1, num2, result):
    assert math_func.simpadd(num1, num2) == result

"""===============FICTURES json=============================="""
from math_func import StudentDB
import pytest

@pytest.fixture(scope='module')
def db():
    print('----------setup----------------')
    db = StudentDB()
    db.connect('data.json')
    yield db
    print('----------teardown----------------')
    db.close()


def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'

def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'