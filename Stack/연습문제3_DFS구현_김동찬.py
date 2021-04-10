# arr = [[], [2, 3], [1, 4, 5], [1, 7], [2, 6], [2, 6], [4, 5, 7], [6, 3]]

# n, m, v = list(map(int, input().split()))
# arr = [[0] * n for _ in range(n)]
# visited = [0] * n
#
# for _ in range(m):
#     x, y = list(map(int, input().split()))
#     arr[x-1][y-1] = 1
#     arr[y-1][x-1] = 1
#
#
# def dfs(v):
#     print(v+1, end=' ')
#     visited[v] = 1
#     for i in range(n):
#         if arr[v][i] == 1 and visited[i] == 0:
#             dfs(i)
#
#
# print(dfs(v))

n, m, v = list(map(int, input().split()))

stack_list = {i: [] for i in range(1, n+1)}

for i in range(1, m+1):
    x, y = map(int, input().split())
    stack_list[x].append(y)
    stack_list[y].append(x)


def dfs(stack_list, v):
    visited = []
    stack = [v]

    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack += reversed(stack_list[current])
    return visited


print(dfs(stack_list, v))
