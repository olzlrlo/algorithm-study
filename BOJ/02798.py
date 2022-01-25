from itertools import combinations

n, m = map(int, input().split())
cards = list(map(int, input().split()))
card = list(combinations(cards, 3))

max = 0
for num in card:
    sum = 0
    for n in num:
        sum += n
    if sum > m:
        continue
    if sum > max:
        max = sum

print(max)
