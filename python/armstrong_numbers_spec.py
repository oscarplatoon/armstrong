# The code is written as driver code. Can you convert it to Unit Test?
import unittest
from armstrong_numbers import find_armstrong_numbers

# print(find_armstrong_numbers([0]) == [0])
# print(find_armstrong_numbers(list(range(0, 8))) == [0, 1, 2, 3, 4, 5, 6, 7])
# print(find_armstrong_numbers(list(range(0,100))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
# print(find_armstrong_numbers(list(range(0,999))) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])


class ArmstrongNumbersTaseCase(unittest.TestCase):

    def test_returns_a_list(self):
        """
        When you call find_armstrong_numbers, it should return an array/list.
        """
        self.assertEqual(type(find_armstrong_numbers(list(range(0, 8)))), list)

    def test_returns_the_correct_list(self):
      """
      When you call:
      find_armstrong_numbers(list(range(0, 8)))
      find_armstrong_numbers(list(range(0,100))
      find_armstrong_numbers(list(range(0,999))
      """
      self.assertEqual(find_armstrong_numbers(list(range(0, 8))), [0, 1, 2, 3, 4, 5, 6, 7])
      self.assertEqual(find_armstrong_numbers(list(range(0,100))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
      self.assertEqual(find_armstrong_numbers(list(range(0,999))), [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

if __name__ == '__main__':
    unittest.main()
