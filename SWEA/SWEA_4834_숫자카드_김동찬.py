t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    cards = list(map(int, input().split()))
    minimum = 100000
    maximum = 6

    # 나누기로도 해보기
    for card in cards:
        card = int(card)
        arr[card] += 1

    max_idx = 0
    max_num = 0

    for idx in range(len(arr)):
        if max_num <= arr[idx]:
            max_num = arr[idx]
            max_idx = idx

    print('#{} {} {}'.format(tc + 1, max_idx, max_num))

