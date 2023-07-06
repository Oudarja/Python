import random

while True:
    choices=["rock","paper","scissor"]
    computer=random.choice(choices)
    player=None
    while player not in choices:
        player=input("rock,paper,scissor?:").lower()
        if player==computer:
            print("Computer: ",computer)
            print("Player: ",player)
            print("Tie")
        elif player=="rock":
            if computer=="paper":
                print("Computer: ",computer)
                print("Player: ",player)
                print("Lose")
            else:
                print("Computer: ",computer)
                print("Player: ",player)
                print("Win")
        elif player=="paper":
            if computer == "rock":
                print("Computer: ",computer)
                print("Player: ",player)
                print("Win")
            else:
                print("Computer: ",computer)
                print("Player: ",player)
                print("Lose")
        else:
            if computer == "rock":
                print("Computer: ",computer)
                print("Player: ",player)
                print("Lose")
            else:
                print("Computer: ",computer)
                print("Player: ",player)
                print("Win")
    play_again=input("Y/N: ").lower()
    if play_again!='y':
        break
print("Bye")
