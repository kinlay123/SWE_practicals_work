import matplotlib.pyplot as plt
import random
import time

# In-place Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Modified Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # Stop if no swaps occurred
            break
    return arr

# Hybrid Merge Sort using Insertion Sort for small subarrays
def merge_sort(arr):
    if len(arr) <= 10:  # Threshold for Insertion Sort
        return insertion_sort(arr)
    
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    return merge(left, right)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def merge(left, right):
    result = []
    i, j = 0, 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Visualization Function
def visualize_sorting(arr, algorithm_name):
    plt.figure(figsize=(10, 6))
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title(f'{algorithm_name} Visualization')
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.show()

# Compare sorting algorithms
def compare_sorting_algorithms(arr):
    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", lambda x: quick_sort(x, 0, len(x) - 1) or x)  # Wrapping in lambda for in-place
    ]
    
    for name, func in algorithms:
        arr_copy = arr.copy()
        start_time = time.time()
        func(arr_copy)
        end_time = time.time()
        print(f"{name} took {end_time - start_time:.6f} seconds")
        visualize_sorting(arr_copy, name)

# Generate a large random array
large_arr = [random.randint(1, 100) for _ in range(50)]

# Compare the algorithms
compare_sorting_algorithms(large_arr)
