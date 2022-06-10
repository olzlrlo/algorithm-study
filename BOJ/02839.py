n = int(input())
total = 0

while n > 0:
    if not n % 5:
        total += (n // 5)
        n = 0
        break
    else:
        n -= 3
        total += 1

if not n:
    print(total)
else:
    print(-1)