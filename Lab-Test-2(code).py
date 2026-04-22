#Experiment-5:
#Task-1: Write a Python program to generate test cases that include English words, phrases with spaces, and at least one emoji-based string.
#And that extend the is_palindrome(text) function from Lab 8 to support Unicode characters and treat emojis and accented characters as valid input.
#to propose multiple doctest test cases, including Unicode examples and edge cases like empty strings and single characters. Implement or update "is_palindrome".
'''import unicodedata

def is_palindrome(text):
    normalized_text = unicodedata.normalize('NFKD', text)
    cleaned_text = ''.join(char for char in normalized_text if char.isalnum()).lower()
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print(is_palindrome("A man, a plan, a canal: Panama"))  # Expected: True
    print(is_palindrome("No lemon, no melon"))  # Expected: True
    print(is_palindrome("Hello, World!"))  # Expected: False
    print(is_palindrome("😊madam😊"))  # Expected: True
    print(is_palindrome(""))  # Expected: True'''
#Justification:
#The is_palindrome function has been updated to handle Unicode characters by normalizing the input text using the NFKD normalization form.
#  This allows the function to treat accented characters and emojis as valid input.
#  The function also removes non-alphanumeric characters and converts the text to lowercase before checking if it is a palindrome.


#Task-2: Write a python program to design Hash Table using separate chaining collision resolution with AI assistance.
#It should be given that HashTable with put(key, value), get(key), remove(key), load_factor(). Dynamic resizing when load factor > 0.75
class HashTable:
    def __init__(self, capacity=8):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[index].append([key, value])
        self.size += 1
        if self.load_factor() > 0.75:
            self._resize()

    def get(self, key):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for pair in self.buckets[index]:
            if pair[0] == key:
                self.buckets[index].remove(pair)
                self.size -= 1
                return

    def load_factor(self):
        return self.size / self.capacity

    def _resize(self):
        old_buckets = self.buckets
        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self.put(key, value)

# Example usage
if __name__ == "__main__":
    ht = HashTable()
    ht.put("key1", "value1")
    ht.put("key2", "value2")
    print(ht.get("key1"))  # Expected: value1
    ht.remove("key1")
    print(ht.get("key1"))  # Expected: None
    print("Load Factor:", ht.load_factor())  # Expected: Load Factor: 0.125
#Justification:
#The HashTable class implements a hash table using separate chaining for collision resolution.
#  The put method adds key-value pairs to the appropriate bucket based on the hash of the key, and it checks for existing keys to update values.
#  The get method retrieves values based on keys, and the remove method deletes key-value pairs.