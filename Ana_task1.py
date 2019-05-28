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

# Q12. From array a remove all items present in array b
a = np.array([1, 2, 3, 4, 5])
b = np.array([5, 6, 7, 8, 9])
np.setdiff1d(a, b)

# Q13. Get the positions where elements of a and b match
a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
np.where(a == b)

# Q14. Get all items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
a[(a >= 5) & (a <= 10)]

# Q15. Convert the function maxx that works on two scalars, to work on two arrays.
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y


maxx(1, 5)

def pair_max(a, b):
    """Compare two arrays element-wise, return maximum"""
    return np.where(a > b, a, b)


a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max(a, b)

# Q16. Swap columns 1 and 2 in the array arr.
arr8 = np.arange(9).reshape(3, 3)
arr8[:, [1, 0, 2]]

# Q17. Swap rows 1 and 2 in the array arr:
arr8[[1, 0, 2], :]

# Q18. Reverse the rows of a 2D array arr.
arr8[::-1, :]

# Q19. Reverse the columns of a 2D array arr.
arr8[:, ::-1]

# Q20. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.
arr9 = np.random.uniform(5, 10, size=(5, 3))

# Q21. Print or show only 3 decimal places of the numpy array rand_arr.
np.set_printoptions(precision=3)
print(arr9)

# Q22. Pretty print rand_arr by suppressing the scientific notation (like 1e10)
np.random.seed(100)
rand_arr = np.random.random([3, 3])/1e3
np.set_printoptions(suppress=True)
print(rand_arr)

# Q23. Limit the number of items printed in python numpy array a to a maximum of 6 elements.
a = np.arange(15)
np.set_printoptions(threshold=6)
print(a)

# Q24. Print the full numpy array a without truncating.
np.set_printoptions(threshold=np.nan)
print(a)
