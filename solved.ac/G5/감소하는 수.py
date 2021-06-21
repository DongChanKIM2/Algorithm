# 0 1 2 3 4 5 6 7 8 9 10 20 21 30 31 32 40 41 42 43
# 1차 시도: 1부터 끝까지 탐색하면서
# 2차 시도: 1000, 100, 10 단위로 더해주면서 탐색
# 3차 시도: 1423 이면 1000 -> 1100 -> 1200 -> 1300 -> 1400 -> 해야만 11 일때 20을 skip하고 21로 안감


import sys
from collections import deque
input = sys.stdin.readline


def check_minimum(start_idx):
    global i, curr_idx, ans
    queue = deque()
    queue.append(start_idx)
    while queue:
        curr = queue.pop()
        # print(curr, queue)
        value = curr
        if value > 9876543210:
            ans = -1
            return
        # 두 자리 수 이상일때까지만 검사가 유효
        flag = 0
        while curr >= 10:
            right_num = curr % 10
            curr //= 10
            left_num = curr % 10
            # print(left_num, right_num)
            if left_num <= right_num:
                flag = 1
                break
        # 검사를 했을 때 내림차순 숫자인걸 확인했고 백트랙킹 검사를 하고 추가해줄 것
        if flag == 1:
            # 추가해주는 조건을 백트랙킹을 고려해서 해주자
            compare_lst = list(map(int, str(value + 1)))
            compare_lst_len = len(compare_lst)
            temp = 0
            # print(compare_lst)
            for i in range(len(compare_lst)-1):
                temp += compare_lst[i] * (10 ** (compare_lst_len - 1 - i))
                if compare_lst[i+1] >= compare_lst[i]:
                    value = temp + 10 ** (compare_lst_len - i - 1)
                    # print(temp, value)
                    # print()
                    queue.append(value)
                    break
        else:
            ans = value
            curr_idx = value


N = int(input())
ans = 0
curr_idx = 0
for i in range(1, N+1):
    curr_idx += 1
    if i < 11:
        ans = i
    # 수가 감소하는 수인지 아닌지 판별하는 함수 필요
    else:
        check_minimum(curr_idx)


if N == 0:
    print(0)
else:
    print(ans)
