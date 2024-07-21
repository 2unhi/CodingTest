def solution(d, budget):
    count, total = 0, 0
    d.sort()
    for i in range(len(d)):
        total += d[i]
        if(total > budget): break
        else: count += 1
    return count