# for x in list 구문에서 list.remove(x) 하면, 인덱스가 뒤엉켜 모든 요소를 탐색할 수 없다.

n, k = map(int, input().split())
a = list(map(int, input().split()))
idx, robots = [i + 1 for i in range(n * 2)], []  # 각 칸의 번호, 로봇 위치


def level1():  # 로봇과 함께 회전, deque 내 rotate 메서드 활용 가능
    last = idx[-1]
    for i in range(n * 2 - 1, 0, -1):
        idx[i] = idx[i - 1]  # 한 칸씩 회전
    idx[0] = last  # 2n번 -> 1번

    bye, new_robots = idx[n - 1], robots.copy()
    if bye in robots:  # 내리는 위치(n번)에 도착하면 내림
        new_robots.remove(bye)

    return new_robots


def level2():  # 가능한 로봇 이동
    bye, new_robots = idx[n - 1], robots.copy()
    i = 0
    for robot in robots:  # 가장 먼저 로봇에 올라간 로봇부터 이동
        if robot == n * 2:  # 2n번일 경우
            if 1 not in new_robots and a[0] > 0:  # 1번에 로봇이 없고, 내구도가 1 이상일 경우
                a[0] -= 1  # 1번의 내구도 1 감소
                if bye == 1:  # 1번이 내리는 위치일 경우
                    new_robots.remove(robot)  # 내림
                    i -= 1
                else:  # 내리는 위치가 아닐 경우
                    new_robots[i] = 1  # 1번으로 이동
        else:
            if robot + 1 not in new_robots and a[robot] > 0:  # 다음 칸에 로봇이 없고 내구도가 1 이상일 경우
                a[robot] -= 1  # 다음 칸의 내구도 1 감소
                if robot + 1 == bye:  # 다음 칸이 내리는 위치일 경우
                    new_robots.remove(robot)  # 내림
                    i -= 1
                else:  # 내리는 위치가 아닐 경우
                    new_robots[i] += 1  # 1번으로 이동
        i += 1

    return new_robots


def level3():  # 올리는 칸의 내구도 확인, 올리기
    if a[idx[0] - 1] > 0:  # 내구도가 0이 아니라면 올리기
        robots.append(idx[0])
        a[idx[0] - 1] -= 1


def level4():  # 종료 조건: True
    return True if a.count(0) >= k else False


answer = 0
while True:
    answer += 1
    robots = level1()
    robots = level2()
    level3()
    if level4():
        print(answer)
        break
