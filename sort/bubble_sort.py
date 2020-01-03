a = [1, 3, 5, 2, 4]

def sort(a):

    a_length = len(a)

    for i in range(a_length):
        # note how we stop sorting the last element from the previous pass
        # because we know that every pass naturally passes the highest value to the back
        # the numbers "bubble" to the top
        # since a[N] is always going to be less than a[N+1]
        for j in range(a_length - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]

sort(a)
print(a)
