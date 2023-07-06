food=["Pizza","Hamburger","Hotdog","Spaghetti","Pudding"]
print(food)
food[0]="Sushi"
print(food)
#appending at the last
food.append("Ice-cream")
print(food)
food.remove("Hotdog")
print(food)
#popping last element
food.pop()

print(food)
food.insert(0,"Cake")
for x in food:
    print(x)

    food.clear()
