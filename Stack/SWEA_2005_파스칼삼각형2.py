T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    triangle = []
    for i in range(N):
        triangle.append([1] * (i + 1))

    print(triangle)

    for i in range(2, N):
        for j in range(1, i):
            triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
    print(triangle)

    print('#{}'.format(tc))
    for i in range(N):
        print(*triangle[i])
