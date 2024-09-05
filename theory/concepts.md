### 1. Dynamic Typing

Python’s dynamic typing allows variables to be defined without explicitly defining their data types. Python code is readable and clear due to its flexibility. However, it’s important to note that Python still enforces type safety at runtime.

### 2. Type Inference

Python performs type inference at runtime, which means that it determines the data type of a variable while the program is executing. This allows for dynamic and flexible code execution. For example:

x = 10

y = “20”

result = x + y  # Python dynamically converts x to a string and performs string concatenation

In the above example, Python recognizes that x is an integer and y is a string, and it dynamically converts x to a string to perform the concatenation.

### 3. Type Conversion

You can convert between different data types using built-in functions like int(), float(), str(), and bool().

num_str = “42”

num_int = int(num_str)

### 4. Polymorphism

Dynamic typing contributes to Python’s support for polymorphism. Due to polymorphism, many types of objects can be treated as though they are all of the same fundamental type. This concept enables you to write flexible and extensible code.

class Dog:

    def speak(self):

        return “Woof!”

class Cat:

    def speak(self):

        return “Meow!”

def animal_sound(animal):

    return animal.speak()

dog = Dog()

cat = Cat()

sound1 = animal_sound(dog)  # Calls Dog’s speak method

sound2 = animal_sound(cat)  # Calls Cat’s speak method

In the example above, the animal_sound function can work with both Dog and Cat objects because of Python’s dynamic typing and support for polymorphism.

### 5. Scope and Global Variables

Understanding variable scope is crucial. Variables defined inside of functions are local to the specific function, but variables specified outside of functions are global. Within a function, the global keyword must be used to change a global variable.

x = 10

def modify_global():

    global x

    x = 20

modify_global()

print(x)  # Outputs 20

### 6. Lists can contain diff data types, they ARE MUTABLE

### 7. Tuples

Tuples are just like Lists in that they cannot have their contents modified once they have been created, while being immutable. They are often used to store related data as a single unit.

Creating a tuple

    my_tuple = (1, 2, 3, “apple”, “banana”)

 Accessing elements

    print(my_tuple[0])  # Output: 1

#Tuples are immutable; the following line would raise an error:

    my_tuple[2] = 4

### 8. Lists of Lists (Nested Lists)

Python allows you to create nested data structures, where one data structure is nested inside another. Lists of lists are a common example of this, where each element in the outer list is a list itself.
# Creating a list of lists
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Accessing elements
print(matrix[1][2])  # Output: 6

### 9. Stacks and Queues

Stacks and queues are abstract data types that can be implemented using lists. Stacks follow the Last-In-First-Out (LIFO) concept, while First-In-First-Out (FIFO) concept is followed by Queues.

# Implementing a stack using a list
stack = []
stack.append(1)
stack.append(2)
stack.pop()  # Removes and returns the top element (2)
# Implementing a queue using a list
from collections import deque
queue = deque()
queue.append(1)
queue.append(2)
queue.popleft()  # Removes and returns the front element (1)

### 10. Sets and Dictionaries as Data Structures

Sets and dictionaries can also be used as data structures to solve specific problems efficiently. For example, sets are used to find unique elements in a collection, and dictionaries are used for fast data retrieval by keys.
# Using a set to find unique elements
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_elements = set(my_list)
# Using a dictionary for efficient data retrieval
student_grades = {“Alice”: 95, “Bob”: 89, “Charlie”: 78}
alice_grade = student_grades[“Alice”]

### 11. Custom Data Structures

Python allows you to define custom data structures by creating classes. You can define the behavior and attributes of your data structure to suit your specific needs.

class MyLinkedList:
    def __init__(self):
        self.head = None
    # Define methods to manipulate the linked list
    # …
# Creating an instance of a custom data structure
my_linked_list = MyLinkedList()


### 12. Encapsulation

The basic concept of encapsulation is to group together within a class data (attributes) and methods that work with that data. Access modifiers are used in Python to achieve encapsulation:

# Public: Methods and attributes are reachable from outside the class.

# Protected: To denote that attributes and methods are meant for internal use only, they are prefixed with a single underscore (e.g., _protected_variable).

# Private: To indicate that they should not be directly accessed, attributes and methods are prefixed with a double underscore (e.g., __private_variable).

class BankAccount:
    def __init__(self, account_number):
        self._account_number = account_number  # Protected attribute
        self.__balance = 0  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(“12345”)
account.deposit(1000)
print(account.get_balance())  # Output: 1000
print(account._account_number)  # Accessing a protected attribute
# Output: “12345”

# Note: Accessing a private attribute directly will result in an AttributeError.

### 13. Inheritance

Inheritance, which enables you to base a subclass or derived class (new class) on an base class or parent class(existing class), is a fundamental concept in object-oriented programming (OOP). The features and functionalities of the base class can be replaced or extended by the subclass.

class Animal:
    def speak(self):
        return “Some generic sound”

class Dog(Animal):
    def speak(self):
        return “Woof!”

class Cat(Animal):
    def speak(self):
        return “Meow!”

dog = Dog()
cat = Cat()
print(dog.speak())  # Output: “Woof!”
print(cat.speak())  # Output: “Meow!”

### 14. Polymorphism

Polymorphism is the ability of various objects to successfully respond to a method or function call regardless of the context. 
Параметрический полиморфизм является истинным, т. к. подразумевает исполнение одного и того же кода для всех допустимых типов аргументов, а ad-hoc-полиморфизм — мнимым,
# Python enables: 
#               AD-HOC-polymorphism,       Перегрузка методов (Overloading)
#               PARAMETRIC Polymorphism,  (Parametric Polymorphism) функции или классы, работают с любыми типами данных.
#               Subtype Polymorphism       дочерние классы наследуются от род.класса и могут Overload методы, св-ва.

