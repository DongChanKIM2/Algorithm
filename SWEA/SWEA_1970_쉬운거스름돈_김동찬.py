t = int(input())
for tc in range(t):
    moneys = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    moneys_cnt = [0, 0, 0, 0, 0, 0, 0, 0]
    how_much = int(input())
    for i in range(len(moneys)):
        if how_much >= moneys[i]:
            mod = how_much // moneys[i]
            moneys_cnt[i] = mod
            how_much -= (mod * moneys[i])
    print('#{}'.format(tc+1))
    print(*moneys_cnt)
