import sys
input = sys.stdin.readline

n, m = map(int, input().split())

list_a = list(map(int, input().split()))
list_b = list(map(int, input().split()))

c = list_a + list_b
c.sort()

print(' '.join(map(str, c)))