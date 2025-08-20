''''
A = [10, 20, 10, 30]
dp 배열 진행 (방식: j를 끝으로 하는 LIS)
초기: dp = [1, 1, 1, 1] (모두 자기 자신만 있을 때 길이는 1)
'''
import sys
input = sys.stdin.readline

N = int(input())

A = list(map(int, input().split()))

dp = [1] * N           # 부분 수열 즉, 자기 자신으로도 수열 하나가 되기 때문에

for i in range(N-1):
    for j in range(i+1, N):
        if A[i] < A[j]:
            dp[j] = max(dp[j], dp[i] + 1)


# for i in range(N):
#     if A[i] > current_max:
#         dp[i] = max(dp) + 1
#         current_max = A[i]
    
print(max(dp))   




