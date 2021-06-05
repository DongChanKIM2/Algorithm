# 1. 원소로 100+1+, 01 두 개 존재
# 2. 100+1+를 없애고 나면 모두 01 이여야만 한다 or 반대 순서도 가능
# 3. stack 으로 풀려했으나 or로 인해 가능한 경우가 너무 많아 현타 와서 구글링....
# 4. 정규 표현식으로 풀면 바로 풀리는 문제

import re

N = int(input())
string_lst = []
for _ in range(N):
    # 우선 하나의 list에 원소로 삽입
    string_lst.append(input())


for i in string_lst:
    # 정규표현식 객체를 return 해주는 re.compile
    p = re.compile('(100+1+|01)+')
    # i(원소)가 p에서 full match(완전히 일치) 하는지 확인
    result = p.fullmatch(i)
    if result:
        print('YES')
    else:
        print('NO')


# T = int(input())
# for tc in range(T):
#     electric = list(input())
#     stack = []
#     start = 0
#     end = -1
#     for i in range(len(electric)):
#         stack.append(electric[i])
#         end += 1
#         # 맨 앞부터 01이면 지워보자
#         if end == 1 and stack[start] == '0' and stack[end] == '1':
#             stack.pop(0)
#             stack.pop(0)
#             end -= 2
#         if end > start:
#             if stack[start] == '1' and stack[end] == '0' and stack[end-1] == '1' and (end-1 != start):
#                 cnt = end - start
#                 end -= cnt
#                 while cnt:
#                     stack.pop(0)
#                     cnt -= 1
#
#     flag = 0
#     # 쓰레기 남은 값들이 1, 2 면 실패
#     if 0 < end <= 2:
#         flag = 1
#
#
#     # 쓰레기값 100001 이 남는 경우가 존재
#     if end > 2:
#         if stack[0] == stack[-1] == '1':
#             for i in range(1, len(stack)-1):
#                 if stack[i] == '0':
#                     flag = 0
#                 else:
#                     flag = 1
#                     break
#         else:
#             flag = 1
#
#     if flag == 0:
#         print('YES')
#     else:
#         print('NO')
