# https://www.acmicpc.net/problem/14503
# n*m 크기 직사각형 공간
# 동서남부 방향
# 칸 좌표는 (r,c)
# (0,0) .............
   
#  .........(n-1, m-1)   

# 현재 주변으로 청소 전방향 완료 > 후진 > 현재 칸 청소       
# d=0 북쪽, =1:동쪽 , =2:남쪽, =3:서쪽


n, m = map(int, input().split())
vaccum_move_map = [[0] * m for _ in range(n)]

x, y, direction = map(int,input().split())



vaccum_map = []
for i in range(n):
    vaccum_map.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    
    nx = x+dx[direction]
    ny = y+dy[direction]

    if vaccum_move_map[nx][ny]==0 and vaccum_map[nx][ny] ==0:
        vaccum_move_map[nx][ny]=1
        count += 1

        x, y = nx, ny

        turn_time =0
        continue
    else:
        turn_time +=1

    if turn_time == 4: # 후진
        nx = x-dx[direction]
        ny = y-dy[direction]

        if vaccum_map[nx][ny] == 0:
            x, y = nx, ny
        else:
            break
        turn_time = 0

print(count)


