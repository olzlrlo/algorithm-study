# Dynamic Programming

# DP 조건 (1) 큰 문제를 작은 문제로 나눌 수 있다.
# DP 조건 (2) 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.

# DP 구현 방법 (1) 재귀(Top-Down): 큰 문제를 해결하기 위해 작은 문제를 호출
# DP 구현 방법 (2) 반복(Bottom-Up): 작은 문제부터 답을 도출
# 일반적으로 반복문을 활용하는 것이 낫다. (오버헤드를 줄일 수 있음)

# 재귀(Top-Down)
memo = [0] * 100  # 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화

def fibo_r(x):  # 피보나치 함수를 재귀함수로 구현(Top-Down)
    if x == 1 or x == 2:
        return 1
    if memo[x]:  # 이미 계산한 적 있는 문제라면 그대로 반환
        return memo[x]
    else:
        memo[x] = fibo_r(x - 1) + fibo_r(x - 2)
        return memo[x]

print(fibo_r(99))

# 반복(Bottom-Up)
fibo_i = [0] * 100  # 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
fibo_i[1], fibo_i[2] = 1, 1
n = 99

for i in range(3, n + 1):
    fibo_i[i] = fibo_i[i - 1] + fibo_i[i - 2]

print(fibo_i[n])
