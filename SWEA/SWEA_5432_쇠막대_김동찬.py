t = int(input())
for tc in range(t):
    n = list(input())
    count = 0
    for i in range(0, len(n)-1):
        if n[i] == '(' and n[i + 1] == '(':
            count += 1
            L = 0
            R = 0
            for j in range(i, len(n)-1):
                if n[j] == '(' and n[j+1] == ')':
                    count += 1
                elif n[j] == '(' and n[j + 1] == '(':
                    L += 1
                elif n[j] == ')' and n[j+1] == ')':
                    R += 1
                    if L == R:
                        break
    print('#{} {}'.format(tc+1, count))
