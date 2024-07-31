import sys
input = sys.stdin.readline

n = int(input())
order = list(map(int, input().split()))
stack= []
now = 1
for k in order:
    stack.append(k)
    while stack and stack[-1] == now:
        stack.pop()
        now += 1

if stack:
    print('Sad')
else:
    print('Nice')



    

