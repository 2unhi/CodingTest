# 방바닥의 크기 입력
N, M = map(int, input().split())
floor = [input().strip() for _ in range(N)]

def count_floor(N, M, floor):
    visited = [[False] * M for _ in range(N)]  # 방문 여부를 체크
    count = 0

    def dfs(x, y, char):
        # '-'의 경우 오른쪽으로 계속 탐색
        if (char == '-'):
            for i in range(y, M):
                if (floor[x][i] == '-' and not visited[x][i]): visited[x][i] = True
                else: break
        # '|'의 경우 아래쪽으로 계속 탐색       
        elif (char == '|'):
            for i in range(x, N):
                if (floor[i][y] == '|' and not visited[i][y]): visited[i][y] = True
                else: break

    for i in range(N):
        for j in range(M):
            # 아직 방문하지 않은 경우
            if (not visited[i][j]):
                visited[i][j] = True
                # 새로운 나무 판자를 발견
                count += 1
                dfs(i, j, floor[i][j])

    return count

print(count_floor(N, M, floor))