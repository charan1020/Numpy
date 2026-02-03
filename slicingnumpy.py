import numpy as np
array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])
#array[start:end:step] here step is optional
print(array[-2])
print(array[0:3])
print(array[0:4:2])
print(array[::-1]) #reversing the array
print(array[:,::-1]) #reversing each row of the array
print(array[::2,:]) #accessing alternate rows
print(array[:,::2]) #accessing alternate columns
print(array[1:3,1:3]) #accessing sub array
print(array[::2,::2]) #accessing alternate rows and alternate columns
print(array[1:4:2,0:4:2]) #accessing alternate rows and alternate columns in the specified range
print(array[::3,::3]) #accessing every third row and every third column
print(array[1:,:3]) #accessing from second row to end and first three columns
print(array[:3,1:]) #accessing first three rows and from second column to end
