# there are two major categories of dynamic programming
# memoization (top down) and tabulation (bottom up)
# this example uses memoization to compute the nth term of the fibonacci sequence

def fibonacci(n):
    lookup = { 0 : 0, 1 : 1 }

    def f(n):
        if n in lookup:
            return lookup[n]
        else:
            lookup[n] = f(n - 1) + f(n - 2)
            return lookup[n]
    return f(n)

def driver():
    print("5th fibonacci number: " + str(fibonacci(5)))

driver()