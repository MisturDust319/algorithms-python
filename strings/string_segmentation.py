from collections import deque

def string_segmentation_recursive(string, dictionary):
    # iterate over the entirety of string
    for i in range(1, len(string)+1):
        # grab the substring of string and check if it's in the dictionary
        first = string[0:i]
        if first in dictionary:
            # if the first substring is in the dictionary
            # create a second substring with the remaining chars in string
            second = string[i:]
            if (not second # if the second string is empty
                or second in dictionary # ...or if it's in the dictionary
                or string_segmentation_recursive(second, dictionary)): # ...or it can be segmented further
                # the string can be segmented, so return True
                return True

    # if after iterating over the entire string,
    # we haven't been able to segment the string,
    # we have to return false
    return False


def string_segmentation_memoized(string, dictionary):
    # a hash to store previously computed substrings
    # the cache stores whether
    cache = {}

    # a helper function to recursively compute a solution
    def _compute_string_segmentation(_string):
        # otherwise iterate over the entirety of string
        for i in range(1, len(_string) + 1):
            # grab the substring of string and check if it's in the dictionary
            first = _string[0:i]
            if first in dictionary:
                # since the first substring is in the dictionary,
                # store it in the cache as True
                cache[_string] = True

                # if the first substring is in the dictionary
                # create a second substring with the remaining chars in string
                second = _string[i:]
                if (not second  # if the second string is empty
                        or second in dictionary  # ...or if it's in the dictionary
                        or (second in cache and cache[second] is True)  # ...or second is in the cache
                        or _compute_string_segmentation(second)):  # ...or it can be segmented further
                    # the string can be segmented, so return True
                    return True
            else:
                # since first isn't in the dictionary,
                # store it in the cache as False
                cache[_string] = False

        # if after iterating over the entire string,
        # we haven't been able to segment the string,
        # we have to return false
        return False

    return _compute_string_segmentation(string)


def string_segmentation_iterative(string, dictionary):
    """
    A solution for the string segmentation problem that uses iteration and memoization
    borrowed from: https://iq.opengenus.org/word-break-problem/
    """
    n = len(string)
    if n == 0:
        return True

    # a cache of
    cache = [False] * (n + 1)
    # the matched index list is a list of indices where substrings that are in the dictionary begin
    matched_index = [-1]

    # we check each possible continuous substring in string that start at the first string
    for i in range(n):
        matched_index_list_size = len(matched_index)

        # we iterate backwards through the list of positive substring matches
        for j in range(matched_index_list_size - 1, -1, -1):
            # we construct our substring as [index after last found substring, i]
            # (when no matches have been found, we just search [0,i]
            # we force this by storing -1 as the initial value in the matched index array)
            # when you have a match, it immediately starts search after the last found positive substring
            # and searches to i, which helps avoid redundant calculations
            # if this doesn't match, it retrieves the index for the second most recently found positive substring
            # and "prepends" this to the last substring, and rechecks the dictionary
            # this cycle of checking, prepending, then checking again will continue until we check substring[0,i]
            # or we get a positive match, in which case we increment i and repeat the process
            sub_string = string[matched_index[j] + 1: i + 1]
            if sub_string in dictionary:
                # if the current substring is true,
                # set the index at i to be true
                cache[i] = True
                # and append this index to the list of positively matched indices
                matched_index.append(i)
                break

    return cache[n - 1]
