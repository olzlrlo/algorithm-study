n = int(input())

i, start, end = 1, 0, 1
while True:
    if start <= n <= end:
        break
    else:
        start = end + 1
        end += (6 * i)
        i += 1

print(i)