import sys

input = sys.stdin.readline

a, b = map(int, input().split())
count=1
double = []
for i in range(3, b+1): 
    if (i%2!=0) and (i%3!=0) and (i%5!=0) and (i%7!=0):
        dd = i*i
        if a<=dd<=b:
            count+=1
print(count)
