# borrowed from
# https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
# and
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/



def knapsack_01_recursive(knapsack, items):
    """
    a recursive implementation of the 0-1 knapsack problem
    time complexity: O(2^n)
        there are redundant subproblems
    space complexity: O(1)
        no data structure is used to store any value
    :param knapsack:
        a knapsack data structure
    :param items:
        a list of tuples representing an item
        the first value is the value of the item, and the second is the weight
    :return:
        an int representing the maximum value you can get by filling the knapsack with your provided items
    """
    def fill_knapsack(remaining_room, n):
        # case of base
        # if we've reached the first element of the array
        # or there is no more room in the knapsack,
        # return 0
        if n==0 or remaining_room==0:
            return 0

        # get the components from the item
        value, weight = items[n-1]

        # if the weight of the nth item is more than the capacity of the knapsack
        # then this item can't be added to the optimal solution
        if weight > remaining_room:
            return fill_knapsack(remaining_room, n-1)

        # otherwise, return the larger of the two values:
        # 1: including the nth item
        # 2: excluding the nth item
        else:
            return max(value + fill_knapsack(remaining_room-weight, n-1),
                       fill_knapsack(remaining_room, n-1))

    return fill_knapsack(knapsack.capacity, len(items))


def knapsack_01_recursive_memoized(knapsack, items):
    """
    a recursive implementation of the 0-1 knapsack problem
    this uses a grid to compute all possible permutations
    :param knapsack:
        a knapsack data structure
    :param items:
        a list of tuples representing an item
        the first value is the value of the item, and the second is the weight
    :return:
        an int representing the maximum value you can get by filling the knapsack with your provided items
    """
    permutations = [[0 if i == 0 else None for _ in range(knapsack.capacity+1)] for i in range(len(items)+1)]

    def fill_knapsack(i, w):
        """
        Recursively find the optimal value to fill a knapsack with an item, i,
        and a remaining capacity w
        :param i:
        The index of the item we will check for fit
        :param w:
        The remaining capacity of the knapsack
        :return:
        The best fit of the knapsack
        """
        # case of base
        # if we've reached the first element of the array
        # or there is no more room in the knapsack,
        # return 0
        if i==0 or w==0:
            return 0

        # get the components from the item
        value, weight = items[i-1]

        # if the weight of the ith item is more than the capacity of the knapsack
        # then this item can't be added to the optimal solution
        if weight > w:
            return fill_knapsack(i-1, w)
        # check the permutation array for precomputed solutions
        if permutations[i][w] is not None:
            return permutations[i][w]
        # otherwise, return the larger of the two values:
        # 1: including the nth item
        # 2: excluding the nth item
        else:
            current_value = max(fill_knapsack(i-1, w), value+fill_knapsack(i-1, w-weight))
            permutations[i][w] = current_value
            return current_value

    return fill_knapsack(len(items), knapsack.capacity)

def knapsack_01_bottom_up(knapsack, items):
    """
    A function to solve the 0-1 knapsack problem iteratively
    time complexity: O(nW)
    space complexity: O(nW)
    :param knapsack:
        a knapsack data structure
    :param items:
        a list of tuples representing an item
        the first value is the value of the item, and the second is the weight
    :return:
        an int representing the maximum value you can get by filling the knapsack with your provided items
    """
    # create a 2d array, max_value[n+1][W+1]
    #   where n is the number of items
    #   and W is the max capacity of the knapsack
    #   note that the ranges increase each dimension by 1
    #   n+1 makes it easier to index up to n
    #   AND it allows us to fill the first row with 0, simplifying calculations
    #   W+1 is done because it allows you to account for all weights, from 0 to max capacity
    # each cell in the array represents the maximum possible value
    #   if item i is added (or ommited) and you have a remaining capacity of w
    #   where i is the index for the current item
    max_value = [[0 if i == 0 else None for _ in range(knapsack.capacity+1)] for i in range(len(items)+1)]

    for i in range(1, len(items)+1):
        for w in range(0, knapsack.capacity+1):
            # grab item i's components
            value, weight = items[i - 1]

            # there are two options for how you choose the value of the current cell
            # the first is if there is still enough room to put the current item in the backpack
            if weight <= w:
                # if you can fit the current item, the goal is still to find the largest value you can for the cell
                # the first option is to omit the current item, and use the value at max_value[i-1][w]
                #   that is the max value found when computing for the previous item with the remaining capacity of w
                # the second option is to include the current item
                #   this is done by adding the current value, to the maximum value computed for the previous item
                #   but with the current weight subtracted000000000000000000000000000001
                max_value[i][w] = max(max_value[i-1][w],
                                      value+max_value[i-1][w-weight])
            # the second is if the current item cannot fit in the backpack
            else:
                # if that's the case, the max capacity for this cell is the same
                # as the max capacity of the backpack when you checked it's max capacity for item i-1
                max_value[i][w] = max_value[i-1][w]

    return max_value[len(items)][knapsack.capacity]

