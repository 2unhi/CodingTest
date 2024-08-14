# 좌석 수 입력
N = int(input())
# 영화관 좌석 정보 입력
seat = input().strip()

# 컵 홀더 수 초기화 (가장 왼쪽은 무조건 놓아야 함)
cup_holder = 1
i = 0
while (i < N):
    # S 좌석일 경우, 하나를 놓고 다음 좌석으로 이동
    if (seat[i] == "S"):
        cup_holder += 1
        i += 1
    # L 좌석일 경우, 하나를 놓고 가운데를 점프하여 그 다음 좌석으로 이동
    elif (seat[i] == "L"):
        cup_holder += 1
        i += 2

print(min(cup_holder, N))