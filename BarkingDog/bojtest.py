import sys
input = sys.stdin.readline

N = int(input())
flowers = list([map(int, input().split())] for _ in range(N))

current = (3, 1)
tmp = []
count = 0
def solution(flowers):
    i = 0
    while i < N:
        sm, sd, em, ed = flowers[i]
        if (sm, sd) <= current < (em, ed):
            max_end = (em, ed)
    # for i in range(N):
    #     sm, sd, em, ed = flowers[i]
    #     if (sm, sd) <= current < (em, ed):
    #         tmp.append((em,ed))
    # current = max(tmp)   
    # count += 1
    # i += 1
    # return result
