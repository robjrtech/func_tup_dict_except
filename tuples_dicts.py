# Tuple of the months
months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

# Display the first and last month
print(months[0],months[-1])

# Demonstrates that tuples are immutable
try:
    months[2] = "April"
except TypeError:
    print("Tuples are immutable: <error message>")

# Dictionary of (Key)students with a (Value)grade
students = {
    "John": 90,
    "Chris": 75,
    "Sarah": 88,
    "Lan": 98
}
# Display the students
print(students)

# Adding another key-value to the dictionary
students["Rex"] = 80

# Demonstrates that dictionaries are mutable
students["Chris"] = 83
print(students)

# Demonstrates unpacking a dictionary and display the name and grade for each student using a for loop
for name, grade in students.items():
    print(f'{name}: {grade}')