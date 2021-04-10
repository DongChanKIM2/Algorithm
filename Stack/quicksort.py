arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(len(arr))
temp_arr = [[0] * 3 for _ in range(3)]
print(temp_arr)
for i in range(len(arr)):
    for j in range(len(arr)):
        temp_arr[i][j] += arr[i][j]
arr[0][0] += 10
print(arr)
print(temp_arr)

