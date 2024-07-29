def solution(n):
    count = 0
    for i in range(n):
        total = 0
        for j in range(i+1, n+1):
            total += j
            if (total == n):
                count += 1
                break
            if(total > n):
                break
    return count