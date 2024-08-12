# ch10 - 백트래킹
# https://velog.io/@blcklamb/%EB%B0%B1%EC%A4%80Python-15650%EB%B2%88-N%EA%B3%BC-M2%EC%9D%B4%EA%B2%8C-%EC%99%9C-%EB%8D%94-%EB%B9%A8%EB%9D%BC
import sys

input= sys.stdin.readline

n,m = list(map(int, input().split()))
result = []

def solution(start):
    if len(result) == m:
        print(' '.join(map(str, result)))
        return
    for i in range(start, n+1):
        if i not in result:
            result.append(i)
            
            solution(i+1)
            result.pop()
            

solution(1)

