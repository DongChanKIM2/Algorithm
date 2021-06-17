import heapq
import sys


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in arr[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


INF = int(1e9)
# N = int(input())
# M = int(input())
N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    # start, end, cost = map(int, input().split())
    start, end, cost = list(map(int, sys.stdin.readline().split()))
    arr[start].append((end, cost))
# print(arr)
# 시작 도시에서 끝 도시로 가는 데 드는 최소 비용
distance = [INF] * (N+1)
# start, end = map(int, input().split())
start, end = map(int, sys.stdin.readline().split())
dijkstra(start)
print(distance[end])
