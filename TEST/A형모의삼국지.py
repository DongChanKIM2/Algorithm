#1. 땅따먹기 게임
# Rule 1. 산악지대는 무조건 0
# Rule 2. 주병력/보조병력으로 나뉘어져 이씀
# Rule 3. 공격 -> 지원 -> 보충 (1번나라 -> 2번나라 -> 3번나라) 병력이 없다면 skip
# Rule 4. 공격: 내 공격 turn일때 (인접한 상대 나라의 병력 * 5) < (내 나라 병력) 이면 1/4씩 보내서 공격
             # 즉 무조건 침공가능할때만 공격하는 것임
# Rule 5. 지원:
# 5-1. 인접한 국가 중 다른나라가 없으면 인접한 지역으로 1/5 병력 보냄
# 5-2. 인접한 국가 중 다른나라가 있으면 5배 벙력 초과일때만 1/5 병력 보냄
# Rule 6.게임종료: 한 국가만 남았을 때
# 게임순서: 파 -> 초 -> 주

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


# 순서대로 공격하면 공격인원이 나뉘게 됨
# 1. 적군기준으로 사방향탐색해서 공격하는 곳인지 정하고 (attack 함수)
# 2. 아군기준으로 공격을 한번에 해야함 (adjacent_cnt arr)
def attack(which_country):
    for i in range(N):
        for j in range(N):
            conquerd_arr[i][j] = 0

    for i in range(N):
        for j in range(N):
            # 산악지대가아닌 적군의 위치를 찾자
            if arr[i][j] != which_country and arr[i][j] != 0:
                cnt = 0
                for direction in range(4):
                    nx = i + dx[direction]
                    ny = j + dy[direction]
                    if nx >= N or ny >= N or nx < 0 or ny < 0:
                        continue
                    # 적군의 위치에서 사방탐색을 해서 아군의 숫자 찾기
                    if arr[nx][ny] == which_country:
                        cnt += military[nx][ny]
                if cnt > (military[i][j] * 5):
                    conquerd_arr[i][j] = 1


def send(which_country):
    for i in range(N):
        for j in range(N):
            adjacent_cnt_arr[i][j] = 0


    # 병력을 보내는 지점에 몇 번 병력을 보내는지 cnt
    for i in range(N):
        for j in range(N):
            if conquerd_arr[i][j] == 1:
                for direction in range(4):
                    nx = i + dx[direction]
                    ny = j + dy[direction]
                    if nx >= N or ny >= N or nx < 0 or ny < 0:
                        continue
                    if arr[nx][ny] == which_country:
                        adjacent_cnt_arr[nx][ny] += 1
    # 실제 침공부터 하자
    for i in range(N):
        for j in range(N):
            if conquerd_arr[i][j] == 1:
                send_military_cnt = 0
                for direction in range(4):
                    nx = i + dx[direction]
                    ny = j + dy[direction]
                    if nx >= N or ny >= N or nx < 0 or ny < 0:
                        continue
                    if adjacent_cnt_arr[nx][ny] > 0:
                        send_military_cnt += int(military[nx][ny] * (1/4))
                military[i][j] = send_military_cnt - military[i][j]
                # 나라도 바꿔주고
                arr[i][j] = which_country
                # 병력도 바꿔주고
                military[i][j] = int(military[i][j])
    # 보낸 병력도 적용해야지
    for i in range(N):
        for j in range(N):
            if adjacent_cnt_arr[i][j] > 0:
                military[i][j] -= adjacent_cnt_arr[i][j] * int(military[i][j] * (1/4))
                                 # int(((adjacent_cnt_arr[i][j]/4) * military[i][j]))
                military[i][j] = int(military[i][j])
            adjacent_cnt_arr[i][j] = 0
            conquerd_arr[i][j] = 0


