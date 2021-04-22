# 덱큐말고 선형큐로도 패보자~~
from collections import deque

# 충분한 가지치기를 못하는 상황 => 어떠한 조건을 더 줘야함
# dfs -> bfs로 변경

# def dfs(v, cnt):
#     # print(ans_lst)
#     # 백만 이상은 돌려보내기
#     if v > M:
#         return
#
#     if v == M:
#         print(cnt)
#         return cnt
#
#     if v in ans_lst:
#         for j in range(len(ans_lst)):
#             if v == ans_lst[j] and cnt_lst[j] > cnt:
#                 cnt_lst[j] = cnt
#                 break
#     else:
#         ans_lst.append(v)
#         cnt_lst.append(cnt)
#
#     if 0 < v + 1 <= 1000000:
#         dfs(v+1, cnt+1)
#     if 0 < v - 1 <= 1000000:
#         dfs(v-1, cnt+1)
    # if 0 < 2 * v <= 1000000:
    #     dfs(v*2, cnt+1)
    # dfs(v-10, cnt+1)

def bfs(v, cnt):
    queue = deque()
    queue.append((v, cnt))

    while queue:
        # 순서대로 빠른 순으로 도달하기때문에 dfs보다 cnt가 순차적이라는 장점이 있음
        current, current_cnt = queue.popleft()

        # 뭔가 실행시간을 줄일 수 있는 백트랙킹 조건을 생각해보자 -> 더 크면 return 시키는 것
        if current in distance_dict.keys():
            if distance_dict[current] > current_cnt:
                distance_dict[current] = current_cnt
            else:
                continue
        else:
            distance_dict[current] = current_cnt

        # 1 2 4 8 7 가능성 고려
        if current == M:
            return current_cnt

        if 0 < current + 1 <= 1000000:
            if current + 1 in distance_dict.keys():
                if current_cnt + 1 < distance_dict[current+1]:
                    queue.append((current+1, current_cnt+1))
            else:
                queue.append((current + 1, current_cnt + 1))

        if 0 < current - 1 <= 1000000:
            if current - 1 in distance_dict.keys():
                if current_cnt + 1 < distance_dict[current-1]:
                    queue.append((current-1, current_cnt+1))
            else:
                queue.append((current - 1, current_cnt + 1))

        if 0 < current * 2 <= 1000000:
            if current * 2 in distance_dict.keys():
                if current_cnt + 1 < distance_dict[current*2]:
                    queue.append((current*2, current_cnt+1))
            else:
                queue.append((current * 2, current_cnt + 1))

        if 0 < current - 10 <= 1000000:
            if current - 10 in distance_dict.keys():
                if current_cnt + 1 < distance_dict[current-10]:
                    queue.append((current-10, current_cnt+1))
            else:
                queue.append((current - 10, current_cnt + 1))


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    # 방문위치랑 cnt 저장하는 dict
    distance_dict = {}
    print('#{} {}'.format(tc+1, bfs(N, 0)))
    # print(distance_dict)

