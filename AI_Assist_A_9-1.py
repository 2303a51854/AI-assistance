'''
AI Assisted Coding - Documentation Generation
Documentation commands:
python -m pydoc filename
python -m pydoc -w filename
python -m pydoc -p 1234
'''
#Documentation Generation -Automatic documentation and code comments:
#Problem 1:
def find_max(numbers):
    return max(numbers)
#Task: Generate documentation for the function in all three formats:
#(a) Docstring
#(b) Inline comments
#(c) Google-style documentation
#Critically compare the three approaches. Discuss the advantages, disadvantages, and suitable use cases of each style.
#Recommend which documentation style is most effective for a mathematical utilities library and justify your answer.
#(a) Docstring
def find_max(numbers):
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers (list): A list of numerical values.
    Returns:
        The maximum value from the list of numbers.
    """
    return max(numbers)
#(b) Inline comments
def find_max(numbers):
    # Use the built-in max function to find the maximum value in the list
    return max(numbers)
#(c) Google-style documentation
def find_max(numbers):
    """
    Finds the maximum value in a list of numbers.

    Args:
        numbers (list): A list of numerical values.
    Returns:
        The maximum value from the list of numbers.
    """    
    return max(numbers)
#Comparison of documentation styles:
#1. Docstring:
#   - Advantages: Provides a clear and structured way to document functions, classes, and modules. It can be easily accessed using help() and is widely supported by IDEs and documentation tools.
#   - Disadvantages: Can become verbose if not written concisely. May require more effort to maintain if the code changes frequently.
#   - Suitable Use Cases: Ideal for documenting functions, classes, and modules in a way that is easily accessible to users and developers.
#2. Inline comments:
#   - Advantages: Provides immediate context and explanations for specific lines of code. Useful for complex logic or non-obvious code sections.
#   - Disadvantages: Can clutter the code if overused. May not provide a comprehensive overview of the function's purpose and usage.
#   - Suitable Use Cases: Best for explaining specific code sections or complex logic that may not be immediately clear from the code itself.
#3. Google-style documentation:
#   - Advantages: Provides a standardized format for documenting code, making it easier to read and understand. It is widely adopted in the industry and supported by many tools.
#   - Disadvantages: Can be more verbose than other styles, especially for simple functions.
#   - Suitable Use Cases: Ideal for larger projects or libraries where consistency and clarity in documentation are important.
#Recommendation:
#For a mathematical utilities library, the most effective documentation style would be the Google-style documentation. This is because it provides a clear and standardized format that can accommodate detailed explanations of mathematical functions, their parameters, and return values. The structured format helps users understand the purpose and usage of each function, which is crucial in a mathematical context where precision and clarity are essential. Additionally, Google-style documentation is widely recognized and supported by various tools, making it easier for developers to maintain and generate comprehensive documentation for the library.


#Problem 2:
def login(user, password, credentials):
    return credentials.get(user) == password
#Task: Generate documentation for the function in all three formats:
#Critically compare the approaches.
#Recommend which style would be most helpful for new developers onboarding a project, and justify your choice.
#(a) Docstring
def login(user, password, credentials):
    """
    Authenticates a user by comparing the provided credentials with stored credentials.

    Args:
        user (str): The username of the user attempting to log in.
        password (str): The password provided by the user.
        credentials (dict): A dictionary containing stored usernames and their corresponding passwords.

    Returns:
        bool: True if the credentials match, False otherwise.
    """
    return credentials.get(user) == password
#(b) Inline comments
def login(user, password, credentials):
    # Check if the provided username exists in the credentials dictionary
    # and if the corresponding password matches the provided password
    return credentials.get(user) == password
#(c) Google-style documentation
def login(user, password, credentials):
    """
    Authenticates a user by comparing the provided credentials with stored credentials.

    Args:
        user (str): The username of the user attempting to log in.
        password (str): The password provided by the user.
        credentials (dict): A dictionary containing stored usernames and their corresponding passwords.

    Returns:
        bool: True if the credentials match, False otherwise.
    """
    return credentials.get(user) == password
#Comparison of documentation styles:
#1. Docstring: Provides a clear and structured way to document the function, making it easy for users to understand its purpose, parameters, and return value. It is easily accessible through help() and supported by IDEs.
#2. Inline comments: Offers immediate context for specific lines of code, which can be helpful for explaining complex logic. However, it may not provide a comprehensive overview of the function's purpose and usage.
#3. Google-style documentation: Similar to docstrings but follows a standardized format that is widely adopted in the industry. It can be more verbose but provides clarity and consistency, especially for larger projects.
#Recommendation:
#For new developers onboarding a project, the Google-style documentation would be most helpful. This is because it provides a clear and standardized format that can accommodate detailed explanations of the function's purpose, parameters, and return values. The structured format helps new developers understand the function's usage and behavior more effectively, which is crucial for onboarding. Additionally, Google-style documentation is widely recognized and supported by various tools, making it easier for new developers to access and maintain the documentation as they become familiar with the codebase.

#Problem 3: Calculator (Automatic Documentation Generation)
#Design a Python module named calculator.py and demonstrate automatic documentation generation.
#calculator.py
def add(a, b):
    """
    Adds two numbers.

    Args:
        a (float): The first number.
        b (float): The second number.

    Returns:
        float: The sum of the two numbers.
    """
    return a + b
def subtract(a, b):
    """Subtracts the second number from the first number.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The difference of the two numbers.
    """    
    return a - b
def multiply(a, b):
    """Multiplies two numbers.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The product of the two numbers.
    """    
    return a * b
def divide(a, b):
    """Divides the first number by the second number.
    Args:
        a (float): The first number.
        b (float): The second number.
    Returns:
        float: The quotient of the two numbers.
    Raises:
        ValueError: If the second number is zero.
    """    
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b
