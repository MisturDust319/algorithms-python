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
    pass
    # # we use dynamic programming
    # # create a matrix of [len(string), len(string)]
    # # each cell in the matrix represents whether the a substring [i,i+l) is in our dictionary
    # # where i is the current index
    # # and l is the length of the substring we are checking
    # # and note we won't actually fill the whole matrix, only the top right half
    # string_length = len(string)
    # computation_matrix = [[None] * string_length] * string_length
    #
    # # we must check every possible continuous substring (from cat we could have c, ca, cat, at, c, but not ct)
    # # we do this by first by calculating all substrings of a particular length
    # # from a single character to the entire string length
    # for substring_length in range(string_length):
    #     # we now step through the string, checking each substring of a certain length
    #     for start_index in range(0, string_length - substring_length):
    #         # get the substring
    #         substring = string[start_index, start_index + string_length]
    #
    #         # if the substring is in the dictionary...
    #         if substring in dictionary:
    #             # then set the matrix cell at [start_index, string_length] to true
