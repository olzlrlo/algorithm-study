# min/max : O(n)
# sort: O(nlogn)

n, m = map(int, input().split()) # 행의 개수, 열의 개수
result = 0

for i in range(n): # 각 행의 숫자 카드
    nums = list(map(int, input().split())
    min_val = min(nums) # 행에서 가장 작은 숫자 카드
    # if min > result:
    #     result = min
    result = max(result, min_val) # 가장 큰 값을 저장

print(result)
