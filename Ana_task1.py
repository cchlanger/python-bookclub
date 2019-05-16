import numpy as np
print(np.__version__)

# Q2. Create a 1D array of numbers from 0 to 9
arr1 = np.arange(10)

# Q3. Create a 3×3 numpy array of all True’s
arr2 = np.full((3, 3), True, dtype=bool)

# Q4. Extract all odd numbers from arr
arr1[arr1 % 2 == 1]

# Q5. Replace all odd numbers in arr with -1
arr1[arr1 % 2 == 1] = -1

# Q6. Replace all odd numbers in arr with -1 without changing arr
arr1 = np.arange(10)
arr3 = np.where(arr1 % 2 == 1, -1, arr1)

# Q7. Convert a 1D array to a 2D array with 2 rows
arr4 = arr1.reshape(2, -1)

# Q8. Stack arrays a and b vertically
a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)
arr5 = np.concatenate([a, b])

# Q9. Stack the arrays a and b horizontally.
arr6 = np.concatenate([a, b], axis=1)

# Q10. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
a = np.array([1, 2, 3])
arr7 = np.concatenate([np.repeat(a, 3), np.tile(a, 3)])

# Q11. Get the common items between a and b
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
np.intersect1d(a, b)
