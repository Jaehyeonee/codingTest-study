import sys
input = sys.stdin.readline


def draw(n):
    dp = [0]*(n+1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + 2 *dp[i-2]
    return dp[n]%10007



n = int(input())
print(draw(n))

# 방법2
# a=b=1
# for i in range(int(input())):
#     a,b = b, 2*a+b
# print(a%10007)

#  방법1
# n = int(input())
# dp = [0]*1001

# dp[0]=1
# dp[1]=1

# for i in range(2, n+1):
#     dp[i]= dp[i-1]+2*dp[i-2]
# print(dp[n]%10007)

