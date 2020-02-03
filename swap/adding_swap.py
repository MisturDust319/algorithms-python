# counting sort


def swap(input, i, j):
    input[i] += input[j]
    input[j] = input[i] - input[j]
    input[i] -= input[j]

    # x = x + y
    # y = x - y
    # x = x - y
    # OR
    # x := x + y
    # y := (x + y) - y = x
    # x := (x + y) - x = y

def driver():
    data = [10, 5]

    print("Before swap:")
    print(data)

    swap(data, 0, 1)

    print("after swap:")
    print(data)

driver()

