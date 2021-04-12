t = int(input())
for tc in range(1, t+1):
    k, n, m = list(map(int, input().split(' ')))
    arr = [0] * (n+1)
    bus_stations = list(map(int, input().split(' ')))
    charge = 0

    # 같은 의미
    bus_stations = [0] + bus_stations + [n]
    # bus_stations.insert(0, 0)
    # bus_stations.append(0)

    # 버스 현재 위치
    last = 0

    # 충전소의 출발점과 도착지 추가해서 +2
    for i in range(1, m+2):
        if bus_stations[i] - bus_stations[i-1] > k:
            charge = 0
            break
        if bus_stations[i] > last + k:
            last = bus_stations[i-1]
            charge += 1

    print('#{} {}'.format(tc, charge))
