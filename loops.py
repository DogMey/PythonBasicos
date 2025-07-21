# While

my_condition = 0

while my_condition <= 10:
    print(f"Condition is {my_condition} and is less or equal to 10")
    my_condition += 1
else: # This block executes when the loop condition becomes False
    print(f"Condition is greater than 10 because is {my_condition}, exiting loop")

while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print("Condition is 15")
        break  # Exit the loop when my_condition is 15
    print(f"Condition is {my_condition} and is less than 20")

while my_condition < 20:
    my_condition += 2
    if my_condition == 15:
        print("Condition is 15")
        continue  # Skip the rest of the loop iteration when my_condition is 15
    print(f"Condition is {my_condition} and is less than 20")

# For loop

my_list = [1, 2, 3, 4, 5]
my_set = {"Kevin", "DogMey", 5}
my_dict = {
    "name": "Kevin", 
    "age": 30, 
    "city": "Bogota",
    "last_name": "Ramirez",
    1 : "Python",
    2 : "JavaScript"
}

for item in my_list:
    print(f"Current item is {item}")

for item in my_set:
    print(f"Current item is {item}")

for item in my_dict: # Iterating over keys
    print(f"Current item is {item}")

for key, value in my_dict.items():  # Iterating over key-value pairs
    print(f"Key: {key}, Value: {value}")
else:
    print("Finished iterating over the dictionary")

for i in range(5):  # Loop from 0 to 4
    print(f"Current index is {i}")

for i in range(1, 10, 2):  # Loop from 1 to 9 with a step of 2
    print(f"Current index is {i}")

# Nested loops
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print(f"Outer loop index: {i}, Inner loop index: {j}")
    print("Finished nested loops")

# List comprehensions
squared_numbers = [x**2 for x in range(10)]  # Create a list of squared numbers from 0 to 9
print(squared_numbers)

# Using a list comprehension with a condition
even_numbers = [x for x in range(20) if x % 2 == 0]  # Create a list of even numbers from 0 to 19
print(even_numbers)

