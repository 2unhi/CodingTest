# 해시맵 풀이

import sys
from collections import defaultdict

input = sys.stdin.read
data = input().split()

N = int(data[0])
numbers = list(map(int, data[1:N+1]))
M = int(data[N+1])
M_list = list(map(int, data[N+2:N+2+M]))

# 카드 개수를 저장할 딕셔너리
num_count = defaultdict(int)

# 카드 개수 세기
for card in numbers:
    num_count[card] += 1

results = []
for i in M_list:
    results.append(num_count[i])

print(*results)