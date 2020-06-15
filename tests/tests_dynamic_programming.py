import unittest

import dynamic_programming.fibonacci_tabulation
import dynamic_programming.fibonacci_memoization
import dynamic_programming.knapsack_problem_0_1_recursive
import dynamic_programming.data_structures

class TestFibonacciMemoization(unittest.TestCase):
    def test_fibonacci(self):
        # the results must be the first six values
        first_six_values = [0, 1, 1, 2, 3, 5]

        computed_numbers = [dynamic_programming.fibonacci_memoization.fibonacci(i) for i in range(6)]

        self.assertCountEqual(first_six_values, computed_numbers)

class TestFibonacciTabulation(unittest.TestCase):
    def test_fibonacci(self):
        # the results must be the first six values
        first_six_values = [0, 1, 1, 2, 3, 5]

        computed_numbers = [dynamic_programming.fibonacci_tabulation.fibonacci(i) for i in range(6)]

        self.assertCountEqual(first_six_values, computed_numbers)

class TestKnapsackProblem01Recursive(unittest.TestCase):
    def test_knapsack(self):
        # create a knapsack
        knapsack = dynamic_programming.data_structures.Knapsack(50)

        # create an array of item/weight pairs
        items = [
            (60, 10),
            (100, 20),
            (120, 30)
        ]

        # the output should be this sum
        expected_result = 220
        result = dynamic_programming.knapsack_problem_0_1_recursive.knapsack_01_recursive(knapsack, items)

        # check for proper output type
        # should be int
        self.assertIsInstance(result, int, "Output should be of type Int")

        # check if the result is correct
        self.assertEqual(result, expected_result)
