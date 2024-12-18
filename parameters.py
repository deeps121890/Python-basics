Positional parameter:
'''
def greet(name, age):
     print(f"Hello, {name}! You are {age} years old.")
greet("Alice", 30)
'''
o/p:  “Hello, Alice ! You are 30 years old.”
'''
def greet(name, age):
     print(f"Hello, {name}! You are {age} years old.") # Calling the function with keyword arguments 
greet(age=30, name="Alice")
'''
o/p: Hello, Alice! You are 30 years old.
'''
def greet(name, age=25):
    print(f"Hello, {name}! You are {age} years old.")
# Calling with only the required parameter
greet("Alice")  # age uses the default value 25
# Calling with both parameters
greet("Bob", 30)  # age is explicitly set to 30
'''
o/p:Hello, Alice! You are 25 years old.
Hello, Bob! You are 30 years old.
'''
def sum_numbers(*args):
    total = 0 for num in args:
        total +=num return total # Calling the function with different numbers of arguments print(sum_numbers(1, 2, 3)) # Output: 6
print(sum_numbers(5, 10, 15, 20)) 
print(sum_numbers(7)) 
'''
o/p:50
7
'''
  def greet(person, greeting="Hello", **kwargs):
    print(f"{greeting}, {person}!")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Calling the function with arbitrary keyword arguments
greet("Alice", greeting="Hi", age=30, city="New York")
'''
o/p:
Hi, Alice!
age: 30
city: New York

