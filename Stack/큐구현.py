n = 3
queue = [0] * n
front = -1
rear = -1


# 삽입(rear)
def enQueue(item):
    global rear
    if rear == n-1:
        print('isFULL')
    else:
        rear += 1
        queue[rear] = item


# 삭제(front)
def deQueue():
    global front
    if front == rear:
        print('isEmpty')
    else:
        front += 1
        return queue[front]


print(queue)
enQueue(1)
print(queue)
enQueue(2)
print(queue)
enQueue(3)
print(queue)

# print(deQueue())
# print(queue)
# print(deQueue())
# print(queue)
# print(deQueue())
# print(queue)

while front != rear:
    print(deQueue())