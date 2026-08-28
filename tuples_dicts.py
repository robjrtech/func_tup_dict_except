months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")

print(months[0],months[-1])

try:
    months[2] = "April"
except TypeError:
    print("Tuples are immutable: <error message>")


students = {
    "John": 90,
    "Chris": 75,
    "Sarah": 88,
    "Lan": 98
}
print(students)
students["Rex"] = 80
students["Chris"] = 83
print(students)

for name, grade in students.items():
    print(f'{name}: {grade}')