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

array = [[2], [3,  4, 7], [1]]
answer = []




for x in array:
        if len(x) == 1:
            result = 1
            answer.append(result)

        
        