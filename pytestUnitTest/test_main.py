import pytest
from main import suma

def test_suma():
    assert suma(2,2) == 4

"""to validate every parameter"""
@pytest.mark.parametrisize(
    "input_a,input_b, expected",
    [
        (3,2,5),
        (2,3,5),
        (suma(3,2),5,10),
        (3, suma(2,5),10)
    ]
)
def test_suma_multi(input_a,input_b):
    assert suma(input_a,input_b) == expected


if __name__ == '__main__':
    unittest.main()