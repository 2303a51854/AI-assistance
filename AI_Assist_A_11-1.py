import collections

#Data Structures with AI : Implementing Fundamental Structures
'''Lab Objectives:
Use AI to assist in designing and implementing fundamental data structures in python.
Learn how to prompt AI for structure creation, optimization, and documentation.
Improve understanding of Lists, Stacks, Queues, Linked Lists, Trees, Graphs, and Hash Tables.
Enhance code quality with AI-generated comments and performance suggestions.'''

#Task-1: Stack Implementation
#Generate a Stack class with push, pop, peek, and is_empty methods. Include AI-generated comments explaining each method.
'''Sample Input Code:
class Stack:
pass
Expected Output:
A functional stack implementation with all required methods and docstrings.'''
#print the input and output for the task.
'''class Stack:
    """A Stack is a linear data structure that follows the Last In First Out (LIFO) principle."""
    
    def __init__(self):
        """Initialize an empty stack."""
        self.items = []
    
    def push(self, item):
        """Add an item to the top of the stack.
        
        Args:
            item: The item to be added to the stack.
        """
        self.items.append(item)
    
    def pop(self):
        """Remove and return the item at the top of the stack.
        
        Returns:
            The item at the top of the stack. If the stack is empty, returns None.
        """
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def peek(self):
        """Return the item at the top of the stack without removing it.
        
        Returns:
            The item at the top of the stack. If the stack is empty, returns None.
        """
        if not self.is_empty():
            return self.items[-1]
        return None
    
    def is_empty(self):
        """Check if the stack is empty.
        
        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0
#Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
print(stack.peek())  # Output: 2
print(stack.pop())   # Output: 2
print(stack.is_empty())  # Output: False'''

#Task-2: Queue Implementation
#Use AI to implement a Queue using Python lists.
#Sample Input Code:
#class Queue:
#pass
#Expected Output:
#FIFO-based queue class with enqueue, dequeue, peek, and size methods.
'''class Queue:
    """A Queue is a linear data structure that follows the First In First Out (FIFO) principle."""
    
    def __init__(self):
        """Initialize an empty queue."""
        self.items = []
    
    def enqueue(self, item):
        """Add an item to the end of the queue.
        
        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)
    
    def dequeue(self):
        """Remove and return the item at the front of the queue.
        
        Returns:
            The item at the front of the queue. If the queue is empty, returns None.
        """
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def peek(self):
        """Return the item at the front of the queue without removing it.
        
        Returns:
            The item at the front of the queue. If the queue is empty, returns None.
        """
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        """Return the number of items in the queue.
        
        Returns:
            The number of items in the queue.
        """
        return len(self.items)
    
    def is_empty(self):
        """Check if the queue is empty.
        
        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0
#Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.peek())  # Output: 1
print(queue.dequeue())  # Output: 1
print(queue.size())  # Output: 1
print(queue.is_empty())  # Output: False'''

#Task-3: Linked List Implementation
#Generate a python code for a Singly Linked List with insert and display methods.
#Sample Input Code:
#class Node:
#pass
#class LinkedList:
#pass
#Expected Output:
#A working linked list implementation with clear method documentation.
'''class Node:
    """A Node is a fundamental part of a linked list, containing data and a reference to the next node."""
    
    def __init__(self, data):
        """Initialize a node with data and set the next reference to None.
        
        Args:
            data: The value stored in the node.
        """
        self.data = data
        self.next = None
class LinkedList:
    """A LinkedList is a linear data structure where each element is a separate object, called a node."""
    
    def __init__(self):
        """Initialize an empty linked list."""
        self.head = None
    
    def insert(self, data):
        """Insert a new node with the given data at the end of the linked list.
        
        Args:
            data: The value to be inserted into the linked list.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
    
    def display(self):
        """Display the contents of the linked list."""
        current_node = self.head
        while current_node:
            print(current_node.data, end=' ')
            current_node = current_node.next
        print()
#Example usage:
linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)
linked_list.display()  # Output: 1 2 3'''

