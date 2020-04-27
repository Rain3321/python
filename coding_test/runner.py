#https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    answer = ''
    name_dict = {}  # 이름이 등장한 횟수를 딕셔너리로 만듬
    for name in participant:
        if name in name_dict:
            name_dict[name] += 1
        else:
            name_dict[name] = 1

    #result = set()  # 결과값 저장할 빈 집합
    for name in completion:
        if name in name_dict:
            name_dict[name] -= 1

    for name in name_dict:
        if name_dict[name] == 1:
            #result.add(name)
            answer = name

    return answer


