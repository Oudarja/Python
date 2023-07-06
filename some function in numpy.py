import numpy as np

arr1=np.linspace(0,15,16)
print(arr1)
arr2=np.ones((4,3),int)
print(arr2)
print(arr1.ndim)
print(arr2.ndim)
print(arr2.size)
print(arr1.size)
print(arr2.shape)
print(arr1.shape)
'''printing with for loop'''
for data in arr1:
    print(data,end=" ")

print("")

'''printing with indexing'''
for i in range(len(arr1)):
    print(arr1[i],end=" ")
'''copying array'''
arr2=arr1.copy()
print("")
print(arr2)
'''reshaping array'''
arr1=arr1.reshape(2,8)
print(arr1)

arr1=arr1.reshape(4,4)
print(arr1)

'''making 2d array or more dimensional array in 1d array'''
arr1=arr1.ravel()
print(arr1);
''' arithmatic operation'''
print(arr1+arr1)
print(arr1-arr1)
print(arr1*arr1)
