# 크루스칼에 대해 들어가기 전 '서로소 집합'이란 것에 대해 알아야 합니다
# 서로소집합이란 겹치는 원소가 없는 집합들입니다
# 즉 정점이 5개 있는 그래프는 초기에 정점 하나 씩, 5개의 집합이 있는 서로소 집합이 생깁니다
# 서로소 집합 자료구조를 이용해서 Union-find 알고리즘을 이용하면 두 개의 원소가 같은 집합인지 판단할 수 있습니다

# 크루스칼이란 프림처럼 확장하며 탐색하는 게 아닌 거리에 따라 최솟값부터 연결하는 구조입니다
# 크루스칼은 프림과 다르게 양방향인것을 의식해서 start, end를 각각 추가안해주고 한번만 연결해줘도 괜찮습니다(union)
# MST (minimum spanning tree)가 되기 위해선 cycle(순환 구조)가 생기면 안됩니다


import sys


def find(x):
    if x != Vroot[x]:
        Vroot[x] = find(Vroot[x])
    return Vroot[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x != y:
        if y >= x:
            Vroot[y] = x
        else:
            Vroot[x] = y


V, E = map(int, sys.stdin.readline().split())
Vroot = [i for i in range(V+1)] # 각 정점의 root
Elist = [] # 간선들의 list

for _ in range(E):
    Elist.append(list(map(int, input().split())))

Elist.sort(key=lambda x: x[2])

ans = 0 # 가중치 합
cnt = 0 # 간선이 모두 연결되었는지 cnt

for start, end, weight in Elist:
    sRoot = find(start)
    eRoot = find(end)
    if sRoot != eRoot:
        union(start, end)
        cnt += 1
        ans += weight
    if cnt == V-1:
        break
# print(Vroot)
# print(Elist)
print(ans)

