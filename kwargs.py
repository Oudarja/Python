#kwargs= parameters that will pack all arguments in to a dictionary
#        useful so that a function can accpet a varying amount of keyword argument
def hello(**kwargs):
    print("Hello")
    for key,value in kwargs.items():
        print(value)
hello(first="Bro",middle="dude",last="Code")
