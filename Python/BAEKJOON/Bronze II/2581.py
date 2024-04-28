M = int(input())
N = int(input())
sosu = []

for num in range(M, N+1):
    count = 0
    if (num > 1):
        for i in range(2, num):
            if(num % i == 0):
                count += 1
                break
        if (count == 0):
            sosu.append(num)

if(len(sosu) > 0):
    print(sum(sosu))
    print(min(sosu))
else:
    print(-1)