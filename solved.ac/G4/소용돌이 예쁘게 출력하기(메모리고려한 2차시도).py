# 메모리를 고려하면 배열 전체를 저장하는 게 아니라 정확히 내가 필요한 직사각형 부분만 저장
# 우 상 좌 하 순서대로 2번 방향 회전하면 이동거리가 1씩 증가
# 전체 순회를 하면서 필요한 부분만 저장을 하도록 변경했지만 결국 런타임 에러.......


dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
r1, c1, r2, c2 = map(int, input().split())
# 정사각형 중 가장 큰 값
maximum_len = max(abs(r1), abs(c1), abs(r2), abs(c2))
# r1, c1 은 r2, c2보다 항상 더 작으므로 음수값이 하나라도 있으면 최대값을 더해줘서
# 좌상단 좌표를 0,0 으로 맞춰주기
if r1 < 0 or c1 < 0:
    r2 += maximum_len
    r1 += maximum_len
    c2 += maximum_len
    c1 += maximum_len
# # 정확히 정답만 담을 arr 생성 및 개수
arr = [[0] * (c2-c1+1) for _ in range(r2-r1+1)]
cnt = (c2-c1+1) * (r2-r1+1)
# # 정사각형 순회할 index 시작점(0)
x = y = maximum_len
# 처음 이동거리는 1이고 방향 전환 2번하면 이동거리가 1씩 증가
# 1을 찍고 시작하므로 이동과 방향전환은 1로 설정
maximum_move = 1
move = 0
curr_dir = 0
dir_change = 0
# 하나씩 증가하는 값
curr = 1
# 이쁘게 출력해주기 위해 최대값
pretty_maximum = 0
while cnt > 0:
    # 해당 범위내일때
    if r1 <= x <= r2 and c1 <= y <= c2:
        arr[x][y] = curr
        cnt -= 1
        if arr[x][y] > pretty_maximum:
            pretty_maximum = arr[x][y]
    # 위치 이동
    move += 1
    nx = x + dx[curr_dir]
    ny = y + dy[curr_dir]
    x, y = nx, ny
    curr += 1
    # 방향전환 및 최대 이동거리 담당
    if move == maximum_move:
        move = 0
        dir_change += 1
        curr_dir += 1
        if dir_change == 2:
            maximum_move += 1
            dir_change = 0
        # 우상좌하 한바퀴 돌면 다시 우상좌하 반복
        if curr_dir == 4:
            curr_dir -= 4


pretty_maximum_len = len(str(pretty_maximum))
for i in range(r1, r2 + 1):
    for j in range(c1, c2 + 1):
        num = arr[i][j]
        num_len = len(str(num))
        # print(num, pretty_maximum_len, num_len)
        if pretty_maximum_len > num_len:
            print(' ' * (pretty_maximum_len - num_len), end='')
            print(arr[i][j], end=' ')
        else:
            print(arr[i][j], end=' ')
    print()
# print(arr)
