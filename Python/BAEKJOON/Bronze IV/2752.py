number = list(map(int, input().split()))
number.sort()

for i in range(3):
    print(number[i], end=' ')