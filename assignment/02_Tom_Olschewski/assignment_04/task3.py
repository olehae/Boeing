
import math
import unittest


def decimal2binary(n):
    # function to convert decimal integers to binary
    x = []
    if n < 0:  # if n is negative, the first value should be negative and all other numbers should be absolutes
        x.append(-(n % 2))
        n = math.floor(abs(n) / 2)
    while n > 0:
        x.append(n % 2)
        n = math.floor(n/2)
    if not x:  # x should at east contain one integer of value 0
        x = [0]
    return x[::-1]


class ArrayTestCase(unittest.TestCase):
    def test_positive(self):
        # Do positive numbers work?
        self.assertEqual(decimal2binary(1), [1])
        self.assertEqual(decimal2binary(2), [1, 0])
        self.assertEqual(decimal2binary(3), [1, 1])

    def test_negative(self):
        # Do negative numbers work?
        self.assertEqual(decimal2binary(-1), [-1])

    def test_zero(self):
        # Does zero work?
        self.assertEqual(decimal2binary(0), [0])


if __name__ == '__main__':
    unittest.main()