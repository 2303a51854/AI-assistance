#Code Review and Quality :
#Task-1: AI-Assisted Bug Detection
'''def factorial(n):
    result = 1
    for i in range(1, n): 
        result = result*i
    return result'''
#Identify the logical bug in the code
#The logical bug in the code is that the loop should iterate from 1 to n (inclusive) instead of 1 to n-1. The correct code should be:
'''def factorial(n):
    result = 1
    for i in range(1, n + 1): 
        result = result * i
    return result

if __name__ == "__main__":
    test_value = int(input("Enter a number: "))  # Example input
    print(f"Factorial of {test_value} is :{factorial(test_value)}")

#Why the bug occurs:
#The bug occurs because the loop is not including the value of n in the multiplication. 
# The loop should iterate up to n to calculate the factorial correctly, but it stops at n-1, resulting in an incorrect calculation of the factorial.
#Provide a corrected version of the code:
def factorial(n):
    result = 1
    for i in range(1, n + 1): 
        result = result * i
    return result
#Compare the corrected code with the original code
#The original code iterates from 1 to n-1, which means it does not include n in the calculation of the factorial.
#The corrected code iterates from 1 to n (inclusive), which ensures that n is included in the calculation, resulting in the correct factorial value.
'''
#Task-2: Improving Readability and Documentation
'''def calc(a, b, c):
    if c == "add":
        return a+b
    elif c == "sub":
        return a-b
    elif c == "mul":
        return a*b
    elif c == "div":'''
#Critique the function's readability, parameter naming, and lack of documentation.
#Rewrite the function with:
#1. Descriptive function and parameter names.
#2. A complete docstring(description, parameters,return value, examples).
#3. Exception handling for division by zero.
#4. Consideration of input validation.
'''def calculate(num1, num2, operation):
    """
    Perform basic arithmetic operations on two numbers.

    Parameters:
    num1 (float): The first number.
    num2 (float): The second number.
    operation (str): The operation to perform. 
                     Valid values are "add", "subtract", "multiply", "divide".

    Returns:
    float: The result of the arithmetic operation.

    Raises:
    ValueError: If an invalid operation is provided.
    ZeroDivisionError: If division by zero is attempted.

    Examples:
    >>> calculate(10, 5, "add")
    15
    >>> calculate(10, 5, "subtract")
    5
    >>> calculate(10, 5, "multiply")
    50
    >>> calculate(10, 5, "divide")
    2.0
    >>> calculate(10, 0, "divide")
    Traceback (most recent call last):
        ...   ZeroDivisionError: Cannot divide by zero.
    >>> calculate(10, 5, "modulus")
    Traceback (most recent call last):
        ...   ValueError: Invalid operation. Supported operations are: add, subtract, multiply, divide.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return num1 / num2
    else:
        raise ValueError("Invalid operation. Supported operations are: add, subtract, multiply, divide.")

#Comparision of the original and rewritten code:
#The original code has non-descriptive function and parameter names, lacks documentation, and does not handle exceptions or validate input.
#The rewritten code has a descriptive function name (calculate) and parameter names (num1, num2, operation). 
#It includes a comprehensive docstring that describes the function's purpose, parameters, return value, and examples.
#Valid and invalid inputs(e.g., division by zero and non-string operations).
#The rewritten code also includes exception handling for division by zero and invalid operations, improving the robustness of the function.
'''

#Task-3: Enforcing Coding Standards(PEP8 compliance).
'''def Checkprime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True'''
#List all PEP8 violations in the code.
#1. Function name should be in lowercase with words separated by underscores (check_prime).
#2. There should be a space around the modulus operator (%).
#3. The function should include a docstring describing its purpose, parameters, and return value.
#4. The function should handle edge cases (e.g., numbers less than 2).
#Refactor the code(function name, spacing, indentation, naming).
'''def check_prime(n):
    """
    Check if a number is prime.

    Parameters:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is prime, False otherwise.
    """
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
#Compare the original and refactored code.
#The original code has a function name that does not follow PEP8 naming conventions (Checkprime). 
#The refactored code has a function name that follows PEP8 naming conventions (check_prime).
#The original code does not have a docstring, while the refactored code includes a comprehensive docstring that describes the function's purpose, parameters, and return value.
#The original code does not handle edge cases (e.g., numbers less than 2), while the refactored code includes a check for numbers less than 2, returning False for those cases.

if __name__ == "__main__":
    # Test Task-3: Check if a number is prime
    test_number = int(input("Enter a Number: "))  # Example input
    print(f"Is {test_number} a prime number? {check_prime(test_number)}")
'''

