def my_permutations(arr, r):
    def generate(choices):
        if len(choices) == r:
            print(choices)
            return

        for nxt in range(len(arr)):
            if arr[nxt] not in choices:
                choices.append(arr[nxt])
                generate(choices)
                choices.pop()

    generate([])

my_permutations("ABC", 2)