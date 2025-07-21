def sum (a, b):
    return a + b

def res (a, b):
    return a - b

def mult (a, b):
    return a * b

def div (a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"