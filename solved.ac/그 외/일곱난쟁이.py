def combination(idx, sidx):
    if sidx == N:
        if sum(sel) == 100:
            for i in sel:
                print(i)
            # print(sel)
        return
    if idx == 9:
        return
    sel[sidx] = numbers[idx]
    combination(idx+1, sidx+1)
    combination(idx+1, sidx)


numbers = []
N = 7
sel = [0] * N
check = [0] * N
for i in range(9):
    numbers.append(int(input()))
combination(0, 0)
