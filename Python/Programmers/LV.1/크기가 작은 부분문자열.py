def solution(t, p):
    count = 0
    t_len = len(t)
    p_len = len(p)
    for i in range(0, t_len - p_len + 1):
        if (int(t[i:i+p_len]) <= int(p)):
            count += 1
    return count