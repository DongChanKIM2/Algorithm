t = int(input())
for tc in range(t):
    n = int(input())
    students = [0] * 200
    for i in range(n):
        x, y = map(int, input().split())
        if y > x:
            for j in range(round(x/2 + 0.1)-1, round(y/2)):
                students[j] += 1
        elif x > y:
            for j in range(round(y/2 + 0.1)-1, round(x/2)):
                students[j] += 1
    print('#{} {}'.format(tc+1, max(students)))
