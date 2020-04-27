#https://programmers.co.kr/learn/courses/30/lessons/62048
import math
def solution(w,h):
    dx = h/w
    check = math.gcd(w,h)
    
    return w*h - check * ((w/check) + (h/check) - 1)
