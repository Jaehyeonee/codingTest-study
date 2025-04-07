def solution(survey, choices):
    answer = ''
    assemble_dic = {}
    dic = {'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    
    i=0
    
    while i < len(choices):
        if 5 <= choices[i] <=7:    # 동의 경우 567
            # assemble_dic[survey[i][1]] = choices[i]
            if choices[i] == 7:     # 매우
                score = 3 
            elif choices[i] == 6:   # 보통
                score = 2
            
            else:                        # 약간
                score =1
            
            key = survey[i][1]
            if key in assemble_dic:
                assemble_dic[key] += score
            else:
                assemble_dic[key] = score
                
            
        elif choices[i] == 4 :  # 4: 모르겠음 선택 시
            pass
        
        else:                    # 비동의 경우 123
            
            if choices[i] == 1:     # 매우
                score = 3 
            elif choices[i] == 2:   # 보통
                score = 2
            else:       # 약간
                score = 1
            
                
            key = survey[i][0]
            if key in assemble_dic:
                assemble_dic[key] += score
            else:
                assemble_dic[key] = score
            
        i+=1
              
    print("지표:점수?? ", assemble_dic)
    
    dic.update(assemble_dic)
    print("final dic?? ", dic)
    
    
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
    
        
    
    
    
    
    
    
    
            

