num=[10,20,30,40,70,110,2]
for x in num:
    print(x)
for x in num:
    print(x*x)

#1+2+3+4+5+..............+n
sum=0;

n=int(input())
for x in range(1,n+1,1):
     sum+=x;

print(sum)

#2*3*4*5*.......n
mul=1
n=int(input())
for x in range(2,n+1,1):
     mul*=x;

print(mul)


for i in range(3):
    print((i+1)*"*")

print("\n")

for i in range(5):
    print((2*(i+1)-1)*"*")


print("\n")

num=6
c=0
for i in range(1,7,1):
    print((num-i)*" ",end="")
    print(i*"*")