#Task-4: Binary Search Tree Implementation
#Use AI to create a BST with insert and in-order traversal methods.
#Sample Input Code:
#class BST:
#pass
#Expected Output:
#BST implementation with recursive insert and traversal methods.
'''class Node:
    """A Node in a Binary Search Tree (BST) contains data and references to left and right child nodes."""
    
    def __init__(self, data):
        """Initialize a node with data and set left and right references to None.
        
        Args:
            data: The value stored in the node.
        """
        self.data = data
        self.left = None
        self.right = None
class BST:
    """A Binary Search Tree (BST) is a binary tree where each node has at most two children, and the left child is less than the parent node, while the right child is greater."""
    
    def __init__(self):
        """Initialize an empty BST."""
        self.root = None
    
    def insert(self, data):
        """Insert a new node with the given data into the BST.
        
        Args:
            data: The value to be inserted into the BST.
        """
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, current_node, data):
        """Helper method to insert a new node recursively.
        
        Args:
            current_node: The current node being compared.
            data: The value to be inserted into the BST.
        """
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursive(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursive(current_node.right, data)
    
    def in_order_traversal(self):
        """Perform in-order traversal of the BST and return a list of values."""
        return self._in_order_recursive(self.root)
    
    def _in_order_recursive(self, current_node):
        """Helper method for in-order traversal recursively.
        
        Args:
            current_node: The current node being traversed.
        
        Returns:
            A list of values in in-order traversal order.
        """
        values = []
        if current_node:
            values.extend(self._in_order_recursive(current_node.left))
            values.append(current_node.data)
            values.extend(self._in_order_recursive(current_node.right))
        return values
#Example usage:
bst = BST()
bst.insert(5)
bst.insert(3)
bst.insert(7)
print(bst.in_order_traversal())  # Output: [3, 5, 7]'''

#Task-5: Hash Table Implementation
#Use AI to implement a hash table with basic insert, search, and delete methods.
#Sample Input Code:
#class HashTable:
#pass
#Expected Output:
#Collision handling using chaining, with well-commented methods.
'''class HashTable:
    """A Hash Table is a data structure that implements an associative array, mapping keys to values using a hash function."""
    
    def __init__(self, size=10):
        """Initialize the hash table with a specified size and create buckets for chaining.
        
        Args:
            size: The number of buckets in the hash table (default is 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Generate a hash value for the given key.
        
        Args:
            key: The key to be hashed.
        
        Returns:
            An index corresponding to the bucket where the key-value pair should be stored.
        """
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table. If the key already exists, update its value.
        
        Args:
            key: The key to be inserted or updated.
            value: The value associated with the key.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Insert new key-value pair
    
    def search(self, key):
        """Search for a value associated with the given key in the hash table.
        
        Args:
            key: The key to be searched for.
        
        Returns:
            The value associated with the key if found, otherwise None.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """Delete a key-value pair from the hash table based on the given key.
        
        Args:
            key: The key to be deleted from the hash table.
        
        Returns:
            True if the key was found and deleted, False otherwise.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]  # Remove the key-value pair
                return True
        return False
#Example usage:
hash_table = HashTable()
hash_table.insert("name", "Alice")
hash_table.insert("age", 30)
print(hash_table.search("name"))  # Output: Alice
print(hash_table.search("age"))   # Output: 30
hash_table.delete("name")
print(hash_table.search("name"))  # Output: None'''

