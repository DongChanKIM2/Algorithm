t = int(input())
for idx in range(t):
    n, m = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    minimum = 0
    maximum = 0

    for value in range(0, m):
        minimum += arr[value]
        maximum += arr[value]

    # temp값 하나랑 인덱스 다시 보기
    # -1, +1 idx로 풀어보기
    for i in range(len(arr) - m + 1):
        new_minimum = 0
        new_maximum = 0
        for j in range(i, m + i):
            new_minimum += arr[j]
            new_maximum += arr[j]
        if minimum >= new_minimum:
            minimum = new_minimum
        if maximum <= new_maximum:
            maximum = new_maximum

    print('#{} {}'.format(idx + 1, maximum - minimum))
