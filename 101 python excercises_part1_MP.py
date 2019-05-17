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