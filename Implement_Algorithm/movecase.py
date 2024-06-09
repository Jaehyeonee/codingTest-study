import sys
def moveing(row, column):
    count=0
    dir = [(-2, 1),(-2, -1), (2,1),(2,-1),(1,2),(1,-2,),(-1,2),(-1, -2)]
    
    for i in range(len(dir)):
        cx = row+dir[i][0]
        cy = column+dir[i][1]
        if cx >=1 and cx<=8 and cy>=1 and cy<=8:
            count+=1
            print(chr(cy-1+int(ord('a'))),cx)

        
    
    return count


def main():
    current = sys.stdin.readline().strip()
    column = int(ord(current[0])) - int(ord('a')) + 1
    row = int(current[1])

    print(current)
    print("열: ",column)
    print("행: ",row)


    res = moveing(row, column)
    print(res)

main()
