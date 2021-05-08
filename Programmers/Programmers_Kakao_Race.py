# 비용: 직선 100원, 코너: 600원
# 계산방법: 움직인거 거리 * 100 + 코너개수 * 500 의 최소비용을 산출하자
# 코너의 정의:
# 1. 위아래로 움직이다가 좌우로 변경
# 2. 좌우로 움직이다가 위아래로 변경


# 상하 좌우 순서(direction: 0, 1, 2, 3)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(board, answer):
    global visited
    start_x, start_y, move, corner, dir = 0, 0, 0, 0, -1
    N = len(board)
    # 최소비용을 구하니까 visited를 했더라도 더 최소비용이면 가야되니까 비용자체를
    visited = [[0] * N for _ in range(N)]
    queue = []
    queue.append((start_x, start_y, move, corner, dir))
    while queue:
        current_x, current_y, current_move, current_corner, current_dir = queue.pop(0)

        if (current_x, current_y) == (N-1, N-1):
            answer.append(current_move*100 + current_corner*500)

        for direction in range(4):
            nx = current_x + dx[direction]
            ny = current_y + dy[direction]
            if nx >= N or ny >= N or nx < 0 or ny < 0:
                continue
            if board[nx][ny] == 1:
                continue

            if board[nx][ny] == 0 and visited[nx][ny] == 0:
                # 위아래로 움직여야하는데 그전에는 좌우로 움직였으면 코너
                if direction == 0 or direction == 1:
                    if current_dir == 2 or current_dir == 3:
                        queue.append((nx, ny, current_move+1, current_corner+1, direction))
                        visited[nx][ny] = (100 * (current_move + 1)) + (500 * (current_corner + 1))
                    else:
                        queue.append((nx, ny, current_move+1, current_corner, direction))
                        visited[nx][ny] = (100 * (current_move + 1)) + (500 * current_corner)

                # 좌우로 움직여야하는데 그전에는 위아래로 움직였으면 코너
                if direction == 2 or direction == 3:
                    if current_dir == 0 or current_dir == 1:
                        queue.append((nx, ny, current_move+1, current_corner+1, direction))
                        visited[nx][ny] = (100 * (current_move + 1)) + (500 * (current_corner + 1))
                    else:
                        queue.append((nx, ny, current_move+1, current_corner, direction))
                        visited[nx][ny] = (100 * (current_move + 1)) + (500 * current_corner)

            # 최소값을 구해야하기 때문에 중복해서 진행
            elif board[nx][ny] == 0 and visited[nx][ny] != 0:
                # 상하로 움직일때
                if direction == 0 or direction == 1:
                    # 그 이전 움직임이 좌우이면
                    if current_dir == 2 or current_dir == 3:
                        if (100 * (current_move + 1)) + (500 * (current_corner + 1)) <= visited[nx][ny]:
                            queue.append((nx, ny, current_move+1, current_corner+1, direction))
                            visited[nx][ny] = (100 * (current_move + 1)) + (500 * (current_corner + 1))
                    else:
                        if (100 * (current_move + 1)) + (500 * current_corner) <= visited[nx][ny]:
                            queue.append((nx, ny, current_move+1, current_corner, direction))
                            visited[nx][ny] = (100 * (current_move + 1)) + (500 * current_corner)

                # 좌우로 움직여야하는데 그전에는 위아래로 움직였으면 코너
                if direction == 2 or direction == 3:
                    if current_dir == 0 or current_dir == 1:
                        if (100 * (current_move + 1)) + (500 * (current_corner + 1)) <= visited[nx][ny]:
                            queue.append((nx, ny, current_move+1, current_corner+1, direction))
                            visited[nx][ny] = (100 * (current_move + 1)) + (500 * (current_corner + 1))
                    else:
                        if (100 * (current_move + 1)) + (500 * current_corner) <= visited[nx][ny]:
                            queue.append((nx, ny, current_move+1, current_corner, direction))
                            visited[nx][ny] = (100 * (current_move + 1)) + (500 * current_corner)


def solution(board):
    answer = []
    bfs(board, answer)
    return min(answer)



