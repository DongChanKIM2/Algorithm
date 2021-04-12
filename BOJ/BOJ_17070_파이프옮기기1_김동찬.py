# direction = 0 => 0 (0,1) v, 1 (1,1) 가로
# direction = 1 => 0 (0,1) v, 2 (1,0) v, 1 (1,1) 대각선
# direction = 2 => 2 (1,0) v, 1 (1,1) 세로
from collections import deque


def pipe(direction, x, y):
    global cnt
    queue = deque()
    queue.append((direction, x, y))
    while queue:
        current_direction, current_x, current_y = queue.popleft()
        if current_x == n-1 and current_y == n-1:
            cnt += 1
            continue
        # 가로로 갈 때
        if current_direction == 0:
            d = [0, 1]
            dx = [0, 1]
            dy = [1, 1]
            for i in range(2):
                nd = d[i]
                nx = current_x + dx[i]
                ny = current_y + dy[i]
                if nx >= n or ny >= n or nx < 0 or ny < 0:
                    continue
                if nd == 0:
                    if arr[nx][ny] == 1:
                        continue
                if nd == 1:
                    if arr[nx][ny] == 1 or arr[nx-1][ny] == 1 or arr[nx][ny-1] == 1:
                        continue
                # if nd == 2:
                #     if arr[nx][ny] == 1:
                #         continue
                queue.append((nd, nx, ny))
        # 대각선일때
        elif current_direction == 1:
            d = [0, 2, 1]
            dx = [0, 1, 1]
            dy = [1, 0, 1]
            for i in range(3):
                nd = d[i]
                nx = current_x + dx[i]
                ny = current_y + dy[i]
                if nx >= n or ny >= n or nx < 0 or ny < 0:
                    continue
                if nd == 0:
                    if arr[nx][ny] == 1:
                        continue
                if nd == 1:
                    if arr[nx][ny] == 1 or arr[nx-1][ny] == 1 or arr[nx][ny-1] == 1:
                        continue
                if nd == 2:
                    if arr[nx][ny] == 1:
                        continue
                queue.append((nd, nx, ny))
        # 세로일때
        elif current_direction == 2:
            d = [2, 1]
            dx = [1, 1]
            dy = [0, 1]
            for i in range(2):
                nd = d[i]
                nx = current_x + dx[i]
                ny = current_y + dy[i]
                if nx >= n or ny >= n or nx < 0 or ny < 0:
                    continue
                # if nd == 0:
                #     if arr[nx][ny] == 1:
                #         continue
                if nd == 1:
                    if arr[nx][ny] == 1 or arr[nx-1][ny] == 1 or arr[nx][ny-1] == 1:
                        continue
                if nd == 2:
                    if arr[nx][ny] == 1:
                        continue
                queue.append((nd, nx, ny))


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
start_x, start_y = 0, 1
cnt = 0
pipe(0, start_x, start_y)
print(cnt)

