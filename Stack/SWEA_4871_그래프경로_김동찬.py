# def dfs(start, end):
#     visited[start-1] = 1
#     result.append(start-1)
#     for i in range(1, v+1):
#         if arr[start-1][i-1] == 1 and visited[i-1] == 0:
#             dfs(i, end)
#     return result
    # if end-1 in result:
    #     return 1
    # else:
    #     return 0


# t = int(input())
# for tc in range(t):
#     result = []
#     v, e = list(map(int, input().split()))
#     visited = [0] * v
#     arr = [[0]*v for _ in range(v)]
#     for i in range(e):
#         x, y = list(map(int, input().split()))
#         arr[x-1][y-1] = 1
#
#     start, end = list(map(int, input().split()))
#     print('#{}'.format(tc+1), end=' ')
#     print(dfs(start, end))


def dfs(start, end):
    visited = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack += reversed(graph[current])
    return visited


t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    graph = {i: [] for i in range(1, n+1)}
    for i in range(m):
        x, y = list(map(int, input().split()))
        graph[x].append(y)
    start, end = list(map(int, input().split()))
    print(dfs(start, end))
