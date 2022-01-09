#모범풀이 10,3,7,4,12,2
#https://g-idler.tistory.com/78

import sys

N = int(sys.stdin.readline())
li = [int(sys.stdin.readline()) for _ in range(N)]
stack, res = [], 0
for i in range(N):
    while stack != [] and stack[-1] <= li[i]:
        stack.pop()
    stack.append(li[i])
    res += len(stack)-1
print(res)




## -- Another Solution -- ##



import sys

#빌딩의 개수 
N = int(sys.stdin.readline())

#빌딩의 높이를 리스트로 만들기
h = [int(sys.stdin.readline()) for _ in range(N)]

stack = []
ans = 0 #옥상 볼수 있는 건물 수 횟수

for i in range(N - 1, -1, -1):
    seeable = 0
    while(True):
        if not len(stack):
            stack.append((0, h[i]))
            break

        if stack[-1][1] < h[i]:
            seeable += stack.pop()[0] + 1

            while(True):
                if not len(stack):
                    stack.append((seeable, h[i]))
                    ans += seeable
                    break
                if stack[-1][1] < h[i]:
                    seeable += stack.pop()[0] + 1
                else:
                    stack.append((seeable, h[i]))
                    ans += seeable
                    break

            break
        else:
            stack.append((0, h[i]))
            break

print(ans)
