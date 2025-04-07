# 유형 : 누적합
# 점수 따먹기 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

matrix = [list(map(int,input().split)) for _ in range(n)]

prefix_sum = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        prefix_sum[i][j] = (matrix[i-1][j-1] + prefix_sum[i-1][j]
        + prefix_sum[i][j-1] - prefix_sum[i-1][j-1])

result = float('-inf')

