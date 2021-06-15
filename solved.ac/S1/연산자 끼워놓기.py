def perm(level):
    global maximum, minimum
    if level >= N-1:
        init = 0
        if arr[0] == '+':
            init = numbers[0] + numbers[1]
        elif arr[0] == '-':
            init = numbers[0] - numbers[1]
        elif arr[0] == '*':
            init = numbers[0] * numbers[1]
        elif arr[0] == '/':
            init = numbers[0] // numbers[1]
        for i in range(1, N-1):
            if init >= 0:
                if arr[i] == '+':
                    init += numbers[i + 1]
                elif arr[i] == '-':
                    init -= numbers[i + 1]
                elif arr[i] == '*':
                    init *= numbers[i + 1]
                elif arr[i] == '/':
                    init //= numbers[i + 1]
            elif init < 0:
                if arr[i] == '+':
                    init += numbers[i + 1]
                elif arr[i] == '-':
                    init -= numbers[i + 1]
                elif arr[i] == '*':
                    init *= numbers[i + 1]
                elif arr[i] == '/':
                    init = abs(init)
                    init //= numbers[i + 1]
                    init = -init
        if init > maximum:
            maximum = init
        if init < minimum:
            minimum = init
        return
    else:
        for i in range(N-1):
            if visited[i] == 0:
                arr[level] = operator_cnt[i]
                visited[i] = 1
                perm(level + 1)
                visited[i] = 0
                arr[level] = 0


N = int(input())
numbers = list(map(int, input().split()))
operator = list(map(int, input().split()))
operator_cnt = []
for i in range(4):
    if i == 0:
        for _ in range(operator[0]):
            operator_cnt += '+'
    elif i == 1:
        for _ in range(operator[1]):
            operator_cnt += '-'
    elif i == 2:
        for _ in range(operator[2]):
            operator_cnt += '*'
    elif i == 3:
        for _ in range(operator[3]):
            operator_cnt += '/'

minimum = 100000000000
maximum = -100000000000
arr = [0] * (N - 1)
visited = [0] * (N - 1)
perm(0)
print(maximum)
print(minimum)
