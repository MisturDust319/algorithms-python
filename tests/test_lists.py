import unittest

# import the data structures
import data_structures

import lists.sum_of_three_values

class ClassTestSumOfThreeValues(unittest.TestCase):
    def setUp(self):
        self.sum = 22
        self.false_sum = 20000
        self.list = [1, 4, 45, 6, 10, 8]

    def test_sum_of_three_values_naive(self):
        """
        Test the naive implementation of sum of three values
        """

        # try to get a positive result
        self.assertTrue(lists.sum_of_three_values.sum_of_three_values_naive(self.list, self.sum))

        # try to get a negative result
        self.assertFalse(lists.sum_of_three_values.sum_of_three_values_naive(self.list, self.false_sum))

    def test_sum_of_three_values_two_pointers(self):
        """
        Test the two pointers variant of the sum of three values
        :return:
        None
        """
        # try to get a positive result
        self.assertTrue(lists.sum_of_three_values.sum_of_three_values_two_pointers(self.list, self.sum))

        # try to get a negative result
        self.assertFalse(lists.sum_of_three_values.sum_of_three_values_two_pointers(self.list, self.false_sum))
