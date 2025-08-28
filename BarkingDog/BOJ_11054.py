import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input().split()))

dp = [1] * n
# 1. 증가하는 가장 긴 부분수열 구하기
for i in range(n):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j]+1)

reverse_dp = [1] * n
reverse_A = A[::-1]


for i in range(1,n):
    for j in range(i):
        if reverse_A[j] < reverse_A[i]:
            reverse_dp[i] = max(reverse_dp[i], reverse_dp[j]+1)

print(dp)
print(reverse_dp[::-1])

ans = 0
for i in range(n):
    ans = max(ans, dp[i]+reverse_dp[::-1][i]-1)
print(ans)

# 2. 감소하는 가장 긴 부분수열 구하기
# 3. Sk에 해당하는 값 하나는 빼주기

