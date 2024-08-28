
student_grades = {
    "Ashar": [29, 55, 78],
    "Rumana": [56, 66, 45],
    "Fayaz": [67, 88, 79]
}

def add_grade():
    """Add a new grade to Ashar's list of grades."""
    student_name = "Ashar"
    grade = 85
    if student_name in student_grades:
        student_grades[student_name].append(grade)
        print(f"Added grade {grade} for {student_name}.")
    else:
        print(f"Student {student_name} not found.")

def calculate_average():
    """Calculate and print the average grade for Ashar."""
    student_name = "Ashar"
    if student_name in student_grades:
        grades = student_grades[student_name]
        average = sum(grades) / len(grades)
        print(f"Average grade for {student_name} is {average:.2f}.")
    else:
        print(f"Student {student_name} not found.")

def add_student():
    """Add a new student named Sarah with an initial empty list of grades."""
    student_name = "Sarah"
    if student_name not in student_grades:
        student_grades[student_name] = []
        print(f"Added new student {student_name}.")
    else:
        print(f"Student {student_name} already exists.")

def remove_student():
    """Remove student Fayaz from the dictionary."""
    student_name = "Fayaz"
    if student_name in student_grades:
        del student_grades[student_name]
        print(f"Removed student {student_name}.")
    else:
        print(f"Student {student_name} not found.")
add_grade()
calculate_average()
add_student()
remove_student()
print("\nUpdated student grades:")
for student, grades in student_grades.items():
        print(f"{student}: {grades}")
