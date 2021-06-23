# 각 날짜마다의 최대 수익을 갱신하면서 접근해보자
# 전부 갱신해주니까 시간초과(N = 1,500,000) 이므로 N ** 2 이면 당연히 시간초과
# N + 1 개의 arr 를 생성해주는 것도 안될거 같지만 단순히 선형탐색만 한다면 괜춘
# 마지막에 어려웠던 부분이 max 구해줄 때 arr[i] 가 기준이 아니라 지금까지의 최대값을 기준으로 해야함
# 반례
"""
10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
"""
import sys
input = sys.stdin.readline


N = int(input())
arr = [0] * (N+1)
schedule = []
for i in range(N):
    T, P = map(int, input().split())
    schedule.append((T, P))
m = 0
for i in range(N):
    m = max(m, arr[i])
    if i + schedule[i][0] > N:
        continue
    arr[i + schedule[i][0]] = max(m + schedule[i][1], arr[i + schedule[i][0]])
    # print(arr)

# print(arr)
print(max(arr))
