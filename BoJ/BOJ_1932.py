# 24.12.15.
# 1932번 정수 삼각형
'''
반례
4
1    
0 1  
1 1 0
0 1 0 1
'''

import sys

input = sys.stdin.readline

n = int(input())
a = [0] * n
for i in range(n):
    a[i] = list(map(int, input().split()))
if n != 1:
    a[1][0] = a[0][0] + a[1][0]
    a[1][1] = a[0][0] + a[1][1]
    for k in range(2, n):
        a[k][0] = a[k - 1][0] + a[k][0]
        a[k][len(a[k]) - 1] = a[k - 1][len(a[k]) - 2] + a[k][len(a[k]) - 1]
        for i in range(1, len(a[k]) - 2):
            a[k][i] = max(a[k - 1][i], a[k - 1][i - 1]) + a[k][i]
    print(a)
    print(max(a[-1]))
else:
    print(a)
    print(a[0][0])