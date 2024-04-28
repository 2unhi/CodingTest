import math

D, H, W = map(int, input().split())
# 높이와 너비의 비율에 따른 대각선의 비율
ratio  = D / (H**2 + W**2)**0.5

print(math.floor(H*ratio), math.floor(W*ratio))