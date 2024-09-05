
# Basic Python syntax
# 1. Variables and Types:
   - Python supports dynamic typing.
   Example:
       x = 10
       name = "Alice"

# 2. Control Flow:
   - If statements:
       if condition:
           # Code block
       elif another_condition:
           # Another block
       else:
           # Default block

   - Loops:
       for i in range(5):
           print(i)

       while condition:
           # Loop until condition is False

# 3. Functions:
   - Defining a function:
       def my_function(param1, param2):
           return param1 + param2

   - Lambda functions:
       square = lambda x: x ** 2

# 4. Classes and Objects:
   - Defining a class:
       class Dog:
           def __init__(self, name):
               self.name = name

           def bark(self):
               return "Woof!"
       
   - Creating an instance:
       my_dog = Dog("Rover")
       print(my_dog.bark())

# 5. List Comprehensions:
   - Example:
       squares = [x ** 2 for x in range(10)]
# 6. type command
type command is used to check the type or class of an object. 

Syntax: type(object)
    type(10)        == int
    type("qwe")     == str
    type((1,2,3))   == tuple
    type([1,2,23])  == list

# 7.  range command
    range command is used to generate a sequence of integers starting 
    from 0 by default to n where n is not included in the generated numbers. 
    We use this command in for loops mostly. 

Syntax: range(start, stop, step) 

    start refers to the starting of range (Optional; 0 by default )
    stop refers to the number before which you want to stop (Mandatory)
    step refers to the increment count (Optional; 1 by default)
# 8. round command
    round command is used to round a number to a given precision in decimal digits. That means if you have so many digits after decimal in a float point number then you can use the round command to round off the specified number. You can mention how many digits you want after the decimal point. 

    Syntax: round(number, digits) 

    number refers to the floating-point number. 
    digits refer to the count of digits you want after the decimal point. (Optional; By default 0)
# 9. input command
input command is used to take input from the user. The flow of the program will be stopped until the user has entered any value. Whatever the user enters it will be converted into a string by the input function. If you want to take an integer as input then you have to convert it explicitly. 

Syntax: input(message)

message refers to the text you want to display to the user. (Optional)
# 10. len command
len command or len() function is used to get the number of items in an object. If the object is a string then len() function returns the number of characters present in it. If the object is a list or tuple it will return the number of elements present in that list or tuple. len() gives an error if you try to pass an integer value to it. 

Syntax: len(object)

object of which you want to find the length (Required)
# 11. isalnum(): 
It checks whether all the characters of a given string are alphanumeric or not. It returns a boolean value. 
Syntax: stringname.isalnum()
# 12. capitalize()
If the first character is uppercase or an integer or any special character, it doesn’t do anything.
# 13. find()
find() command is used to search for a substring in a string. It returns the index of the first occurrence of the substring if it is present otherwise it returns -1. 

Syntax: string.find(substring)

string refers to the string in which you want to search.
substring refers to the value that you want to search.
# 14. count(): count() function returns the count of occurrences of a substring in a string object.
Syntax: stringname.count(substring, start, end)

stringname refers to the string in which you want to search.
substring refers to the value whose count you want to find.
start refers to that starting index within the string where search starts (Optional)
end refers to that ending index within the string where the search ends (Optional)
# 15. center()
center command is used to align a string in the center, using a specified character (by default it is space) as the fill character. 

Syntax: string.center(length, character)

string is the string that you want to align in center
length is the full length taken by the new string in which both sides will be filled by character and in the center, we will have the original string.
character refers to the character used to fill the missing space on each side. Default is ” ” (space).

# 16. List Commands append()
Just like a string we have various commands for list objects as well. Lists are used to multiple elements in a single object. We can use lists to store elements of different data types. Some of the most important list methods are: 

append(): append command is used to add an element at the end of the list.

Syntax: list.append(element)

