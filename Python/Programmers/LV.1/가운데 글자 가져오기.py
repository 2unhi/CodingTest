def solution(s):
    median = int(len(s)/2)
    if (len(s) % 2 == 1):
        return s[median]
    else:
        return s[median-1:median+1]