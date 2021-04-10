N = 20
queue = [(1, 0)]

new_people = 1
last_people = 0

while N > 0:
    num, cnt = queue.pop(0)
    last_people = num #마지막으로 받으러 온 사람
    cnt += 1 #저번보다 하나 더

    N -= cnt
    new_people += 1

    queue.append((num, cnt))
    queue.append((new_people, 0))
    print(queue)

# print(queue)
print(last_people)

