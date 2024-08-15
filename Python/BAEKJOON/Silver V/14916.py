# 거스름돈 액수 입력
N = int(input())

def minimum_coin(N):
    # 사용할 동전 개수
    coin = 0

    while (N > 0):
        # 5원으로 나누어지는 경우
        if (N % 5 == 0):
            coin += N // 5
            N = 0
        # 2원을 1번 사용 후 거스름돈에서 2원을 뺌
        else:
            N -= 2
            coin += 1
        
    # 음수일 경우 -1 반환
    if (N < 0): return -1

    return coin

print(minimum_coin(N))