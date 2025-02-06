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

for target in nums:
    if target in dic:
        print(dic[target], end = ' ')
    else:
        print(0, end=' ')