"""
Implementation of Kadane's algorithm
an algorithm used to find the largest possible sum of a continuous sub-array
it uses dynamic programming
"""


def kadanes_algorithm(array):
    """
    Kadane's Algorithm
    an algorithm that finds the largest possible sum of a continuous sub-array
    this implementation is of O(n) time complexity, but constant space complexity
    borrowed from: https://hackernoon.com/kadanes-algorithm-explained-50316f4fd8a6
    """
    # a sub-array sum can result in a local maximum and a global maximum
    # just because the current sum is large, doesn't mean it was the largest sum found yet
    # we initially init both to the first element in the array
    local_max = global_max = array[0]

    # we check the rest of the array to see if there is a sum that can be found greater
    # than the value of the first element (a sub-array of one item)
    for current_value in array[1:]:
        # we want to find the largest possible sub-array sum
        # if a sum is lower than 0, it is better to try to start a new sum starting fresh with the current value
        # to check which option we choose, we choose the greater of two values:
        # - the previous local max (the sub-array sum thus far)
        # - 0 (starting fresh)
        local_max = max(local_max, 0) + current_value

        # since the current local sum may not be the greatest local sum, we keep a global max sum
        # after every local sum is calculated, if it is the greatest sum so far, we store it as the global sum
        global_max = max(local_max, global_max)

    # return the global sum
    return global_max
