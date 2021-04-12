queue = [0] * 4
queue_size = len(queue)
front = rear = 0


def enqueue(item):
    global rear
    if (rear + 1) % queue_size == front:
        print('isFull')
    else:
        rear = (rear + 1) % queue_size
        queue[rear] = item


def dequeue():
    global front
    if front == rear:
        print('isEmpty')
    else:
        front = (front + 1) % queue_size
        return queue[front]


enqueue(1)
enqueue(2)
enqueue(3)
enqueue(4)
print(queue)
print(dequeue())

