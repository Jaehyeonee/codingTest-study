import sys
input = sys.stdin.readline

n, m = map(int,input().split())

result = []

def solution():
    if len(result) == m:
        
        print(' '.join(map(str, result)))
        return
    
    for i in range(1, n+1):
        result.append(i)
        
        solution()
        
        result.pop()
       

solution()