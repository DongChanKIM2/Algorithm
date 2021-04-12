t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    queue = [0] * n
    queue_idx = [0] * n
    top = -1

    while len(arr) > top + 1:
        for i in range(n):
            if queue[i] == 0:
                top += 1
                temp = arr[top]
                queue[i] += temp
                queue_idx[i] = top + 1
            if top + 1 >= len(arr):
                break
        for i in range(n):
            queue[i] //= 2

    result = 0
    if max(queue) > 1:
        while max(queue) > 1:
            for i in range(len(queue)):
                queue[i] //= 2
        for i in range(len(queue)):
            if queue[i] == max(queue):
                result = queue_idx[i]
    elif max(queue) == 1:
        for i in range(len(queue)):
            if queue[i] == max(queue):
                result = queue_idx[i]

    print('#{} {}'.format(tc+1, result))

