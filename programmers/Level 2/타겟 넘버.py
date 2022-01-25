answer = 0

def dfs(numbers, idx, result):
    if idx == len(numbers): # 탐색을 완료했다면,
        if result == key: # 타겟 넘버라면,
            global answer
            answer += 1
        return

    number = numbers[idx]
    dfs(numbers, idx + 1, result + number)
    dfs(numbers, idx + 1, result - number)

def solution(numbers, target):
    global key, answer
    key = target

    dfs(numbers, 0, 0)

    return answer
