N = int(input())

def bugs_count(N):
    dp = [0] * (N + 1)
    dp[1], dp[2] = 1, 2
    
    for i in range(3, N+1):
        dp[i] = dp[i - 1] * 2
        if ((i - 4) >= 1 and (i - 1) % 2 == 0): dp[i] -= dp[i - 4]  
        if ((i - 3) >= 1 and (i - 1) % 2 == 1): dp[i] -= dp[i - 3]

    return dp[N]

print(bugs_count(N))