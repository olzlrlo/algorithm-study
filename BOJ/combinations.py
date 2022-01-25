def my_combinations(arr, r):
    def generate(choices):
        if len(choices) == r:  # r개 다 골랐으면 출력 + return
            print(choices)
            return

        # 이전에 선택한 것의 다음 인덱스부터 탐색 (혹은 0)
        start = arr.index(choices[-1]) + 1 if choices else 0
        for nxt in range(start, len(arr)):
            choices.append(arr[nxt])
            generate(choices)
            choices.pop()

    generate([])


my_combinations("ABCDE", 2)