class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

shapes = [Circle(5), Rectangle(4, 6)]
for shape in shapes:
    print(f”Area: {shape.area()}”)

### 15. Abstraction

Abstraction is the process of decreasing complexity by grouping things into classes based on essential characteristics and behaviors and hiding unimportant data. The Python ‘abc’ module can be used to create abstract base classes to accomplish abstraction.

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return “Car started”
    def stop(self):
        return “Car stopped”

class Motorcycle(Vehicle):
    def start(self):
        return “Motorcycle started”
    def stop(self):
        return “Motorcycle stopped”

car = Car()
motorcycle = Motorcycle()
print(car.start())  # Output: “Car started”
print(motorcycle.stop())  # Output: “Motorcycle stopped”


### 16. Exception Hierarchy

Python has a built-in exception hierarchy with a base Base Exception class at the top. Various exception classes inherit from it, including Exception, Arithmetic Error, Lookup Error, and others. It can be easier to identify and handle certain exceptions if you have a thorough understanding of the exception hierarchy.

### 17. File Modes:

“r”: Read (default mode). Opens the file for reading.
“w”: Write. enables writing by opening the file. The file will be truncated if it already exists. It will create a new, empty file if it doesn’t already exist.
“a”: Append. enables writing by opening the file, but instead of overwriting it, data is added to the end of the file.
“b”: Binary mode. Used in combination with other modes (e.g., “rb” for reading binary files).
# Opening a file in read mode
file = open(“example.txt”, “r”)
# Perform read/write operations here
# Closing the file
file.close()

It’s essential to close the file using close() when you’re done to free up system resources and ensure that changes are saved.


### 18. List Comprehensions
List comprehensions are a concise(quick) way of constructing new lists from existing lists or iterable objects. They enable you to create a new list in a single line of code by adding an expression to each item in an iterable.

# Using a list comprehension to create a list of squares

numbers = [1, 2, 3, 4, 5]
squared_numbers = [x**2 for x in numbers]

List comprehensions are not only elegant but also more efficient than traditional loops when creating new lists.


### 19. Decorators
Decorators are a unique and powerful feature of Python. They allow you to change the behavior of a function or method without changing the initial source code. Decorators are widely used for tasks like performance monitoring, authentication, and logging.

# Creating a simple decorator
def my_decorator(func):
    def wrapper():
        print(“Something is happening before the function is called.”)
        func()
        print(“Something is happening after the function is called.”)
    return wrapper
@my_decorator
def say_hello():
    print(“Hello!”)
say_hello()

Python frameworks like Flask and Django make extensive use of decorators 
to enhance the functionality of web routes and views.


### 20. Generators
Generators are a memory-efficient way to work with sequences of data, especially when dealing with large datasets. Generators produce values one at a time using the yield keyword rather than creating and storing an entire series in memory.

# Creating a simple generator

def countdown(n):
    while n > 0:
        yield n
        n -= 1
for i in countdown(5):
    print(i)

Generators are crucial for tasks that involve streaming data, and they are commonly used in scenarios like reading large log files or processing data from external sources.


### 21. Lambda Functions
Lambda functions, also referred to as anonymous functions, are tiny functions that only support a single expression and can be defined in a single line. They are frequently used as parameters for higher-order functions like map and filter as well as for basic operations.

# Using a lambda function to double a number

double = lambda x: x * 2
Lambda functions are handy when you need a quick, throwaway function for a specific task.

### 22. Virtual Environments
A best practice for Python programming is to use virtual environments. They allow you to create isolated environments with their own dependencies, preventing conflicts between packages used in different projects.

# Creating a virtual environment using venv
python -m venv myenv
# Activating the virtual environment
source myenv/bin/activate
The usage of virtual environments, which help maintain orderly and reproducible development environments, facilitates collaboration and project management.


### 23. Regular Expressions
Regular expressions (regex) are an effective tool for text editing and pattern matching. Regular expressions are supported by Python’s re package, enabling effective text extraction, searching, and manipulation.

import re
# Matching email addresses using a regular expression
pattern = r’\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b’
text = “Contact us at support@example.com or info@website.co.uk”
matches = re.findall(pattern, text)
Regular expressions are invaluable for tasks like data validation, text parsing, and web scraping.



### 24. Web Scraping
Web scraping is the process of extracting data from websites. Python’s libraries, such as Beautiful Soup and Requests, provide tools for parsing HTML and making HTTP requests.

import requests
from bs4 import BeautifulSoup
url = ‘https://example.com’
response = requests.get(url)
soup = BeautifulSoup(response.text, ‘html.parser’)

# Extracting data from the webpage
Web scraping is a valuable skill for data collection, competitive analysis, and automation of online tasks.


### 25. Database Connectivity
Python supports a wide range of database systems through libraries like SQLite, MySQL, and PostgreSQL. Understanding how to connect to databases and execute SQL queries is essential for building data-driven applications.

import sqlite3
# Connecting to a SQLite database
conn = sqlite3.connect(‘mydatabase.db’)
# Creating a cursor object for executing SQL queries
cursor = conn.cursor()
# Executing SQL queries
cursor.execute(‘SELECT * FROM users’)


### 26. Concurrency and Parallelism
Python provides libraries like threading and multiprocessing for working with concurrency and parallelism. These tools allow you to execute tasks concurrently, improving performance and responsiveness.

import threading
def print_numbers():
    for i in range(1, 6):
        print(f”Number {i}”)
def print_letters():
    for letter in ‘abcde’:
        print(f”Letter {letter}”)
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)
thread1.start()
thread2.start()


### 27. The PEP 8 style guide provides recommendations for code formatting, naming conventions, and more.