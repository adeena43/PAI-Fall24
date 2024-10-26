import matplotlib.pyplot as plt

student_names = [
    "Adina", "Sara", "Hafsa", "Arwa", "Raghib",
    "Abdul Rahman", "Fahad", "Talha", "Umar", "Saif",
    "John", "Rehan", "Maria", "Kahsif", "Rizwan",
    "Rubab", "Laiba", "Amna", "Alisha", "Romaisa"
]
heights = [160, 155, 170, 165, 172, 168, 158, 174, 162, 169, 164, 160, 170, 167, 165, 159, 175, 168, 166, 161]

colors = [
    "blue", "orange", "green", "red", "purple", "brown", "pink", "gray", "olive", "cyan",
    "magenta", "yellow", "teal", "lightblue", "darkgreen", "lightgreen", "navy", "coral", "skyblue", "lime"
]

plt.figure(figsize=(12, 6))
plt.bar(student_names, heights, color=colors)
plt.xlabel("Students")
plt.ylabel("Height (cm)")
plt.title("Student Heights - Bar Chart")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(heights, labels=student_names, colors=colors, autopct='%1.1f%%', startangle=140)
plt.title("Student Heights - Pie Chart")
plt.show()
