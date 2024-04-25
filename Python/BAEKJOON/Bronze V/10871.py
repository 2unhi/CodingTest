N, X = map(int, input().split())
nums = list(map(int, input().split()))

for i in range(N):
    if(nums[i] >= X):
        continue
    else:
        print(nums[i], end=' ')