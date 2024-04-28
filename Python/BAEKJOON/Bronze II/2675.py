T = int(input())

for _ in range(T):
    count, word = input().split()
    for i in word:
        print(i*int(count), end='')
    print()