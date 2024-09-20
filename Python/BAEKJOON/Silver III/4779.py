cantor = ['' for _ in range(13)]
cantor[0] = '-'

for i in range(1, 13):
    cantor[i] = cantor[i-1] + (' ' * (3**(i-1))) + cantor[i-1]

while (True):
    try:
        N = int(input())
        print(cantor[N])
    except:
        break