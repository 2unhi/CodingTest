N, k = map(int, input().split())
scores = list(map(int, input().split()))

scores.sort(reverse=True) # 점수를 내림차순으로 정렬
print(scores[k-1]) # 커트라인 점수 출력