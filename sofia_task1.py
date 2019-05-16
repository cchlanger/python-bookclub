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

#Q10_Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
a = np.array([1,2,3])
np.hstack([np.repeat(a,3),np.concatenate([a,a,a])])

#Q11_Get the common items between a and b
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a,b)

#Q12_From array a remove all items present in array b
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
a[b[np.searchsorted(b,a)] != a]

#Q13_Get the positions where elements of a and b match
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
np.where(a == b)

#Q14_Get all items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
a [np.where ((a>=5) & (a<=10))]

#Q15_Convert the function maxx that works on two scalars, to work on two arrays.
#Q16_Swap columns 1 and 2 in the array arr.
arr = np.arange(9).reshape(3,3)
arr[:, [1,0,2]]

#Q17_Swap rows 1 and 2 in the array arr
arr = np.arange(9).reshape(3,3)
arr [[1,0,2],:]

#Q18_Reverse the rows of a 2D array arr.
arr = np.arange(9).reshape(3,3)
arr [[2,1,0],:]
#arr [::-1]

#Q19_Reverse the columns of a 2D array arr.
arr = np.arange(9).reshape(3,3)
arr [:,::-1]

#Q20_Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.
np.random.uniform (5,10, (5, 3))

#Q21_Print or show only 3 decimal places of the numpy array rand_arr.
rand_arr = np.random.random((5,3))
np.around(rand_arr,3)
#np.set_printoptions(precision=3)

#Q22_Pretty print rand_arr by suppressing the scientific notation (like 1e10)
np.random.seed(100)
rand_arr = np.random.random([3,3])/1e3
print (rand_arr, "")
#np.set_printoptions(suppress=True, precision = 6)

#Q23_Limit the number of items printed in python numpy array a to a maximum of 6 elements.
np.set_printoptions(threshold = 6)
a = np.arange(15)
a

#Q24_Print the full numpy array a without truncating.
np.set_printoptions(threshold= 1000)
a = np.arange(15)
a
#np.set_printoptions(threshold=np.nan)

#Q25_Import the iris dataset keeping the text intact.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')
iris [:3]
#Q26_Extract the text column species from the 1D iris imported in previous question.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
species = iris [:,4]
species [:5]

#Q27_Convert the 1D iris to 2D array iris_2d by omitting the species text field.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
iris_2d = np.array([row.tolist()[:4] for row in iris_1d])
iris_2d [:4]
#iris_1d = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0,1,2,3])
#iris_2d[:4]

#Q28_Find the mean, median, standard deviation of iris's sepallength (1st column)
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='float')
sepallength = np.array([row.tolist()[:1] for row in iris])
sepallength.mean()
np.median(sepallength)
sepallength.std()