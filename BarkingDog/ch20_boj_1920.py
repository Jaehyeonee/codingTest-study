# https://dev-sungjun.tistory.com/30
import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int, input ().split()))

m = int(input())
num = list(map(int, input().split()))

A.sort()

for target in num:
    start = 0
    end = n-1
    while start <= end:
       mid = (start+end)//2
       if target > A[mid]:
            start = mid + 1
       elif target < A[mid]:
            end = mid - 1
       else:
           start = mid
           end = mid
           break
    if start == mid and end == mid:
        print(1)
    else:
        print(0)








