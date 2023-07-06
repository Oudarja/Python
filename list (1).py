number=[2,3,2,11]
print(number);
'''append 2 to list'''
number.append(2)
print(number)
number.sort()
print(number)
number.reverse()
print(number)
'''it will pop from the last element form the list'''
number.pop();
print(number)
'''copy all items to number2'''
number2=number.copy()
print(number2)
'''clear all terms of number2'''
number2.clear()
print(number2)
'''find the nearest position of 2'''
pos=number.index(2);
print(pos)
