N = int(input())
XY = [list(map(int, input().split())) for _ in range(N)]

XY = sorted(XY)

for x, y in XY:
    print(x, y)