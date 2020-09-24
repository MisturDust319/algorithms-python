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


def string_segmentation_memoized(string, words):
    pass


def string_segmentation_iterative(string, words):
    pass
