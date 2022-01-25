import sys
input = sys.stdin.readline

n = int(input())
eggs, broken = [], [False] * n
for _ in range(n):
    eggs.append(list(map(int, input().split())))


def hit(egg, eggs_list, broken_list):
    if egg == n:  # 가장 오른쪽 계란일 경우 종료
        global max_val
        max_val = max(max_val, broken_list.count(True))
        return

    if broken_list[egg] or broken_list.count(False) == 1:  # 현재 계란이 깨졌거나, 칠 계란이 없을 경우
        hit(egg + 1, eggs_list, broken_list)  # 안 깨고 넘어감
    else:
        for i in range(n):  # 계란 중 하나 선택
            if i == egg or broken_list[i]:
                continue
            # 깰 수 있는 경우 내구도 갱신
            eggs_list[egg][0] -= eggs_list[i][1]
            eggs_list[i][0] -= eggs_list[egg][1]
            if eggs_list[egg][0] <= 0:
                broken_list[egg] = True
            if eggs_list[i][0] <= 0:
                broken_list[i] = True
            hit(egg + 1, eggs_list, broken_list)  # 깨고 다음 계란 집기

            # 깨지 않은 경우를 고려하기 위해 정보 초기화
            eggs_list[egg][0] += eggs_list[i][1]
            eggs_list[i][0] += eggs_list[egg][1]
            broken_list[egg], broken_list[i] = False, False


max_val = 0
hit(0, eggs, broken)
print(max_val)