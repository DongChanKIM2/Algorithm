# 구해야 하는 것: 리프노드(자식의 개수가 0인 노드)
# 중간에 한 노드를 지우면 지운 노드의 하위 노드들은 다 삭제
# 1. 꼬리인지 확인하고 2. 최상단 노드에 도달할 수 있는지 조건 두 개 충족해야함


N = int(input())
arr = list(map(int, input().split()))
del_node_num = int(input())
# 부모가 아예 없도록
arr[del_node_num] = -2


ans = 0
for i in range(len(arr)-1, -1, -1):
    flag = 0
    # 내 밑에 새끼가 더 없는지 확인
    for j in range(i, len(arr)):
        if i == arr[j]:
            flag = 1
            break
    if flag == 0:
        # 무조건 최상단에 올라가거나 중간에 삭제한 노드에서 빠질 수 밖에 없음
        while True:
            # 한단계 위 idx
            upper_idx = arr[i]
            # 처음부터 삭제된 노드
            if upper_idx == -2:
                break
            if upper_idx == -1:
                ans += 1
                break
            # 올라가다가 부모까지 가거나 삭제된 노드 만나는 경우
            if arr[upper_idx] == -1:
                ans += 1
                break
            elif arr[upper_idx] == -2:
                break
            i = upper_idx
print(ans)
