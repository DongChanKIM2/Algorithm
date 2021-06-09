# 중요했던 점
# 1. 초기값과 달라지면 시간절약을 위해 break
# 2. 전체 숫자가 동일하면 더해주고 아니면 아니면 재귀반복문 돌리는게 시간상 중요


def check(arr, N, start_x, start_y):
    global minus, zero, plus
    temp_minus = 0
    temp_zero = 0
    temp_plus = 0
    same = True
    color = arr[start_x][start_y]
    # 판별작업

    for i in range(start_x, start_x+N):
        for j in range(start_y, start_y+N):
            if arr[i][j] == -1:
                temp_minus += 1
            elif arr[i][j] == 0:
                temp_zero += 1
            elif arr[i][j] == 1:
                temp_plus += 1
            if color != arr[i][j]:
                same = False
                break

    if same:
        if temp_minus == N ** 2:
            minus += 1
        elif temp_zero == N ** 2:
            zero += 1
        elif temp_plus == N ** 2:
            plus += 1
    else:
        # 재귀
        check(arr, int(N//3), start_x, start_y)
        check(arr, int(N//3), start_x, start_y + N//3)
        check(arr, int(N//3), start_x, start_y + (N//3)*2)
        check(arr, int(N//3), start_x + N//3, start_y)
        check(arr, int(N//3), start_x + N//3, start_y + N//3)
        check(arr, int(N//3), start_x + N//3, start_y + (N//3)*2)
        check(arr, int(N//3), start_x + (N//3)*2, start_y)
        check(arr, int(N//3), start_x + (N//3)*2, start_y + N//3)
        check(arr, int(N//3), start_x + (N//3)*2, start_y + (N//3)*2)


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
k = 0
for i in range(1, 8):
    if 3 ** i == N:
        k = i

minus = 0
zero = 0
plus = 0
check(arr, N, 0, 0)
print(minus)
print(zero)
print(plus)
