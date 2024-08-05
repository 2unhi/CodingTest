from itertools import combinations

# 9명의 난쟁이 키를 입력
dwarf9 = [int(input()) for _ in range(9)]

# 9명의 난쟁이 중 7명을 선택하는 모든 조합 구하기
for seven in combinations(dwarf9, 7):
    # 키의 합이 100인 경우
    if (sum(seven) == 100):
        # 오름차순으로 정렬하여 출력
        result = sorted(seven)
        for height in result:
            print(height)
        break