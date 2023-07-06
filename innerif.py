num1=input("Enter 1st number: ")
num2=input("Enter 2nd number: ")
num3=input("Enter 3rd number: ")
if(num1>num2):
    if(num1>num3):
        print(f"{num1} is the greatest")
    else:
        print(f"{num3} is the greatest")
else:
    if(num2>num3):
        print(f"{num2} is the greatest")
    else:
        print(f"{num3} is the greatest")
