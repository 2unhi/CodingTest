def solution(num, k):
    for i, n in enumerate(str(num)):
        if (n == str(k)):
            return i + 1
    return -1