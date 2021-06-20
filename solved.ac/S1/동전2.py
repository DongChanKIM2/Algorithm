N, K = map(int, input().split())
coins = []
arr = [10001] * (K+1)
# arr[0] = 1

for _ in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)
        arr[coin] = 1

for coin in coins:
    for i in range(1, K):
        if i + coin <= K:
            if arr[i+coin] > arr[i] + 1:
                arr[i+coin] = arr[i] + 1

if arr[K] != 10001:
    print(arr[K])
else:
    print(-1)


