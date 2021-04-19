# 처음에는 리스트로 숫자들을 7개 단위씩 뭉쳐서 append 해주려고 시도했는데
# 백트랙킹 과정에서 7번째 숫자를 지울 때 이상하게 꼬이는 걸 확인함
# 리스트라 그런가..? 파라미터로 들고다니니까 주소가 겹치지 않을 거라고 생각했는데 문자열로 하니까 해결됨
# 리스트를 파라미터로 들고다니는건 지양하다록 해야겠다


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def dfs(start, end, number):
    global numbers
    # print(numbers)
    if len(number) == 7:
        # print(numbers)
        if number in numbers:
            return
        else:
            numbers.append(number)
            return
    for direction in range(4):
        nx = start + dx[direction]
        ny = end + dy[direction]
        if nx >= 4 or ny >= 4 or nx < 0 or ny < 0:
            continue
        number += arr[nx][ny]
        dfs(nx, ny, number)
        number = number[:-1]
    # return numbers


t = int(input())
for tc in range(t):
    numbers = []
    arr = [list(input().split()) for _ in range(4)]
    # 7개를 먼저 temp
    number = ''
    # result

    for i in range(4):
        for j in range(4):
            # 시작점은 전부
            number = ''
            # if (i, j) == (0, 0) or (i, j) == (0, 1):
            number += arr[i][j]
            # print(number)
            dfs(i, j, number)
    print('#{} {}'.format(tc+1, len(numbers)))

