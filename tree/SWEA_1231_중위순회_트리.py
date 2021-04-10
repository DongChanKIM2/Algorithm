def inorder(root):
    if root == 0:
        return
    else:
        inorder(left[root])
        # for idx in dictionary:
        print(dictionary[root], end='')
        inorder(right[root])


for tc in range(10):
    n = int(input())
    left = [0] * (n+1)
    right = [0] * (n+1)
    dictionary = {}
    for i in range(1, n+1):
        trees = list(input().split())
        dictionary[i] = trees[1]
        if len(trees) == 3:
            if left[int(trees[0])]:
                right[int(trees[0])] = int(trees[2])
            else:
                left[int(trees[0])] = int(trees[2])
        if len(trees) == 4:
            if left[int(trees[0])]:
                right[int(trees[0])] = int(trees[2])
            else:
                left[int(trees[0])] = int(trees[2])
            if left[int(trees[0])]:
                right[int(trees[0])] = int(trees[3])
            else:
                left[int(trees[0])] = int(trees[3])

    # print(left)
    # print(right)
    print('#{} '.format(tc+1), end='')
    inorder(1)
    print()
    # print(dictionary)
    # 1 SOFTWARE
