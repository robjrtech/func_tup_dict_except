# print("Basic Addition")
# a = int(input("Pick a number: "))
# b = int(input("Pick a number: "))

# def add(a,b):
#     return a + b
# print(add(a,b))



# print("Basic Subtraction")
# a = int(input("Pick a number: "))
# b = int(input("Pick a number: "))

# def add(a,b):
#     return a - b
# print(add(a,b))



# print("Basic Multiplication")
# a = int(input("Pick a number: "))
# b = int(input("Pick a number: "))

# def add(a,b):
#     return a * b
# print(add(a,b))



# print("Basic Division")
# a = int(input("Pick a number: "))
# b = int(input("Pick a number: "))

# def add(a,b):
#     return a / b
# print(add(a,b))



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

