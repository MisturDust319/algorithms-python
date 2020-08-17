# from: https://www.educative.io/m/sum-of-three-values
# "Given an array of integers and a value,
# determine if there are any three integers in the array whose sum equals the given value."
# solutions based on https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/

# the Counter class will help track instances of
from collections import Counter

def sum_of_three_values_naive(list, sum):
    """
    A naive implementation of the triplet sum that runs in Theta(n^3) time
    :param list:
    the list of ints to search for the sum in
    :param sum:
    the value we want to search for in the list
    :return:
    True if sum is found, False otherwise
    """
    list_length = len(list)

    # this code works by find every possible triplet in the list, and summing them together
    # i is the first item
    # it iterates to the third to last element, because we're trying to find a triplet with the remaining values
    for i in range(list_length - 2):
        # j is the second value, it is the range of values above i to the second to last element
        # note this means the range changes on each iteration of the outer loop
        for j in range(i+1, list_length-1):
            # k is the third item in the sum, and is the range of values above j to the final element in the list
            # it is dynamic, and changes with each iteration of the outer loops
            for k in range(j+1, list_length):
                # add together the triplet
                # if it equals sum, return True
                if list[i] + list[j] + list[k] == sum:
                    return True

    # if after exhaustively finding each possible triplet and summing them together yields no sum equal to value,
    # return False
    return False

def sum_of_three_values_two_pointers(list, sum):
    """
    A solution to the "Sum of Three Values" problem that sorts the list and uses 2 'pointers'
    to increase code efficiency
    :param list:
    the list of ints to search for the sum in
    :param sum:
    the value we want to search for in the list
    :return:
    True if sum is found, False otherwise
    """

    # first sort the array
    list.sort()
    # grab the list size, since it will be reused in the problem
    list_length = len(list)

    # this solution works by stepping through the list one element at a time
    # and only forming triplets of values above the current value
    for i in range(0, list_length-2):
        # get the first value in the triplet from the list at i
        val1 = list[i]
        # if value is already greater than the sum, we can stop early
        # since we know after sorting all values above i are equal to or greater than i
        if val1 > sum:
            return False

        # the other two values in the triplet are found by using upper and lower bounds
        # the lower bound starts at the element immediately after the current value
        lower_bound = i+1
        # the upper bound starts at the final element of the list
        upper_bound = list_length-1
        # only continue when the lower bound is less than the upper bound
        while lower_bound < upper_bound:
            # get the triplet sum
            triplet_sum = val1 + list[lower_bound] + list[upper_bound]
            # first we check if the triplet sum is equal to the sum
            if triplet_sum is sum:
                # if yes, we've found our value and can return true
                return True

            # otherwise...
            # this code depends on a sorted list
            # we know the values ascend as we go further in the list
            # so, if the triplet sum is too low, we try again by incrementing the lower bound,
            # increasing the triplet sum
            elif triplet_sum < sum:
                lower_bound += 1
            # or if the triplet sum is too high, decrement the upper bound,
            # decreasing the triplet sum
            else:
                upper_bound -= 1

    # if we've reached this point, we've thoroughly searched the list and know that the triplet sum doesn't exist
    # in this list
    # So, return false
    return False