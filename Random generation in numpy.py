import numpy as np
'''creating 1d random array'''
arr=np.random.rand(5)
print(arr)
'''creating random 2d array'''
arr=np.random.rand(5,3)
print(arr)

'''creating random 3d array'''
arr=np.random.rand(5,3,2)
print(arr)
'''np.random.rand() create uniformal distribution of random
 random number but np.random.randn create normal distribution'''
arr=np.random.randn(5)
print(arr)

'''randomly number generated between in a range'''
''' randint(start,end-1,number of number to generated)'''
arr=np.random.randint(0,10,10)
print(arr)
''' Now 2d array of random number using randint'''
arr=np.random.randint(1,15,(4,4))
print(arr)
'''creating array with initial value one initial value will be float'''
arr=np.ones(4);
print(arr)
arr=np.ones(4,int)
print(arr);
''' Now 2d array with all one'''
arr=np.ones((5,5),int)
print(arr)
