# C. Linear Search
def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

# D. Binary Search
def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Testing the searching implementations
search_list = [11, 12, 22, 25, 64] 
target = 22

print("Array:", search_list, "| Target:", target)
print("Linear Search Index:", linear_search(search_list, target))
print("Binary Search Index:", binary_search(search_list, target))