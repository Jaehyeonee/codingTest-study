'''
    https://www.acmicpc.net/problem/2577
'''
import sys
input = sys.stdin.readline

a= int(input())
b = int(input())
c = int(input())
multi_num = str(a*b*c)
arr = [0]* 10

for i in range(len(multi_num)):
    idx = int(multi_num[i])
    arr[idx] += 1

for j in range(10):
    print(arr[j])



