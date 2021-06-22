# 1. 이동회수의 최소값을 구하거나 탈출하지 못한다면 -1 출력
# 2. 열쇠 ~ 문 대응
# 3. 기존의 구현 문제와 차이점은 한번 방문한 위치를 중복해서 방문할 수 잇는 점이다 -> 매우 중요!!
# 4. BFS로 최소값은 구할 수 있을 것 같은데 실패하는 걸 어떻게 찾지
# 5. 열쇠를 찾지 않았는데 간 길을 중복해서 가면 실패라고 볼 수 있을 것 같다
# 6. 열쇠를 찾으면 방문처리 전부 취소하고 열쇠있던 장소를 방문처리하면 될듯(1로 하면 출구랑 중복되므로 2로)
# 7. 먼저 열쇠를 찾는다고 무조건 최단거리라는 보장이 없음..
# 8. 3차원 visited 조건이 필요함 -> 비트마스킹 기법/ 열쇠상태가 동일하면 동일한 장소 중복 접근 불가능
# 9, 열쇠는 중복될 수 있으므로 더하기가 아닌 무조건 or 로 해야만 함!
from collections import deque


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y, keys, ans):
    queue = deque()
    arr[x][y] = '.'
    visited[keys][x][y] = 1
    queue.append((x, y, keys, ans))
    flag = 0
    while queue:
        curr_x, curr_y, curr_keys, curr_ans = queue.popleft()
        for direction in range(4):
            nx = curr_x + dx[direction]
            ny = curr_y + dy[direction]
            if 0 <= nx < N and 0 <= ny < M:
                if arr[nx][ny] == '1':
                    curr_ans += 1
                    flag = 1
                    break
                elif visited[curr_keys][nx][ny] != 0:
                    continue
                elif arr[nx][ny] == '.':
                    visited[curr_keys][nx][ny] = 1
                    queue.append((nx, ny, curr_keys, curr_ans+1))
                elif arr[nx][ny] == '#':
                    continue
                # 열쇠를 찾으면 현재 내가 지닌 key를 바꿔주기
                elif arr[nx][ny] in all_keys:
                    key = ord(str(arr[nx][ny])) - 97
                    key = 2 ** key
                    keys = curr_keys | key
                    # print(nx, ny, key, keys)
                    visited[keys][nx][ny] = 1
                    queue.append((nx, ny, keys, curr_ans+1))
                elif arr[nx][ny] in all_doors:
                    door = ord(str(arr[nx][ny])) - 65
                    door = 2 ** door
                    if door & curr_keys:
                        visited[curr_keys][nx][ny] = 1
                        queue.append((nx, ny, curr_keys, curr_ans+1))
                    else:
                        continue
        if flag == 1:
            print(curr_ans)
            break
    if flag == 0:
        print(-1)


N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
# 내가 달리지는 상태는 열쇠의 종류에 따라 달라지므로 2 ** 6 = 64
visited = [[[0] * M for _ in range(N)] for _ in range(64)]
init_x, init_y = 0, 0
all_keys = ['a', 'b', 'c', 'd', 'e', 'f']
all_doors = ['A', 'B', 'C', 'D', 'E', 'F']
ans = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            init_x, init_y = i, j

my_keys = 0
bfs(init_x, init_y, my_keys, ans)
