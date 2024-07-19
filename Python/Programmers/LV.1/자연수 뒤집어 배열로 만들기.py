def solution(n):
    num = list(str(n))
    num = num[::-1]
    return list(map(int, num))