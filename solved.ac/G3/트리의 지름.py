# 그래프간의 최장거리를 구하기 위해선 임의의 한 점에서 최대 거리 점을 구하고 그 점에서의 최대 거리를 구함
# 즉 임의의 점에서 DFS 를 통해 기준점을 구하고, 기준점에서 DFS을 실행하는 DFS 2번 실행 문제
# DFS, BFS 가 그래프 탐색의 도구라는 걸 다시금 깨닫게 된 문제
# 증명: https://blog.myungwoo.kr/112
# 구현: https://www.youtube.com/watch?v=1VNWJTbE2pM
# 풀이 순서
# 1. 간선들간의 정보를 담은 arr 생성
# 2. 무작위로 기준, 도착점 (1, 1) 생성하고나서 dfs 실행하면 기준 1로 도착점을 연결하는 dfs 반환
# 3. 기준 1에서 자기자신을 제외한 나머지 점들과의 거리를 담은 result_first 생성
# 4. dfs 한번 더 실행해서 지름 구하기


# start_node 점에서 출발해서 now_node 점으로 연결하는 구조
def dfs(start_node, now_node, arr, result):
    for edge, distance in arr[now_node]:
        # 아직 1번 기준점에서 방문하지 않았고 출발한 점은 고려하지 않음
        if result[edge] == 0 and edge != start_node:
            result[edge] = result[now_node] + distance
            # 출발점을 도착점으로 바꾸고 새로운 도착점으로 이동
            dfs(now_node, edge, arr, result)


# 그래프 간선들간의 연결 정보 arr 생성
V = int(input())
arr = [[] for _ in range(V+1)]
for i in range(V):
    temp = list(map(int, input().split()))
    for j in range(1, len(temp)//2):
        arr[temp[0]].append([temp[j * 2 - 1], temp[j * 2]])

result_first = [0 for _ in range(V+1)]
# 1번 점에서 시작 / 현재 위치 / arr / 1번 점에서 거리를 담아줄 result
dfs(1, 1, arr, result_first)
# 자기 자신과는 연결해주지 않기 때문에 거리 정보가 갱신되지 않지만 굳이 찜찜하자면 바꾸기
# result_first[1] = 0

maximum = 0
maximum_idx = 0
for i in range(len(result_first)):
    if result_first[i] > maximum:
        maximum = result_first[i]
        maximum_idx = i

result_final = [0 for _ in range(V + 1)]
dfs(maximum_idx, maximum_idx, arr, result_final)
# result_final[maximum_idx] = 0
print(max(result_final))
