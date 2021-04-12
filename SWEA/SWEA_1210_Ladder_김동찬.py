for tc in range(1, 11):
    n = int(input())
    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))

    x, y = 99, 0
    for i in range(100):
        if arr[99][i] == 2:
            y = i

    dx = [0, 0, -1]
    dy = [-1, 1, 0]

    while x != 0:
        for i in range(3):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= 100 or ny >= 100:
                continue
            if arr[nx][ny] == 1:
                x, y = nx, ny
                arr[x][y] += 1

    print('#{} {}'.format(tc, y))
