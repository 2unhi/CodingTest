lines = list(map(int, input().split()))
lines.sort()

if(lines[0] + lines[1] <= lines[2]):
    print((lines[0] + lines[1]) * 2 - 1)
else:
    print(sum(lines))