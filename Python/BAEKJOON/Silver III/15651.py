N, M = map(int, input().split())
NM_list = []

def dfs():
    if len(NM_list) == M:
        for i in range(M):
            print(NM_list[i], end=' ')
        print('')
        return

    for i in range(1,N+1):
        NM_list.append(i)
        dfs()
        NM_list.pop()

dfs()