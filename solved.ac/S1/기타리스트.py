# 가장 어려운 부분: 최소값, 최대값을 구하는게 아니라 미지막 연주곡이 최대값이 되는 경우를 구하는 거라
# 연주곡 수: N / 시작볼륨: S / 최대볼륨: M
# 볼륨값: 0부터 M까지
# 마지막 곡 볼륨을 조절하지 못한다면 -1 출력


N, S, M = map(int, input().split())
volumes = list(map(int, input().split()))

# 모든 곡마다 연주가능한 모든 음량 표시
arr = [[0]*(M+1) for _ in range(N)]
# 초기값
for i in range(1):
    if 0 <= S + volumes[i] <= M:
        arr[i][S + volumes[i]] = 1
    if 0 <= S - volumes[i] <= M:
        arr[i][S - volumes[i]] = 1

for i in range(1, N):
    for j in range(M+1):
        if arr[i-1][j] == 1:
            if 0 <= j + volumes[i] <= M:
                arr[i][j+volumes[i]] = 1
            if 0 <= j - volumes[i] <= M:
                arr[i][j-volumes[i]] = 1
for i in range(M, -1, -1):
    if arr[N-1][i] == 1:
        print(i)
        break
else:
    print(-1)
