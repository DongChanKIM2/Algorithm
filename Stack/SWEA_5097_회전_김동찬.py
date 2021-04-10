t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    queue = [0] * n
    arr = list(map(int, input().split()))
    for i in range(len(arr)):
        queue[i] = arr[i]
    for i in range(m):
        temp = queue.pop(0)
        queue.append(temp)
    print('#{} {}'.format(tc+1, queue[0]))