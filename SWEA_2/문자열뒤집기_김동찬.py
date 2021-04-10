a = list(input())
b = []

# 1번 방법
while len(a) > 0:
    b.append(a[-1])
    a.pop()
for i in range(len(b)):
    print(b[i], end='')

# 2번 방법
for i in range(len(a)//2):
    a[i], a[len(a)-i-1] = a[len(a)-i-1], a[i]
print(a)