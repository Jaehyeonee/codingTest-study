"""
 스택 2개를 활용해 문제를 해결할 수 있다.
 [ stack_1 ]<cursor>[ stack_2 ]
"""
import sys
input = sys.stdin.readline
word = list(input().strip()). # 왼쪽 스택
n = int(input())

cursor = len(word)

right_stack = []              # 오른쪽 스택

for i in range(n):
    command = list(input().split())

    if command[0] == 'L' and word:
        right_stack.append(word.pop())
    elif command[0] == 'D' and right_stack:
        word.append(right_stack.pop())
    elif command[0] == 'B' and word:
        word.pop()
    elif command[0] == 'P':
        word.append(command[1])

right_stack.reverse()
# print(right_stack[::-1])
answer = word + right_stack
print(''.join(answer))
