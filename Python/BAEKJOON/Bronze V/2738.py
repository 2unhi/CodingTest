N, M = map(int, input().split())
A, B = [], []

# 행렬A 원소 입력
for i in range(N):
    a = list(map(int, input().split()))
    A.append(a)

# 행렬B 원소 입력
for i in range(N):
    b = list(map(int, input().split()))
    B.append(b)

# 행렬A, B 원소 합 출력
for row in range(N):
    for col in range(M):
        result = A[row][col] + B[row][col]
        print(result, end=' ')
    print()