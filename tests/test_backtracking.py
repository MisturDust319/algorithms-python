"""
Tests for backtracking problems
"""
import pytest

from backtracking.boggle import find_all_strings


@pytest.mark.backtracking
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