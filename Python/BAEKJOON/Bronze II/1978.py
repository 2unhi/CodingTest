N = int(input())
nums = list(map(int, input().split()))
sosu = 0 # 소수 개수 저장

for num in nums:
    count = 0 # 비교 숫자에서 나누어 떨어지는 수가 있는지를 저장
    if (num > 1):
        for i in range(2, num):
            if (num % i) == 0:
                count += 1
        if (count == 0):
            sosu += 1

print(sosu)