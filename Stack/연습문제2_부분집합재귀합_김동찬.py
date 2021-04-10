def powerset(idx):
    if idx == N:
        count = []
        # print(sel, ":", end=' ')
        total = 0
        for i in range(N):
            if sel[i]:
                total += arr[i]
                count.append(arr[i])
        if total == 10:
            print(count)
            count.append(1)
        # print(count)

    else:
        sel[idx] = 1
        powerset(idx+1)
        sel[idx] = 0
        powerset(idx+1)


N = 10
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sel = [0] * N
# count = []


# if total == 10:
print(powerset(0))
# print(count)

