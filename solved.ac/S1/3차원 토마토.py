# 1. M: 가로길이(열) N: 세로길이(행) H: 높이
# 2. 일반적인 탐색문제와 차이점은 위, 아래도 고려를 해줘야함(3차원)
# 3. 토마토가 익기 위해선 익은 토마토 (좌우상하위아래) 주변에 하루 지나면 같이 익게 됨
# 4. 출력 방법: 다 익으면 몇일이 지났는지 / 처음부터 다 익엇으명 1 V / 다 못 익으면 0 출력
# 5. 최대길이가 각각 100씩이므로 재귀로 풀면 깊이 초과 날듯 -> bfs로 풀어야만 하네
# 6. 토마토는 하나 이상 있는 경우만 주어지므로 안 익은게 없으면 다 익은거로
import sys
from collections import deque
input = sys.stdin.readline

dx = [1, -1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]


def bfs(queue):
    answer = 0
    while queue:
        # print(queue)
        z, y, x, ans = queue.popleft()
        answer = ans
        for direction in range(6):
            nz = z + dz[direction]
            ny = y + dy[direction]
            nx = x + dx[direction]
            # 방문하지 않은 녀석들(방문하지 않았다는 것은 아직 익지 않았다는 뜻이니까)
            # 한 번이라도 방문했으면 익은 토마토
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and arr[nz][ny][nx] == 0 and visited[nz][ny][nx] == 0:
                queue.append((nz, ny, nx, ans+1))
                arr[nz][ny][nx] = 1
                visited[nz][ny][nx] = ans + 1
    return answer


# 3차원 z -> y -> x 순서대로 index 접근
M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[0] * M  for _ in range(N)] for _ in range(H)]

flag = 0
change = 1
tomatos = deque()
# 익은 토마토들 deque에 저장
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x] == 1:
                flag = 1
                tomatos.append((z, y, x, 0))
answer = bfs(tomatos)
# 안 익은 녀석 있는지 확인
for z in range(H):
    for y in range(N):
        for x in range(M):
            if arr[z][y][x] == 0:
                flag = -1


if flag == 0:
    print(0)
elif flag == -1:
    print(-1)
else:
    print(answer)
