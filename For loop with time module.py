import time
for i in range(10,0,-1):
    print(i)
    time.sleep(0.003)

print("Happy new year")
rows=int(input("Enter row: "))
column=int(input("Enter column: "))
symbol=input("Enter symbol: ")
for i in range(0,rows):
    for j in range(0,column):
        print(symbol,end="")
    print()
#print() is used to add new line  and only print usually contain newline so to restrict newline end="" is used

 
