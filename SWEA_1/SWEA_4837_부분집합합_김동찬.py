def summary(bit):
    total = 0
    for z in range(len(bit)):
        total += bit[z]
    return total

t = int(input())
for tc in range(t):
    bit = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]


    x, y = list(map(int, input().split()))
    count = 0

    for a in range(2):
        bit[0] = a
        for b in range(2):
            bit[1] = b * 2
            for c in range(2):
                bit[2] = c * 3
                for d in range(2):
                    bit[3] = d * 4
                    for e in range(2):
                        bit[4] = e * 5
                        for f in range(2):
                            bit[5] = f * 6
                            for g in range(2):
                                bit[6] = g * 7
                                for h in range(2):
                                    bit[7] = h * 8
                                    for i in range(2):
                                        bit[8] = i * 9
                                        for j in range(2):
                                            bit[9] = j * 10
                                            for k in range(2):
                                                bit[10] = k * 11
                                                for m in range(2):
                                                    bit[11] = m * 12
                                                    if summary(bit) == y and (a + b + c + d + e + f + g + h + i + j + k + m) == x:
                                                        count += 1
    print('#{} {}'.format(tc+1, count))

