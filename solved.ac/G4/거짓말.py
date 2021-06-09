# 0. union&Find 문제로 트리 문제
# 1. Find를 통해 루트를 찾고 Union을 통해 작은 노드 기준으로 묶어주기
# 2. Party들을 전부 1번 작업 수행
# 3. Party list를 하나씩 돌려가면서 True의 부모노드와 겹치는게 있다면 거짓말을 못 하는 것!


def find(child):
    if parent[child] == child:
        return child
    else:
        # 9번줄에서 return 된 걸 받아서 다시 return 해줘야 union에 제대로 들어감
        child = find(parent[child])
        return child


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


N, M = map(int, input().split())
truths = list(map(int, input().split()))[1:]
parties = []
for _ in range(M):
    temp = list(map(int, input().split()))[1:]
    parties.append(temp)
# 루트노드
parent = [i for i in range(N+1)]


# parties 내부의 요소들 중 2명 이상의 사람이 있으면 union&Find 수행
for party in parties:
    if len(party) >= 2:
        for member in range(len(party)-1):
            union(party[member], party[member+1])

# 3. Party list를 하나씩 돌려가면서 멤버의 부모노드가 True의 부모노드와 겹치는게 있다면 거짓말을 못 하는 것!
cnt = 0
for party in parties:
    flag = 0
    for member in party:
        if flag == 0:
            for true in truths:
                if find(member) == find(true):
                    cnt += 1
                    flag = 1
                if flag == 1:
                    break
        else:
            break
print(M - cnt)
