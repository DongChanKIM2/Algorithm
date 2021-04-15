from collections import deque


def dfs(head_x, head_y, change, cnt, dx, dy):
    # print(head_x, head_y, cnt)
    queue = []
    queue.append((head_x, head_y, change, cnt, dx, dy))
    while queue:
        head_x, head_y, change, cnt, dx, dy = queue.pop(0)
        print(head_x, head_y, cnt)
        if head_x >= n or head_x < 0 or head_y >= n or head_y < 0:
            return
        for i in range(len(change)):
            if cnt == int(change[i][0]):
                if change[i][1] == 'L':
                    dx, dy = Left(dx, dy)
                elif change[i][1] == 'D':
                    dx, dy = Right(dx, dy)
        nx = head_x + dx
        ny = head_y + dy
        queue.append((nx, ny, change, cnt+1, dx, dy))
        # dfs(nx, ny, change, cnt+1, dx, dy)


def Right(x, y):
    if (x, y) == (0, 1):
        return 1, 0
    elif (x, y) == (1, 0):
        return 0, -1
    elif (x, y) == (0, -1):
        return -1, 0
    elif (x, y) == (-1, 0):
        return 0, 1

def Left(x, y):
    if (x, y) == (0, 1):
        return -1, 0
    elif (x, y) == (-1, 0):
        return 0, -1
    elif (x, y) == (0, -1):
        return 1, 0
    elif (x, y) == (1, 0):
        return 0, 1


# 보드 크기 n
n = int(input())
arr = [[0] * n for _ in range(n)]
# 사과 개수 k
k = int(input())
# 사과 위치
for _ in range(k):
    row, col = map(int, input().split())
    arr[row-1][col-1] = 1
# 뱀의 방향전환
L = int(input())
change = []
for _ in range(L):
    X, C = input().split()
    X = int(X)
    change.append((X, C))
cnt = 0
dfs(0, 0, change, cnt, 0, 1)
