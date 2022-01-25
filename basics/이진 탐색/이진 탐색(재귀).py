# 배열 내부의 데이터가 정렬되어 있어야 함
# 데이터 개수나 값이 1000만 단위 이상일 경우 이진탐색과 같은 O(logN)의 알고리즘으로 접근

def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


n, target = map(int, input().split())
arr = list(map(int, input().split()))

result = binary_search(arr, target, 0, n - 1)

if not result:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)