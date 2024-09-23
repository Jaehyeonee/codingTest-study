import sys
input = sys.stdin.readline

n = int(input())
meeting = []

for i in range(n):
    s, e = map(int,input().split())
    meeting.append((s, e))


meeting.sort(key = lambda x:(x[1], x[0]) )
last_time = meeting[len(meeting)-1][1]

def solve(result):

    for i in range(len(result)):
        for _ in range(len(result)):
            end = result[i][1]
            if end == last_time:
                return len(result)
            else:
                if result[i+1][0] < end:
                    result.pop(i+1)
                else: 
                    break
    

print(solve(meeting))