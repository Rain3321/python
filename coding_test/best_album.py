#https://programmers.co.kr/learn/courses/30/lessons/42579
def solution(genres, plays):
    answer = []
    count_total_play = {}
    time = 0
    #print(sorted(zip(genres, plays, range(len(genres))), reverse=True))
    check = (sorted(zip(genres, plays, range(len(genres))), reverse=True))
    for genre, play in zip(genres, plays):
        if genre in count_total_play:
            count_total_play[genre] += play
        else:
            count_total_play[genre] = play
    count_sorted = sorted(count_total_play.items(), reverse=True, key=(lambda item:item[1]))
    for genre, play in count_sorted:
        i = 0
        for a, b, c in check:
            if i > 1:
                break
            if a == genre:
                if time == b:
                    if answer[-1] > c:
                        answer.insert(-1, c)
                else:
                    answer.append(c)
                    
                i = i + 1
                time = b
                
    return answer
