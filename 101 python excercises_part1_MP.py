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
#14. Q. Get all items between 5 and 10 from a.
a = np.array([2, 6, 1, 9, 10, 3, 27])
b = np.where((a>=5) & (a<=10))
a[b]
#15. Convert the function maxx that works on two scalars, to work on two arrays.
def maxx(x, y):
    """Get the maximum of two items"""
    if x >= y:
        return x
    else:
        return y
pair_max = np.vectorize (maxx, otypes=[float])
a = np.array([5, 7, 9, 8, 6, 4, 5])
b = np.array([6, 3, 4, 8, 9, 7, 1])
pair_max(a,b)
#16. Swap columns 1 and 2 in the array arr
arr = np.arange(9).reshape(3,3)
arr
arr[:, (1,0,2)]
#17. Swap rows 1 and 2 in the array arr
arr = np.arange(9).reshape(3,3)
arr[(1,0,2),:]
#18. Reverse the rows of a 2D array arr
arr = np.arange(9).reshape(3,3)
arr[(2,1,0),:]#my solution
arr[::-1]#their solution
#19. Reverse the columns of a 2D array arr.
arr[:,(2,1,0)] #my solution
arr[:, ::-1] #their solution
#20. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10
rand_arr = np.random.randint(low=5, high=10, size=(5,3)) + np.random.random((5,3))