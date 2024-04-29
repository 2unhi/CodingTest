N = int(input())
three = []

for i in range(N):
    nums = list(map(int, input().split()))
    nums.sort()
    three.append(nums[-3])

for j in range(len(three)):
    print(three[j])