import sys
from collections import deque
input = sys.stdin.readline

q = deque()
stack = []

N = int(input())
A = list(map(int, input().split())) # 자료구조
B = list(map(int, input().split())) # 초기원소
M = int(input())
C = list(map(int, input().split()))

# 자료구조에 초기 원소 넣기
# Stack의 경우 넣고 빠지는 원소가 같기 때문에 무시해도 됨
# 따라서 큐 자료구조에 들어가는 원소만 신경써줌

q = deque()
for i in range(N):
    if A[i] == 0 : # queue이면
        q.append(B[i])

for i in range(M):
    q.appendleft(C[i])
    print(q.pop(), end= ' ')
