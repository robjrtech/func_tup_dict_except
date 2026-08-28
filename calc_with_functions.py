# Ask user for 2 input
print("Basic Addition")
a = int(input("Pick a number: "))
b = int(input("Pick a number: "))

# Addition: Evaluates the numbers provided 
def add(a,b):
    return a + b
print(add(a,b))

# Ask user for 2 input
print("Basic Subtraction")
a = int(input("Pick a number: "))
b = int(input("Pick a number: "))

# Subtraction: Evaluates the numbers provided 
def add(a,b):
    return a - b
print(add(a,b))


# Ask user for 2 input
print("Basic Multiplication")
a = int(input("Pick a number: "))
b = int(input("Pick a number: "))

# Multiplication: Evaluates the numbers provided 
def add(a,b):
    return a * b
print(add(a,b))

# Ask user for 2 input
print("Basic Division")
a = int(input("Pick a number: "))
b = int(input("Pick a number: "))

# Division: Evaluates the numbers provided 
def divide(a,b):
    return a / b
print(divide(a,b))

# Ask user for 3 inputs
# Evaluates the numbers provided and math symbol. 
# Validates if the user is not dividing by zero by using a try/except logic 
print("Basic Calculator")
a = int(input("Pick a number: "))
o = input("Pick a symbol (+, - , *, /): ")
b = int(input("Pick a number: "))

def calc(a,o,b):
        if o == "+":
            return a + b
        elif o == "-":
            return a - b
        elif o == "*":
            return a * b
        try:
            o == "/"
            return a / b
        except ZeroDivisionError:
            print("Sorry you cannot divide by zero")
print(calc(a,o,b))

