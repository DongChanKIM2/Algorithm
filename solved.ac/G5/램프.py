# 1. 완전탐색 문제라 모든 열을 껏다 켯다 반복하는 방법을 생각해봤지만 1000번이므로 당연히 범위초과
# 2. 그렇다면 한 행을 기준으로 잡아서 한 행을 완전히 키면 다른 행도 기준 행과 완전히 동일해야만 완전히 켜짐
# 3. 한 행을 완전히 키려면 0의 수보다 K가 이상이어먄 하고, 홀수면 홀수, 짝수면 짝수로 매칭이 되어야함


# N: 행 / M: 열
N, M = map(int, input().split())
lamps = [list((input())) for _ in range(N)]
# 열을 스위치를 누를 수 있는 수(중복가능) (범위: 0 <= K <= 1000) 단순히 생각하면 1000번
k = int(input())

ans = 0

for i in range(N):
    zero = 0
    for j in lamps[i]:
        if j == '0':
            zero += 1
    same_col = 0
    if k >= zero and zero % 2 == k % 2:
        for j in range(N):
            if lamps[i] == lamps[j]:
                same_col += 1
    if same_col > ans:
        ans = same_col
print(ans)