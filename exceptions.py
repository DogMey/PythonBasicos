# print(5 + "5")  # This will raise a TypeError because you cannot add an int and a str

a = 5
b= 1

try:
    print(a + b)  # This will raise a TypeError
except:
    print("Cannot add")
else:
    print("Addition successful")
finally:
    print("This block always executes, regardless of whether an exception occurred or not")

b = '1'

try:
    print(a + b)  # This will raise a TypeError
except TypeError:
    print("Cannot add an int and a str")
except ValueError: # This block will not execute because the exception is TypeError, not ValueError
    print("Cannot add an int and a str")

try:
    print(a + b)
except ValueError as error:
    print(error)
except Exception as error:
    print(f"An unexpected error occurred: {error}")