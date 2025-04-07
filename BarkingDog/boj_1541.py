# 그리디 : 잃어버린 괄호

'''
예시 ) 10+20-30+10+20-30+10+20
1. - 를 기준으로 나눔
2. ['10+20', '30+10+20', '3+10+20']
3. for문으로 돌면서 +를 기준으로 나누고 int로 형 변환해서 더 해줌
4. [10,20] = 30, [30,10,20]=60, [3,10,20]=60
5. tmp = 30으로 첫 수로 두고 나머지를 전부 빼줌
6. 따라서 30(=tmp) - 60 - 60 = -90

'''
import sys
input = sys.stdin.readline
 
exp = input().strip().split('-')
# print(exp)
tmp = []

for i in exp:
    cnt = 0
    for j in i.split('+'):
        cnt += int(j)
    tmp.append(cnt)

result = tmp[0]
for i in tmp[1:]:
    result -= i
print(result)
    
    
