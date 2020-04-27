#https://programmers.co.kr/learn/courses/30/lessons/64065
def solution(s):
    answer = []

    temp = []
    split_s = s.replace('}', '{').split('{')
    split_s.sort(key=len)
    for x in split_s:
        if x == '' or x ==',':
            continue
        else:
            #print(x)
            item = x.split(',')
            #print(c)
            for number in item:
                if number == ',':
                    continue
                flag = True
                if not temp:
                    temp.append(int(number))
                else:
                    for same in temp:
                        if int(number) == same:
                            flag = False
                            break
                    if flag:
                        temp.append(int(number))
                #print(temp)

    #print(b)
    answer = temp
    return answer
