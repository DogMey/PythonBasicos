my_dict  = dict()
print(type(my_dict))  # This is an empty dictionary

my_dict = {
    "name": "Kevin", 
    "age": 30, 
    "city": "Bogota",
    "last_name": "Ramirez",
    1 : "Python",
    2 : "JavaScript"
}

my_other_dict = {
    "name": "DogMey",
    "age": 5,
    "city": "Bogota",
    "last_name": "Ramirez",
    "lenguages": {"Python", "JavaScript"},
    "pets": ["Max", "Maya", "Tony"]
}

print(my_dict)
print(my_other_dict)

print(my_dict["name"])  # Access value by key
print(my_other_dict["lenguages"])  # Access value by key

my_dict["name"] = "Santiago"  # Modify value by key
print(my_dict)

my_dict["country"] = "Colombia"  # Add new key-value pair
print(my_dict)

my_dict.pop("age")  # Remove key-value pair by key
print(my_dict)

print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_other_dict.items())  # Get all key-value pairs

print("name" in my_dict)

print(my_dict.setdefault("country", "USA"))  # Set default value if key does not exist
print(my_dict.fromkeys(["name", "age"], "Hola"))  # Create a new dictionary with default values