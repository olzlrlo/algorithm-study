n = int(input())
min = n

for i in range(n):
    sum = i
    for s in str(i):
        sum += int(s)
    if sum == n and i < min:
        min = i
if min == n:
    print(0)
else:
    print(min)
