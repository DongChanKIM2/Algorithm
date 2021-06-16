# 우선순위큐: 우선순위를 설정하고 우선순위가 높은 순서에 따라 데이터를 추출할 수 있음
# 우선순위 큐를 구현하기 위해 Heap 을 사용할 수 있음
# Heap 라이브러리는 파이썬에서는 최소힙으로 구현되 있어서 우선순위가 낮은 순서인 최소값부터 POP 됨
# 파이썬에서 Heap 은 오름차순이 기본으로 설정되있어서 (노드, 거리)가 아니라 (거리, 노드)로 넣어야 최소거리가 먼저 삽입됨
# 즉 최소값을 탐색하는 절차를 생략할 수 있읍니다
# heapq는 이진트리기반이므로 i번 원소는 항상 i*2 + 1 번째와 i*2 + 2 번째 원소보다 작거나 같습니다


import heapq


INF = int(1e9)
# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())
# 시작 노드 번호를 입력받기
start = int(input())
# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:  # 큐가 비어있지 않다면
        print(q, distance)
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


# 다익스트라 알고리즘을 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경우 거리를 출력
    else:
        print(distance[i])