# 자연수 n 입력
n = int(input())

# 특별한 경우 먼저 처리
if (n == 0): print(0)
elif (n == 1): print(1)
else:
    # 초기 피보나치 수 설정
    a, b = 0, 1
    
    # F(2)부터 F(n)까지 계산
    for _ in range(2, n + 1):
        a, b = b, a + b
    
    print(b)