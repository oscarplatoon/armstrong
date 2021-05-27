# The code is written as driver code. Can you convert it to Unit Test?
from armstrong_numbers import find_armstrong_numbers
import unittest

class armstong_test(unittest.TestCase):
    '''test for Armstrong number'''
    def test_returns_a_list(self):
        self.assertEqual(type(find_armstrong_numbers([5])),list)

    def test_list_to_0(self):
        self.assertEqual(find_armstrong_numbers([0]),[0])

    def test_list_to_8(self):
        self.assertEqual(find_armstrong_numbers(list(range(0,8))),[0, 1, 2, 3, 4, 5, 6, 7])

    def test_list_to_999(self):
        self.assertEqual(find_armstrong_numbers(list(range(0,999))),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])



if __name__ == '__main__':
    unittest.main()


