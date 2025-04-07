import sys
input = sys.stdin.readline

n = int(input())
pi = list(map(int, input().split()))

pi.sort()
time = 0 
answer = []

for i in pi:
    time += i
    answer.append(time)

print(sum(answer))