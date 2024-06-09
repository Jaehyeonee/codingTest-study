
#왼쪽 방향부터 
n, m = map(int, input().split())
# 방문 표시용 map 
pin = [[0]*m for _ in range(n)]
x, y, direction  = map(int, input().split())  # (1,1) direction=1 => 1 1 1
pin[x][y] = 1 # 현재 위치 저장

maps=[]
for i in range(n):
    k = list(map(int, input().split()))
    maps.append(k)


# 북 동 남 서
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
    cx = x+ dx[direction]
    cy = y+ dy[direction]

    # 회전후 경우의 수
    # - 회전 후 칸이 비었고 육지면 한칸이동
    # - 회전 후 칸이 차있거나 바다인 경우 그냥 회전 한번 더하기
    # - 회전을 했는데 다 못가면 뒤로가기

    if pin[cx][cy] == 0 and maps[cx][cy]==0: 
        pin[cx][cy] = 1
        x ,y = cx, cy
        count += 1 
        turn_time +=1
        continue
    else:
        turn_time +=1

    if turn_time == 4:
        cx = x - dx[direction]
        cy = y - dy[direction]

        if maps[cx][cy] == 0:
            x, y = cx, cy
        
        else:
            break
        turn_time = 0

print(count)


    

    


    
    







