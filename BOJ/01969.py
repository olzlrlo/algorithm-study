n, m = map(int, input().split())
DNA_list = []
for _ in range(n):
    DNA_list.append(input())

result, distance = '', 0
for i in range(m):
    cnt = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j, DNA in enumerate(DNA_list):
        cnt[DNA[i]] += 1
    max_val = max(cnt.values())
    for key in cnt.keys():
        if cnt[key] == max_val:
            result += key
            distance += (n - max_val)
            break

print(result)
print(distance)

