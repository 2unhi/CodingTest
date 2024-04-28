N = int(input())
fibo = [0, 1]

for i in range(2, N+1):
    fibo.append(fibo[-1] + fibo[-2])

print(fibo[N])