N, K = map(int, input().split())
table = list(input())

count = 0
for i in range(N):
    if (table[i] == "P"):
        for j in range(i-K, i+K+1):
            if (0<j<N and table[j] == "H"):
                table[j] = 0
                count += 1
                break
print(count)