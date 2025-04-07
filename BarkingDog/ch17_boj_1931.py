# import sys
# input = sys.stdin.readline

# n = int(input())
# meeting = []

# for i in range(n):
#     s, e = map(int,input().split())
#     meeting.append((s, e))


# meeting.sort(key = lambda x:(x[1], x[0]) )
# last_time = meeting[len(meeting)-1][1]

# def solve(result):

#     for i in range(len(result)):
#         for _ in range(len(result)):
#             end = result[i][1]
#             if end == last_time:
#                 return len(result)
#             else:
#                 if result[i+1][0] < end:
#                     result.pop(i+1)
#                 else: 
#                     break
    

# print(solve(meeting))



import sys
input = sys.stdin.readline

'''
n개의 회의실 사용표
시작 끝 시간
회실 사용 최대 개수 겹치면 x

회의 시작 시간 = 끝나는 시간

'''

n = int(input())
meetings = []

for i in range(n):
    start, end = map(int, input().split( ))
    meetings.append((start, end))

meetings.sort(key = lambda x : (x[1], x[0]))
lst = meetings[-1][1]

def solve(meetings):
    for i in range(len(meetings)):
        for _ in range(len(meetings)):
            ends = meetings[i][1]
            if ends == lst:
                answer = len(meetings)
                return answer
            else:
                if ends > meetings[i+1][0]:
                    meetings.pop(i+1)
                else:
                    break 
        
print(solve(meetings))
