t = int(input())
for tc in range(t):
    memory = list(map(int, input()))
    count = 0
    for i in range(len(memory)-1):
        if memory[i] == 0 and memory[i+1] == 1:
            count += 1
        elif memory[i] == 1 and memory[i+1] == 0:
            count += 1
    if memory[0] == 1:
        count += 1
    print('#{} {}'.format(tc+1, count))