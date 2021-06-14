# 1. 목표: 충돌했을 때의 시간을 출력
# 2. 순서: 우선 이동하고(1초) 이동이 끝나고 나서 방향 전화이 잇으면(1초에 방향전환) 전환하기
# 3. 게임종료 규칙: 벽이나, 나 자신에게 충돌햇을 때
# 4. 머리가 들어가고 꼬리가 줄어드는 구조이므로 LIFO(BFS)로 풀이하는 게 적합


from collections import deque


def rotate_left(dx, dy):
    # global dx, dy
    # 북쪽을 보고 있다면 서쪽으로
    if dx == -1 and dy == 0:
        dx = 0
        dy = -1
    # 동쪽을 보고 있다면 북쪽으로
    elif dx == 0 and dy == 1:
        dx = -1
        dy = 0
    # 남쪽을 보고 있다면 동쪽으로
    elif dx == 1 and dy == 0:
        dx = 0
        dy = 1
    # 서쪽을 보고 있다면 남쪽으로
    elif dx == 0 and dy == -1:
        dx = 1
        dy = 0
    return dx, dy


def rotate_right(dx, dy):
    # global dx, dy
    # 북쪽을 보고 있다면 동쪽으로
    if dx == -1 and dy == 0:
        dx = 0
        dy = 1
    # 동쪽을 보고 있다면 남쪽으로
    elif dx == 0 and dy == 1:
        dx = 1
        dy = 0
    # 남쪽을 보고 있다면 서쪽으로
    elif dx == 1 and dy == 0:
        dx = 0
        dy = -1
    # 서쪽을 보고 있다면 북쪽으로
    elif dx == 0 and dy == -1:
        dx = -1
        dy = 0
    return dx, dy


def bfs(x, y, dx, dy):
    queue = deque()
    queue.append((x, y))
    arr[x][y] = 2
    time = 0
    while True:
        # 방향 전환
        if direction_changes[time] == 'L':
            dx, dy = rotate_left(dx, dy)
        elif direction_changes[time] == 'D':
            dx, dy = rotate_right(dx, dy)
        time += 1
        # 이동
        nx = x + dx
        ny = y + dy
        # print(time, nx, ny, dx, dy)
        # 게임 정지 조건
        if nx >= N or ny >= N or nx < 0 or ny < 0 or arr[nx][ny] == 2:
            break
        # 사과가 없이 이동하면 꼬리 한칸 자르고 머리 한칸 팽창
        if arr[nx][ny] == 0:
            queue.append((nx, ny))
            tail_x, tail_y = queue.popleft()
            arr[nx][ny] = 2
            arr[tail_x][tail_y] = 0
        # 사과가 있다면 머리만 한칸 팽창
        elif arr[nx][ny] == 1:
            queue.append((nx, ny))
            arr[nx][ny] = 2
        # 머리위치 갱신
        x, y = nx, ny
        # print(time)
    return time



N = int(input())
arr = [[0]*N for _ in range(N)]
K = int(input())
for _ in range(K):
    x, y = map(int, input().split())
    arr[x-1][y-1] = 1
L = int(input())
direction_changes = [0] * 10001
for _ in range(L):
    X, C = input().split()
    direction_changes[int(X)] = C
# print(arr)
# print(direction_changes)

print(bfs(0, 0, 0, 1))
# print()