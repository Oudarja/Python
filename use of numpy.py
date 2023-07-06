import numpy as np
arr=np.array([2,3,8,9,7])
print(arr)
print(arr.dtype)

'''For changing one element in array whole array data type has been
 changed'''
arr=np.array([2,3,8,9,7.5])
print(arr);
print(arr.dtype);

'''array type declaration when array is created'''
'''Now if i want to change any element in another data type
 then also type can not be changed'''
arr=np.array([2,3,4,8,5.5],int)
print(arr);
print(arr.dtype);

'''creating array with line space'''
'''linspace(start,end,parts)'''
arr=np.linspace(0,15,100);
print(arr)

'''creating array with arange function'''
'''arange(start,end-step,step)'''
arr=np.arange(1,15,2);
print(arr);

'''with out step default value is 1'''
arr=np.arange(1,15);
print(arr);

'''creating array with zeroes with initial value'''
arr=np.zeros(5);
print (arr);


'''creating array with type '''
arr=np.zeros(5,float);
print(arr);


'''' creating 2d array with zeros'''
arr=np.zeros((4,3),int);
print(arr);
'''' creating 3d array with zeros'''
arr=np.zeros((4,3,2,3),int);
print(arr);
