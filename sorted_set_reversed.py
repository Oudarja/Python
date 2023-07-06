'''Using sorted():  sorted() is used to print the container is sorted order. It doesn’t sort the container but just prints the container in sorted order for 1 instance. The use of set() can be combined to remove duplicate occurrences.'''
lis = [1, 3, 5, 6, 2, 1, 3]
print("The list in sorted order is : ")
for i in sorted(lis):
    print(i, end=" ")

print('\r')


# using sorted() and set() to print the list in sorted order
# use of set() removes duplicates.
print("The list in sorted order (without duplicates) is : ")
for i in sorted(set(lis)):
    print(i, end=" ")
print('\r')

 #python code to demonstrate working of reversed()
# initializing list
lis = [1, 3, 5, 6, 2, 1, 3]
# using revered() to print the list in reversed order
print("The list in reversed order is : ")
for i in reversed(lis):
    print(i, end=" ")

print('\r')
print('\n')


'''The pass statement is a null statement. But the difference between pass and comment is that comment is ignored by the interpreter whereas pass is not ignored.
The pass statement is generally used as a placeholder i.e. when the user does not know what code to write. So user simply places pass at that line. Sometimes, pass is used when the user doesn’t want any code to execute. So user can simply place pass where empty code is not allowed, like in loops, function definitions, class definitions, or in if statements. So using pass statement user avoids this error.'''

li =['a', 'b', 'c', 'd']
for i in li:
    if(i =='a'):
        pass
    else:
        print(i)
