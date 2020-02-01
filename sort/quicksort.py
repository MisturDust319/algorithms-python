# quicksort sorts around a pivot
# elements smaller than the pivot go before it, and larger after
# this is recursively applied at smaller sections of the list
# https://medium.com/basecs/pivoting-to-understand-quicksort-part-1-75178dfb9313

# often the pivot starts as the last element

def partition(array, start, end):
    # find the rightmost element
    # this is the pivot
    pivot = array[end]

    # i is used to track where to place values lower than the pivot
    # starting at 1 below start just makes managing this easier
    i = start - 1
    # j is the main index for running through the array
    j = start

    while j < end:
        # when the value at the current index is less than the pivot value
        if array[j] < pivot:

            i += 1
            # put the current value at the front of the current array section
            array[i], array[j] = array[j], array[i]
            # see the comment by the return statement for an explanation of why this works

        j += 1

    # because we put all elements below the pivot in the range [begin, i]
    # if we place the pivot at i, everything below i+1 is below the pivot
    # and everything above i+1 is higher
    array[i+1], array[end] = array[end], array[i+1]
    return i+1

def quicksort(array, start, end):
    # only continue sorting if there's at least two elements to sort
    if start < end:
        # partition the array
        # and find the index
        partition_index = partition(array, start, end)

        # split the array around the pivot
        # then repeat on the left, then right halves
        quicksort(array, start, partition_index - 1)
        quicksort(array, partition_index + 1, end)

def driver():
    data = [1, 5, 2, 4]

    print("Before sorting:")
    print(data)

    quicksort(data, 0, len(data)-1)

    print("after sorting:")
    print(data)

driver()