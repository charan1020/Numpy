import numpy as np
#scalar arithmetic it is a single value operation on each element of the array
'''
array=np.array([1,2,3])
print(array+1)
print(array-2)
print(array*3)
print(array/4)
print(array**5)'''

#vectorized math funcs
'''
array=np.array([1.01,2.5,3.99])
print(np.sqrt(array))
print(np.round(array)) #rounding off the values
print(np.floor(array)) #floor is the greatest integer less than or equal to the value
print(np.ceil(array)) #ceil is the smallest integer greater than or equal to the value
print(np.exp(array)) #e raised to the power of each element
print(np.log(array)) # log is the natural logarithm (base e)
print(np.sin(array)) 
print(np.pi/2)

raddi=np.array([1,2,3])
print(np.pi*raddi**2) #area of circle =pi*r^2
print(2*np.pi*raddi) #circumference of circle =2*pi*r
print((4/3)*np.pi*raddi**3) #volume of sphere =(4/3)*pi*r^3
print(4*np.pi*raddi**2) #surface area of sphere =4*pi*r^2
print((4/3)*np.pi*raddi**3/(4*np.pi*raddi**2)) #ratio of volume to surface area of sphere =r/3
'''
#element wise array arithmetic
''''
array1=np.array([1,2,3])
arra2=np.array([4,5,6])
print(array1+arra2)
print(array1-arra2)
print(array1*arra2)
print(array1/arra2)
print(array1**arra2)
'''

#comparison operations
scores=np.array([91,55,100,73,82,64])
scores[scores<60]=0
print(scores)
print(scores==100)
print(scores>=60)


