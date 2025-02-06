import sys
input = sys.stdin.readline

n = int(input())
card = sorted(list(map(int, input().strip().split())))

m = int(input())
nums =list(map(int, input().strip().split()))
dic = {}

for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1


def binary_search(card, target, start, end):
    if start > end :
        return 0
    mid = (start + end)//2
    if target == card[mid]:
        return dic[target]
    
    elif target < card[mid]:
        return binary_search(card, target, start, mid-1)
    else:
        return binary_search(card, target, mid+1, end)

for target in nums:
    print(binary_search(card, target, 0, n-1),end=' ')