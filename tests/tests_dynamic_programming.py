import unittest

import dynamic_programming.fibonacci_memoization

class TestFibonacciMemoization(unittest.TestCase):
    def test_fibonacci(self):
        # the results must be the first six values
        first_six_values = [0, 1, 1, 2, 3, 5]

        computed_numbers = [dynamic_programming.fibonacci_memoization.fibonacci(i) for i in range(6)]

        self.assertCountEqual(first_six_values, computed_numbers)