n = int(input())
places = list(map(int, input().split()))
b, c = map(int, input().split())
total = 0

for place in places:
    total += 1
    if place <= b:
        continue
    total += (place - b) // c
    if (place - b) % c:
        total += 1

print(total)