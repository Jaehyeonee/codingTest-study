import sys
input = sys.stdin.readline

n = int(input())
score = [0]*301
for i in range(1,n+1):
    score[i] = int(input())

dp = [0]*301

dp[1] = score[1]
dp[2] = score[1]+score[2]
dp[3] = max(score[1]+score[3], score[2]+score[3])

for i in range(4, n+1) :
    dp[i] = max(score[i-1]+score[i]+dp[i-3], dp[i-2]+score[i])

print(dp[n])