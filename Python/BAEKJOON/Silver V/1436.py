N = int(input())
movieNumber = 666
count = 0

while (True):
    if '666' in str(movieNumber):
        count += 1
        if count == N:
            break
    movieNumber += 1

print(movieNumber)