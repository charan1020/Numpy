#broadcasting allows numpy to perform operations on arrays
#of different shapes in a way that makes sense mathematically.
#When operating on two arrays, numpy compares their shapes element-wise.
import numpy as np
'''
array1=np.array([[1,2,3,4]]) #2d array of shape (1,4)
array2 =np.array([[1],[2],[3],[4]])
print(array1.shape)
print(array2.shape)
print(array1 * array2)
'''
array=np.array([[1,2,3,4,5,6,7,8,9,10]])
array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
print(array*array2)