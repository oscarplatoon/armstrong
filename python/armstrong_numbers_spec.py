# The code is written as driver code. Can you convert it to Unit Test?
import unittest
from armstrong_numbers import find_armstrong_numbers

class TestFindArmstrong(unittest.TestCase):
    
    """
    When you call find_armstrong_numbers it should return a list.
    """
    def test_returns_a_list(self):
        self.assertEqual(type(find_armstrong_numbers(list(range(0, 8)))), list)

    """
    When you call:
    find_armstrong_numbers(list(range(0, 8)) you get back [0, 1, 2, 3, 4, 5, 6, 7]
    find_armstrong_numbers(list(range(0, 100)) you get back [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    find_armstrong_numbers(list(range(0, 999)) you get back [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407]
    """
    def test_returns_the_correct_list(self):
        self.assertEqual(find_armstrong_numbers(list(range(0, 8))), [0, 1, 2, 3, 4, 5, 6, 7])
        self.assertEqual(find_armstrong_numbers(list(range(0,100))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEqual(find_armstrong_numbers(list(range(0,999))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')

    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()

# print(find_armstrong_numbers([0]) == [0]) 
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

