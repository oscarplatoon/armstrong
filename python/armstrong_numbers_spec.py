# The code is written as driver code. Can you convert it to Unit Test?
import unittest
from armstrong_numbers import find_armstrong_numbers

class ArmstrongNumbersTestCase(unittest.TestCase):
    """Tests for armstrong_numbers.py"""
    
    def test_to_zero(self):
        """When you call find_armstrong_numbers, you should receive a list with 0"""
        self.assertEqual(find_armstrong_numbers([0]), [0])
    def test_to_8(self):
        """When you call find_armstrong_numbers, you should receive a list of armstrong numbersfrom 0 to 7"""
        self.assertEqual(find_armstrong_numbers(list(range(0,8))),[0, 1, 2, 3, 4, 5, 6, 7])
    def test_to_999(self):
        """When you call find_armstrong_numbers, you should receive a list of armstrong numbers from 0 to 407"""
        self.assertEqual(find_armstrong_numbers(list(range(0,999))),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

if __name__ == '__main__':
    unittest.main()
