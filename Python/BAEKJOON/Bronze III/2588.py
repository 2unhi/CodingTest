N1 = int(input())
N2 = input()

for i in range(3, 0, -1):
    print(N1 * int(N2[i-1]))

print(N1 * int(N2))