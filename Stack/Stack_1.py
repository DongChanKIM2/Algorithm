def push(item):
    if len(arr) < 4:
        arr.append(item)


def pop():
    if len(arr) == 0:
        return None
    else:
        return arr.pop(-1)


arr = []
for i in range(5):
    push(i)
    print(arr)

for i in range(3):
    pop()
    print(arr)