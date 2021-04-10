t = int(input())
for tc in range(t):
    n, m = list(map(int, input().split()))
    result = []
    for i in range(n):
        temp = list(input())
        result.append(temp)

    for j in range(n):
        reverse_result = []
        for k_idx in range(0, n-m+1):
            new_result = []
            for num_k in range(m):
                new_result.append(result[j][k_idx+num_k])
            reverse_result = []
            for k in range(1, m+1):
                reverse_result.append(new_result[-(k)])
            if new_result == reverse_result:
                print('#{}'.format(tc + 1), end=' ')
                for z in new_result:
                    print(z, end='')
                print()

    for k in range(n):
        reverse_result = []
        for k_idx in range(0, n-m+1):
            new_result = []
            for num_k in range(m):
                new_result.append(result[k_idx+num_k][k])
            reverse_result = []
            for i in range(1, m+1):
                reverse_result.append(new_result[-(i)])
            if new_result == reverse_result:
                print('#{}'.format(tc + 1), end=' ')
                for i in new_result:
                    print(i, end='')
                print()







