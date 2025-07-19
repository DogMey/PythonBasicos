my_tuple = tuple()
my_other_tuple = ()

my_tuple = (22, 1.62, "Kevin", "DogMey")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[1:3])
print(my_tuple[-1])

print(my_tuple.index("Kevin"))
print(my_tuple.count("Kevin"))

# This will raise a TypeError because tuples are immutable
# my_tuple[1] = 1.63

my_other_tuple = (1, 2, 3, 4, 5)

my_sum_tuple = my_tuple + my_other_tuple
print(my_sum_tuple)

list(my_sum_tuple)  # Convert tuple to list
print(type(list(my_sum_tuple)))