import sys
input = sys.stdin.readline

n = int(input())
arr =[]

for _ in range(n):
    arr.append(input().strip().split())

# data = [[int(age), name] for age, name in arr]
for i in range(n):
    arr[i][0] = int(arr[i][0])

arr.sort(key = lambda x : x[0])

for i in range(n):
    print(' '.join(map(str, arr[i])))