# 지원부터 하자(이거하고나서 보충)
# Rule 5. 지원:
# 5-1. 인접한 국가 중 다른나라가 없으면 인접한 지역으로 1/5 병력 보냄
# 5-2. 인접한 국가 중 다른나라가 있으면 5배 벙력 초과일때만 1/5 병력 보냄
# 아... 생각해보니까 5-1, 5-2를 순차적으로 진행하면 안되고 동시에 해야된다.. shit...
# temp_military를 만들어서 5-1, 5-2의 차이를 더해주고 temp_military를 합치는 방향으로 가는게 맞겟다
def advocate(which_country):
    for i in range(N):
        for j in range(N):
            temp_military[i][j] = 0
    # 5-1부터 구현
    for i in range(N):
        for j in range(N):
            if arr[i][j] == which_country:
                flag = 0
                for direction in range(4):
                    nx = i + dx[direction]
                    ny = j + dy[direction]
                    if nx >= N or ny >= N or nx < 0 or ny < 0:
                        continue
                    if arr[nx][ny] == 0:
                        continue
                    if arr[nx][ny] != arr[i][j]:
                        flag = 1
                # 사방에 아군밖에 없는 경우
                cnt = 0
                if flag == 0:
                    # 병력을 다 보내고
                    for direction in range(4):
                        nx = i + dx[direction]
                        ny = j + dy[direction]
                        if nx >= N or ny >= N or nx < 0 or ny < 0:
                            continue
                        if arr[nx][ny] == which_country:
                            temp_military[nx][ny] += int(military[i][j] * 0.2)
                            cnt += 1
                    # 내꺼에서 병력을 빼주자
                    temp_military[i][j] -= int(military[i][j] * 0.2) * cnt
                    # print('---', int(military[i][j] * (0.2)))
                    # temp_military[i][j] = int(temp_military[i][j])
                # 사방중에 적군이 있는 경우
                elif flag == 1:
                    for direction in range(4):
                        nx = i + dx[direction]
                        ny = j + dy[direction]
                        if nx >= N or ny >= N or nx < 0 or ny < 0:
                            continue
                        if arr[nx][ny] == which_country:
                            if military[i][j] > military[nx][ny] * 5:
                                temp_military[nx][ny] += int(military[i][j] * 0.2)
                                # temp_military[nx][ny] = int(temp_military[nx][ny])
                                temp_military[i][j] -= int(military[i][j] * 0.2)
                                # temp_military[i][j] = int(temp_military[i][j])

    for i in range(N):
        for j in range(N):
            military[i][j] += temp_military[i][j]

def suppling():
    for i in range(N):
        for j in range(N):
            military[i][j] += supply[i][j]


# 파: 1, 초: 2, 주: 3
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    military = [list(map(int, input().split())) for _ in range(N)]
    supply = [list(map(int, input().split())) for _ in range(N)]
    # 침략당했다라고 표시할 arr
    conquerd_arr = [[0] * N for _ in range(N)]
    # 침략하려고 공격을 보내는 지점 표시할 arr
    adjacent_cnt_arr = [[0] * N for _ in range(N)]
    # 지원보낼때 적군과 인접한 곳과 아닌곳 합쳐줄 arr
    temp_military = [[0] * N for _ in range(N)]
    ans = 0

    temp = 0
    first = 0
    second = 0
    third = 0
    zero = 0

    while True:
        if first + zero == N ** 2:
            break
        if second + zero == N ** 2:
            break
        if third + zero == N ** 2:
            break

        first = 0
        second = 0
        third = 0
        zero = 0
        execute = 0

        temp += 1
        if temp >= 4:
            temp -= 3
        idx = temp
        for i in range(N):
            for j in range(N):
                if arr[i][j] == idx:
                    execute = 1
        if execute == 1:
            attack(idx)
            send(idx)
            advocate(idx)
            suppling()
        for i in range(N):
            for j in range(N):
                if arr[i][j] == 0:
                    zero += 1
                if arr[i][j] == 1:
                    first += 1
                if arr[i][j] == 2:
                    second += 1
                if arr[i][j] == 3:
                    third += 1

    # print(conquerd_arr)
    # print(adjacent_cnt_arr)
    # print(arr)
    # print(military)
    # print(temp_military)
    for i in range(N):
        for j in range(N):
            ans += military[i][j]
    print('#{} {}'.format(tc+1, ans))
    # print(sum(military))
