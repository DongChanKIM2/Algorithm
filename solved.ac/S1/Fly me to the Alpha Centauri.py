# 1. 이동법칙: 이전 이동거리의 -1, 0, +1 만큼 가능
# 2. 처음 이동 이전은 0이므로 무조건 +1 이 됨
# 3. 목표지점의 -1 거리에 도착을 하게 목표값을 구하고 마지막에 +1 헤주면 정답 도출
# 3.1 생각해보니까 마지막에 1 이동을 하려면 순차적으로 바뀌어야 하니까 완전 거꾸로 답을 내야 하는 문제였음
# 4. 대부분의 DP 문제가 그렇듯이 최적화처리를 안해주니까 메모리 초과 발생...
# 5. 중복되는 배열은 추가하지 않도록 조건을 추가해주니 시간 초과 발생...
# 6. DP로 풀려했으나 시간초과 및 2^^31 (오버플로우)로 포기 => 규칙성으로 해결할 수 밖에 없는 문제


T = int(input())
for tc in range(T):
    # 현재위치, 목표위치
    X, Y = map(int, input().split())
    # 시작과 도착을 0으로 하는게 직관적이므로 이동시
    dist = Y - X
    i = 1
    ans = 0
    while ans < dist:
        # ans += i
        ans += (i * 2)
        i += 1
    i -= 1
    if ans - dist >= i:
        # print(ans, dist, i, i*2-1)
        print(i*2-1)
    else:
        # print(ans, dist, i, i*2)
        print(i*2)


# T = int(input())
# for tc in range(T):
#     # 현재위치, 목표위치
#     X, Y = map(int, input().split())
#     # 시작과 도착을 0으로 하는게 직관적이므로 이동시
#     Y -= X
#     X -= X
#     # 움직인 힛수, 현재 위치, 이전 이동거리를 넣어줄 arr 생성
#     moving_arr = [(1, Y - 1, 1)]
#     flag = 0
#     ans = 0
#     while True:
#         if flag == 1:
#             break
#         for i in moving_arr:
#             # print(i)
#             moving_cnt = i[0]
#             curr = i[1]
#             before_move = i[2]
#             # 출발점에 도착했으면 break
#             # if curr == X:
#             #     flag = 1
#             #     ans = moving_cnt
#             #     break
#             if curr - (before_move - 1) < Y and (moving_cnt + 1, curr - (before_move - 1), before_move - 1) not in moving_arr:
#                 moving_arr.append((moving_cnt + 1, curr - (before_move - 1), before_move - 1))
#                 if curr - (before_move - 1) == X:
#                     flag = 1
#                     ans = moving_cnt
#                     break
#             if curr - before_move < Y and (moving_cnt + 1, curr - before_move, before_move) not in moving_arr:
#                 moving_arr.append((moving_cnt + 1, curr - before_move, before_move))
#                 if curr - before_move == X:
#                     flag = 1
#                     ans = moving_cnt
#                     break
#             if curr - (before_move + 1) >= 0 and (moving_cnt + 1, curr - (before_move + 1), before_move + 1) not in moving_arr:
#                 moving_arr.append((moving_cnt + 1, curr - (before_move + 1), before_move + 1))
#                 if curr - (before_move + 1) == X:
#                     flag = 1
#                     ans = moving_cnt
#                     break
#     print(ans + 2)
