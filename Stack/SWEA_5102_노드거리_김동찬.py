def dfs(start, end):
    queue = []
    queue.append((start, 0))
    visited = [0] * v
    visited[start] = 1
    while queue:
        current, dist = queue.pop(0)
        # print(dist)
        if current == end:
            return dist
        for i in range(v):
            if arr[current][i] == 1 and visited[i] == 0:
                queue.append((i, dist+1))
                visited[i] = 1
    return 0


t = int(input())
for tc in range(t):
    v, e = map(int, input().split())
    arr = [[0]*v for _ in range(v)]
    distance = [[0]*v for _ in range(v)]
    stack = []
    for i in range(e):
        x, y = map(int, input().split())
        arr[x-1][y-1] = 1
        arr[y-1][x-1] = 1
    start, end = map(int, input().split())
    start -= 1
    end -= 1
    print('#{} {}'.format(tc+1, dfs(start, end)))
