# def dfs(start, end):
#     visited[start] = 1
#     result.append(start)
#     for i in range(0, 100):
#         if arr[start][i] == 1 and visited[i] == 0:
#             dfs(i, end)
#     if end in result:
#         return 1
#     else:
#         return 0
#
#
# for tc in range(1, 11):
#     n, m = list(map(int, input().split()))
#     start_end_arr = list(map(int, input().split()))
#     start_arr = []
#     end_arr = []
#     arr = [[0]*100 for _ in range(100)]
#     visited = [0] * 100
#     result = []
#     for i in range(len(start_end_arr)):
#         if i % 2:
#             end_arr.append(start_end_arr[i])
#         else:
#             start_arr.append(start_end_arr[i])
#     for i in range(len(start_arr)):
#         arr[start_arr[i]][end_arr[i]] = 1
#
#     print('#{} {}'.format(tc, dfs(0, 99)))


def dfs(start, end):
    visited = []
    stack = [start]
    while stack:
        current = stack.pop()
        if current not in visited:
            visited.append(current)
            stack += reversed(stack_list[current])
    return visited


for tc in range(1, 11):
    n, m = list(map(int, input().split()))
    start_end_arr = list(map(int, input().split()))
    start_arr = []
    end_arr = []
    result = []
    for i in range(len(start_end_arr)):
        if i % 2:
            end_arr.append(start_end_arr[i])
        else:
            start_arr.append(start_end_arr[i])
    stack_list = {i: [] for i in range(0, 100)}
    for i in range(len(start_arr)):
        stack_list[start_arr[i]].append(end_arr[i])

    print(stack_list)
    # print('#{} {}'.format(tc, dfs(0, 99)))
