#백준 정렬왕

while True:

    number=int(input())

    #0을 입력하면 프로그램 반복 종료
    if number == 0:
        break

    #0이 아니라면
    else:
        words=[]

        for i in range(number):
            word=input()

            #입력받은 단어를 words 리스트의 원소로 삽입
            words.append(word)

        #단어를 소문자로 바꾼뒤 -> 정렬 (sort는 대문자끼리/소문자끼리 정렬 먼저함. 대문자가 소문자보다 무조건 앞)
        words.sort(key=lambda word: word.lower())

        #words 리스트 변수의 맨 앞 단어를 출력
        print(words[0])
        
        
## -- Another Solution -- ##
        
num=int(input())   # 단어 개수 입력

while(num!=0):
    word_list=[]
    
    for i in range(0, num):
        word=input()
        word_list.append(word)
    
		# 모든 글자를 소문자로 바꾸었을 때 기준으로 sort하는 함수     
    word_list.sort(key=lambda word: word.lower())
    print(word_list[0])
    num=int(input())    # 단어 개수 입력
    
    
