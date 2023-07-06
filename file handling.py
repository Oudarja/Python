import os
path="F:\\test.txt"

if os.path.exists(path):
    print("Location exists")
    if os.path.isfile(path):
        print("This is a file")
        #reading file
        with open('F:\\test.txt') as file:
            print(file.read())
    elif os.path.isdir(path):
        print("This is a directory")
    else:
        print("Nothing")
else:
    print("The location does not exists")
#writing in a file
text="I am trying from the root to be red in codeforces.\nOneday i will be for sure."

with open('F:\\test1.txt','w') as file:
    file.write(text)
