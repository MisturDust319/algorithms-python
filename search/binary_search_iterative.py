# Binary search can quickly find a value in a sorted array

def search(a, s):
    """
    performs a binary search on a
    :param a:
    a sorted array to search
    :param s:
    the value to search
    :return:
    """
    # i and j are the lower and upper limits of the search range
    # start at the first element...
    i = 0
    # ...and the last element of the array
    j = len(a) - 1

    # it is possible the value isn't in the array
    # if j is lower than i, then we've not found it in the only range of values it could occupy
    # so its not in the array
    while i <= j:
        # m is the midpoint of the range
        # it is the midpoint we check for our search value
        m = (i + j) // 2
        v = a[m]

        # if v equals s (our search value)
        if s == v:
            return True
        # if not at point m, s could be above or below m
        # since a is sorted, if v is greater than s, than search the range of values below m
        elif v > s:
            # this is done by setting the upper limit of the range, j, to m-1
            j = m - 1
        # otherwise, s is in the range above m
        else:
            # set the lower search limit to m+1
            i = m + 1

    return False