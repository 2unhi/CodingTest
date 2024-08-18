N = int(input())
A = list(map(int, input().split()))
A.sort()  # 배열A 정렬

M = int(input())
M_list = list(map(int, input().split()))

# 이분탐색 알고리즘
def binary_search(arr, target, start, end):
    while (start <= end):
        mid = (start + end) // 2
        if (arr[mid] == target): return True
        elif (arr[mid] < target): start = mid + 1
        else: end = mid - 1
    return False

# 배열A에 속하는지 확인 후 결과 출력
for target in M_list:
    if binary_search(A, target, 0, N-1):
        print(1)
    else:
        print(0)
