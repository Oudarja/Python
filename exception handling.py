try:
    numerator=int(input("Enter a numerator"))
    denominator=int(input("Enter a denominator"))
    result=numerator/denominator
except ZeroDivisionError:
    print('You can not divide by zero idiot')
except ValueError:
    print('Enter only number please')
else:
    print(result)
finally:
    print("This will always execute")
