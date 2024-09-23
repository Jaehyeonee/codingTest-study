import sys
input = sys.stdin.readline

n, k = map(int, input().split())

# def factorial(n):
#     ans = 1
#     for i in range(2, n+1):
#         ans *= i
#     return ans

# def coef(n, k):
#     return (factorial(n) // factorial(k) // factorial(n-k)) % 10007

# print(coef(n,k))

def coef(n,k):
    dp = [[0]*(k+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = 1
    for i in range(k+1):
        dp[i][i] = 1
    for i in range(1, n+1):
        for j in range(1, k+1):
            dp[i][j] = dp[i-1][j] + dp[i-1][j-1]
    return dp[n][k]
print(coef(n,k) % 10007)