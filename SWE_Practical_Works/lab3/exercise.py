import time
from collections import Counter

def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

def fibonacci_iterative(n):
    fib_sequence = []
    a, b = 0, 1
    while a <= n:
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

def index_of_first_exceeding(value):
    a, b = 0, 1
    index = 0
    while a <= value:
        a, b = b, a + b
        index += 1
    return index

def is_fibonacci(number):
    if number < 0:
        return False
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number

def fibonacci_ratios(n):
    fib_sequence = fibonacci_iterative(n)
    ratios = [fib_sequence[i+1] / fib_sequence[i] for i in range(1, len(fib_sequence) - 1)]
    return ratios

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return result, end - start

# Example usage
n = 30

# Using the recursive Fibonacci function
print("Recursive Fibonacci:")
for i in range(10):
    print(f"F({i}) = {fibonacci_recursive(i)}")

# Using the modified iterative Fibonacci function
print("\nIterative Fibonacci (up to n):")
fib_list = fibonacci_iterative(n)
print(f"Fibonacci numbers up to {n}: {fib_list}")

# Index of the first Fibonacci number exceeding a value
value_to_check = 20
index_exceeding = index_of_first_exceeding(value_to_check)
print(f"\nIndex of the first Fibonacci number exceeding {value_to_check}: {index_exceeding}")

# Check if a number is a Fibonacci number
number_to_check = 21
is_fib = is_fibonacci(number_to_check)
print(f"\nIs {number_to_check} a Fibonacci number? {is_fib}")

# Calculate the ratios between consecutive Fibonacci numbers
ratios = fibonacci_ratios(n)
print("\nRatios of consecutive Fibonacci numbers approaching the golden ratio:")
for ratio in ratios:
    print(ratio)

def fibonacci_memoized(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci_memoized(n-1, memo) + fibonacci_memoized(n-2, memo)
    return memo[n]

memoized_result, memoized_time = measure_time(fibonacci_memoized, n)
print(f"\nMemoized: F({n}) = {memoized_result}, Time: {memoized_time:.6f} seconds")
