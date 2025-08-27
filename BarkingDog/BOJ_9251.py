
'''
2차원 dp배열 생성시 패딩이 되는 0행 0열 만들기
max(같은 열 이전 행, 같은 행 이전 열)

'''

import sys
input = sys.stdin.readline

s1 = input().strip()
s2 = input().strip()

# print(s1, s2)
ls1 = len(s1)
ls2 = len(s2)

dp = [[0]*(ls2+1) for _ in range(ls1+1)]

for i in range(1, ls1+1):
    for j in range(1, ls2+1):
        if s1[i-1] == s2[j-1]:
            dp[i][j] = 1 + dp[i-1][j-1]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])
