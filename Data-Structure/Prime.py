# 전체 그래프 중 N개의 정점 N-1개의 간선으로 모든 정점을 연결한 부분집합을 spanning tree 라고 합니다
# 이런 spanning tree 들 중 가장 작은 값을 지니는 것을 Minimum spanning tree (MST) 이라 합니다
# MST 를 구하는 방법으론 크루스칼, 프림이 있습니다
# Prim 은 시작 정점에서부터 출발해 신장트리 집합을 확장하는 방법이고
# 크루스칼은 그리디 방법으로 모든 경우에서 최적 해답을 구하는 것입니다
# 수학적으로 프림 알고리즘은 증명하려면 너무 복잡해지므로 우선 코드로만 구헌하자
# 시간복잡도(N: 노드의 갯수, E: 간선의 개수)
# 프림: O(N^2) 크루스칼: O(E log(E)) / 간선의 개수가 많으면 프림 , 노드의 개수가 많으면 크루스칼을 사용하자

import heapq
import sys


def prim(start, weight):
    visit = [0] * (V+1)
    q = [[weight, start]]
    ans = 0 # 가중치 정답
    cnt = 0 # 간선 수
    while cnt < V: # spanning tree가 되기 위해선 최대 간선수가 V-1 개
        w, end = heapq.heappop(q)
        if visit[end]:
            continue # 방문한 곳이면 무시
        visit[end] = 1
        ans += w
        cnt += 1
        for start, weight in arr[end]:
            heapq.heappush(q, [weight, start])
    return ans


input = sys.stdin.readline
V, E = map(int, input().split())
arr = [[] for _ in range(V+1)]
for _ in range(E):
    start, end, weight = map(int, input().split())
    arr[start].append((end, weight))
    arr[end].append((start, weight))
print(prim(1, 0))