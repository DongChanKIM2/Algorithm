t = int(input())
for tc in range(t):
    n, m, k = map(int, input().split())
    peoples = list(map(int, input().split()))
    peoples.sort()
    status = 'Possible'
    arr = [0] * (peoples[-1] + 1)
    count = 0
    total = 0
    for i in range(len(arr)):
        for people in peoples:
            if i == people:
                count += 1
        if i % m == 0 and i != 0:
            total += k
        arr[i] += total - count
        if arr[i] < 0:
            status = 'Impossible'
            break
    # print(arr)
    print('#{} {}'.format(tc+1, status))
