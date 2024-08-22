
marks_dict = {}
for i in range(1, 4):
    subject = input(f"Enter the name of subject {i}: ")
    marks = float(input(f"Enter the marks for {subject}: "))
    marks_dict[subject] = marks

total_marks = sum(marks_dict.values())

average = total_marks / len(marks_dict)

percentage = (total_marks / (100 * len(marks_dict))) * 100

print("\nMarks Dictionary:")
for subject, marks in marks_dict.items():
    print(f"{subject}: {marks}")

print(f"\nTotal Marks: {total_marks}")
print(f"Average Marks: {average:.2f}")
print(f"Percentage: {percentage:.2f}%")
