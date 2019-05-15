print("hello")

import numpy as np

# Create a 3×3 numpy array of all True’s
a = np.full((3,3),True)

#Q. Extract all odd numbers from arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
new_arr = arr[arr % 2 == 1]

#Q. Replace all odd numbers in arr with -1
new_arr = arr[arr % 2 == 1]
arr [new_array] = -1

#Q. Replace all odd numbers in arr with -1 without changing arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr.copy()
arr[arr % 2 ==1]

#Q. Convert a 1D array to a 2D array with 2 rows
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]).reshape((2,5))

#Q. Stack arrays a and b vertically
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
np.concatenate ([a,b], axis = 0)

#Q. Stack the arrays a and b horizontally.
a = np.arange(10).reshape(2,-1)
b = np.repeat(1, 10).reshape(2,-1)
np.concatenate ([a,b], axis = 1)

#Q. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
a = np.array([1,2,3])
np.hstack([np.repeat(a,3),np.concatenate([a,a,a])])

#Q. Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

#Q. From array a remove all items present in array b
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
a[b[np.searchsorted(b,a)] != a]

#Q. Get the positions where elements of a and b match
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a == b)

#Q. Get all items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
a [np.where ((a>=5) & (a<=10))]

#Q. Convert the function maxx that works on two scalars, to work on two arrays.
#Q. Swap columns 1 and 2 in the array arr.
arr = np.arange(9).reshape(3,3)