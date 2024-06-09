import sys
n = int(sys.stdin.readline().strip())

count = 0

for h in range(n+1):
    for m in range(60):
        for s in range(60):
            if '3' in str(h)+str(m)+str(s):
                count+=1
print(count)

def threeCount(h):
    num=0
    for h in range(h+1):
        for m2 in range(60):
            for s2 in range(60):
                if '3' in str(h)+str(m2)+str(s2):
                    num+=1
    return num


def main():
    h = int(input())
    r = threeCount(h)
    print(r)

main()
