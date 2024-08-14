# 구매한 물건 가격 입력
price = int(input())

# 잔돈 계산
change = 1000 - price

# 거스름돈 동전 종류 리스트
coins = [500, 100, 50, 10, 5, 1]

# 동전 개수 카운트
coin_count = 0

for coin in coins:
    if (change >= coin):
        coin_count += change // coin  # 해당 동전으로 계산 가능한 개수 추가
        change %= coin  # 나머지 잔돈 업데이트

print(coin_count)