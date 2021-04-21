# from collections import deque
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    queue = []
    queue.append((x, y))
    while queue:
        current_x, current_y = queue.pop(0)
        for i in range(4):
            nx = current_x + dx[i]
            ny = current_y + dy[i]
            # 제외조건으로도 해보자
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1 and visited[nx][ny] == 0:
                visited[nx][ny] = visited[current_x][current_y] + 1
                queue.append((nx, ny))



N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
visited[0][0] = 1
bfs(0, 0)
# print(visited)
print(visited[N-1][M-1])
