import unittest
import calc #module

"""giving access to testing capabilities"""
class testCalc(unittest.TestCase): 

    """first test"""
    def test_add(self):
         self.assertEqual(calc.add(5, 10), 15)
         self.assertEqual(calc.add(-1, 1), 0)
         self.assertEqual(calc.add(-1, -2), -3)
         """to run it in terminal you should go to the directory & type
         > python -m unittest test_calc.py
         if it throws 'OK' it's all good"""

    def test_subtract(self):
            self.assertEqual(calc.subtract(10, 5), 5)
            self.assertEqual(calc.subtract(-1, 1), -2)
            self.assertEqual(calc.subtract(-1, -1), 0)

    def test_multiply(self):
            self.assertEqual(calc.multiply(10, 5), 50)
            self.assertEqual(calc.multiply(-1, 1), -1)
            self.assertEqual(calc.multiply(-1, -1), 1)

    def test_divide(self):
            self.assertEqual(calc.divide(10, 5), 2)
            self.assertEqual(calc.divide(-1, 1), -1)
            self.assertEqual(calc.divide(-1, -1), 1)

            """"error if divide by 0"""
            with self.assertRaises(ValueError):
                calc.divide(10, 0)

"""command runs in editor
this conditional would run the test, even if we type:
 >  python test_calc.py 
 it's same as this command ↑ """
if __name__ == '__main__':
    unittest.main()