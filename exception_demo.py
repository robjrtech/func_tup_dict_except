# Safe to divide function
def safe_divide(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b

# Pass: The safe divide function test
try:
    result = safe_divide(30,5)
    print("Result:", result)
except ValueError as error:
    print("Error: ", error)
finally:
    print("Division operation completed")

# Failed: The safe divide function test
try:
    result = safe_divide(10,0)
    print("Result:", result)
except ValueError as zero_error:
    print("Error:", zero_error)
finally:
    print("Division operation completed")

# Catching a generic Exception
try:
    result = safe_divide(10, "2")
except Exception as error:
    print("Something went wrong:", error)