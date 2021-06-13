# BFS로 시도했다가 시간초과나서 DFS로 변경
# 확실히 시간적인 부분에선 BFS가 DFS보다 유리함
# DP로도 풀어볼 것

# 가로 대각선 세로
dx = [0, 1, 1]
dy = [1, 1, 0]


def bfs(x, y, direction):
    global ans
    if x >= N or y >= N:
        return
    if x == N-1 and y == N-1:
        ans += 1
        return
    if direction == 0:
        if (0 <= x < N and 0 <= y + 1 < N) and arr[x][y+1] == 0:
            bfs(x, y+1, 0)s
        if (0 <= x + 1 < N and 0 <= y + 1 < N) and (arr[x+1][y] == 0 and arr[x][y+1] == 0 and arr[x+1][y+1] == 0):
            bfs(x+1, y+1, 1)
    elif direction == 1:
        if (0 <= x < N and 0 <= y + 1 < N) and arr[x][y+1] == 0:
            bfs(x, y+1, 0)
        if (0 <= x + 1 < N and 0 <= y + 1 < N) and (arr[x + 1][y] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y + 1] == 0):
            bfs(x + 1, y + 1, 1)
        if (0 <= x + 1 < N and 0 <= y < N) and arr[x+1][y] == 0:
            bfs(x+1, y, 2)
    elif direction == 2:
        if (0 <= x + 1 < N and 0 <= y + 1 < N) and (arr[x + 1][y] == 0 and arr[x][y + 1] == 0 and arr[x + 1][y + 1] == 0):
            bfs(x + 1, y + 1, 1)
        if (0 <= x + 1 < N and 0 <= y < N) and arr[x + 1][y] == 0:
            bfs(x + 1, y, 2)


# 집의 크기는 N >= 3 이상이므로 시작 위치보다 항상 큼
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# 가로:0 / 대각선:1 / 세로:2
start_x, start_y, direction = 0, 1, 0
ans = 0
# print(arr)
bfs(start_x, start_y, direction)
print(ans)
