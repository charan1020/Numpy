# NumPy Practice Questions with Solutions
# Level: Basic to Advanced
# Use: Exams, Interviews, Hands-on Practice

import numpy as np

# Q1. Create a NumPy array from a Python list
arr1 = np.array([1, 2, 3, 4, 5])
print("Q1:", arr1)

# Q2. Create a 3x3 array of zeros
q2 = np.zeros((3, 3))
print("Q2:\n", q2)

# Q3. Create a 2x4 array filled with 7
q3 = np.full((2, 4), 7)
print("Q3:\n", q3)

# Q4. Create an identity matrix of size 4
q4 = np.eye(4)
print("Q4:\n", q4)

# Q5. Find the data type of array elements
q5 = arr1.dtype
print("Q5:", q5)

# Q6. Create an array from 10 to 50 with step 5
q6 = np.arange(10, 51, 5)
print("Q6:", q6)

# Q7. Create 6 evenly spaced numbers between 0 and 1
q7 = np.linspace(0, 1, 6)
print("Q7:", q7)

# Q8. Reshape a 1D array into 2x3
q8 = np.array([1, 2, 3, 4, 5, 6]).reshape(2, 3)
print("Q8:\n", q8)

# Q9. Find shape and dimensions
q9_shape = q8.shape
q9_dim = q8.ndim
print("Q9 Shape:", q9_shape, "Dimensions:", q9_dim)

# Q10. Access element 5 from array
q10 = np.array([[1, 2, 3], [4, 5, 6]])
print("Q10:", q10[1, 1])

# Q11. Element-wise addition of arrays
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print("Q11:", a + b)

# Q12. Multiply each element by 10 (broadcasting)
print("Q12:", a * 10)

# Q13. Sum, Mean, Max, Min
print("Q13 Sum:", np.sum(a))
print("Q13 Mean:", np.mean(a))
print("Q13 Max:", np.max(a))
print("Q13 Min:", np.min(a))

# Q14. Square root of elements
q14 = np.array([1, 4, 9, 16])
print("Q14:", np.sqrt(q14))

# Q15. Transpose of matrix
q15 = np.array([[1, 2], [3, 4]])
print("Q15:\n", q15.T)

# Q16. Generate 5 random integers between 1 and 100
print("Q16:", np.random.randint(1, 101, 5))

# Q17. Index of maximum value
q17 = np.array([10, 50, 30])
print("Q17:", np.argmax(q17))

# Q18. Matrix multiplication
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])
print("Q18:\n", np.dot(m1, m2))

# Q19. Determinant of a matrix
print("Q19:", np.linalg.det(m1))

# Q20. Replace values greater than 5 with 5
q20 = np.array([2, 6, 8, 4, 1])
q20[q20 > 5] = 5
print("Q20:", q20)
