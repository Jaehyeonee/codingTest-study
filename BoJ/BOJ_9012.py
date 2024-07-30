def solve(command):
    stack=[]
    for i in command:
        if i == '(':
            stack.append(i)    
        
        elif i == ')': ## ')'일때 
            if stack:
                if stack[-1] == '(':
                    stack.pop()
            else:
                stack.append(')')
         
    if stack:
        return 'NO'
    else:
        return 'YES'


T = int(input())
for _ in range(T):
    command = input()
    print(solve(command))