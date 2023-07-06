''' enumerate() is used to loop through the containers printing the index number along with the value present in that particular index.'''


for (key,value) in enumerate(['The','Big','Bang','Theory']):
    print(key,value)
''' for printing value in specific distance from each other'''
for key, value in enumerate(['Geeks', 'for', 'Geeks','is', 'the', 'Best','Coding', 'Platform']):
    print(value, end='   ')

    '''using zip to combine two similliar list he loop exists only till the smaller container ends. A detailed explanation of zip() and enumerate() can be found'''

    questions = ['name', 'colour', 'shape']
    answers = ['apple', 'red', 'a circle']

# using zip() to combine two containers
# and print values
for question, answer in zip(questions, answers):
    print('What is your {0}?  I am {1}.'.format(question, answer))


    # python code to demonstrate working of items()

d = {"geeks": "for", "only": "geeks"}
    #key    :  value
print("The key value pair using items is : ")
for i, j in d.items():
    print(i, j)
