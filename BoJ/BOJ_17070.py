import sys
input =  sys.stdin.readline


n = int(input())
home = list([map(int, input().split) for _ in range(n)])

direction = [[]]