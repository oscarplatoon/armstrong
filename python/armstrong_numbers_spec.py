# The code is written as driver code. Can you convert it to Unit Test?
import unittest
from armstrong_numbers import find_armstrong_numbers

class find_armstrong_numbers(unittest.TestCase):

    print(find_armstrong_numbers(0) == [0]) 
    print(find_armstrong_numbers(8) == [0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(find_armstrong_numbers(100) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    print(find_armstrong_numbers(999) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407])

if __name__ == '__main__':
    unittest.main()