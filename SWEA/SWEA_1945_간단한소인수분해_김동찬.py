t = int(input())
for i in range(t):
    n = int(input())
    for e in range(0, 8):
        for d in range(0, 10):
            for c in range(0, 12):
                for b in range(0, 16):
                    for a in range(0, 25):
                        if n == (11 ** e) * (7 ** d) * (5 ** c) * (3 ** b) * (2 ** a):
                            print('#{} {} {} {} {} {}'.format(i+1, a, b, c, d, e))

# print(11 ** 7)
# print(7 ** 9)
# print(5 ** 11)
# print(3 ** 15)
# print(2 ** 24)