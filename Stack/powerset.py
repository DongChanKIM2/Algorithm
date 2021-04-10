N = 3
arr = [1, 2, 3]
sel = [0] * N


def powerset(idx):
    if idx == N:
        count = 0
        print(sel, ":", end=' ')
        for i in range(N):
            if sel[i]:
                print(arr[i], end=' ')
                count += arr[i]
        print(count)
        return
    else:
        sel[idx] = 1
        powerset(idx+1) #여기로 다시 돌아온다 첫번째 return
        sel[idx] = 0
        powerset(idx+1) # 두번째 return

powerset(0)

