import sys
input = sys.stdin.readlines
numbers=[]
f = open('/Users/jenzennii/Development/codingTest-study/BarkingDog/text.txt', 'r')
for i in f.readlines():
    for j in i.split():
        numbers.append(int(j[::-1]))
numbers = numbers[1:]
numbers.sort()
print('\n'.join(map(str,numbers)))
