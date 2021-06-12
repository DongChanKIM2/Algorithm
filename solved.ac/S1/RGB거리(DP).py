N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
# 해당 인덱스의 집을 r, g, b로 칠할때의 비용
dp = [[0, 0, 0] for _ in range(N)]
dp[0][0] = cost[0][0]
dp[0][1] = cost[0][1]
dp[0][2] = cost[0][2]

for i in range(1, N):
    # 빨간색으로 칠하는 경우, 이전이 초록이나 파랑이어야 함 두 경우를 비교
    # 두 경우중 값이 작은 것을 선택하고 그 값에 현재 집을 색칠하는 비용 누적
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + cost[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + cost[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + cost[i][2]

print(min(dp[N - 1]))
