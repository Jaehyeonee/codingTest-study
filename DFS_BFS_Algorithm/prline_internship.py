# # digital number setting switch

# def solve(array):
#     digital = [['a','b','c','e','f','g'], ['c','f'], ['a','c','d','e','g'], # 0, 1, 2
#            ['a','c','d','f','g'], ['b','c','d','f'],['a','b','d','f','g'], # 3, 4, 5
#            ['a','b','d','e','f','g'],['a','b','c','f'],['a','b','c','d','e','f','g'], # 6,7, 8
#            ['a','b','c','d','f','g'] # 9
#            ]
    
#     s = len(array)
#     pair = []

#     for i in range(s):
#         for x in array[i]:
#             if len(array[i]) == 1:
#                 answer = 1
#             else:
#                 pair.append(digital[x])

#     print(pair)

#     return answer



# solve([[3, 7, 9], [1]])



    
# def calculate_min_switches(switch_mapping, numbers):
#     answer = []

#     for num_list in numbers:
#         print(num_list)
#         common_segments = set(switch_mapping[num_list[0]])
#         print("1-1. common_segments: ", common_segments)
#         for num in num_list[0:]:
#             common_segments.intersection_update(switch_mapping[num])
#             print("${num}. common_segments: ", common_segments)

#         min_switches = len(common_segments)
#         print("minswitch: ",min_switches)
#         answer.append(min_switches)

#     return answer

# 입력값 정의
# switch_mapping = {
#     0: {'a', 'b', 'c', 'e', 'f', 'g'},
#     1: {'c', 'f'},
#     2: {'a', 'c', 'd', 'e', 'g'},
#     3: {'a', 'c', 'd', 'f', 'g'},
#     4: {'b', 'c', 'd', 'f'},
#     5: {'a', 'b', 'd', 'f', 'g'},
#     6: {'a', 'b', 'd', 'e', 'f', 'g'},
#     7: {'a', 'b', 'c', 'f'},
#     8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
#     9: {'a', 'b', 'c', 'd', 'f', 'g'}
# }

array = [[2], [3,  4, 7], [1]]


answer= []
switch = []


def solve(array):
    # 입력값 정의
    switch_mapping = {
        0: {'a', 'b', 'c', 'e', 'f', 'g'},
        1: {'c', 'f'},
        2: {'a', 'c', 'd', 'e', 'g'},
        3: {'a', 'c', 'd', 'f', 'g'},
        4: {'b', 'c', 'd', 'f'},
        5: {'a', 'b', 'd', 'f', 'g'},
        6: {'a', 'b', 'd', 'e', 'f', 'g'},
        7: {'a', 'b', 'c', 'f'},
        8: {'a', 'b', 'c', 'd', 'e', 'f', 'g'},
        9: {'a', 'b', 'c', 'd', 'f', 'g'}
}

    for x in array:
        if len(x) == 1:
            result = 1
            answer.append(result)
        else:
            result = 0
            common = switch_mapping[x[0]]
            for i in x:  # 3 7 9 
                for j in x[1:]: # 7 9 
                    if i!=j and i<j:
                        print("befor:", common)
                        common = common.intersection(switch_mapping[j])       
            switch.append(common)  
            print(switch)    
            for i in x:
                switch_mapping[i] = switch_mapping[i].difference(common)

      
    print(answer)
          
    return answer


solve(array)