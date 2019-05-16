import numpy as np

# bool array

b = np.ones((3, 3), dtype=bool)

# extract odd numbers

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
odd = arr[np.mod(arr, 2) == 1]

# replace ood numbers with -1

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = arr.copy()
out[np.mod(out, 2) == 1] = -1

# reshape array

arr = np.arange(10)
out = arr.reshape((2, 5))

# stack vertically

a = np.arange(10).reshape(2, -1)
b = np.repeat(1, 10).reshape(2, -1)

c = np.vstack((a, b))

# stack horizontally

d = np.hstack((a, b))

# create sequences without hardcoding

a = np.array([1, 2, 3])

out = np.concatenate((np.repeat(a, 3), np.tile(a, 3)))

# common numbers v1

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

out = set(a) & set(b)

# common numbers v2

out = np.unique(a[np.isin(a, b)])

# find positions where two arrays match

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])

out = np.nonzero([a == b])

# convert scalar to vecotrized function


def maxx(x, y):
    """Get the maximum of two items"""
    temp = np.vstack((x, y))
    return np.max(temp, axis=0)


maxx(a, b)

# swap columns

arr = np.arange(9).reshape(3, 3)
temp = arr.copy()
arr[:, 0], arr[:, 1] = temp[:, 1], temp[:, 0]

arr = arr[:, [1, 0, 2]]

# reverse rows

arr = arr[::-1, :]

# print only 3 decimal places

rand_arr = np.random.random((5, 3))

# load in iris dataset

test = np.genfromtxt("iris.data", dtype=(np.float, np.float, np.float,
                                         np.float, "U10"), delimiter=",")
test["f4"]

# convert to 2d

url = ("https://archive.ics.uci.edu/ml/"
       "machine-learning-databases/iris/iris.data")
iris_1d = np.genfromtxt(url, delimiter=',', dtype=None)
iris_2d = []

# make strides
arr = np.arange(15)
# create arange objects

out = []

for i in range(0, len(arr) - 4, 2):
    out.append(np.arange(i, i + 4))
fin = np.vstack(out)
