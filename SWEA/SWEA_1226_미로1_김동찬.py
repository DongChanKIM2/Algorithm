def bfs(start_x, start_y):
    # global moving
    queue = []
    moving = 0
    queue.append((start_x, start_y, moving))
    while queue:
        # 8방향 탐색
        dx = [2, 2, -2, -2, 1, 1, -1, -1]
        dy = [1, -1, 1, -1, 2, -2, 2, -2]
        current_x, current_y, moving = queue.pop(0)
        # 시작위치 visited
        arr[current_x][current_y] = 1
        # 목적지에 도달했다면 moving(얼마나 이동했나) return
        if current_x == end_x and current_y == end_y:
            return moving
        for direction in range(8):
            nx = current_x + dx[direction]
            ny = current_y + dy[direction]
            # 테두리 검사
            if nx >= l or ny >= l or nx < 0 or ny < 0:
                continue
            if arr[nx][ny] == 0:
                current_x, current_y = nx, ny
                # moving += 1
                queue.append((current_x, current_y, moving+1))
                arr[current_x][current_y] = 1

    # return moving

t = int(input())
for tc in range(t):
    l = int(input())
    arr = [[0]*l for _ in range(l)]
    start_x, start_y = map(int, input().split())
    end_x, end_y = map(int, input().split())
    print(bfs(start_x, start_y))
    # print(arr)