N1, N2, N3 = map(int, input().split())

if (N1 == N2 == N3):
    print(10000 + N1*1000)
elif(N1 == N2 or N1 == N3):
    print(1000 + N1*100)
elif(N2 == N3):
    print(1000 + N2*100)
else:
    print(max(N1, N2, N3)*100)