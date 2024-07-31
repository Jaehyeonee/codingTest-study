import sys
input = sys.stdin.readline

n, k = map(int, input().split())

q = [i for i in range(1, n+1)]

answer = []
idx = 0
while q: 
    idx += k-1
    if idx >= len(q):
        idx %= len(q)
        print(idx)
        print(q[idx])
    answer.append(str(q.pop(idx)))

print("<", ", ".join(answer), ">", sep="")

