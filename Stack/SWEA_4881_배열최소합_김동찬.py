def perm(idx):
    global result
    result = 100000
    count = 0
    new_arr = [0]*n
    if idx == length:
        for index in range(len(permute_arr)):
            new_arr[index] += permute_arr[index]
        for new_arr_idx in range(n):
            count += new_arr[new_arr_idx]
            if count > result:
                break
        if result > count:
            result = count

    else:
        for per_i in range(idx, length):
            permute_arr[idx], permute_arr[per_i] = permute_arr[per_i], permute_arr[idx]
            perm(idx+1)
            permute_arr[idx], permute_arr[per_i] = permute_arr[per_i], permute_arr[idx]
    return result


t = int(input())
for tc in range(t):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    permute_arr = [0] * n
    length = len(permute_arr)
    for i in range(len(permute_arr)):
        permute_arr[i] += i
    final_arr = []
    # result = 10000
    print(perm(0))
    # for i in final_arr:
    #     count = 0
    #     for j in range(len(i)):
    #         count += arr[j][i[j]]
    #         if count >= result:
    #             break
    #     if result > count:
    #         result = count
    # print('#{} {}'.format(tc+1, result))
