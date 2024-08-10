# 나무 조각의 초기 순서 입력
wood_pieces = list(map(int, input().split()))

# 버블 정렬을 수행하며 매 교환마다 상태 출력
while (wood_pieces != [1, 2, 3, 4, 5]):
    for i in range(4):
        if (wood_pieces[i] > wood_pieces[i + 1]):
            wood_pieces[i], wood_pieces[i + 1] = wood_pieces[i + 1], wood_pieces[i] # 자리 바꾸기
            print(" ".join(map(str, wood_pieces)))
