# Assignment – Code Translation: Converting Between Programming Languages

"""Task 1 – JavaScript to Python (Array Processing Logic)
Scenario
A frontend application written in JavaScript processes user scores. The
backend team wants the same logic implemented in Python for analytics
processing.
Task
Translate a JavaScript function that:
• Takes an array of numbers
• Filters values greater than 50
• Returns the average of filtered values
Instructions
• Prompt AI to convert JavaScript array methods (filter, reduce) into
  equivalent Python logic.
• Ensure list comprehension or Pythonic style is used.
• Compare outputs of both implementations with sample input.
• Document differences in handling arrays between JS and Python.
Expected Output
• Equivalent Python function.
• Same output for identical inputs.
• Clean and Pythonic implementation.
"""

# Python function to calculate average of numbers above 50
def average_above_50(arr):
    filtered = [num for num in arr if num > 50]
    total = sum(filtered)
    return total / len(filtered) if filtered else 0

# Example
print("Python Output:")
print(average_above_50([30, 60, 80, 40, 100]))  # Output: 80


"""Task 2 – Python OOP to C++ Class Translation
Scenario
A data modeling module is written in Python using OOP. The system is being
migrated to a high-performance C++ environment.
Task
Translate a Python class that:
• Contains private attributes
• Uses getter/setter methods
• Includes a method that calculates a derived value
Instructions
• Convert the Python class into a C++ class.
• Ensure:
  o Proper access modifiers
  o Constructor handling
  o Correct data types
• Compile and test the C++ version.
• Compare how encapsulation differs between Python and C++.
Expected Output
• Fully working C++ class equivalent to Python version.
• Proper use of access specifiers (private, public).
"""

# Python class for data modeling
class DataModel:
    def __init__(self, value):
        self.__value = value  # Private attribute

    def get_value(self):
        return self.__value  # Getter method

    def set_value(self, new_value):
        self.__value = new_value  # Setter method

    def calculate_derived(self):
        return self.__value * 2  # Method to calculate derived value

# Example usage
print("\nPython Class Output:")
data = DataModel(10)
print(data.get_value())  # Output: 10
print(data.calculate_derived())  # Output: 20


# C++ equivalent code
print("\nC++ Equivalent Code:")
print("""
#include <iostream>
using namespace std;

class DataModel {
private:
    int value;

public:
    DataModel(int v) : value(v) {}

    int getValue() const {
        return value;
    }

    void setValue(int v) {
        value = v;
    }

    int calculateDerived() const {
        return value * 2;
    }
};

int main() {
    DataModel data(10);
    cout << data.getValue() << endl;  // Output: 10
    cout << data.calculateDerived() << endl;  // Output: 20
    return 0;
}
""")


"""Task 3 – REST API Call Translation: Python to JavaScript
Scenario
A backend developer wrote an API request using Python requests. The
frontend team needs the same functionality in JavaScript (Fetch API).
Task
Translate Python API request code into JavaScript.
Instructions
• Convert:
  o GET request logic
  o JSON parsing
  o Error handling (try-except → try-catch)
• Ensure proper async/await usage in JavaScript.
• Compare differences in error handling mechanisms.
Expected Output
• Equivalent JavaScript code using Fetch API.
• Proper async handling.
• Similar output structure.
"""

# Python API request
import requests

try:
    response = requests.get("https://api.example.com/data")
    response.raise_for_status()  # raises HTTPError if status != 200
    data = response.json()
    print(data)
except requests.exceptions.RequestException as e:
    print("Error:", e)


# JavaScript equivalent code
print("\nJavaScript Equivalent Code:")
print("""
async function fetchData() {
  try {
    const response = await fetch("https://api.example.com/data");

    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }

    const data = await response.json();
    console.log(data);
  } catch (error) {
    console.error("Error:", error);
  }
}

// Example usage
fetchData();
""")


"""Task 4 – SQL Aggregation to MongoDB Query Translation
Scenario
A company is migrating from relational databases (SQL) to MongoDB
(NoSQL).
Task
Translate an SQL aggregation query into a MongoDB aggregation pipeline.
Example Logic:
• Group records by category
• Calculate average price
• Filter groups where average price > threshold
Instructions
• Provide SQL query to AI.
• Generate equivalent MongoDB query.
• Explain differences between relational and document-based querying.
• Validate results conceptually.
Expected Output
• Working MongoDB aggregation query.
• Clear understanding of grouping and aggregation differences.
"""

# SQL Query
print("\nSQL Query:")
print("""
SELECT category, AVG(price) AS avg_price
FROM products
GROUP BY category
HAVING AVG(price) > 100;
""")

# MongoDB Query
print("\nMongoDB Query:")
print("""
db.products.aggregate([
  {
    $group: {
      _id: "$category",              // group by category
      avg_price: { $avg: "$price" }  // calculate average
    }
  },
  {
    $match: {
      avg_price: { $gt: 100 }        // filter groups
    }
  }
]);
""")


"""Task 5 – Real-Time Application: Algorithm Translation Across Three
Languages
Scenario
A tech company maintains codebases in multiple languages (Python, Java, and
Go). A common algorithm must be implemented consistently across systems.
Task
Choose an algorithm (e.g., binary search, palindrome check, prime number
checker) and translate it across:
• Python
• Java
• One additional language (Go / C# / JavaScript)
Instructions
• Ensure logic remains identical across languages.
• Handle:
  o Data types
  o Loop differences
  o Input/output handling
• Test each version with same input values.
• Briefly document translation challenges.
Expected Output
• Three equivalent working implementations.
• Clear logical consistency.
• Understanding of syntactic vs structural differences.
"""

# Python implementation of binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Test
print("\nPython Binary Search Output:")
print(binary_search([1, 3, 5, 7, 9], 7))  # Output: 3


# Java implementation of binary search
print("\nJava Binary Search Code:")
print("""
public class BinarySearch {
    public static int binarySearch(int[] arr, int target) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = (left + right) / 2;
            if (arr[mid] == target) {
                return mid;
            } else if (arr[mid] < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {1, 3, 5, 7, 9};
        System.out.println(binarySearch(arr, 7)); // Output: 3
    }
}
""")


# Go implementation of binary search
print("\nGo Binary Search Code:")
print("""
package main

import (
    "fmt"
)

func binarySearch(arr []int, target int) int {
    left, right := 0, len(arr)-1
    for left <= right {
        mid := (left + right) / 2
        if arr[mid] == target {
            return mid
        } else if arr[mid] < target {
            left = mid + 1
        } else {
            right = mid - 1
        }
    }
    return -1
}

func main() {
    arr := []int{1, 3, 5, 7, 9}
    fmt.Println(binarySearch(arr, 7)) // Output: 3
}
""")