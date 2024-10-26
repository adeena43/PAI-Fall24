import matplotlib.pyplot as plt

students = ["Student 1", "Student 2", "Student 3", "Student 4", "Student 5",
            "Student 6", "Student 7", "Student 8", "Student 9", "Student 10"]
math_marks = [78, 85, 96, 72, 88, 90, 65, 75, 80, 95]
science_marks = [82, 87, 94, 70, 85, 91, 68, 78, 83, 92]

plt.figure(figsize=(10, 6))
plt.scatter(math_marks, science_marks, color='blue', label="Students' Marks")

plt.title("Comparison of Marks in Mathematics and Science")
plt.xlabel("Mathematics Marks")
plt.ylabel("Science Marks")

plt.legend(loc="upper left")

plt.show()
