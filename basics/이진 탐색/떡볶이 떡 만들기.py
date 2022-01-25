# Parametric Search: 원하는 조건을 만족하는 가장 알맞은 값 찾는 문제
# 탐색 범위 1 ~ 10억: "이진 탐색!"

n, m = map(int, input().split())
lengths = list(map(int, input().split()))


def cut(arr, height):
    total = 0
    for x in arr:
        if x > height:
            total += (x - height)
    return total


start, end, result = 0, max(lengths), 0
while start <= end:
    mid = (start + end) // 2
    total = cut(lengths, mid)
    if total >= m:  # 많이 잘랐을 경우 - mid(절단기 높이) 높여야 함
        start = mid + 1
        result = mid
        print(result)
    else:  # 적게 잘랐을 경우 - mid(절단기 높이) 줄여야 함
        end = mid - 1

print(result)