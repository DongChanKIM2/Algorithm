for tc in range(1, 11):
    n = int(input())
    arr = list(map(int, input().split()))
    queue = [0] * 8
    for i in range(8):
        queue[i] = arr[i]

    while queue[-1] > 0:
        for i in range(5):
            t = queue.pop(0)
            t -= (i + 1)
            queue.append(t)
            if queue[-1] <= 0:
                break
    queue[-1] = 0
    print('#{}'.format(tc), end=' ')
    for i in queue:
        print(i, end=' ')
    print()