n = int(input())
numbers = list(map(int, input().split()))
op = list(map(int, input().split()))
operators = ['+'] * op[0] + ['-'] * op[1] + ['*'] * op[2] + ['/'] * op[3]
min_val, max_val = 10**9, -10**9

def permutations(arr):
    visited = [False] * len(arr)
    def generator(choices, visited):
        if len(choices) == len(arr):
            total = numbers[0]
            for i in range(len(choices)):
                if choices[i] == '+':
                    total += numbers[i + 1]
                elif choices[i] == '-':
                    total -= numbers[i + 1]
                elif choices[i] == '*':
                    total *= numbers[i + 1]
                elif total < 0:
                    total = - ((-total) // numbers[i + 1])
                else:
                    total //= numbers[i + 1]
            global min_val, max_val
            min_val = min(min_val, total)
            max_val = max(max_val, total)

        for i in range(len(arr)):
            if not visited[i]:
                visited[i] = True
                choices.append(arr[i])
                generator(choices, visited)
                visited[i] = False
                choices.pop()

    generator([], visited)

permutations(operators)
print(max_val)
print(min_val)