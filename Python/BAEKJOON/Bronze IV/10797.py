day = int(input())
car = list(map(int, input().split()))
count = 0

for i in range(5):
    if car[i] == day:
        count += 1
    else:
        continue

print(count)