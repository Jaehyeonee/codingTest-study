from itertools import permutations
def solution(k, dungeons):
    answer = -1
    per = list(permutations(dungeons, len(dungeons)))
    for idx in per:
        count = 0
        save_k = k
        for need, use in idx:
            if save_k >= need:
                save_k -= use
                count += 1                
            answer = max(answer, count)
    return answer

print(solution(80,[[80,20],[50,40],[30,10]]))
