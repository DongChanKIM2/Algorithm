# N개의 집이 있고 빨초파 색으로 색칠할 때 비용의 최솟값
# 규칙
# 1. 1번 집의 색과 2번 집의 색은 다르게
# 2. N번 집의 색과 N-1번 집의 색은 다르게
# 3. i는(2부터 N-1까지) 의 색은 i-1, i+1의 색과 다르게
# 4. 사실 3번 조건은 1, 2번 조건을 포함하는 개념
# 5. 정리: idx가 연속으로 중복되면 안 됨
# 6. 시간: 완전탐색으론 대략 2 * N 인데 N = 1000이므로 다른 방법 필요
# 7. 백트랙킹으로는 풀 수 없는 문제 -> 무조건 DP로


def paint(level, idx):
    global ans, temp
    # print(ans, temp, level, idx)
    if temp >= ans:
        return
    if level >= N-1:
        ans = temp
        return
    for i in range(3):
        if i != idx:
            temp += costs[level+1][i]
            paint(level+1, i)
            temp -= costs[level+1][i]


N = int(input())
# 빨 초 파 칠하는 각각의 비용
costs = [list(map(int, input().split())) for _ in range(N)]
# 최대값: 1000 * 1000
ans = 1000001
# level과 색깔 idx가 필요할 듯
for i in range(3):
    temp = costs[0][i]
    paint(0, i)
print(ans)
