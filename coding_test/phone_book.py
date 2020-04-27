#https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    
    for i in phone_book:
        for j in phone_book:
            if i != j:
                if len(i) > len(j):
                    if j== i[:len(j)]:
                        return False
    return True
