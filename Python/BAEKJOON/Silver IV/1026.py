N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = sorted(A)
B = sorted(B)[::-1]

S = 0
for i in range(N):
    S += (A[i]*B[i])

print(S)