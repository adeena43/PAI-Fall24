import numpy as np

arr = [2, 5, 9, 10]
matrix = np.random.choice(arr, size = (4,4))
print(matrix)

id = np.eye(4, 4)
mul = matrix*id
print(mul)

odd = np.arange(1, 32, 2).reshape(4,4)
final = odd*mul
print(final)
