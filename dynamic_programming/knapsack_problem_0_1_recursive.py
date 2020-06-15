# borrowed from
# https://www.geeksforgeeks.org/python-program-for-dynamic-programming-set-10-0-1-knapsack-problem/
# and
# https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/



def knapsack_01_recursive(knapsack, items):
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

