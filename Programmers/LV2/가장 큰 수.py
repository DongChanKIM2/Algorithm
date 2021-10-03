def solution(numbers):
    numbers.sort(reverse=True)
    if numbers[0] != 0:
        merged = mergesort(numbers)
        mergedStr = list(map(str, merged))
        ans = "".join(mergedStr)
    else:
        ans = '0'
    return ans
    
def mergesort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        mid = len(numbers) // 2
        left_arr = mergesort(numbers[0:mid])
        right_arr = mergesort(numbers[mid:len(numbers)])
        
        l = r = 0
        mergedArr = []
        
        while l < len(left_arr) and r < len(right_arr):
            tmp_left = str(left_arr[l]) + str(right_arr[r])
            tmp_right = str(right_arr[r]) + str(left_arr[l])
            if tmp_left > tmp_right:
                mergedArr.append(left_arr[l])
                l += 1
            elif tmp_left < tmp_right:
                mergedArr.append(right_arr[r])
                r += 1
            elif tmp_left == tmp_right:
                mergedArr.append(left_arr[l])
                l += 1                
                
        mergedArr += left_arr[l:]
        mergedArr += right_arr[r:]
            
        
        return mergedArr