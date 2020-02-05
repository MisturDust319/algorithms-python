# there are two major categories of dynamic programming
# memoization (top down) and tabulation (bottom up)
# this example uses memoization to compute the nth term of the fibonacci sequence

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0 for i in range(n+1)]
    dp[0], dp[1] = 0, 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def driver():
    print("5th fibonacci number: " + str(fibonacci(5)))

driver()