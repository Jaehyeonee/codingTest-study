## -- solution 1 -- ##

import sys
lines = sys.stdin.readlines()
for line in lines[:-1]: #빈칸공백 제거X-> 마지막이 빈칸 제외하고 문장 전체를 의미
    stack = []
    for t in line:
        if t in '([':
            stack.append(t)
        elif t == "]":
            if not stack or stack.pop() != '[':
                print('no')
                break
        elif t == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif t == '.': 
            if stack: #.하나만 있지 않은 경우 -> false
                print('no')
            else:
                print("yes")
                
                
## -- solution 2 -- ##


import sys
lines = sys.stdin.readlines()
for line in lines[:-1]: #빈칸공백 제거X-> 마지막이 빈칸 제외하고 문장 전체를 의미
    stack = []
    for t in line:
        if t in '([':
            stack.append(t)
        elif t == "]":
            if not stack or stack.pop() != '[':
                print('no')
                break
        elif t == ')':
            if not stack or stack.pop() != '(':
                print('no')
                break
        elif t == '.':
            if stack: #.하나만 있지 않은 경우 -> false
                print('no')
                break
            else:
                print("yes")
                break

