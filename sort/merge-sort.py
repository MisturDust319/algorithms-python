# from https://www.interviewbit.com/tutorial/merge-sort-algorithm/

def merge(array, start, mid, end):
    # this is used to hold the merged data
    temp = [0] * (end - start + 1)
    
    # i: index for lower range
    # j: index for upper range
    # k: index for temp
    i, j, k = start, mid+1, 0

    # traverse both subarrays
    # at each step, insert the smaller of the current subarray item into temp
    # and increment the selected subarray's index
    while i <= mid and j <= end:
        # subarray 1: [start, mid]
        # subarray 2: [mid, end]
        v1 = array[i]
        v2 = array[j]
        
        # if the item in subarray 1 is smaller, insert it into the temp array
        # and increment the corresponding index  
        if v1 <= v2:
            temp[k] = v1
            i += 1
        # otherwise, insert the current item in subarray 2
        else:
            temp[k] = v2
            j += 1

        # regardless, increment the temp array index
        k += 1

    # add in any remaining elements
    # first check subarray 1 for remaining elements
    while i <= mid:
        temp[k] = array[i]
        i += 1
    # then subarray 2
    while j <= end:
        temp[k] = array[j]
        j += 1
        k += 1

    # copy temp into original array
    for i in range(start, end+1):
        # adjust the index for temp, as it has a different start
        array[i] = temp[i - start]

def sort(array, start, end):
    if start < end:
        # find the midpoint of the input array
        mid = (start + end) // 2

        # merge sort only works if the arrays you are merging are both sorted
        sort(array, start, mid)
        sort(array, mid+1, end)
        merge(array, start, mid, end)

def driver():
    data = [2, 0, 2, 0, 3, 2, 2]

    print("Before sorting:")
    print(data)

    sort(data, 0, len(data) - 1)

    print("after sorting:")
    print(data)

driver()