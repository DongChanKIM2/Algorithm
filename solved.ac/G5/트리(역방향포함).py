# 트리문제에서 노드번호에 따라 위로 올라가는게 아닌 내려가는 경우도 있음
# 이러한 경우를 고려해야만 트리 문제를 풀 수 있음


# 최상단으로 올라가면 0(루트노드)를 만나거나 제거된 노드를 만나거나 둘 중 하나일 수 밖에 없음
def dfs(del_num, arr):
    arr[del_num] = -2
    for i in range(N):
        # -2가 루트면 그 밑에 애들도 다 -2로
        if arr[i] == del_num:
            dfs(i, arr)
            
            
N = int(input())
arr = list(map(int, input().split()))
del_node_num = int(input())
# 1. 제거된 노드 밑에 연결된 애들은 다 제거시켜주기
dfs(del_node_num, arr)
ans = 0
# 2. 내가 꼬리인지 아닌지는 내 i(인덱스)가 arr에 포함 되있는지 아닌지만 확인하면 됨
for i in range(N):
    if i not in arr and arr[i] != -2:
        ans += 1
print(ans)