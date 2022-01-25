import sys
input = sys.stdin.readline
n = int(input())
students, likes = [], dict()  # 학생 순서, 각 학생이 좋아하는 학생들
classroom = [[0] * n for _ in range(n)]  # 학생들 자리
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for _ in range(n * n):
    read = list(map(int, input().split()))
    students.append(read[0])
    likes[read[0]] = read[1:]


def cond1(arr):  # 첫 번째 조건: 좋아하는 학생이 가장 많이 인접한 칸
    max_val, max_list = -1, []
    for x in range(n):  # 모든 행에 대해
        for y in range(n):  # 모든 열에 대해
            if not classroom[x][y]:  # 빈 자리일 경우
                cnt = 0
                for i in range(4):  # 상하좌우 탐색
                    nx, ny = x + dx[i], y + dy[i]
                    # 범위를 벗어나지 않고, 좋아하는 학생이 인접한 칸에 있을 경우
                    if 0 <= nx < n and 0 <= ny < n and classroom[nx][ny] in arr:
                        cnt += 1
                if cnt > max_val:
                    max_val = cnt
                    max_list = [[x, y]]
                elif cnt == max_val:
                    max_list.append([x, y])

    return max_list


def cond2(arr):  # 두 번째 조건: 비어있는 칸이 가장 많이 인접한 칸
    max_val, max_list = -1, []
    for x, y in arr:  # 첫 번째 조건을 만족하는 모든 칸의 행과 열에 대해
        cnt = 0
        for i in range(4):  # 상하좌우 탐색
            nx, ny = x + dx[i], y + dy[i]
            # 범위를 벗어나지 않고, 비어있는 칸일 경우
            if 0 <= nx < n and 0 <= ny < n and not classroom[nx][ny]:
                cnt += 1
        if cnt > max_val:
            max_val = cnt
            max_list = [[x, y]]
        elif cnt == max_val:
            max_list.append([x, y])

    return max_list


for student in students:  # 모든 학생들에 대해
    first = cond1(likes[student])  # 첫 번째 조건 확인
    if len(first) == 1:
        classroom[first[0][0]][first[0][1]] = student
    else:
        second = cond2(first)  # 두 번째 조건 확인
        if len(second) == 1:
            classroom[second[0][0]][second[0][1]] = student
        else:
            third = sorted(second)  # 정렬으로 세 번째 조건 확인
            classroom[third[0][0]][third[0][1]] = student

score = 0
for x in range(n):
    for y in range(n):
        cnt = 0
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if classroom[nx][ny] in likes[classroom[x][y]]:  # 좋아하는 학생이 인접한지 확인
                    cnt += 1
        if cnt:
            score += 10**(cnt - 1)

print(score)
