#https://programmers.co.kr/learn/courses/30/lessons/42578
def solution(clothes):
    answer = 1
    count_item = {}
    for item, sort in clothes:
        #print(item, sort)
        if sort in count_item:
            count_item[sort] += 1
        else:
            count_item[sort] = 1
#    print(count_item)
    for item in count_item:
        answer = answer * (count_item[item]+1)
    
    return answer-1
