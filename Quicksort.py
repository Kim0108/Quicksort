# 數字列表
numbers = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]

# 排序程式碼
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)
# 排序
sorted_numbers = quicksort(numbers)
print(sorted_numbers)
