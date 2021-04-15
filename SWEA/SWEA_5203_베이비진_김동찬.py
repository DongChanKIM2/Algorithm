def perm(player, idx, order):
    global ans
    if N == idx:
        triplet(player)
        running(player)
        if flag == 1 and order == 2:
            ans = 2
        elif flag == 1 and order == 1:
            ans = 1
    else:
        for j in range(idx, N):
            player[j], player[idx] = player[idx], player[j]
            perm(player, idx+1, order)
            player[j], player[idx] = player[idx], player[j]


def triplet(arr):
    global flag
    if len(arr) >= 3:
        for tri in range(0, len(arr)-3):
            if arr[tri] == arr[tri+1] == arr[tri+2]:
                flag = 1
            return


def running(arr):
    global flag
    if len(arr) >= 3:
        for r in range(0, len(arr)-3):
            if arr[r] + 2 == arr[r+1] + 1 == arr[r+2]:
                flag = 1
            return


t = int(input())
for tc in range(t):
    arr = list(map(int, input().split()))
    first_player = []
    second_player = []
    flag = 0
    ans = 0
    for i in range(len(arr)):
        if i % 2:
            second_player.append(arr[i])
            N = len(second_player)
            perm(second_player, 0, 2)

        else:
            first_player.append(arr[i])
            N = len(first_player)
            perm(first_player, 0, 1)
        if flag == 1:
            break
    if flag == 0:
        print('#{} {}'.format(tc+1, 0))
    else:
        print('#{} {}'.format(tc+1, ans))
