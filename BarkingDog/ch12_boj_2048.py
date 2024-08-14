# 시뮬레이션 2차 
import sys
from copy import deepcopy
input = sys.stdin.readline

n = int(input().strip())
block = [list(map(int, input().split())) for _ in range(n)]

# top = 마지노선을 의미
def move(board, direction):
    if direction == 0: #동
        for i in range(n):
            top = n-1
            for j in range(n-2, -1, -1):
                # print('board[i][j]', (i,j))
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = tmp
    elif direction == 1: # 서
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp

    elif direction == 2: # 남
        for i in range(n):
            top = n-1
            for j in range(n-2, -1, -1):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[top][i] == 0:
                        board[top][i] = tmp
                    elif board[top][i] == tmp:
                        board[top][i] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][i] = tmp    
    else: # 북
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[j][i]:
                    tmp = board[j][i]
                    board[j][i] = 0
                    if board[top][i] == 0:
                        board[top][i] = tmp
                    elif board[top][i] == tmp:
                        board[top][i] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][i] = tmp
    return board

def dfs(board, cnt):
    global ans
    if cnt == 5:
        ans = max(map(max, board))
        return
    for i in range(4):
        global tmp_board 
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)    
ans = 0
dfs(block, 0)
print(tmp_board)
print(ans)