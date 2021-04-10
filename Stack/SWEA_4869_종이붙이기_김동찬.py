n = int(input())
# size = [n, 20]
pieces = [[10, 20], [20, 10], [20, 20]]
temp = []
pieces_order = []
x = 0
y = 0

for i in range(100000):
    i %= 3
    x += pieces[i][0]
    y += pieces[i][1]
    temp.append(i)

    if y < 20:
        y += pieces[i][1]
        temp.append(i)

    if x > n or y > 20:
        x, y = 0, 0
        temp = []

    if x == n and y == 20 and temp not in pieces_order:
        pieces_order.append(temp)
        temp = []
        x, y = 0, 0

    if y == 20:
        y = 0

print(pieces_order)
print(len(pieces_order))
