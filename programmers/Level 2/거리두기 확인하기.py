from collections import deque


def bfs(i, j, place):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    queue = deque([(i, j, 0)])

    while queue:
        x, y, depth = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < 5 and 0 <= ny < 5 and depth < 2:
                if nx == i and ny == j:
                    continue
                if place[nx][ny] == 'P':
                    return False  # 거리준수X
                elif place[nx][ny] == 'O':
                    queue.append((nx, ny, depth + 1))

    return True


def solution(places):
    answer = []

    for place in places:
        p_list = []
        for x, line in enumerate(place):
            for y, p in enumerate(line):
                if p == 'P':
                    p_list.append((x, y))

        for i, j in p_list:
            if not bfs(i, j, place):
                answer.append(0)
                break
        else:
            answer.append(1)

    return answer