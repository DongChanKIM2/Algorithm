# 1. 숫자를 모두 이어붙이고 나서 가장 큰 제곱수 되는 걸 찾기
# 2. 제곱수가 없다면 -1 출력
# 3. 큰 숫자대로 정렬해서 순열로 풀면 될듯
# 4. 인줄 풀었지만 문제 의도가 다르다. 문제 말이 이상해 ㅡㅡ
# 5. 행열 인덱스가 등차수열인 경우에만 성립하는 거 ex) (2,3)(2,1) 일땐 o (2,1)(2,3)(2,2) 는 성립x


def perm(level):
    global ans
    if level >= N:
        temp_ans = 0
        for i in range(len(arr)-1, -1, -1):
            temp_ans += arr[i] * (10 ** (len(arr) - i - 1))
        if temp_ans ** 0.5 == int(temp_ans ** 0.5):
            print('temp:', arr, temp_ans)
        return
    else:
        for i in range(N):
            if visited[i] == 1:
                continue
            else:
                visited[i] = 1
                arr[level] = temp[i]
                perm(level + 1)
                arr[level] = 0
                visited[i] = 0
    pass


N, M = map(int, input().split())
# arr = []
temp = []
for _ in range(N):
    numbers = int(input())
    for _ in range(M):
        divide = numbers % 10
        temp.append(divide)
        numbers //= 10
temp.sort()
temp.reverse()
# 내가 실제로 출력하고 싶은 길이와 배열 및 방문체크 배열
N = len(temp)
arr = [0] * N
visited = [0] * N
ans = 0
for i in range(N):
    perm(i)
