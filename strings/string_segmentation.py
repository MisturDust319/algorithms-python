from collections import deque


def string_segmentation_recursive(string, dictionary):
    # iterate over the entirety of string
    for i in range(1, len(string) + 1):
        # grab the substring of string and check if it's in the dictionary
        first = string[0:i]
        if first in dictionary:
            # if the first substring is in the dictionary
            # create a second substring with the remaining chars in string
            second = string[i:]
            if (not second  # if the second string is empty
                    or second in dictionary  # ...or if it's in the dictionary
                    or string_segmentation_recursive(second, dictionary)):  # ...or it can be segmented further
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


def string_segmentation_tabulation(string, dictionary):
    """
    A solution for the string segmentation problem that uses tabulation
    borrowed from: https://iq.opengenus.org/word-break-problem/
    """
    n = len(string)
    if n == 0:
        return True

    # a cache equal in length to the size of our input string
    # each value in the cache is a boolean value, and cell i represents whether a substring of of length i
    # has been found or not
    cache = [False] * (n + 1)
    # the matched index list is a list of indices where substrings that are in the dictionary begin
    # we also keep a list of indices
    # each index is the index of the final character of a substring that has been matched in the dictionary
    matched_indices = deque([-1])

    # we check each possible continuous substring in string that start at the first string
    # we process substrings by
    for max_search_index in range(n):
        for previously_matched_index in reversed(matched_indices):
            # there are two ways we can construct a substring
            # first, the most basic way is from [0,max_search_index], the largest possible substring to search
            # this is the default behavior when no matches have been found so far
            # or if the second method has exhausted all possible other values
            # note we force this behavior by storing -1 as the first (and possibly only) value in matched_indices
            # the other way we may construct a substring is from [previously_matched_index+1,max_search_index]
            # this starts the search immediately after the last positive matching index
            # allowing us to possibly skip checking lower indices for other matches
            # if this new substring isn't a match, the code "prepends" previous positive matches to the substring
            # to see if a match is made
            # (ex. if "west" and "westwing" are in the dictionary and our string is "westwing")
            # this is because if a match is made, we can't partially backtrack,
            # we either keep it or swap it out for something else
            sub_string = string[previously_matched_index + 1: max_search_index + 1]
            if sub_string in dictionary:
                # if the current substring is true,
                # set the index at max_search_index to be true
                cache[max_search_index] = True
                # and append this index to the list of positively matched indices
                matched_indices.append(max_search_index)
                break

    return cache[n - 1]
