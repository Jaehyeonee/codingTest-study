import sys
input = sys.stdin.readline

n = int(input())

num = list(int(input()) for _ in range(n))

def merge_sort(num):
    if len(num) <= 1:
        return num
    mid = len(num) // 2
    left = num[:mid]
    right = num[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result=[]
    i, j = 0,0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result += left[i:]
    result += right[j:]

    return result

ans = merge_sort(num)
for i in range(n):
    print(ans[i])
