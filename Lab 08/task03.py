#Create 3x3 matrix containing only even numbers. Multiply each
#  element of this array with 4 and then multiply resultant 
# matrix with 3x3 identity matrix (identity matrix should not be hardcoded).

import numpy as np

matrix = np.arange(2, 19, 2).reshape(3, 3)
print(matrix)

matrix = matrix*4
print(matrix)

id = np.eye(3, 3)
print(id)
matrix = matrix*id
print(matrix)
