N = int(input())
fact = 1

for i in range(N, 0, -1):
    fact *= i

print(fact)