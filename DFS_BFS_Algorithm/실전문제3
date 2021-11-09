n, m = map(int,input().split())

#LEFT RIGHT UP DOWN
d =[-1, 1, -1, 1] 

ice = []

for _ in range(n):
    ice.append(list(map(int,input())))


def side(x, y):

    if x<=-1 or x >=n or y<=-1 or y>=m:
        return False
    
    if ice[x][y]==0:
        ice[x][y]=1

        side(x-1, y)
        side(x+1 ,y)
        side(x, y-1)
        side(x, y+1)
        return 'icing'

    
    return False

            

ice_cnt = 0

for i in range(n):
    for j in range(m):
        if side(i, j) =='icing':
            ice_cnt +=1

print(ice_cnt)
