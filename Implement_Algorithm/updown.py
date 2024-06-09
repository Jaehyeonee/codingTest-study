n = int(input())
plans = input().split()
x, y = 1, 1 # 시작좌표는 항상
# 위 아래 오 왼
dir_x = [-1, 1, 0, 0]   # x가 바뀐다 = 위 아래  (행)
dir_y = [0,0, 1, -1]    # y가 바뀐다 = 오 왼쪽  (열)

moves = ['U', 'D', 'R', 'L']

for plan in plans:
    for i in range(len(moves)):
        if plan == moves[i]:
            cx = x+dir_x[i]
            cy = y+dir_y[i]
    if cx < 1 or cy < 1 or cx > n or cy > n:
        # print("pass")
        continue

    x, y = cx, cy
    print(x,y)
print("final:" , (x, y))

