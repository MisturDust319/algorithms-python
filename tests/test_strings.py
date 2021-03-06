import pytest

from strings.string_segmentation import string_segmentation_recursive
from strings.string_segmentation import string_segmentation_memoized
from strings.string_segmentation import string_segmentation_tabulation
from strings.substring_palindromes import _find_palindromes_in_substring
from strings.substring_palindromes import find_substring_palindromes

@pytest.fixture
def create_string_segmentation_input():
    string = "applepie"
    words = {"apple": None, "pie": None, "pear": None, "pier": None}

    return string, words


@pytest.mark.strings
def test_string_segmentation_recursive_true(create_string_segmentation_input):
    # arrange: set up any variables we need
    string, words = create_string_segmentation_input
    # act: call your functions and perform any needed data operations
    result = string_segmentation_recursive(string, words)
    # assert: use an assert statement to test your results
    assert result is True


@pytest.mark.strings
def test_string_segmentation_recursive_false(create_string_segmentation_input):
    # arrange: set up any variables we need
    # get basic input
    string, words = create_string_segmentation_input
    # for the first test, remove one piece of data from the dictionary: apple
    del words["apple"]
    # this should cause a failure
    result = string_segmentation_recursive(string, words)
    assert result is False

    # try again with after deleting a second key from the dictionary
    del words["pie"]

    result = string_segmentation_recursive(string, words)
    assert result is False


@pytest.mark.strings
def test_string_segmentation_memoized_true(create_string_segmentation_input):
    # arrange: set up any variables we need
    string, words = create_string_segmentation_input
    # act: call your functions and perform any needed data operations
    result = string_segmentation_memoized(string, words)
    # assert: use an assert statement to test your results
    assert result is True


@pytest.mark.strings
def test_string_segmentation_memoized_false(create_string_segmentation_input):
    # arrange: set up any variables we need
    # get basic input
    string, words = create_string_segmentation_input
    # for the first test, remove one piece of data from the dictionary: apple
    del words["apple"]
    # this should cause a failure
    result = string_segmentation_memoized(string, words)
    assert result is False

    # try again with after deleting a second key from the dictionary
    del words["pie"]

    result = string_segmentation_memoized(string, words)
    assert result is False


@pytest.mark.strings
def test_string_segmentation_tabulation_true(create_string_segmentation_input):
    # arrange: set up any variables we need
    string, words = create_string_segmentation_input
    # act: call your functions and perform any needed data operations
    result = string_segmentation_tabulation(string, words)
    # assert: use an assert statement to test your results
    assert result is True


@pytest.mark.strings
def test_string_segmentation_tabulation_false(create_string_segmentation_input):
    # arrange: set up any variables we need
    # get basic input
    string, words = create_string_segmentation_input
    # for the first test, remove one piece of data from the dictionary: apple
    del words["apple"]
    # this should cause a failure
    result = string_segmentation_tabulation(string, words)
    assert result is False

    # try again with after deleting a second key from the dictionary
    del words["pie"]

    result = string_segmentation_tabulation(string, words)
    assert result is False

@pytest.mark.parametrize(
    "palindrome,expected",
    [("aa", 1), ("baab", 2), ("aabb", 2), ("aqzb", 0), ("abaa", 2)]
)
def test_substring_palindromes(palindrome, expected):
    assert find_substring_palindromes(palindrome) == expected

