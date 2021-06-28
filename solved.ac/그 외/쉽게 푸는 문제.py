start, end = map(int, input().split())
arr = [0] * (end+1)
curr_num, curr_idx = 1, 1
for i in range(1, end+2):
    for j in range(curr_num):
        if curr_idx >= end+1:
            break
        arr[curr_idx] = curr_num
        curr_idx += 1
    curr_num += 1
print(sum(arr[start:end+1]))