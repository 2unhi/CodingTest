import math

# 테스트 케이스의 수 입력
T = int(input())

for _ in range(T):
    # 각 테스트 케이스에 대한 사이트 값 N, M 입력
    N, M = map(int, input().split())
    
    # 조합 계산
    bridge = math.comb(M, N)
    print(bridge)