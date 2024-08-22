# DP 테이블 준비
dp = [[0] * 15 for _ in range(15)]

# 0층 거주민 수 초기화
for i in range(1, 15):
    dp[0][i] = i

# DP 테이블 채우기
for k in range(1, 15):
    for n in range(1, 15):
        dp[k][n] = dp[k][n-1] + dp[k-1][n]

# 테스트 케이스 입력
T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    print(dp[k][n])