#Task-4: AI as a Code Reviewer in Real Projects:
'''def processData(d):
    return[x*2 for x in d if x%2==0]'''
#Reviewing the function for:
#1. Readability and naming:
#The function name (processData) is not descriptive of what the function does.
#The parameter name (d) is not descriptive of the data it represents.
#2. Reusability and modularity:
#The function is not modular as it combines data processing and filtering in a single line, making it less reusable for different types of data processing.
#3. Edge cases(non-list input,empty list, non-integer elements):
#The function does not handle edge cases such as non-list input, empty list, or non-integer elements, which could lead to errors or unexpected behavior.

#Generate a code covering(Better naming and function purpose clarity, Input validation and type hints and Suggestions for generalization(e.g., configurable multiplier)).
'''from typing import List, Union 
def process_data(data: List[Union[int, float]], multiplier: int = 2) -> List[Union[int, float]]:
    """
    Process a list of numbers by filtering out odd numbers and multiplying even numbers by a specified multiplier.

    Parameters:
    data (List[Union[int, float]]): A list of integers or floats to be processed.
    multiplier (int): The value by which to multiply the even numbers. Default is 2.

    Returns:
    List[Union[int, float]]: A list of processed numbers where even numbers are multiplied by the multiplier and odd numbers are filtered out.

    Raises:
    ValueError: If the input data is not a list or contains non-numeric elements.
    """
    if not isinstance(data, list):
        raise ValueError("Input data must be a list.")
    
    processed_data = []
    for x in data:
        if isinstance(x, (int, float)):
            if x % 2 == 0:
                processed_data.append(x * multiplier)
        else:
            raise ValueError("All elements in the input list must be integers or floats.")
    
    return processed_data
#Refactoring the function based on AI feedback:
#The refactored function has a more descriptive name (process_data) and parameter names (data, multiplier).
#It includes a comprehensive docstring that describes the function's purpose, parameters, return value, and exceptions.
#The function now includes input validation to ensure that the input data is a list and that all elements are numeric (integers or floats).
#The function is more modular and reusable, allowing for a configurable multiplier instead of hardcoding the value of 2.
if __name__ == "__main__":
    # Test Task-4: Process a list of numbers
    test_data = [1, 2, 3, 4, 5, 6]  # Example input
    print(f"Processed data: {process_data(test_data)}")'''

#Task-5: AI-Assisted Performance Optimization:
'''def sum_of_squares(numbers):
    total = 0
    for num in numbers:
        total += num**2
    return total
#Test the function with a large list(e.g.,range(1000000)).
if __name__ == "__main__":
    large_list = range(1000000)  # Example input
    print(f"Sum of squares: {sum_of_squares(large_list)}")'''

#Time complexity: O(n)
#Suggest performance improvements(e.g., using built-in functions, vectorization with NumPy if applicable).
import numpy as np
def sum_of_squares(numbers):
    """
    Calculate the sum of squares of a list of numbers.

    Parameters:
    numbers (List[Union[int, float]]): A list of integers or floats.

    Returns:
    Union[int, float]: The sum of squares of the input numbers.
    """
    return np.sum(np.square(numbers))
#The refactored function uses NumPy's vectorized operations to calculate the sum of squares, which is typically faster than a for loop for large lists of numbers.
if __name__ == "__main__":
    large_list = np.array(range(1000000))  # Convert range to NumPy array
    print(f"Sum of squares: {sum_of_squares(large_list)}")

#Optimized version:
#The optimized version of the function uses NumPy's vectorized operations to calculate the sum of squares, which is typically faster than a for loop for large lists of numbers.
#Execution time comparison:
#Before optimization: The original function using a for loop may take significantly longer to execute, especially as the size of the input list increases (e.g., range(1000000)).
#After optimization: The refactored function using NumPy's vectorized operations should execute much faster, even for large input sizes, due to the efficiency of NumPy's underlying implementations.
