# N: 노드(점)의 개수
# 간선의 개수: N - 1
# 부모, 자식, 가중치
# 1. 이 문제에서는 input 을 sys 로만 받아야 런타임에러가 안 납니다(sys > input) 으로 사용하고 재귀 깊이 1000 -> 100000
# 2. BFS를 사용하면 이런 문제를 해결할 수 있습니다(나중에 도전~~)

import sys
sys.setrecursionlimit(100000)


def dfs(start_node, curr_node, arr, result):
    for edge, distance in arr[curr_node]:
        if result[edge] == 0 and edge != start_node:
            result[edge] = result[curr_node] + distance
            dfs(curr_node, edge, arr, result)


# N = int(input())
N = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    # parent, child, weight = map(int, input().split())
    parent, child, weight = map(int, sys.stdin.readline().split())
    arr[parent].append([child, weight])
    arr[child].append([parent, weight])

first_result = [0] * (N+1)
dfs(1, 1, arr, first_result)

maximum = 0
maximum_idx = 0

for i in range(len(first_result)):
    if first_result[i] > maximum:
        maximum = first_result[i]
        maximum_idx = i

final_result = [0] * (N+1)
dfs(maximum_idx, maximum_idx, arr, final_result)

if N == 1:
    print(0)
else:
    print(max(final_result))
