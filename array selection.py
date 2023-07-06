import numpy as np

arr=np.random.randint(1,15,(6,5))
print(arr)
arr1=arr[0:4,0:3]
print(arr1)

arr2=arr[4:,]
print(arr2)
arr3=arr[3:5,2:4]
print(arr3)
arr4=arr1>6
print(arr4)
