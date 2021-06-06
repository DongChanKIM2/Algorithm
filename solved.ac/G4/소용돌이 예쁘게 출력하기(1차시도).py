# 1. 정사각형 모눈종이로 0,0 에서 1로 시작해서 반시계모양으로 숫자 채워놓기
# 2. 10000 * 10000 = 1억 => 연산을 할 수 있을 거 같기도하고 못할 거 같기도 한 애매한 숫자
# 3. 1번 이동 후 i이동, 방향 전환 후 i이동
# 우 상 좌 좌 하 하 우 우 우 상 상 상 좌 좌 좌 좌 하 하 하 하 우 우 우 우 우
# 4. 3번처럼 오름차순으로 풀려했으나 내림차순으로 하는게 나을 거 같아서 전환
# 5. 좌 상 우 하
# 6. 2번에서 우려한듯이 전체 배열을 저장하니 메모리초과가 발생.....
# 7. 순회는 전체를 하되 정말 필요한 부분만 빼서 저장을 해야하는게 point(귀찮아서 정사각형으로 했는데 직사각형으로 전환)


dx = [0, -1, 0]
dy = [-1, 0, 1]
r1, c1, r2, c2 = map(int, input().split())
# 우선 r1, r2, c1, c2 중 절대값으로 큰 기준으로 배열을 만들어보자
biggest = max(abs(r1), abs(r2), abs(c1), abs(c2))
arr = [[0] * (biggest * 2 + 1) for _ in range(biggest * 2 + 1)]
# cnt 만큼 arr 를 돌면서 숫자 삽입
cnt = (biggest * 2 + 1) ** 2
# print(biggest, cnt)

if r1 < 0:
    r2 -= r1
    r1 = 0
if c1 < 0:
    c2 -= c1
    c1 = 0

if biggest == 0:
    print(1)
else:
    # 제일 큰 수 지정
    arr[biggest * 2][biggest * 2] = cnt
    curr_x, curr_y = biggest * 2, biggest * 2
    # 3번 테두리 감싸주기
    for direction in range(3):
        for j in range(biggest * 2):
            nx = curr_x + dx[direction]
            ny = curr_y + dy[direction]
            cnt -= 1
            arr[nx][ny] = cnt
            curr_x, curr_y = nx, ny
    biggest = biggest * 2 - 1
    # 2번씩 반복적으로 끝까지 감싸주기
    while cnt > 1:
        # 하 좌 반복
        for i in range(biggest):
            nx = curr_x + 1
            ny = curr_y
            cnt -= 1
            # print(nx, ny)
            arr[nx][ny] = cnt
            curr_x = nx
        for i in range(biggest):
            nx = curr_x
            ny = curr_y - 1
            cnt -= 1
            arr[nx][ny] = cnt
            curr_y = ny
        if cnt == 1:
            break
        biggest -= 1
        # 상 우 반복
        for i in range(biggest):
            nx = curr_x - 1
            ny = curr_y
            cnt -= 1
            # print(nx, ny)
            arr[nx][ny] = cnt
            curr_x = nx
        for i in range(biggest):
            nx = curr_x
            ny = curr_y + 1
            cnt -= 1
            arr[nx][ny] = cnt
            curr_y = ny
        if cnt == 1:
            break
        biggest -= 1

    if r1 < 0:
        r2 -= r1
        r1 = 0
    if c1 < 0:
        c2 -= c1
        c1 = 0

    maximum = 0
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if arr[i][j] > maximum:
                maximum = arr[i][j]
    maximum = str(maximum)
    maximum_len = len(maximum)

    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            num = arr[i][j]
            num = str(num)
            num_len = len(num)
            if maximum_len > num_len:
                print(' ' * (maximum_len - num_len), end='')
                print(arr[i][j], end=' ')
            else:
                print(arr[i][j], end=' ')
        print()


