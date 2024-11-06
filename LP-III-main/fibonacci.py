def recursive_fibonacci(n):
    if n <= 1:
        return n
    return recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2)

def fibonacci_series_recursive(n):
    return [recursive_fibonacci(i) for i in range(n + 1)]

def non_recursive_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fib1, fib2 = 0, 1
    series = [fib1, fib2]
    for i in range(2, n + 1):
        next_fib = fib1 + fib2
        fib1, fib2 = fib2, next_fib
        series.append(next_fib)
    return series

n = int(input("Enter a number to calculate Fibonacci: "))

# Print the nth Fibonacci number
print(f"The {n}th Fibonacci number (Recursive): {recursive_fibonacci(n)}")
print(f"The {n}th Fibonacci number (Non-Recursive): {non_recursive_fibonacci(n)[-1]}")

# Print the entire Fibonacci series up to the nth term
print(f"Fibonacci series up to {n} (Recursive): {fibonacci_series_recursive(n)}")
print(f"Fibonacci series up to {n} (Non-Recursive): {non_recursive_fibonacci(n)}")

