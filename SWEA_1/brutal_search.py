# for i1 in range(1, 5):
#     for i2 in range(1, 5):
#         if i2 != i1:
#             for i3 in range(1, 5):
#                 if i3 != i1 and i3 != i2:
#                     for i4 in range(1, 5):
#                         if i4 != i1 and i4 != i2 and i4 != i3:
#                             print(i1, i2, i3, i4)

N = 3
card = [4, 5, 6]
run = False
tri = False

for i in range(N):
    for j in range(N):
        if j != i:
            for k in range(N):
                if k != i and k != j:
                    print(card[i], card[j], card[k])
                    if card[i] + 1 == card[j] and card[i] + 2 == card[k]:
                        run = True
                    if card[i] == card[j] and card[i] == card[k]:
                        tri = True
                    if run:
                        print("런")
                    if tri:
                        print('트리')
