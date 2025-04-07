def solution(survey, choices):
    answer = ''

    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    score_dic= {1:3, 2:2, 3:1, 4:0, 5:1, 6:2, 7:3}
    
    for i in range(0, len(choices)):
        # choice = choices[i]
        if choices[i] < 4:
            key = survey[i][0]
            dic[key] += score_dic[choices[i]]
        elif choices[i]>4:
            key = survey[i][1]
            dic[key] += score_dic[choices[i]]  
        
   

    jipyo = [['R', 'T'], ['C', 'F'], ['J', 'M'], ['A', 'N']]
    
    for j in jipyo:
        c1 = j[0]
        c2 = j[1]
        

        if dic[c1] == dic[c2]:
            if c1 < c2:
                answer += c1
            else:
                answer += c2
        elif dic[c1] > dic[c2]:
            answer += c1
        else:
            answer += c2

    return answer

  
