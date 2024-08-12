import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
notebook = [[0]*m for _ in range(n)]
stickers = []


def rotate(s):
    s = zip(*s[::-1])
    return [list(i) for i in s]

def put(sticker):
    sr, sc =  len(sticker), len(sticker[0])
    for x in range(n-sr+ 1):
        for y in range(m-sc+1):
            if compare(x, y, sr, sc, sticker):
                for sx in range(sr):
                    for sy in range(sc):
                        notebook[x+sx][y+sy] += sticker[sx][sy]
                return True
    return False


def compare(x, y, sr, sc, sticker):
    for sx in range(sr):
        for sy in range(sc):
            if notebook[x+sx][y+sy]== sticker[sx][sy] == 1:
                return False
    return True




for i in range(k):
    R, C = map(int, input().split())
    sticker = [list(map(int, input().split())) for _ in range(R)]
    stickers.append(sticker)


for s in stickers:
    for i in range(4):
        if put(s):
            break
        s = rotate(s)

count = sum(map(sum, notebook))

print(count)

    
