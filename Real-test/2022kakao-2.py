# /*
# deque로 효율성 높이기,
# while문에 반복되는 함수 연산자 sum() 를 넣지 않고 빼는게 더 효율적임
# 지역변수를 사용하는 것이 조금 더 효율적임 len(q1)을 L1이라는 전역변수로 빼는 것을 추천
# while True 보다는 while 1이 조금 더 빠르다고 함.
# */


from collections import deque
def solution(queue1, queue2):
    answer = 0
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    l = len(queue1) 
    q1 = deque(queue1)
    q2 = deque(queue2)

        

    while 1:
        # if not queue1 or not queue2:     초기 구현 코드  >>  이렇게 하면 예외의 경우를 전부 처리하지 못하고, 무한루프에 빠짐
        #     return -1
        if answer > (len(q1)+len(q2))*2:
            return -1
       
        elif q1_sum < q2_sum  :
            
            el = q2.popleft()
            q1.append(el)
            q1_sum += el
            q2_sum -= el
            answer +=1
            
        
            
        elif q1_sum > q2_sum:
            el = q1.popleft()
            q2.append(el)
            q1_sum -= el
            q2_sum += el
            
            answer +=1
            

        elif q1_sum == q2_sum:
            answer = answer
            break
    
        
    
    return answer