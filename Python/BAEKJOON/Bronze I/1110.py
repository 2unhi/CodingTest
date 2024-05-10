N = int(input())
num = N
count = 0

while (True):
    first = N // 10
    second = num % 10
    last = (first + second) % 10
    num = (second * 10) + last

    count += 1

    if (num == N):
        break

print(count)