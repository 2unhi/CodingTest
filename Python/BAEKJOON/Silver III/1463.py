# 자연수 N 입력
N = int(input())

# DP 테이블 초기화 및 채우기
dp = [0] * (N+1)

for n in range(2, N+1):
    # 우선 dp[i-1] + 1로 지정
    dp[n] = dp[n-1] + 1
    # 2로 나누어 떨어질 경우
    if (n % 2 == 0): dp[n] = min(dp[n], dp[n//2] + 1)
    # 3으로 나누어 떨어질 경우
    if (n % 3 == 0): dp[n] = min(dp[n], dp[n//3] + 1)

print(dp[N])