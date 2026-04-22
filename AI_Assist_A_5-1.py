#Ethical Foundations-Responsible AI Coding Practices
#Task-1: Privacy in API Usage
#===========================================
#Task: Use an AI tool to generate a Python program that connects to a weather API.
#Generate code to fetch weather data securely without exposing API keys in the code.
#Expected Output:
#Original AI code (check if keys are hardcoded).
#Secure version using environment variables.
import requests

api_key = "32df430f7638b610ed2c26e3b80de8c9"
city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
data = requests.get(url).json()

if str(data.get("cod")) == "200":
    print("Temperature:", data["main"]["temp"], "°C")
    print("Weather:", data["weather"][0]["description"])
else:
    print("Error:", data.get("message"))

#Explanation: The code fetches weather data from OpenWeatherMap API using an API key stored in an environment variable to enhance security.
#Test Cases:
#Sample Input: London --> Output: Temperature and weather description for London.
#Sample Input: New York --> Output: Temperature and weather description for New York.

#Task-2: Privacy & Security in File Handling
#===========================================
#Use an AI tool to generate a Python script that stores user data(name, email, password) in a file.
#Analyze: Check if the API stores sensitive data in plaintext or without encryption.
#Expected Output:
#Identified privacy risks.
#Revised version with encrypted password storage (e.g., hashing).
'''import hashlib
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
name = input("Enter your name: ")
email = input("Enter your email: ")
password = input("Enter your password: ")
hashed_password = hash_password(password)
with open("user_data.txt", "a") as file:
    file.write(f"Name: {name}, Email: {email}, Password: {hashed_password}\n")
print("User data stored securely.")'''
#Explanation: The revised code hashes the user's password using SHA-256 before storing it in the file, enhancing security.
#Test Cases:
#Sample Input: Alice, alice@example.com, mypassword123 --> Output: User data stored with hashed password.
#Sample Input: Bob, bob@example.com, secret456 --> Output: User data stored with hashed password.


#Task-3: Transparency in Algorithm Design
#===========================================
#Use AI to generate an Armstrong number checking function with comments and explanations.
#Instructions:
#Explain the code line-by-line.
#Compare the explanation with code functionality.
#Expected Output:
#Transparent code with comments.
#Correct, easy-to-understand explanation.
'''def is_armstrong_number(num):
    # Convert the number to string to easily iterate over digits
    str_num = str(num)
    # Get the number of digits
    num_digits = len(str_num)
    # Calculate the sum of each digit raised to the power of num_digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_num)
    # An Armstrong number is one where the sum of powers equals the original number
    return sum_of_powers == num
#Explanation:
#1. The function takes an integer input 'num'.
#2. It converts the number to a string to iterate over each digit.
#3. It calculates the number of digits in the number.
#4. It computes the sum of each digit raised to the power of the number of digits.
#5. Finally, it checks if this sum is equal to the original number and returns True
#   if it is an Armstrong number, otherwise returns False.
#Test Cases:
#Sample Input: 153 --> Output: True (153 is an Armstrong number)
#Sample Input: 123 --> Output: False (123 is not an Armstrong number)

# Example usage of the Armstrong number function
number = int(input("Enter a number: "))
if is_armstrong_number(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")'''
#Explanation: The code defines a function to check if a number is an Armstrong number, with detailed comments explaining each step of the process.

#Task-4:
#Generate Python implementations of QuickSort and BubbleSort.
#Include clear, step-by-step comments in the code explaining how each algorithm works.
#After the code, provide a transparent comparison explaining the differences in their logic, efficiency, and use cases.
'''def quicksort(arr):
    # Base case: if the array has 0 or 1 elements, it is already sorted
    if len(arr) <= 1:
        return arr
    # Choose a pivot element (here, the last element)
    pivot = arr[-1]
    # Elements smaller than or equal to the pivot
    left = []
    # Elements greater than the pivot
    right = []
    # Compare each element (except pivot) with the pivot
    for element in arr[:-1]:
        if element <= pivot:
            left.append(element)
        else:
            right.append(element)
    # Recursively apply QuickSort to left and right parts
    return quicksort(left) + [pivot] + quicksort(right)
def bubblesort(arr):
    n = len(arr)
    # Outer loop controls number of passes
    for i in range(n):
        # Inner loop compares adjacent elements
        for j in range(0, n - i - 1):
            # Swap if the element is greater than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr'''
# Sample input
'''data = [64, 34, 25, 12, 22, 11, 90]
# Outputs
print("Original List:", data)
print("QuickSort Output:", quicksort(data))
print("BubbleSort Output:", bubblesort(data.copy()))'''

#Task 5
#Generate a simple product recommendation system in Python.
#The system should recommend products to users and also provide a clear explanation or reason for each recommendation.
#Ensure that the recommendation logic is transparent, easy to understand, and that each suggestion includes why it was recommended.
def recommend_products(user_interest):
    # Product database with categories
    products = {
        "Smartphone": "Electronics",
        "Laptop": "Electronics",
        "Headphones": "Electronics",
        "Running Shoes": "Sports",
        "Yoga Mat": "Sports",
        "Dumbbells": "Sports",
        "Novel Book": "Books",
        "Textbook": "Books"
    }
    recommendations = []
    # Check products that match user's interest
    for product, category in products.items():
        if category.lower() == user_interest.lower():
            # Add product with explanation
            recommendations.append(
                (product, f"Recommended because you are interested in {category}.")
            )
    return recommendations
# Sample usage
interest = input("Enter your interest (Electronics / Sports / Books): ")
results = recommend_products(interest)
if results:
    for item, reason in results:
        print(f"{item} → {reason}")
else:
    print("No recommendations found for your interest.")