list is the list object in which you want to add an element
element refers to the new item that you want to add to the list
# 17. copy()
copy() is used to create a new copy of the list object. It returns a new list object.

Syntax: list.copy()
# 18. insert()
insert command is used to add an element at a specified position in the list object. It takes two parameters position and element. 

Syntax: listname.insert(position, element)

position at which you want to insert a new element. If you give a position greater than the number of elements in the list, it will always insert at the end.
element refers to the new element that needs to be added.
# 19. pop()
pop() method is used to remove an element from a specified position in the list. It returns the element after removing it from the list.

Syntax: listname.pop(position)

position from which you want to remove the element.
# 20. reverse()
reverse method reverses the order of all elements in the list. It modifies the original list object and it doesn’t return anything.

Syntax: list.reverse()
# 21. sort()
sort method is used to sort the elements of the list in ascending order by default. 

Syntax: list.sort()
# 22. Tuple Commands count(): 
count method is used to count the occurrences of an element in the tuple. 

Syntax: tuple.count(element)
# 23. index()
This method is used to find the index of the first occurrence of an element. If the element is not found in the whole tuple then it will raise a ValueError.

Syntax: tuple.index(element)

tuple is the tuple object in which you want to search an element
element refers to the item that you wanna search
# 24. Advanced Python Commands List
# Set Commands
# add(): add command is used to add a new element in the set. 

Syntax: setname.add(element)

setname is the name of that set variable in which you want to add a new element.
element refers to the new item that you want to add. 
# 25. clear()
clear removes all the elements of a set. It does not take any parameters.

Syntax: setname.clear()
# 26. discard()
discard is used to remove the specified element from the set. If the specified element is not found in the set it will not give an error. 

Syntax: setname.discard(element)

setname is the name of that set variable from which you want to remove an element.
element refers to the element that you want to remove.
# 27. remove()
remove command is also used to remove a specified element from the set but it is different from discard because remove will give an error if the specified element is not found in the set.

Syntax: setname.remove(element)

setname is the name of that set variable from which you want to remove an element.
element refers to the element that you want to remove.
# 28. difference()
difference method is used to get a set that contains the difference of two sets. The difference of sets means it will have only those elements that are present in only one set and not in another set. Suppose we have two sets A and B. Set A has {1,2,3} and set B has {2, 4, 6}. Then the difference of A and B will be {1,3}. 

Syntax: setA.difference(setB)

Elements of setB will be removed from setA if present.
# 29. difference_update()
difference_update method is used to get a set of elements that are present in the first set and not common in both sets. That means it removes the elements that exist in both sets. It does not return a new set, it just removes common elements from the first set. 

Syntax: setA.difference_update(setB)

Elements that exist in both setA and setB will be removed from setA.
# 30. intersection()
intersection method returns a set having elements that exist in all the specified sets. 


Syntax: set.intersection(set1, set2, … setn)

Set of elements that exist in the set, set1, set2, … setn will be returned.
# 31. issubset()
issubset method checks whether all elements of set A are present in set B or not. It returns a boolean value.

Syntax: setA.issubset(setB)
# 32. symmetric_difference()
This method returns a set containing elements from both the sets except those that are common in both sets. 
Syntax: setA.symmetric_difference(setB)

# 33. union()
union method returns a set containing all elements from both sets, except the duplicated ones.

Syntax: setA.union(setB)
### Dictionary Commands
Dictionary is a built-in type in Python. It is used to store key-value pairs. It is ordered, modifiable, and does not allow duplicate keys. That means in a dictionary we can not add two pairs having the same value of keys. Python provides a set of built-in methods that we can use on dictionary objects. 
# 34. fromkeys(): 
fromkeys() method is used to generate a dictionary with specified keys and a specified value. 

Syntax: dict.fromkeys(keys, value)
keys is the tuple or list of key elements.
value refers to the value which would be paired with all the specified keys.
# 35. get()
get method is used to get a value of the specified key. If a key is not found in the dictionary it will return nothing unless we specify something in the parameters. 

