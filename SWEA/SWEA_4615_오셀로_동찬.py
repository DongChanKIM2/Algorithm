t = int(input())
for tc in range(t):
    n, m = map(int, input().split())
    arr = [[0]*n for _ in range(n)]
    # 8방향 설정
    dx = [-1, -1, 0, 1, 1, 1, 0, -1]
    dy = [0, 1, 1, 1, 0, -1, -1, -1]
    length = n // 2
    # 초기 바둑판 셋팅
    arr[length-1][length-1] = 2
    arr[length][length] = 2
    arr[length][length-1] = 1
    arr[length-1][length] = 1

    # 돌 넣는 횟수만큼
    for i in range(m):
        y, x, color = map(int, input().split())
        x -= 1
        y -= 1
        arr[x][y] = color
        x_temp = 0
        y_temp = 0
        x_temp += x
        y_temp += y
        # 돌을 넣었을 때 8방향 모두 끝까지 수행
        for direction in range(8):
            while True:
                nx = x_temp + dx[direction]
                ny = y_temp + dy[direction]
                # 테두리에서 벗어나면 제외하기
                if nx < 0 or ny < 0 or nx >= n or ny >= n:
                    # print(1)
                    x_temp, y_temp = x, y
                    break
                if arr[nx][ny] == 0:
                    # print(2)
                    x_temp, y_temp = x, y
                    break
                # 테두리 내부이면 같은 게 있는지 끝까지 탐색
                if arr[nx][ny] == color:
                    # 같은 게 있다면! 원래 위치가 될때까지 복사하면서 가자
                    while not (nx == x and ny == y):
                        nx -= dx[direction]
                        ny -= dy[direction]
                        arr[nx][ny] = color
                        # print(3)
                        # print(arr)
                    x_temp, y_temp = x, y
                    break
                else:
                    x_temp, y_temp = nx, ny

    count_white = 0
    count_black = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                count_black += 1
            elif arr[i][j] == 2:
                count_white += 1

    print('#{} {} {}'.format(tc+1, count_black, count_white))
