t = int(input())
for tc in range(1, t+1):
    k, n, m = list(map(int, input().split(' ')))
    arr = [0] * (n+1)
    bus_stations = list(map(int, input().split(' ')))
    for bus_station in bus_stations:
        arr[bus_station] = 1

    charge = 0
    bus = 0 # 버스 위치

    while True:
        # 버스가 이동할 수 있는 최대 거리 이동
        bus += k
        #  버스가 종점 이상에 갔을 때
        if bus >= n:
            break
        for i in range(bus, bus-k, -1):
            if arr[i] == 1:
                charge += 1
                bus = i
                print(bus)
                break
        else:
            charge = 0
            break

    print('#{} {}'.format(tc, charge))