Syntax: dictionary.get(key, value)

dictionary is the name of the dictionary object in which you want to search. 
key refers to the key that you want to search in the dictionary.
value is the value that would be returned if the key is not found in the dictionary.
# 36. items()
items method is used to display the dictionary elements. It will display all the key-value pairs present in the dictionary. It returns a view object which will contain all the key-value pairs as tuples in a list. It does not take any parameters.

Syntax: dictionary.items()
# 37. keys()
keys method is used to get all the keys present in the dictionary. It returns a view object containing all keys of the dictionary as a list. It does not take any parameters.

Syntax: dictionary.keys()
# 38. values()
values method is used to get all the values present in the dictionary. It returns a view object containing all values of the dictionary as a list. It does not take any parameters.

Syntax: dictionary.values()
# 39. pop()
pop method is used to remove a key-value pair from the dictionary by specifying the key. It returns the value of the key-value pair that is need to be removed. 

Syntax: dictionary.pop(key)

key refers to the key of the pair that you want to remove from the dictionary.
# 40. popitem()
popitem command is used to remove the last inserted pair from the dictionary. It does not take any parameters. It returns the removed pair as a tuple.

Syntax: dictionary.popitem()
# 41. setdefault()
setdefault method is used to get the value of a specified key. If the key does not exist it will insert the key with the value passed as a parameter. If you don’t specify any value it will insert the key with value None. 

Syntax: dictionary.setdefault(key, value)









# Medium syntax
# 1. List, Dict, and Set Comprehensions:
   - Syntax for creating lists, dictionaries, or sets in a concise way:
       squares = [x ** 2 for x in range(10)]
       dict_comp = {x: x**2 for x in range(5)}

# 2. Generators and Yield:
   - Yield produces a generator that can be iterated lazily:
       def my_generator():
           yield 1
           yield 2
           yield 3

# 3. Exception Handling:
   - Use try-except-finally for handling exceptions:
       try:
           1 / 0
       except ZeroDivisionError:
           print("Cannot divide by zero")
       finally:
           print("Always runs")

# 4. Decorators:
    Functions that modify the behavior of other functions:
       def decorator(func):
           def wrapper(*args, **kwargs):
               print("Before function")
               result = func(*args, **kwargs)
               print("After function")
               return result
           return wrapper

       @decorator
       def say_hello():
           print("Hello!")
    # Property Decorators
    Concept: Python provides @property decorators to manage getters and setters.

        Example:
        class Employee:
            def __init__(self, name):
                self._name = name

            @property
            def name(self):
                return self._name
# 5. match-case Syntax:
    def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case _:
            return "Unknown"











# Advanced Syntax
# 1. The Walrus Operator (:=):
   - Allows assignment inside expressions:
       if (n := len(my_list)) > 10:
           print(f"List is too long ({n} elements)")

# 2. Asynchronous Programming (async/await):
   - Writing asynchronous code using async and await:
       async def fetch_data():
           await some_io_operation()

# 3. Context Managers:
   - Using with to manage resources:
       with open("file.txt") as f:
           data = f.read()

# 4. Metaclasses:
   - Control class creation by defining a metaclass:
       class Meta(type):
           def __new__(cls, name, bases, dct):
               return super().__new__(cls, name, bases, dct)
# 5. Positional-Only Parameters
    Concept: In Python 3.8+, you can define functions where some parameters can only be passed positionally,
    not by name. This is done by using / in function definitions.

    Example:
    `def my_func(a, b, /, c):`
        `return a + b + c`

    Analogy: Similar to forcing parameters to be passed without using the argument names, 
    which ensures the function is used in a particular way, like requiring mandatory arguments in C 
    or other statically typed languages.
