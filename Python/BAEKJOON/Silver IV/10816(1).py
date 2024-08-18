# 이분 탐색 풀이

import sys, bisect

input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
numbers = list(map(int, input().strip().split()))
numbers.sort()  # 숫자 카드 정렬

M = int(input().strip())
M_list = list(map(int, input().strip().split()))

# 이분 탐색 알고리즘 (내장함수 사용)
def num_count(arr, value):
    left_index = bisect.bisect_left(arr, value)
    right_index = bisect.bisect_right(arr, value)
    return right_index - left_index

result = []
for i in M_list:
    result.append(str(num_count(numbers, i)))

print(*result)
