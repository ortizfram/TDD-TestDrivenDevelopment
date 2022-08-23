import unittest
import calc #module

"""giving access to testing capabilities"""
class testCalc(unittest.TestCase): 

    """first test"""
    def test_add(self):
         result = calc.add(10, 5)
         """testing"""
         self.assetEquals(result, 15)
         """to run it in terminal you should go to the directory & type
         > python -m unittest test_calc.py
         if it throws 'OK' it's all good"""


"""command runs in editor
this conditional would run the test, even if we type:
 >  python test_calc.py 
 it's same as this command ↑ """
if __name__ == '__main__':
    unittest.main()