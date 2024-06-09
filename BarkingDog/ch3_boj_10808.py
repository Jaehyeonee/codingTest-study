'''
https://www.acmicpc.net/problem/10808
'''
import sys
input = sys.stdin.readline

n = input()
arr = [0] * 26
for i in range(len(n)-1):
    
    idx = ord(n[i])- ord('a')
    
    arr[idx] += 1
    
for j in range(len(arr)):
    print(arr[j], end= ' ')
    