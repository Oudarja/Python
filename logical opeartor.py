num1=int(input("Enter 1st number: "))
num2=int(input("Enter 2nd number: "))
num3=int(input("Enter 3rd number: "))

if(num1>num2 and num1>num3):
    print(num1)
elif (num2>num1 and num2>num3):
    print(num2)
else:
    print(num3)

    #checking vowel consnonant
ch=input("Give one character")

if(not(ch=='a' or ch=='e' or ch=='o' or ch=='i' or ch=='u')):
    print("Consnonant")
else:
    print("vowel")
temparature=int(input())
if(temparature>=0 and temparature<=30):
    print("Go outside")
elif temparature>30 or temparature<0:
    print("Not go")
val=0;
if not(val):
    print("Hey")
else:
    print("Hello")
