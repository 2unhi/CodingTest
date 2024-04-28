T = int(input())

for _ in range(T):
    OX = list(input())
    count, sum = 0, 0

    for i in OX:
        if(i == "O"):
            count += 1
            sum += count
        else:
            count = 0

    print(sum)