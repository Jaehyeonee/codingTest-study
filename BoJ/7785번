import sys

pe = {}

for _ in range(int(sys.stdin.readline())):
  p, c = sys.stdin.readline().rstrip().split()

  if c == 'enter':
    pe[p] = 'enter'
  else:
    if pe[p]:
      del pe[p]

for people in sorted(pe, reverse=True):    #sorted는 얕은 복사(people 변수 자체를 바꿔주진 않음). sort는 원본 자체를 바꿔줌
  print(people)
  

  
