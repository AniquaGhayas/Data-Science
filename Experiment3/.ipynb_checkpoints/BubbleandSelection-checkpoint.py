# A. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                # Swap elements
                a[j], a[j + 1] = a[j + 1], a[j]
    return a

# B. Selection Sort
def selection_sort(arr):
    n = len(arr)
    a = arr.copy()
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # Swap elements
        a[i], a[min_idx] = a[min_idx], a[i]
    return a

# Testing the sorting implementations
test_array = [64, 25, 12, 22, 11]
print("Original Array:", test_array)
print("Bubble Sorted:", bubble_sort(test_array))
print("Selection Sorted:", selection_sort(test_array))