my_set = set()
my_set = {"Kevin", "DogMey", 5}

print(type(my_set))

my_other_set = {}
print(type(my_other_set)) # This is actually a dictionary, not a set

my_other_set = {"Kevin", "DogMey", 5}
print(type(my_other_set)) # Now this is a set

print(len(my_other_set))  # Get the number of elements in the set
print(my_other_set)

# print(my_other_set[0]) # This will raise a TypeError because sets are unordered

my_other_set.add("Ramirez")  # Add an element to the set
print(my_other_set)

# The set use a hash table, so it does not allow duplicate elements
my_other_set.add("Kevin")  # Adding a duplicate element has no effect
print(my_other_set) # The set remains unchanged

# Is for that reason that the order of elements in a set is not guaranteed!!!!!!!

my_other_set.remove("Kevin") # Remove an element from the set
print(my_other_set)

print("Kevin" in my_other_set) # Check if an element is in the set
print("DogMey" in my_other_set)

my_other_set.clear()  # Clear all elements from the set
print(my_other_set)

del my_other_set  # Delete the set
# print(my_other_set)  # This will raise a NameError because the set no longer

my_other_set = {"Java", "Javascript", "Python"}
my_other_set = my_other_set.union(my_set)  # Union with another set (my_set is empty)
print(my_other_set)