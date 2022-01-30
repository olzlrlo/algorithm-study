a, b, c, m = map(int, input().split())
total = 0


def working(tired, work, depth):
    if tired < 0:
        tired = 0
    elif tired > m:
        return

    if depth == 24:
        global total
        if work > total:
            total = work
        return

    working(tired + a, work + b, depth + 1)
    working(tired - c, work, depth + 1)


working(0, 0, 0)
print(total)
