# 1. dfs로 풀었더니 시간초과 append 하고 pop 하는게 아무래도 2중 for문보다 시간이 많이 걸리는듯
# 2. 2 ** 100 > 100 ** 2 (같은 느낌)


import sys
input = sys.stdin.readline


# def dfs(i, j):
#     global ans
#     stack = []
#     stack.append((i, j))
#     while stack:
#         # print(stack)
#         curr_x, curr_y = stack.pop()
#         if curr_x == N-1 and curr_y == N-1:
#             ans += 1
#         elif 0 <= curr_x < N and 0 <= curr_y < N and arr[curr_x][curr_y] != 0:
#             if curr_x + arr[curr_x][curr_y] < N:
#                 stack.append((curr_x+arr[curr_x][curr_y], curr_y))
#             if curr_y + arr[curr_x][curr_y] < N:
#                 stack.append((curr_x, curr_y+arr[curr_x][curr_y]))


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
ans = 0
# dfs(0, 0)
# print(ans)
for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            break
        value = arr[i][j]
        down = i + value
        right = j + value
        if down < N:
            dp[down][j] += dp[i][j]
        if right < N:
            dp[i][right] += dp[i][j]

print(dp[-1][-1])