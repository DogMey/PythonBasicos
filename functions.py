def my_function():
    print("This is a function")

my_function()  # Calling the function

def add_numbers(a, b):
    return a + b

print(f"The sum is: {add_numbers(5,3)}")  # Output: The sum is: 8

def add_only_numbers(a: int, b: int) -> int: # Really not necessary but good practice
    return a + b

print(f"The sum is: {add_only_numbers(5, 3)}")  # Output: The sum is: 8

def division(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
print(division(10, 2))  # Output: 5.0
print(division(10, 0))  # Output: Cannot divide by zero

def print_name (name, subname):
    print(f"Hi {name} {subname}")

print_name("Kevin", "Ramirez")  # Output: Name: Kevin, Subname: Ramirez
print_name(subname="Ramirez", name="Kevin")  # Output: Name: Kevin, Subname: Ramirez

def print_alias (name, subname, alias = "Anonimous"):
    print(f"Hi {name} {subname}, your alias is {alias}")

print_alias("Kevin", "Ramirez")  # Output: Hi Kevin Ramirez, your alias is No alias
print_alias("Kevin", "Ramirez", "DogMey")  # Output: Hi Kevin Ramirez

def sum_numbers(*args): # This allows for a variable number of arguments
    return sum(args)

print(f"The sum is: {sum_numbers(1, 2, 3, 4)}")  # Output: The sum is: 10

def print_info(**kwargs):  # This allows for a variable number of keyword arguments
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Kevin", age=30, city="Bogota")  # Output: name: Kevin, age: 30, city: Bogota