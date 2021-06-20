# K는 10000이하
# 3 10
# 1 2 5

N, K = map(int, input().split())
coins = []
for _ in range(N):
    coin = int(input())
    coins.append(coin)

# 동전들 표시해줄 ARR (1 ~ 100,000)
arr = [0] * (K+1)
arr[0] = 1

for i in coins:
    for j in range(i, K+1):
        arr[j] += arr[j-i]

print(arr[-1])