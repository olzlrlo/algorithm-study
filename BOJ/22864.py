a, b, c, m = map(int, input().split())
max = 0

def working(tired, work, depth):
    if tired < 0 or tired > m:
        return

    if depth == 24:
        global max
        if work > max:
            max = work
        return

    working(tired + a, work + b, depth + 1)
    working(tired - c, work, depth + 1)

working(0, 0, 0)
print(max)
