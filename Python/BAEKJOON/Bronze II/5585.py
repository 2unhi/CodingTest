# 물건의 가격 입력
price = int(input())

# 잔돈 계산
change = 1000 - price

# 거스름돈 동전 종류
coins = [500, 100, 50, 10, 5, 1]

# 동전 개수를 세기 위한 변수
coin_count = 0

for coin in coins:
    if (change >= coin):
        coin_count += change // coin  # 해당 동전으로 줄 수 있는 개수를 추가
        change %= coin  # 남은 잔돈 업데이트

print(coin_count)