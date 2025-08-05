import sys
from collections import deque
input = sys.stdin.readline

n, m, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
deq = deque()
cycle = min(n,m)//2
result = [[0]*m for _ in range(n)]

for cy in range(cycle):
    deq.extend(matrix[cy][cy:m-cy])
    deq.extend([row[m-cy-1] for row in matrix[cy+1:n-cy-1]])
    deq.extend(matrix[n-cy-1][cy:m-cy][::-1])
    deq.extend([row[cy] for row in matrix[cy+1:n-cy-1][::-1]])

    # print(deq)

    deq.rotate(-r)
    # print(deq)


    for j in range(cy, m-cy):
        result[cy][j] = deq.popleft()

    for j in range(cy+1, n-cy-1):
        result[j][m-cy-1] = deq.popleft()

    for j in range(m-cy-1, cy-1, -1):
        result[n-cy-1][j] = deq.popleft()

    for j in range(n-cy-2, cy, -1):
        result[j][cy] = deq.popleft()

for r in result:
    print(*r)

'''
3 4 8 12
2 11 10 16
1 7 6 15
5 9 13 14

'''