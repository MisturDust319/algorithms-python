"""
Substring Palindromes
Given an input string,
find all non-single letter palindromes in all substrings
from: https://www.educative.io/m/find-all-palindrome-substrings
"""


def _find_palindromes_in_substring(string, lower_bound, upper_bound):
    """
    Counts all palindromes in a substring
    borrowed from: https://www.educative.io/m/find-all-palindrome-substrings
    """
    count = 0

    # it is expected that you provide an upper and lower bound
    # around the midpoint of the string, and it iteratively increases the upper and lower bounds
    # until it fails to match a palindrome
    while (lower_bound >= 0
            and upper_bound < len(string)):
        # check that the upper and lower bound match
        if string[lower_bound] != string[upper_bound]:
            # if they don't, stop checking for more palindromes
            break
        # if they do match, increment the count...
        count += 1

        # ...and readjust the bounds
        lower_bound -= 1
        upper_bound += 1

    return count

def find_substring_palindromes(string):
    # get the length of string
    string_length = len(string)
    count = 0
    for i in range(string_length):
        count += _find_palindromes_in_substring(string, i - 1, i + 1)
        count += _find_palindromes_in_substring(string, i, i + 1)

    return count
