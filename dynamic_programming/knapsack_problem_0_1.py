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
    permutations = [[0 if i == 0 else None for _ in range(knapsack.capacity+1)] for i in range(len(items)+1)]

    for i in range(1, len(items)+1):
        for w in range(0, knapsack.capacity+1):
            value, weight = items[i - 1]
            if weight <= w:
                permutations[i][w] = max(permutations[i-1][w], value+permutations[i-1][w-weight])
            else:
                permutations[i][w] = permutations[i-1][w]

    return permutations[len(items)][knapsack.capacity]