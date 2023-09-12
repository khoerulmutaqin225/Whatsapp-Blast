import numpy as np
from scipy import linalg

# Matriks A
A = np.array([[1, 2], [3, 4]])

# Invers matriks A
inv_A = linalg.inv(A)

# Matriks b sebagai array 2D
b = np.array([[5, 6]])

# Transposisi matriks b
b_T = b.T

# Perkalian elemen-wise antara A dan b
element_wise_product = A * b

# Perkalian matriks antara A dan b_T
matrix_product = A.dot(b_T)

# Matriks b sebagai array 1D
b_1D = np.array([5, 6])

# Perkalian matriks antara A dan b_1D
matrix_product_1D = A.dot(b_1D)

print("Matriks A:\n", A)
print("\nInvers Matriks A:\n", inv_A)
print("\nMatriks b (array 2D):\n", b)
print("\nTransposisi Matriks b:\n", b_T)
print("\nPerkalian Elemen-wise antara A dan b:\n", element_wise_product)
print("\nPerkalian Matriks antara A dan b_T:\n", matrix_product)
print("\nMatriks b (array 1D):\n", b_1D)
print("\nPerkalian Matriks antara A dan b_1D:\n", matrix_product_1D)
