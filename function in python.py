#function=a function is block of code which is executed when it is called
'''keyword argument= argument preceded by an identifier when we pass them to a function
                   The order of argument does not matter.Unlike positional argument python knows the order of argument that dunction receives'''
def hello(first_name,last_name,year):
    print("Hello "+first_name+" "+last_name)
    print("You are "+str(year)+" years old")
    print("Have a nice day")

def multiply(a,b):
    return a*b
def checkkeywordargument(**kwargs):
    for key, value in kwargs.items():
        print ("%s == %s" %(key, value))
hello("Bro","code",23)
print(multiply(2,3))
#nensted function call
print(round(abs(float(input("Enter a whole positive number: ")))))
#args parameter in python
#args=parameters that will pack all argument into a tuple useful so that a function can #accpet a varying  amount of argument
def add(*stuff):
    sum=0
    for i in stuff:
        sum+=i
    return sum

print(add(1,3,2,4))
