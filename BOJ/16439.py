from itertools import combinations

n, m = map(int, input().split())
preference = []
for _ in range(n):
    preference.append(list(map(int, input().split())))

result = set()
for i in range(1, 4):
    for chicken_list in list(combinations([x for x in range(m)], i)):
        total = 0
        for p in preference:
            max_val = -1
            for chicken in chicken_list:
                if max_val < p[chicken]:
                    max_val = p[chicken]
            total += max_val
        result.add(total)

print(max(result))