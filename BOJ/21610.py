n, m = map(int, input().split())
water, orders, clouds = [], [], [(n, 1), (n, 2), (n - 1, 1), (n - 1, 2)]
dx, dy = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]
for _ in range(n):
    water.append(list(map(int, input().split())))
for _ in range(m):
    orders.append(list(map(int, input().split())))


def move():  # 모든 구름이 d 방향으로 s 칸 이동
    for i, cloud in enumerate(clouds):
        x, y = cloud
        nx = x + dx[d - 1] * s
        ny = y + dy[d - 1] * s
        while nx > n:
            nx -= n
        while ny > n:
            ny -= n
        while nx <= 0:
            nx += n
        while ny <= 0:
            ny += n

        clouds[i] = (nx, ny)


def rain():
    for x, y in clouds:
        water[x - 1][y - 1] += 1


def water_copy():
    for x, y in clouds:
        cnt = 0
        for i in [1, 3, 5, 7]:
            nx, ny = x + dx[i], y + dy[i]
            if 0 < nx <= n and 0 < ny <= n and water[nx - 1][ny - 1]:
                cnt += 1
        water[x - 1][y - 1] += cnt


def new_cloud():
    new_list = []
    for x in range(n):
        for y in range(n):
            if water[x][y] > 1 and (x + 1, y + 1) not in clouds:
                new_list.append((x + 1, y + 1))
                water[x][y] -= 2

    return new_list


def get_total():
    total = 0
    for x in range(n):
        for y in range(n):
            total += water[x][y]

    print(total)
    return


for i in range(m):
    d, s = orders[i]
    move()
    rain()
    water_copy()
    clouds = new_cloud()

get_total()