#slicing= create a substring by extracting elements from another string
#          indexing[] or slice[]
#          [start,stop,step]
name="Bro Code"
first_name=name[0:3:1]
last_name=name[4:8:1]
funky_name=name[0:8:2];
print(first_name)
print(last_name)
print(funky_name)
#reversing a string  with indexing
#here -1 means read from back ward
name=name[::-1]
print(name)
website="http://google.com"
#slice object is creasted
#negative number is for index from backward
slice=slice(7,-4)

print(website[slice])
