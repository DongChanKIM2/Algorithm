import math


Row, Col = map(int, input().split())
table = []
for _ in range(Row):
    table.append(input())

ans = -1
for row in range(Row):
    for col in range(Col):
        for rd in range(-Row, Row + 1):
            for cd in range(-Col, Col + 1):
                # 이동이 없으면 고려할 필요가 없음
                if rd == 0 and cd == 0:
                    continue
                string = []
                n = row
                m = col

                # n, m 이 테두리 내부에 있다면 추가
                while (0 <= n < Row) and (0 <= m < Col):
                    string.append(table[n][m])

                    val = math.sqrt(int("".join(string)))
                    # 최대값 교체
                    if val == int(val):
                        ans = max(ans, int(val)**2)

                    # 이동
                    n += rd
                    m += cd
print(ans)


