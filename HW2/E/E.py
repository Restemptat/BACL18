import sys
sys.setrecursionlimit(5000)
def solution(a, b):
    if a < 0 or b < 0:
        print("it's error: numb < 0")
        return 0 
    s = 0
    if a > 0:
        a -= 1
        s += 1
    if b > 0:
        b -= 1
        s += 1
    return 0 if s == 0 else s + solution(a, b)