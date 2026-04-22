#Task - 1: Zero Shot Code
#===========================
#Write a python program to find the given year is leap year or not.
'''year = int(input("Enter a year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")'''
#Explanation: A year is a leap year if it is divisible by 4 but not divisible by 100, unless it is also divisible by 400.
#Correct logical conditions: (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
#Test Cases:
#Sample Input: 2020 --> Output: 2020 is a leap year.
#Sample Input: 1900 --> Output: 1900 is not a leap year.

#Task - 2: One Shot Code
#===========================
#Write a python program to convert the centimeters to inches using mathematical formulas. Sample Input: 10cm --> Output: 3.94inches.
'''cm = float(input("Enter length in centimeters: "))
inches = cm/2.54
print(f"{cm} cm is equal to {inches:.2f} inches.")'''
#Python function with correct conversion logic: inches = cm / 2.54
#Accurate calculation: 1 inch = 2.54 centimeters
#Explanation: The program takes input in centimeters, divides it by 2.54 to convert to inches, and prints the result formatted to two decimal places.
#Test Cases:
#Sample Input: 10 --> Output: 10 cm is equal to 3.94 inches.
#Sample Input: 25.4 --> Output: 25.4 cm is equal to 10.00 inches.

#Task - 3: Few Shot Code
#===========================
#Write a python program that accepts a full name as input and formats it as "Last, First".Sample Input1: John Doe --> Output1: Doe, John, Sample Input2: Jane Smith --> Output2: Smith, Jane.
'''full_name = input("Enter full name (First Last): ")
first_name, last_name = full_name.split()
formatted_name = f"{last_name}, {first_name}"
print(formatted_name)'''
#Explanation: The program splits the input string into first and last names, then formats and prints them in "Last, First" order.
#Test Cases:
#Sample Input1: John Doe --> Output1: Doe, John
#Sample Input2: Jane Smith --> Output2: Smith, Jane.

#Task - 4: Zero-Shot vs Few-Shot Comparison
#===========================================
#Use the zero-shot prompting to generate a python program that counts the number of vowels in a given string.
input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
count = sum(1 for char in input_string if char in vowels)
print(f"Number of vowels: {count}")