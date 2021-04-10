arr = [1, 2, 3]
N = 3


def perm(idx):
    if idx == N:
        print(arr)
    else:
        for i in range(idx, N):
            # 순서를 바꾸고
            arr[idx], arr[i] = arr[i], arr[idx]
            perm(idx+1)
            # 원상복귀
            arr[idx], arr[i] = arr[i], arr[idx]
perm(0)
answer = [0, 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712, 365596]
print(len(answer))