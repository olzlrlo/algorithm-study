from collections import defaultdict
import operator

def solution(genres, plays):
    
    getGenres, getPlays = defaultdict(int), defaultdict(list)  # 장르 별 총 재생 수, 장르 내 노래 재생 수
    for i, (genre, play) in enumerate(zip(genres, plays)):  # 정렬을 위해서 음수로 저장
        getGenres[genre] -= play
        getPlays[genre].append((-1 * play, i))
    
    answer = []
    getGenres =  sorted(getGenres.items(), key = operator.itemgetter(1))  # dictionary의 item 기준 정렬
    
    for genre, _ in getGenres:
        plays = sorted(getPlays[genre])
        answer.append(plays[0][1])
        if len(plays) > 1:
            answer.append(plays[1][1])

    return answer
