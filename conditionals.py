my_condition = True

if my_condition:
    print("Condition is True")

my_condition = 5+3

if my_condition: # Evaluates to True since 8 is a non-zero value
    print("Condition is True")

if my_condition > 6:  # Explicitly checking the condition
    print("Is higher than 6")
else:
    print("Is not higher than 6")

my_condition = 5

if my_condition > 10 and my_condition < 20:
    print("Is between 10 and 20")
else:
    print("Is not between 10 and 20")

if my_condition > 10 and my_condition < 20:
    print("Is between 10 and 20")
elif my_condition == 5:
    print("Is 5")
else:
    print("Is not between 10 and 20 or 5")

my_string = ""

if my_string:  # Empty string evaluates to False
    print("String is not empty")

if not my_string:  # Checking if the string is empty
    print("String is empty")

