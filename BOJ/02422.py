from collections import defaultdict
import sys


def sol(num, num_list):
    if len(num_list) == 3:
        global total
        total += 1
        return

    for i in range(num + 1, n + 1):
        if i not in bad_dict[num] and i not in bad_dict[num_list[0]]:
            sol(i, num_list + [i])


read = sys.stdin.readline
n, m = map(int, read().split())
bad_dict = defaultdict(list)
for _ in range(m):
    b1, b2 = map(int, read().split())
    bad_dict[min(b1, b2)].append(max(b1, b2))

total = 0
for x in range(1, n - 1):
    sol(x, [x])

print(total)





