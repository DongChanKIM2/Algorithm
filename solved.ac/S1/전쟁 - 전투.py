# 전형적인 DFS, BFS 문제
# 가로 세로 길이가 100이므로 재귀 초과날수도 잇을 거 같으므로 bfs로 접근하려 했지만 dfs로 하는게 맞음
# W, B 출력
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    global white, black, temp
    visited[x][y] = 1
    queue = deque()
    queue.append((x, y))
    while queue:
        curr_x, curr_y = queue.popleft()
        for direction in range(4):
            nx = curr_x + dx[direction]
            ny = curr_y + dy[direction]
            if 0 <= nx < M and 0 <= ny < N:
                if arr[nx][ny] == arr[curr_x][curr_y] and visited[nx][ny] == 0:
                    visited[nx][ny] = temp + 1
                    temp += 1
                    queue.append((nx, ny))
                else:
                    continue
    if arr[x][y] == 'W':
        white += temp ** 2
    else:
        black += temp ** 2


N, M = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visited = [[0] * N for _ in range(M)]
white = 0
black = 0
for i in range(M):
    for j in range(N):
        temp = 1
        if visited[i][j] == 0:
            visited[i][j] = 1
            bfs(i, j)

print(white, black)