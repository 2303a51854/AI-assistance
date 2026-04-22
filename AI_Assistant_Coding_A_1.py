# Function-Based Fibonacci Sequence Generator

def generate_fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.

    Args:
        n (int): Number of terms in the Fibonacci sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to n terms.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Iterative Fibonacci Implementation
def fibonacci_iterative(n):
    """
    Generate Fibonacci sequence up to n terms using an iterative approach.

    Args:
        n (int): Number of terms in the Fibonacci sequence.

    Returns:
        list: A list containing the Fibonacci sequence up to n terms.
    """
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

# Recursive Fibonacci Implementation
def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using recursion.

    Args:
        n (int): The position of the Fibonacci number to calculate.

    Returns:
        int: The nth Fibonacci number.
    """
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Input from the user
n = int(input("Enter the number of terms: "))

# Generate and print the Fibonacci sequence
fibonacci_sequence = generate_fibonacci(n)
print(f"Fibonacci sequence up to {n} terms:", fibonacci_sequence)

# Iterative approach
print("Iterative Fibonacci sequence:", fibonacci_iterative(n))

# Recursive approach
print("Recursive Fibonacci sequence:", [fibonacci_recursive(i) for i in range(n)])







# Write a python program to check whether a given number is Armstrong number or not.
#Examples:Input : 153, Output : Armstrong Number
#Input : 370, Output : Armstrong Number
