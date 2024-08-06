import sys

input = sys.stdin.read
data = input().splitlines()

# 회원 수 입력
N = int(data[0])

# 회원 정보를 저장할 리스트
members = []

for i in range(1, N + 1):
    age, name = data[i].split()
    age = int(age)
    members.append((age, name, i - 1))  # (나이, 이름, 인덱스 번호)

# 나이 기준으로 정렬하고 나이가 같으면 인덱스 번호를 기준으로 정렬
members.sort(key=lambda x: (x[0], x[2]))

# 정렬된 최종 결과 출력
for member in members:
    print(member[0], member[1])