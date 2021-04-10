t = int(input())
for tc in range(t):
    n = int(input())
    result_idx = []
    result = []
    bus_stop = [0] * 5000

    for i in range(n):
        a, b = list(map(int, input().split()))
        for idx in range(a - 1, b):
            bus_stop[idx] += 1

    p = int(input())
    
    #  for문 하나로 줄이기
    for j in range(p):
        c_idx = int(input())
        result_idx.append(c_idx)
    for idx_c in result_idx:
        result.append(bus_stop[idx_c - 1])

# print(result)
    result = map(str, result)
    result = ' '.join(result)
    print('#{} {}'.format(tc+1, result))
