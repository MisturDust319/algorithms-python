# selection sort works by finding the smallest element, and placing it at the array beginning

# selection sort works by dividing the array into two subarrays
# and finding the largest element of the first subarray
# which would be the element smaller than the first element of the second subarray
# this continuously pushes
def sort(array):
    l = len(array)

    for i in range(l):
        # find the minimum index
        # the index of the smallest element in the second subarray
        # which is also the largest element in the first subarray
        min_i = i

        for j in range(i+1, l):
            if array[j] < array[min_i]:
                temp = array[min_i]
                array[min_i] = array[j]
                array[j] = temp

def driver():
    data = [2, 0, 2, 0, 3, 2, 2]

    print("Before sorting:")
    print(data)

    sort(data)

    print("after sorting:")
    print(data)


driver()