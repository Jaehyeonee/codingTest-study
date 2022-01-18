# m번 더하기, n은 수 배열, k는 연속가능 횟수


n, m, k = map(int, input().split())

data = list(map(int,input().split()))

data.sort(reverse= True) #내림차순으로정렬
high_num = data[0]   #가장 큰수
next_num = data[1]   #두번째로 큰수

result =0


while True:
    for i in range(k):#가장 큰 수 k번 더하기
        if m==0:
            break
        result += high_num
        m-=1
    if m == 0:
        break
    

    result += next_num
    m-=1

print(result)
