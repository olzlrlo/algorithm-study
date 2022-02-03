from itertools import permutations
import sys

read = sys.stdin.readline
n, k, cards = int(read()), int(read()), []
for _ in range(n):
    cards.append(int(read()))

numbers = set()
for x in list(permutations(cards, k)):
    num = ''
    for s in x:
        num += str(s)
    numbers.add(num)

print(len(numbers))
