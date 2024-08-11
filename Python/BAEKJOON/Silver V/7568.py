# 사람 수 입력
N = int(input())

# 사람의 몸무게와 키를 저장
people = []

for _ in range(N):
    weight, height = map(int, input().split())
    people.append((weight, height))

# 덩치 등수를 저장
ranks = []

for i in range(N):
    rank = 1 # 초기 등수는 1로 설정하고 비교 후 더하기
    for j in range(N):
        if (i != j): # 자신을 제외한 다른 사람과 비교
            if (people[i][0] < people[j][0] and people[i][1] < people[j][1]):
                rank += 1
    ranks.append(rank)

print(" ".join(map(str, ranks)))