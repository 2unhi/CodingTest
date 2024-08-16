# 스크린 크기와 바구니 크기 입력
N, M = map(int, input().split())

# 사과 개수 입력
J = int(input())

# 사과 위치 리스트 입력
apples = [int(input()) for _ in range(J)]

# 바구니 초기 위치 (바구니 양쪽) 및 거리 계산
left, right = 0, M
distance = 0

for apple in apples:
    # 사과가 바구니의 왼쪽에 떨어진 경우
    if (apple < left):
        distance += left - apple
        left, right = apple, (apple + M - 1)
    # 사과가 바구니의 오른쪽에 떨어진 경우
    elif (apple > right):
        distance += apple - right
        left, right = (apple - M + 1), apple

print(distance)