#Task-6: Graph Representation
#Use AI to implement a graph using an adjacency list.
#Sample Input Code:
#class Graph:
#pass
#Expected Output:
#Graph with methods to add vertices, add edges, and display connections.
'''class Graph:
    """A Graph is a collection of vertices (nodes) and edges (connections) that can represent various relationships."""
    
    def __init__(self):
        """Initialize an empty graph using an adjacency list."""
        self.graph = {}
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph.
        
        Args:
            vertex: The vertex to be added to the graph.
        """
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices in the graph. This method assumes an undirected graph.
        
        Args:
            vertex1: The first vertex in the edge.
            vertex2: The second vertex in the edge.
        """
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
    
    def display(self):
        """Display the graph as an adjacency list."""
        for vertex, edges in self.graph.items():
            print(f"{vertex}: {', '.join(edges)}")
#Example usage:
graph = Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_edge("A", "B")
graph.add_edge("A", "C")
graph.display()  
# Output: A: B, C
#         B: A
#         C: A'''

#Task-7: Priority Queue Implementation
#Use AI o implement a priority queue using Python’s heapq module.
#Sample Input Code:
#class PriorityQueue:
#pass
#Expected Output:
#Implementation with enqueue (priority), dequeue (highest priority), and display methods.
'''import heapq 

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def enqueue(self, item, priority):
        heapq.heappush(self._queue, (priority, self._index, item))
        self._index += 1

    def dequeue(self):
        return heapq.heappop(self._queue)[-1]

    def display(self):
        for priority, index, item in self._queue:
            print(f"Item: {item}, Priority: {priority}")
#Example usage:
pq = PriorityQueue()
pq.enqueue("Task 1", 3)
pq.enqueue("Task 2", 1)
pq.enqueue("Task 3", 2)
pq.display()
# Output: Item: Task 2, Priority: 1
#         Item: Task 3, Priority: 2
#         Item: Task 1, Priority: 3
print(pq.dequeue())  
# Output: Task 2
print(pq.dequeue())  
# Output: Task 3
print(pq.dequeue())  
# Output: Task 1'''

#Task-8: Deque Implementation
#Use AI to implement a double-ended queue using collections.deque.
#Sample Input Code:
#class DequeDS:
#pass
#Expected Output:
#Insert and remove from both ends with docstrings.

'''import collections
class DequeDS:
    def __init__(self):
        self._deque = collections.deque()

    def append_left(self, item):
        """Add an item to the left end of the deque.
        
        Args:
            item: The item to be added.
        """
        self._deque.appendleft(item)

    def append_right(self, item):
        """Add an item to the right end of the deque.
        
        Args:
            item: The item to be added.
        """
        self._deque.append(item)

    def pop_left(self):
        """Remove and return an item from the left end of the deque.
        
        Returns:
            The removed item.
        """
        return self._deque.popleft()

    def pop_right(self):
        """Remove and return an item from the right end of the deque.
        
        Returns:
            The removed item.
        """
        return self._deque.pop()

    def display(self):
        """Display the contents of the deque."""
        print(list(self._deque))
#Example usage:
deque_ds = DequeDS()
deque_ds.append_right("A")
deque_ds.append_right("B")
deque_ds.append_left("C")
deque_ds.display()
# Output: ['C', 'A', 'B']
print(deque_ds.pop_left())  
# Output: C
print(deque_ds.pop_right())  
# Output: B
print(deque_ds.display())  
# Output: ['A']'''

