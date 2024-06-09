import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
ws =[]
w=0

def dfs(x,y):
    global w
    
    if x<0 or x>=n or y<0 or y>=n:
        return False
    if graph[x][y] == 1:
        
        graph[x][y] = -1
        
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        w+=graph[x][y]         
        return True
    
    return False

count = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            count+=1
            ws.append(abs(w))
            ws.sort()
            w = 0
            
print(count)
print(*ws)
print(graph)

