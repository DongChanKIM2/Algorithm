# 삭제 없이 추가 기능만 구현해도 해결되는 문제
def heap_push(value):
    global heap_size
    heap_size += 1
    heap[heap_size] = value

    child = heap_size
    parent = heap_size//2

    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        child = parent
        parent = child // 2


t = int(input())
for tc in range(t):
    n = int(input())
    arr = list(map(int, input().split()))

    heap = [0] * (n+1)
    heap_size = 0

    # heap push 함수로 하나씩 추가해줌
    for v in arr:
        heap_push(v)
    print(heap)

    ans = 0

    node = n // 2

    while node:
        ans += heap[node]
        node = node // 2

    # print("#{} {}".format(tc, ans))
