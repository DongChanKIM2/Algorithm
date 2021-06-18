def KMP(s, p):
    global table
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != p[j]:
            j = table[j-1]
        if s[i] == p[j]:
            if j == len(p) - 1:
                print('find')
                j = table[j]
            else:
                j += 1


def make_table(p):
    global table
    j = 0
    for i in range(1, len(p)):
        while j > 0 and p[i] != p[j]:
            # 왜 j -= 1 이 아니라 이렇게 하는지 좋을지는 abdababc 를 시도해보자
            j = table[j-1]
        if p[i] == p[j]:
            j += 1
            table[i] = j


string = "abcabdababcabb"
pattern = "abdababc"
table = [0] * len(pattern)
make_table(pattern)
KMP(string, pattern)
print(table)