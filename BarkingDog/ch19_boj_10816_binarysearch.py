import sys
input = sys.stdin.readline

n = int(input())
card = sorted([map(int, input().split())])
m = int(input())
problem = [map(int,input().split())]
dic = {}

for c in card:
    if c in dic:
        dic[c] += 1
    else:
        dic[c] = 1 

def binary_search(card, p, start, end):
    if start > end :
        return 0
    mid = (start + end)//2
    if p == card[mid]:
        return dic[mid]
    
    elif p < card[mid]:
        return binary_search(start, mid-1)
    else:
        return binary_search(mid+1, end)

for target in problem:
    print(binary_search(card, target, 0, n-1, end=' '))