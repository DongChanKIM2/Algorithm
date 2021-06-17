import sys

def bf(start):
    distance[start] = 0
    for i in range(N):
        for j in range(M):
            curr = arr[j][0]
            next = arr[j][1]
            cost = arr[j][2]
            if distance[curr] != INF and distance[next] > distance[curr] + cost:
                distance[next] = distance[curr] + cost
                if i == N - 1:
                    return True
    return False


input = sys.stdin.readline
INF = int(1e9)
N = int(input())
M = int(input())
arr = []
for _ in range(M):
    # start, end, cost = map(int, input().split())
    start, end, cost = list(map(int, sys.stdin.readline().split()))
    arr.append((start, end, cost))
# 시작 도시에서 끝 도시로 가는 데 드는 최소 비용
distance = [INF] * (N+1)
# start, end = map(int, input().split())
start, end = map(int, input().split())
negative_cycle = bf(start)
print(distance[end])
# if negative_cycle:
#     print("-1")
# else:
#     print(distance)
#     # 출발지(start)가 1일때라고 가정
#     for i in range(2, N+1):
#         if distance[i] == INF:
#             print(-1)
#         else:
#             print(distance[i])
