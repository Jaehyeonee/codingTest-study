
import sys
input = sys.stdin.readline

# dp[i] = max(d[i-1], cur, dp[i-1]+cur)
'''
> 잘못된 점화식에서의 문제

dp[i] = max(dp[i-1], cur, dp[i-1]+cur)라고 하면:

dp[i-1] = i-1번째 원소를 끝으로 하는 연속합

그런데 dp[i]는 i번째 원소를 반드시 포함해야 하는데, dp[i-1]을 그대로 가져와버리면 “i번째 원소를 건너뛴 경우”까지 들어감 ❌

그러면 dp[i]가 “연속 부분합”이 아니라 그냥 “0~i까지 구간에서 최대 연속합”으로 의미가 바뀌어버림 → 정의가 틀림.
'''
# MIN = -10001
n = int(input())

lst = list(map(int, input().split()))

dp = [0] * n 
dp[0] = lst[0]

for i in range(1, n+1):
    # cur = lst[i-1]
    dp[i] = max(lst[i], dp[i-1]+lst[i]) 

print(max(dp))