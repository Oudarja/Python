import random
hobe=1
while(hobe):
    guess=int(input("Enter a number to win between 1 to 5: \n"))
    rand=random.randint(1,5)
    if(guess==rand):
        print("You have won")
    else:
        print("You have lost")
        print("Random number was :",rand)
