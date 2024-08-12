import sys
input= sys.stdin.readline

n,m = map(int,input().split())
result = []

def solution(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
        result.append(i)
        solution(i)
        result.pop()

solution(1)