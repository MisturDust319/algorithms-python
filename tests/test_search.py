import unittest
import pytest

import search.binary_search_iterative
from search.boggle import find_all_strings, find_all_strings_history


class TestBinarySearch(unittest.TestCase):
    def test_binary_search(self):
        """
        Test binary search
        :return:
        """

        test_array = range(6)

        for i in range(6):
            self.assertTrue(
                search.binary_search_iterative.search(test_array, i),
                "Test the function finds all values in the array")


@pytest.mark.search
@pytest.mark.strings
def test_find_all_strings():
    # test data borrowed from: https://www.educative.io/m/boggle
    grid = [['c', 'a', 't'],
            ['r', 'r', 'e'],
            ['t', 'o', 'n']]

    dictionary = {"cat", "cater", "cartoon", "toon", "moon",
                  "not", "tone", "apple", "ton", "art"}

    result = find_all_strings(grid, dictionary)
    expected_result = {"not", "cat", "art", "cater", "ton", "tone"}

    assert result == expected_result


@pytest.mark.search
@pytest.mark.strings
def test_find_all_strings_history():
    # test data borrowed from: https://www.educative.io/m/boggle
    grid = [['c', 'a', 't'],
            ['r', 'r', 'e'],
            ['t', 'o', 'n']]

    dictionary = {"cat", "cater", "cartoon", "toon", "moon",
                  "not", "tone", "apple", "ton", "art"}

    result = find_all_strings_history(grid, dictionary)
    expected_result = {"not", "cat", "art", "cater", "ton", "tone"}

    assert result == expected_result
