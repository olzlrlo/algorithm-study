from collections import defaultdict


def solution(clothes):
    answer = 1
    fashion_dict = defaultdict(int)
    for name, kind in clothes:
        fashion_dict[kind] += 1

    for key in fashion_dict.keys():  # 경우의 수
        answer *= (fashion_dict[key] + 1)

    return answer - 1
