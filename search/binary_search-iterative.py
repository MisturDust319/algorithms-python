a = [1, 2, 3, 4, 5, 6]


def search(a, s):
    i = 0
    j = len(a) - 1

    while i <= j:
        m = (i + j) // 2
        v = a[m]

        if s == v:
            return True
        elif v > s:
            j = m - 1
        else:
            i = m + 1

    return False


print(search(a, 1))