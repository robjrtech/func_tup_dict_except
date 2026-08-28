course_grades = {
    "Math": (88,100,72,78,88,68,66,92),
    "Science": (75,80,69,70,90,100,85),
    "History": (90,56,72,70,80,100,93),
    "Physical-Education": (100,72,70,80,100,93),
    "English": (92,72,78,88,68,66,92),
    "Robotics": (),
}

def get_average_grade(grades_tuple):
    try:
        average = sum(grades_tuple) / len(grades_tuple)
        return average
    except ZeroDivisionError:
        print("Warning: There are no grades in this tuple.")
        return None

for course, grades_tuple in course_grades.items():
    average = get_average_grade(grades_tuple)

    if average is not None:
        print(f"The average grade for {course} is {average:.1f}")
    else:
        print(f"No average grade available for {course}.")