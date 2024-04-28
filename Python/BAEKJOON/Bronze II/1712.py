A, B, C = map(int, input().split())

# C*num = A + B*num

if (B >= C):
    print(-1)
else:
    print(A//(C-B) + 1)
