# 유형: DP
'''
dp[1] = 1
dp[2] = 2
Op[3] = 4 : 1+1+1, 1+2, 2+1, 3
dp[4] = 7 : 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2, 1+3, 3+1
dp[5] = 13 : 1+1+1+1+1, 1+2* 5개, 2+2+1 * 3개, 3+1+1 *3게, 3+2 
dp[6] = 24 : 1+1+1+1+1+1, 1+2*5개, 2+2+1+1 * 6개, 3+1+1+1*4개, 3+2+1 6개, 3+3 1개
dp[7] = 44

점화식으로 표현 : f(n) = f(n-3) + f(n-2) + f(n-1) -> *단 n>3
dp[4] = 1+3 | 2+2 | 3+1
         4     2     1  = 7개
dp[5] = 1+4 | 2+3 | 3+2
         7     4     2  = 13개
dp[6] = 1+5 | 2+4 | 3+3
         13    7     4  = 24개
...


'''
import sys
input = sys.stdin.readline

def solution(n):
    dp = [0]*(n+1)
    for i in range(1,n+1):
        if i == 1:
            dp[i] = 1
        elif i == 2:
            dp[i] =2
        elif i ==3:
            dp[i]=4
        else:
            dp[i] = dp[i-1]+dp[i-2]+dp[i-3]
    return dp[i]


t = int(input())
for i in range(t):
    n = int(input())
    print(solution(n))
