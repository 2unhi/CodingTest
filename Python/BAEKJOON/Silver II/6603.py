def lotto(index, level):
    global choose, k, S
    if(level == 6):
        for i in choose:
            print(i, end=" ")
        print()
        return
    
    for i in range(index, k):
        choose.append(S[i])
        lotto(i+1, level+1)
        choose.pop()

while (True):
    choose = []
    lst = list(map(int, input().split()))

    k = lst[0]
    S = lst[1:]

    if (k == 0):
        break

    lotto(0, 0)
    print()