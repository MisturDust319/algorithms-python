import unittest

import search.binary_search_iterative


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        """
        Test binary search
        :return:
        """

        test_array = range(6)

        for i in range(6):
            self.assertTrue(search.binary_search_iterative.search(test_array, i),
                            "Test the function finds all values in the array")
