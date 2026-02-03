import numpy as np
#for 2d array we use two square brackets inside the main square brackets
#for 3d array we use three square brackets inside the main square brackets
array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['J','K','L'],['M','N','O'],['P','Q','R']],
                 [['S','T','U'],['V','W','X'],['Y','Z',' ']]])
print(array.ndim)
print(array.shape)
print(array[0][0][0]) # Accessing element A #here first 0 is for first 2d array, second 0 is for first row, third 0 is for first column
print(array[0][2][2]) # Accessing element I
print(array[2][0][0])
word =array[0,0,0] +array[2,0,0]+array[2,0,0]
print(word)