# 6. F-String Enhancements
    Concept: Python 3.8 improved f-strings by allowing = 
    to be used for self-documenting expressions, which makes debugging easier.

    Example:
    `x = 42`
    `print(f'{x=}')`
# 7. Assignment Expressions in List Comprehensions
    Concept: The walrus operator can also be used in list comprehensions to evaluate 
    and store values as part of the expression.

    Example:
    `result = [y := f(x), y**2 for x in range(5)]`
# 8. Positional-Only vs. Keyword-Only Arguments
    Concept: In Python 3.8+, functions can now declare both positional-only 
            and keyword-only arguments in the same signature, providing more control over how a function is called.

    Example:
    `def function(positional, /, keyword_only, *, another_keyword):`
        `pass`
# 9. asyncio and Asynchronous Programming (Async/Await)
    Concept: Python 3.5 introduced the async and await keywords, 
    and in later versions, these features have been refined. 
    Python uses the asyncio event loop for asynchronous programming, 
    which allows non-blocking I/O operations (similar to Node.js event loop).

    Example:

    `async def fetch_data():
        await asyncio.sleep(1)
        return "Data fetched"`
    Analogy: Like the event loop in Node.js, Python's asyncio uses coroutines to handle multiple tasks simultaneously without threading or multiprocessing.
# 10. async and await with contextlib (Asynchronous Context Managers):
    Concept: In Python 3.7+, context managers support asynchronous operations using async with.

    Example:
    `async with some_resource() as resource:
        await process(resource)`
# 11. Type Hinting & Static Type Checking (Type Annotations)
    Concept: Type hints were introduced in Python 3.5 and enhanced in later versions. They allow for static type checking, but Python remains dynamically typed.

    Example:

    `def add(a: int, b: int) -> int:
        return a + b`
    Analogy: Similar to type annotations in TypeScript, where types are checked statically but the underlying language remains dynamic.
# 12. Data Classes (@dataclass)
    Concept: Python 3.7 introduced dataclass, which automatically generates 
    boilerplate code like __init__, __repr__, and __eq__ methods for classes.

    Example:
    `from dataclasses import dataclass

    @dataclass
    class Employee:
        name: str
        position: str`
# 13. Mutable Default Arguments (Common Pitfall)
    Concept: Default values in Python functions are evaluated once. 
    If you use a mutable object (like a list) as a default, it can lead to unexpected behavior.

    Example:

    def append_to_list(value, my_list=[]):
        my_list.append(value)
        return my_list

    # Problematic behavior
    append_to_list(1)  # [1]
    append_to_list(2)  # [1, 2]
    Fix: Use None as the default, and initialize inside the function.

    def append_to_list(value, my_list=None):
        if my_list is None:
            my_list = []
        my_list.append(value)
        return my_list

# 14. Weak References
    Concept: The weakref module allows references to objects that don't prevent their garbage collection, 
    useful in certain performance-sensitive applications.

    Example:
    import weakref
    obj = SomeClass()
    weak_ref = weakref.ref(obj)

# 15. The __slots__ Mechanism
    Concept: Using __slots__ in classes limits the attributes the instance can have,
    saving memory by avoiding the default __dict__.

    Example:
    class MyClass:
        __slots__ = ['attr1', 'attr2']
        def __init__(self, attr1, attr2):
            self.attr1 = attr1
            self.attr2 = attr2

# 16. Coroutines and Generators
    Concept: Generators (yield) allow for iteration over large datasets without 
    loading everything into memory at once. 
    Coroutines, used with async functions, 
    are specialized generators designed for asynchronous code execution.

    Example (Coroutine):

    async def fetch_data():
        yield "Data"
    Analogy: Coroutines in Python function similarly to async functions in JavaScript/Node.js, both 
    allowing non-blocking code execution.

# 17. Enum Classes
    Concept: Enums are symbolic names for a set of values.

    Example:
    from enum import Enum

    class Color(Enum):
        RED = 1
        GREEN = 2
        BLUE = 3
