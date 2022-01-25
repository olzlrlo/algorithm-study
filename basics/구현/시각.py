# 하루는 86400초이므로, 완전탐색 가능
# 00:00:00 - n:59:59

n = int(input())
result = 0

for h in range(n + 1):
    for m in range(60):
        for s in range(60):
            # 문자열로 변환, '3'이 포함되어 있으면 count
            if '3' in str(h) + str(m) + str(s):
                result += 1

print(result)
