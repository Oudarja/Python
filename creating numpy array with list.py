import numpy as np
from numpy import *
list=[1,2,3,4,5,6]
arr=array(list)
print(arr);
'''creating 2d array '''
'''if two array element is not equal then 2 d array can not be
created'''
list=[[1,2,3,4],[5,6,7,8]]
arr=np.array(list);
print(arr);

'''creating array with full function'''
'''full(number_of_element,value)'''
matrix=np.full(5,10)
print(matrix)
'''creating 2 d with full'''
matrix=np.full((4,3),10)
print(matrix)

'''creating identity matrix'''
''' all diagonal value will be one'''
matrix=np.eye(3)
print(matrix)
'''creating diagonal matrix with given value'''
matrix=np.diag([4,5,6]);
print(matrix)
