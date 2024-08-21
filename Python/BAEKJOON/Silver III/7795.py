import sys, bisect

# 입력 받기
T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    arr_A = list(map(int, sys.stdin.readline().split()))
    arr_B = list(map(int, sys.stdin.readline().split()))
    arr_B.sort() # 배열B 정렬

    count = 0

    # A의 각 원소에 대해 B에서 더 작은 원소의 개수를 이분 탐색으로 계산
    for i in arr_A:
        check = bisect.bisect_right(arr_B, i - 1)
        count += check
    
    print(count)
