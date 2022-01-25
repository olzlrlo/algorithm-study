import sys
input = sys.stdin.readline

n = int(input())
meetings = []
answer = 0

for _ in range(n):
    t1, t2 = map(int, input().split())
    meetings.append((t2, t1))
meetings.sort()

now = 0
for meeting in meetings:
    fin, start = meeting
    if start >= now:
        now = fin
        answer += 1

print(answer)
