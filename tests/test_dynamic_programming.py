import pytest
import unittest

import dynamic_programming.fibonacci_tabulation
import dynamic_programming.fibonacci_memoization
import dynamic_programming.knapsack_problem_0_1
import dynamic_programming.data_structures
from dynamic_programming.kadanes_algorithm import kadanes_algorithm

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

class TestKnapsackProblem01(unittest.TestCase):
    def test_knapsack_recursive(self):
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
        result = dynamic_programming.knapsack_problem_0_1.knapsack_01_recursive(knapsack, items)

        # check for proper output type
        # should be int
        self.assertIsInstance(result, int, "Output should be of type Int")

        # check if the result is correct
        self.assertEqual(result, expected_result)

    def test_knapsack_recursive_memoized(self):
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
        result = dynamic_programming.knapsack_problem_0_1.knapsack_01_recursive_memoized(knapsack, items)

        # check for proper output type
        # should be int
        self.assertIsInstance(result, int, "Output should be of type Int")

        # check if the result is correct
        self.assertEqual(result, expected_result)

    def test_knapsack_bottom_up(self):
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
        result = dynamic_programming.knapsack_problem_0_1.knapsack_01_bottom_up(knapsack, items)

        # check for proper output type
        # should be int
        self.assertIsInstance(result, int, "Output should be of type Int")

        # check if the result is correct
        self.assertEqual(result, expected_result)

@pytest.mark.dynamic_programming
@pytest.mark.lists
def test_kadanes_algorithm():
    test_data = [0]

    assert type(kadanes_algorithm(test_data)) is int

@pytest.mark.dynamic_programming
@pytest.mark.lists
def test_kadanes_algorithm_output_type():
    test_data = [-4, 2, -5, 1, 2, 3, 6, -5, 1]
    expected_result = 12

    assert kadanes_algorithm(test_data) == expected_result