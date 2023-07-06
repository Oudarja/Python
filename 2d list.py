#2d list in python
drinks=["coffe","soda","tea"]
dinner=["pizza","humburger","hotdog"]
dessert=["cake","icecream"]
food=[drinks,dinner,dessert]

for i in food:
    for j in i:
        print(j,end=" ")
    print()
#tuples in python .Tuples are unchangeable
student=("Bro",21,"male")
print(student.count("Bro"))
print(student.index("male"))
for x in student:
    print(x)
