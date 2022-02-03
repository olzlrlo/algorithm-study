def zero(x):
    if 0 <= x <= 9:
        return '0' + str(x)
    else:
        return str(x)


n, k = map(int, input().split())
hour, minute, second, total = n, 60, 60, 0
for h in range(hour + 1):
    for m in range(minute):
        for s in range(second):
            if str(k) in zero(h) + zero(m) + zero(s):
                total += 1

print(total)

