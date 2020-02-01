# counting sort

def sort(data, k):

    # count the number of each value in the input
    count = [0 for i in range(k+1)]
    for v in data:
        count[v] += 1

    # add find the sum of all values right of the final item
    # this gives a count of the number of items at or below the current index
    # starting at 0 for the first item
    total = 0
    for i in range(k+1):
        count[i], total = total, count[i] + total

    output = [0 for i in range(len(data))]

    for v in reversed(data):
        output[count[v]] = v

        # since we have a new element at index v
        # the count of values at or below v should be incremented
        count[v] += 1

    return output

def driver():
    data =  [2, 0, 2, 0, 3, 2, 2]

    print("Before sorting:")
    print(data)

    data = sort(data, 3)

    print("after sorting:")
    print(data)

driver()