#Task-9: Real-Time Application Challenge – Choose the Right Data Structure 
#Scenario: Your college wants to develop a Campus Resource Management System that handles:
#1. Student Attendance Tracking – Daily log of students entering/exiting the campus.
#2. Event Registration System – Manage participants in events with quick search and removal.
#3. Library Book Borrowing – Keep track of available books and their due dates.
#4. Bus Scheduling System – Maintain bus routes and stop connections.
#5. Cafeteria Order Queue – Serve students in the order they arrive.
#Student Task:
# For each feature, select the most appropriate data structure from the list below:
# Stack
# Queue
# Priority Queue
# Linked List
# Binary Search Tree (BST)
# Graph
# Hash Table
# Deque
# Justify your choice in 2–3 sentences per feature.
# Implement one selected feature as a working Python program with AI-assisted code generation.
#Expected Output:
# A table mapping feature → chosen data structure → justification.
# A functional Python program implementing the chosen feature with comments and docstrings.
'''class HashTable:
    """A Hash Table is a data structure that implements an associative array, mapping keys to values using a hash function."""
    
    def __init__(self, size=10):
        """Initialize the hash table with a specified size and create buckets for chaining.
        
        Args:
            size: The number of buckets in the hash table (default is 10).
        """
        self.size = size
        self.table = [[] for _ in range(size)]
    
    def _hash(self, key):
        """Generate a hash value for the given key.
        
        Args:
            key: The key to be hashed.
        
        Returns:
            An index corresponding to the bucket where the key-value pair should be stored.
        """
        return hash(key) % self.size
    
    def insert(self, key, value):
        """Insert a key-value pair into the hash table. If the key already exists, update its value.
        
        Args:
            key: The key to be inserted or updated.
            value: The value associated with the key.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)  # Update existing key
                return
        bucket.append((key, value))  # Insert new key-value pair
    
    def search(self, key):
        """Search for a value associated with the given key in the hash table.
        
        Args:
            key: The key to be searched for.
        
        Returns:
            The value associated with the key if found, otherwise None.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for k, v in bucket:
            if k == key:
                return v
        return None
    
    def delete(self, key):
        """Delete a key-value pair from the hash table based on the given key.
        
        Args:
            key: The key to be deleted from the hash table.
        
        Returns:
            True if the key was found and deleted, False otherwise.
        """
        index = self._hash(key)
        bucket = self.table[index]
        
        for i, (k, v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                return True
        return False
# Example usage for Student Attendance Tracking:
attendance_table = HashTable()
attendance_table.insert("student_001", "Present")
attendance_table.insert("student_002", "Absent")
print(attendance_table.search("student_001"))  # Output: Present
print(attendance_table.search("student_002"))  # Output: Absent
attendance_table.delete("student_002")
print(attendance_table.search("student_002"))  # Output: None'''

#Task-10:Smart E-Commerce Platform – Data Structure Challenge
#An e-commerce company wants to build a Smart Online Shopping System with:
#1. Shopping Cart Management – Add and remove products dynamically.
#2. Order Processing System – Orders processed in the order they are placed.
#3. Top-Selling Products Tracker – Products ranked by sales count.
#4. Product Search Engine – Fast lookup of products using product ID.
#5. Delivery Route Planning – Connect warehouses and delivery locations.
#Student Task:
# For each feature, select the most appropriate data structure from the list below:
# Stack
# Queue
# Priority Queue
# Linked List
# Binary Search Tree (BST)
# Graph
# Hash Table
# Deque
# Justify your choice in 2–3 sentences per feature.
# Implement one selected feature as a working Python program with AI-assisted code generation.
#Expected Output:
# A table mapping feature → chosen data structure → justification.
# A functional Python program implementing the chosen feature with comments and docstrings.
class DequeDS:
    def __init__(self):
        self._deque = collections.deque()

    def append_left(self, item):
        """Add an item to the left end of the deque.
        
        Args:
            item: The item to be added.
        """
        self._deque.appendleft(item)

    def append_right(self, item):
        """Add an item to the right end of the deque.
        
        Args:
            item: The item to be added.
        """
        self._deque.append(item)

    def pop_left(self):
        """Remove and return an item from the left end of the deque.
        
        Returns:
            The removed item.
        """
        return self._deque.popleft()

    def pop_right(self):
        """Remove and return an item from the right end of the deque.
        
        Returns:
            The removed item.
        """
        return self._deque.pop()

    def display(self):
        """Display the contents of the deque."""
        print(list(self._deque))
#Example usage:
deque_ds = DequeDS()
deque_ds.append_right("A")
deque_ds.append_right("B")
deque_ds.append_left("C")
deque_ds.display()
# Output: ['C', 'A', 'B']
print(deque_ds.pop_left())
# Output: C
print(deque_ds.pop_right())
# Output: B
print(deque_ds.display())
# Output: ['A']
print(deque_ds.pop_left())
# Output: A
print(deque_ds.display())
# Output: []
