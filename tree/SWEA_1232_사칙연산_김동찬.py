for tc in range(10):
    n = int(input())
    arr = [0] * (n + 1)
    # for i in range(n):
    trees = [list(input().split()) for _ in range(n)]
    for i in range(n):
        # print(int(trees[i][0]))
        trees[i][0] = int(trees[i][0])
        # if len(trees[i]) == 2:
        arr[i+1] = trees[i][1]

    # print(arr)
    # print(trees)

    for j in range(n, 0, -1):
        if arr[j] == '-':
            arr[j] = int(arr[int(trees[j-1][2])]) - int(arr[int(trees[j-1][3])])
        elif arr[j] == '+':
            arr[j] = int(arr[int(trees[j-1][2])]) + int(arr[int(trees[j-1][3])])
        elif arr[j] == '/':
            arr[j] = int(arr[int(trees[j - 1][2])]) / int(arr[int(trees[j - 1][3])])
        elif arr[j] == '*':
            arr[j] = int(arr[int(trees[j - 1][2])]) * int(arr[int(trees[j - 1][3])])
    # print(arr)
    print('#{} {}'.format(tc+1, int(arr[1])))
