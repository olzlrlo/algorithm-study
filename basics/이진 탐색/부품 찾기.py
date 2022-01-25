n = int(input())
arr = list(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))


def binary_search(arr, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if arr[mid] == target:
        return mid + 1
    elif arr[mid] > target:
        return binary_search(arr, target, start, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, end)


arr.sort()
for target in targets:
    if binary_search(arr, target, 0, n - 1):
        print("yes", end=' ')
    else:
        print("no", end=' ')

