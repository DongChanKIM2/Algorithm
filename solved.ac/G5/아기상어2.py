# 상어들간의 최소거리를 구하는 문제
# 상어 위치를 전부 모아서 DFS 탐색으로 하는게 순서에 맞을 듯
# 전체 탐색은 dfs로 하지만 개별 거리 탐색은 bfs로 하는게 거리 탐색에 맞음
# 문제를 잘못 이해함. 상어간의 거리가 아니라 모든 0 에서 상어간의 최대거리를 구하는 거였음
from collections import deque
import sys
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


def dfs(stack):
    global ans
    for shark in stack:
        shark_x, shark_y = shark
        specific_stack = deque()
        specific_stack.append((shark_x, shark_y, 0))
        flag = 0
        visited = [[0] * M for _ in range(N)]
        while specific_stack:
            curr_x, curr_y, temp = specific_stack.popleft()
            for direction in range(8):
                nx = curr_x + dx[direction]
                ny = curr_y + dy[direction]
                if 0 <= nx < N and 0 <= ny < M:
                    if arr[nx][ny] == 1:
                        flag = 1
                        break
                    elif visited[nx][ny] == 0:
                        visited[nx][ny] = 1
                        specific_stack.append((nx, ny, temp+1))
            if flag == 1:
                if temp > ans:
                    ans = temp
                break


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
# visited = [[0] * M for _ in range(N)]
stack = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            stack.append((i, j))
ans = 0
dfs(stack)
print(ans+1)
