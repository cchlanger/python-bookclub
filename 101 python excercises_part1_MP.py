import numpy as np
print(np.__version__)
np.arrange(0,10,1)
np.ones((3,3), dtype=np.bool_)
np.ones((3,3), dtype=bool)
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[1::2]
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr[1::2]=-1
arr
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
arr_copy=arr.copy()
arr_copy[1::2]=-1
arr
arr_copy
arr=np.arange(10)
arr.reshape((2,5))
np.vstack([a,b])
np.hstack([a,b])
np.r_[np.repeat(a, 3), np.tile(a, 3)]
#11. How to get the common items between two python numpy arrays?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c=np.intersect1d(a,b) #not from the book
c
#12. How to remove from one array those items that exist in another?
a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])
c = np.setdiff1d(a,b) #still didn't figure that out myself
#13. How to get the positions where elements of two arrays match?
a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])
c= np.where(a==b)
c #still couldn't find the proper function