# The code is written as driver code. Can you convert it to Unit Test?
import unittest
from armstrong_numbers import find_armstrong_numbers

class armstrong_test(unittest.TestCase):
    '''Test that the output is a list'''
    def test_returns_list_type(self):
        self.assertEqual(type(find_armstrong_numbers([5,6])), list )

    '''test the functions output 0-0'''
    def test_lists_to_0(self):
       self.assertEqual(find_armstrong_numbers([0]),[0])
    '''test the functions output 0-8'''
    def test_lists_to_8(self):
       self.assertEqual(find_armstrong_numbers(list(range(0,8))),[0, 1, 2, 3, 4, 5, 6, 7])
    '''test the functions output 0-100'''
    def test_lists_to_100(self):
       self.assertEqual(find_armstrong_numbers(list(range(0,100))),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    '''test the functions output 0-999'''
    def test_lists_to_999(self):
       self.assertEqual(find_armstrong_numbers(list(range(0,999))),[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])
    


if __name__ == '__main__':
     unittest.main()
