# N은 세로길이이므로 행의 수 / k는 음식물 쓰레기의 수
# 100 by 100 이므로 그냥 dfs로 풀어도 될 듯
dx = [1, -1, 0 , 0]
dy = [0, 0, 1, -1]


def dfs(x, y):
    global ans, temp
    stack = []
    stack.append((x, y))
    while stack:
        curr_x, curr_y = stack.pop()
        for direction in range(4):
            nx = curr_x + dx[direction]
            ny = curr_y + dy[direction]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == 1 and visitied[nx][ny] == 0:
                    stack.append((nx, ny))
                    visitied[nx][ny] = 1
                    temp += 1
    if temp > ans:
        ans = temp


N, M, K = map(int, input().split())
arr = [[0] * M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().split())
    arr[r-1][c-1] = 1
visitied = [[0] * M for _ in range(N)]
ans = 0
for i in range(N):
    for j in range(M):
        temp = 1
        if arr[i][j] == 1 and visitied[i][j] == 0:
            visitied[i][j] = 1
            dfs(i, j)
print(ans)
