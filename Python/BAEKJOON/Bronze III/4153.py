while (True):
    nums = list(map(int, input().split()))

    if sum(nums) == 0:
        break

    long = max(nums)
    nums.remove(long)

    if (nums[0]**2 + nums[1]**2 == long**2):
        print("right")
    else:
        print("wrong")