t = int(input())
for tc in range(t):
    n = int(input())
    cards = list(input().split())
    result = []
    length = len(cards)
    if n % 2 == 0:
        for i in range(length//2):
            result.append(cards[i])
            result.append(cards[i + (length//2)])
    else:
        for i in range(length//2):
            result.append(cards[i])
            result.append(cards[i + (length//2) + 1])
        result.append(cards[(length//2)])

    print('#{}'.format(tc+1), end=' ')
    for i in result:
        print(i, end=' ')
    print()