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
np.set_printoptions(threshold=1000)
print(a)
# using threshold=np.nan (suggested solution) raises error

# Q25. Import the iris dataset keeping the text intact.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
# Since we want to retain the species, a text field, I have set the dtype to object.
# Had I set dtype=None, a 1d array of tuples would have been returned.

# Q26. Extract the text column species from the 1D iris imported in previous question.
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
species = np.array([row[4] for row in iris_1d])

# Q27. Convert the 1D iris to 2D array iris_2d by omitting the species text field.
iris_2d = np.array([row.tolist()[:4] for row in iris_1d])

# Q28. Find the mean, median, standard deviation of iris's sepallength (1st column)
sepallen = np.array([row[0] for row in iris_1d])
mu, med, sd = np.mean(sepallen), np.median(sepallen), np.std(sepallen)
# alternatively,
sepallen = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

# Q29. Create a normalized form of iris's sepallength whose values range exactly between 0 and 1
# so that the minimum has value 0 and maximum has value 1.
S = (sepallen - sepallen.min())/(sepallen.max() - sepallen.min())


# Q30. Compute the softmax score of sepallength.
def softmax(x):
    """Compute softmax values for each sets of scores in x.
    Turns numbers into probabilities that sum to one. >> PDF?"""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)


softmax(sepallen)

# Q31. Find the 5th and 95th percentile of iris's sepallength
np.percentile(sepallen, q=[5, 95])

# Q32. Insert np.nan values at 20 random positions in iris dataset
i, j = np.where(iris)
# i, j contain the row and column numbers of iris
np.random.seed()
iris[np.random.choice((i), 20), np.random.choice((j), 20)] = np.nan
# alternatively,
nrow, ncol = iris.shape
iris[np.random.randint(nrow, size=20), np.random.randint(ncol, size=20)] = np.nan

# Q33. Find the number and position of missing values introduced in iris_2d's sepallength (1st column)
iris_2d[np.random.randint(150, size=20), np.random.randint(4, size=20)] = np.nan
print("Number of missing values: \n", np.isnan(iris_2d[:, 0]).sum())
print("Position of missing values: \n", np.where(np.isnan(iris_2d[:, 0])))

# Q34. Filter the rows of iris_2d that has
# petallength (3rd column) > 1.5 and sepallength (1st column) < 5.0
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
iris_2d[np.where((iris_2d[:, 0] < 5.0) & (iris_2d[:, 2] > 1.5))]

# Q35. Select the rows of iris_2d that does not have any nan value.
nrow, ncol = iris_2d.shape
iris_2d[np.random.randint(nrow, size=50), np.random.randint(ncol, size=50)] = np.nan
any_nan_in_row = np.array([~np.any(np.isnan(row)) for row in iris_2d])
iris_2d[any_nan_in_row][:ncol]

# Q36. Find the correlation between SepalLength(1st column) and PetalLength(3rd column) in iris_2d
iris_2d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0, 1, 2, 3])
np.corrcoef(iris_2d[:, 0], iris_2d[:, 2])[0, 1]

# Q37. Find out if iris_2d has any missing values.
iris_2d[np.random.randint(nrow, size=5), np.random.randint(ncol, size=5)] = np.nan
np.isnan(iris_2d).any()

# Q38. Replace all ccurrences of nan with 0 in numpy array
zeroed = np.where(np.isnan(iris_2d), 0, iris_2d)
print(np.isnan(iris_2d).any(), np.isnan(zeroed).any())
