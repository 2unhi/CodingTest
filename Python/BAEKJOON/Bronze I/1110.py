N = int(input())
num = N
count = 0

while (True):
    first = num // 10
    second = num % 10
    num = (second * 10) + (first + second) % 10

    count += 1

    if (num == N): break

print(count)