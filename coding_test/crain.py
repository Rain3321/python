#https://programmers.co.kr/learn/courses/30/lessons/64061
def solution(board, moves):
    stack = []
    answer = 0
    
    for time in moves:
        for item in range(len(board)):
            if board[item][time-1] != 0:
                if not stack:
                    stack.append(board[item][time-1])
                    board[item][time-1] = 0
                    break
                else:
                    last = stack.pop()
                    if board[item][time-1] == last: 
                        answer = answer+2
                        board[item][time-1] = 0
                        break
                    else:
                        stack.append(last)
                        stack.append(board[item][time-1])
                        board[item][time-1] = 0
                        break
    
    return answer


