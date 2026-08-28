# This function ask the user for their name and greets them.
def greet_user():
    name = input("Hello, please enter your name? ")
    if name == None:
        print("Hello! Welcome!")
    else:
        print(f"Hello, {name}! Welcome")
greet_user()


def add_two_numbers():
    print("Basic addition.")
    a = int(input("Pick a number: "))
    b = int(input("Pick a number: "))
    return a + b

result = add_two_numbers()
print("The sum is:", result)



def is_even():
    num = float(input("Is your number divisible by 2? "))
    if num % 2 == 0:
        print(f"{num} is even: True")
        return True
    else:
        print(f"{num} is odd: False")
        return False

result = is_even() 
if result == True: 
    print("True")
elif result == False:
    print("False")
else:
    print("Try again!")
