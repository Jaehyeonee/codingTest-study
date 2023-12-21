from collections import Counter
def solution(friends, gifts):
    answer = 0
    

    From_to=[]
    dic = {}

    # 프렌즈 딕셔너리 초기화 value = 준선물, 받은 선물 , 선물 지수 임.
    friends_dict = {friend_key: [0]*len(friends) for friend_key in friends}
    counter_dict = {friend_key: [0]*len(friends) for friend_key in friends}

    give_dict = {friend_key: 0 for friend_key in friends}
    get_dict = {friend_key: 0 for friend_key in friends}
    jisu_dict = {friend_key: 0 for friend_key in friends}
    # print("프렌즈 딕셔너리 초기화 = ", friends_dict)

   

    for i in range(len(gifts)):
        From_to.append(gifts[i].split(" "))

    # for i in From_to:
    #     From.append(i[0])
    #     to.append(i[1])
 
    # print("선물을 준 사람: ", From)
    # print("선물을 받은 사람: ", to)

    for j in range(len(From_to)):
        key = From_to[j][0]
        value = From_to[j][1]

        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]

    friends_dict.update(dic)    
    print(friends_dict)
    

    give_counts = {key: len(values) for key, values in dic.items()}
    give_dict.update(give_counts)
    

    # 키에 해당하는 값이 다른 키의 요소에 몇 번 있는지 계산
    get_counts = {}
    for key, values in friends_dict.items():
        for value in values:
            if value in get_counts:
                get_counts[value] += 1
            else:
                get_counts[value] = 1

    get_dict.update(get_counts)


    jisu_counts = {}

    for key in friends:
        jisu_counts[key] = give_dict[key] - get_dict[key]

    jisu_dict.update(jisu_counts)

    print("준 선물 개수: ", give_dict)
    print("받은 선물 개수: ", get_dict)
    print("선물 지수: ", jisu_dict)



    counting = {}
    for key in friends_dict:
        if isinstance(friends_dict[key], list):  # 리스트인 경우에만 처리
            
            counts = Counter(friends_dict[key])
            print(counts)
            counting[key] = counts

    
    counter_dict.update(counting)

    for k in friends:
        for i in range(len(counter_dict[k])):
            
            print(counter_dict[k])


    



    return answer


solution(["muzi", "ryan", "frodo", "neo"], ["muzi frodo", "muzi frodo", "ryan muzi", "ryan muzi", "ryan muzi", "frodo muzi", "frodo ryan", "neo muzi"])


# def solution(friends, gifts):
#     answer = 0
    

#     From_to=[]
#     From =[]
#     to = []
#     dic = {}
   

#     for i in range(len(gifts)):
#         From_to.append(gifts[i].split(" "))



#     for i in From_to:
#         From.append(i[0])
#         to.append(i[1])
 
#     print("선물을 준 사람: ", From)
#     print("선물을 받은 사람: ", to)

#     for j in range(len(From_to)):
#         key = From_to[j][0]
#         value = From_to[j][1]

#         if key in dic:
#             dic[key].append(value)
#         else:
#             dic[key] = [value]

        
#     print(dic)
    

#     element_counts = {key: len(values) for key, values in dic.items()}

#     # 키에 해당하는 값이 다른 키의 요소에 몇 번 있는지 계산
#     value_counts = {}
#     for key, values in dic.items():
#         for value in values:
#             if value in value_counts:
#                 value_counts[value] += 1
#             else:
#                 value_counts[value] = 1

#     print("준 선물 개수: ", element_counts)
#     print("받은 선물 개수: ", value_counts)


    

    

    
        
    




#     return answer