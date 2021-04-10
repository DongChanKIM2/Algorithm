def reverse(arr):
    b = []
    for reverse_num in range(1, len(arr)+1):
        b.append(arr[-reverse_num])
    if arr == b:
        return True


for tc in range(1, 11):
    n = int(input())
    result = [list(input()) for _ in range(100)]
    # result = []
    # for i in range(100):
    #     temp = list(input())
    #     result.append(temp)
    total = 0

    for i in range(0, 100):
        count = 0
        for j in range(0, 100):
            new_result = []
            for k in range(0, 100-j):
                new_result.append(result[i][j+k])
                if reverse(new_result) == 1:
                    count = k+1
                if count > total:
                    total = count

    for i in range(0, 100):
        count = 0
        for j in range(0, 100):
            new_result = []
            for k in range(0, 100-j):
                new_result.append(result[j+k][i])
                if reverse(new_result) == 1:
                    count = k+1
                if count > total:
                    total = count

    print('#{} {}'.format(tc, total))
