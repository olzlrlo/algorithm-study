import operator

def solution(genres, plays):
    answer = []
    index = range(len(genres)) # 노래 수
    dict_plays = dict() # 장르 별 총 재생 수
    dict_index = dict() # 장르 별 {고유 번호: 재생 수}

    for i, genre, play in zip(index, genres, plays):
        if genre not in dict_plays: # 초기화
            dict_plays[genre] = 0 # {장르: 0}
            dict_index[genre] = dict() # {장르: {}}
        dict_plays[genre] += play
        dict_index[genre][i] = play

    # 장르를 재생 수 기준으로 정렬
    # key = operator.itemgetter(1): value 기준 정렬
    dict_plays = sorted(dict_plays.items(), key = operator.itemgetter(1), reverse = True)

    for genre, _ in dict_plays:
        plays = dict_index[genre] # 장르 별 {고유 번호: 재생 수} 정보
        plays = sorted(plays.items(), key=operator.itemgetter(1), reverse = True) # 재생 수 기준 정렬
        answer.append(plays[0][0]) # 첫 번째 곡 추가
        if len(plays) > 1: # 두 곡 이상 존재할 경우
            answer.append(plays[1][0]) # 두 번째 곡도 추가

    return answer
