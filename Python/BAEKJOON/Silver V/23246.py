n = int(input())
climbing = [list(map(int, input().split())) for _ in range(n)]

# lambda 함수를 활용하여 순차적인 정렬 기준 적용
climbing = sorted(climbing, key = lambda x : (x[1] * x[2] * x[3], x[1] + x[2] + x[3], x[0]))

for b, p, q, r in climbing[:3]:
    print(b, end= ' ')