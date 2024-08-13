# 빙고 입력
bingo = []
for _ in range(5):
    bingo.append(list(map(int, input().split())))

# 사회자가 부르는 숫자 입력
call_numbers = []
for _ in range(5):
    call_numbers.extend(list(map(int, input().split())))

# 번호 체크 리스트, 해당 위치가 불린 경우 True로 표시!
check = [[False] * 5 for _ in range(5)]

# 숫자 위치 저장용 딕셔너리
number_position = {}
for i in range(5):
    for j in range(5):
        number_position[bingo[i][j]] = (i, j)

def count_bingo():
    count = 0
    # 가로줄 빙고 확인 (5줄)
    for i in range(5):
        if all(check[i]): count += 1
    
    # 세로줄 빙고 확인 (5줄)
    for j in range(5):
        if all(check[i][j] for i in range(5)): count += 1
    
    # \ 대각선 빙고 확인 (1줄)
    if all(check[i][i] for i in range(5)): count += 1
    
    # / 대각선 빙고 확인 (1줄)
    if all(check[i][5 - 1 - i] for i in range(5)): count += 1
    
    return count

# 숫자 불린 순서에 따라 체크
for index, number in enumerate(call_numbers):
    x, y = number_position[number]
    check[x][y] = True
    
    if count_bingo() >= 3:
        print(index + 1)
        break
