import sys
input = sys.stdin.read
data = input().split()

K = int(data[0])
N = int(data[1])
lan_line = [int(data[i]) for i in range(2, 2 + K)]

# 이분 탐색을 위한 랜선 초기 설정
start, end = 1, max(lan_line)
result = 0

while (start <= end):
    mid = (start + end) // 2
    
    # 중간 길이로 잘라서 만들 수 있는 랜선의 개수 계산
    count = 0
    for lan in lan_line:
        count += lan // mid
    
    # N개 이상의 랜선을 만들 수 있는 경우, 길이를 늘려서 탐색
    if (count >= N):
        result = mid
        start = mid + 1
    # 불가능한 경우, 길이를 줄여서 탐색
    else:
        end = mid - 1

print(result)