#https://programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    div = n // 3
    reminder = n %3
    while True:
        print(div, reminder)
        if not reminder:
            reminder = 4
            div = div -1
        answer = str(reminder) + answer
        reminder = div %3
        div = div //3
        print(div, reminder)
        if not div:
            if not reminder:
                break
            else:
                continue
        
    return answer
