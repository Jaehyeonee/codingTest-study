def solution(n, lost, reserve):
		#중복되지 않는다 했으니까 set함수로
		#set: 두 리스트에서 중복되는 원소 없애줌
		#체육복을 도난당한 사람중에 여벌이 있던 사람을 제외한 lost, reserve 배열 만들기
    #학생번호는 고유하니까 lost배열에 있는 학생 넘버와 reserve배열에 있는 학생넘버를 빼면 서로 빌려주고 빌려받을 사람들만 남게됨.
		r_lost =set(lost)-set(reserve)   
    r_reserve = set(reserve)-set(lost)
    
    for i in r_reserve:
        if i-1 in r_lost:
            r_lost.remove(i-1)
            
        elif i+1 in r_lost:
            r_lost.remove(i+1)
            
    return n-len(r_lost)
