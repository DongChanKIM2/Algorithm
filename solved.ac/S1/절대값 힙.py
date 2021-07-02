# 이 문제는 특이한게 최소값이 아니라 최대값을 구해야합니다

import heapq
import sys
input = sys.stdin.readline


def hip(x):
    if x == 0:
        if len(q) == 0:
            print(0)
        else:
            print(heapq.heappop(q)[1])
    else:
        heapq.heappush(q, (abs(x), x))


N = int(input())
q = []
for _ in range(N):
    hip(int(input()))
    # print(q)