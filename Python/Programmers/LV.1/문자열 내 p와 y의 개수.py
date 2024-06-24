def solution(s):
    answer = True
    p, y = 0, 0
    for i in s:
        if (i.lower() == "p"): p += 1
        elif (i.lower() == "y"): y += 1
        
    if (p != y): answer = False
    return answer