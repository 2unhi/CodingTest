def solution(n):
    num = list(str(n))
    num.sort(reverse=True)
    answer = int("".join(num))
    return answer