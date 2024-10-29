import time
import math

# Modified Linear Search to return all indices of the target
def linear_search(arr, target):
    indices = []
    comparisons = 0
    for i in range(len(arr)):
        comparisons += 1
        if arr[i] == target:
            indices.append(i)
    return indices, comparisons  # Return list of indices and number of comparisons

# Binary Search to find the index of a target in a sorted list
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    
    while left <= right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid, comparisons  # Return the index and number of comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1, comparisons  # Target not found

# Binary Search to find the insertion point for a target in a sorted list
def find_insertion_point(arr, target):
    left, right = 0, len(arr)
    comparisons = 0
    
    while left < right:
        comparisons += 1
        mid = (left + right) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid
            
    return left, comparisons  # Return insertion point index and comparisons

# Jump Search Implementation
def jump_search(arr, target):
    length = len(arr)
    step = int(math.sqrt(length))
    prev = 0
    comparisons = 0
    
    while prev < length and arr[min(step, length)-1] < target:
        comparisons += 1
        prev = step
        step += int(math.sqrt(length))
    
    for i in range(prev, min(step, length)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons  # Return index and comparisons
    
    return -1, comparisons  # Target not found

# Compare performance of different search algorithms
def compare_search_algorithms(arr, target):
    # Linear Search
    start_time = time.time()
    linear_result, linear_comparisons = linear_search(arr, target)
    linear_time = time.time() - start_time
    
    # Binary Search (on sorted array)
    arr_sorted = sorted(arr)
    start_time = time.time()
    binary_result, binary_comparisons = binary_search(arr_sorted, target)
    binary_time = time.time() - start_time
    
    # Jump Search (on sorted array)
    start_time = time.time()
    jump_result, jump_comparisons = jump_search(arr_sorted, target)
    jump_time = time.time() - start_time

    # Insertion Point Search (Binary Search)
    insertion_point, insertion_comparisons = find_insertion_point(arr_sorted, target)

    print(f"Linear Search: Indices {linear_result}, Comparisons: {linear_comparisons}, Time: {linear_time:.6f} seconds")
    print(f"Binary Search: Found at index {binary_result}, Comparisons: {binary_comparisons}, Time: {binary_time:.6f} seconds")
    print(f"Jump Search: Found at index {jump_result}, Comparisons: {jump_comparisons}, Time: {jump_time:.6f} seconds")
    print(f"Insertion Point for {target} in sorted list: Index {insertion_point}, Comparisons: {insertion_comparisons}")

# Test with a larger list
large_list = list(range(10000))
compare_search_algorithms(large_list, 8888)

def main():
    # Create a list of 20 random integers between 1 and 100
    import random
    test_list = [random.randint(1, 100) for _ in range(20)]
    
    print("Original list:", test_list)
    print("Sorted list:", sorted(test_list))
    
    target = random.choice(test_list)  # Choose a random target from the list
    print(f"\nSearching for: {target}")
    
    # Linear Search
    result, comparisons = linear_search(test_list, target)
    print(f"Linear Search: Indices {result}, Comparisons: {comparisons}")
    
    # Binary Search (iterative)
    sorted_list = sorted(test_list)
    result, comparisons = binary_search(sorted_list, target)
    print(f"Binary Search: Found at index {result}, Comparisons: {comparisons}")
    
    # Binary Search to find insertion point
    insertion_point, comparisons = find_insertion_point(sorted_list, target)
    print(f"Insertion Point for {target} in sorted list: Index {insertion_point}, Comparisons: {comparisons}")
    
    # Jump Search
    result, comparisons = jump_search(sorted_list, target)
    print(f"Jump Search: Found at index {result}, Comparisons: {comparisons}")
    
    # Compare performance
    print("\nPerformance Comparison:")
    compare_search_algorithms(list(range(100000)), 99999)

if __name__ == "__main__":
    main()
