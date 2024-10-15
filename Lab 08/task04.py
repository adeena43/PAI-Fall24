import numpy as np

dtype = [('name', 'U10'), ('height', 'f4'), ('class', 'i4')]

students = np.array([('John', 5.9, 10),
                     ('Susan',5.5, 9),
                     ('Michael', 6.0, 10),
                     ('Jackson', 6.2, 10),
                     ('Mary', 5.2, 9)], dtype = dtype)

sorted_students = np.sort(students, order = ['class', 'height'])

print(students)
print(sorted_students)
