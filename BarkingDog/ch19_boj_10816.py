import sys
input = sys.stdin.readline
n = int(input())
card = [map(int, input().split()) ]
m = int(input())
problem = [map(int, input().split()) ]

n_dic = {}

for n in card:
  if n in n_dic:
    n_dic[n] += 1
  else:
    n_dic[n] = 1

for m in problem:
  if m in n_dic:
    print(n_dic[m], end=' ')
  else:
     print(0, end=' ')
