i=1

while(i<=100):
    print(i)
    i+=1
print("End")

i=1;
sum=0;
while(i<=100):
    if(i==100):
        break
    if(i==50):
        i+=1
        continue
    sum+=i
    i+=1

print(sum)
name=""
while len(name)==0:
    name=input("Enter Your name")
    print(name)
