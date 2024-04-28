N = int(input())
nums = []

for i in range(N):
    num = int(input())
    nums.append(num)

nums.sort()

for word in nums:
    print(word)