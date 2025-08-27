'''
⭐️주의 
이번잔 안 마심        dp[i-1]   <-- dp[i-1]에 또 다시 i-1에 대한 3가지의 경우가 들어 있기 때문에 dp[i-1]만 고려해주면 됨!
이번잔만 마심         dp[i-2] + 현재값
이번잔 + 이전 잔 마심  dp[i-3] + 현재값 + 직전값


⭐️주의 
n = 1인 경우 
amount[2], wine[2]가 없기 때문에 n > 1 경우로 [2] 초기화 해주기

'''

import sys
input = sys.stdin.readline

n = int(input())
wine = [0]
for _ in range(n):
    grape = int(input())
    wine.append(grape)

amount = [0] * (n+1)
amount[1] = wine[1] 

if n > 1:
    amount[2] = wine[1] + wine[2]

# 0 0 0 (0)

for i in range(3, n+1):
    amount[i] = max(amount[i-1], amount[i-3]+wine[i-1]+ wine[i],amount[i-2]+ wine[i])


print(amount[-1])