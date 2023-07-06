#Dictionary=A changeable,unordered,collection of unique key:value pairs .Fast because they use hashing
            #allows us to access value through hashing ,allow us to access value quickly
capitals={'USA':'Washington DC',
           'India':'Delhi',
           'China':'Beijing',
           'Russia':'Moscow'
          }
print(capitals['USA'])
print(capitals.get('India'))
#whene key does not exist then print none

print(capitals.get('Germany'))

#print all keys
print(capitals.keys())
#print all values

print(capitals.values())

# print all items in dictionary

print(capitals.items())
for key,value in capitals.items():
    print(key,value)

#update Dictionary
capitals.update({'Germany':'Berlin'})

print(capitals)
#remove a key value pair from dictionary
capitals.pop('China')
print(capitals)
#clear all items from
capitals.clear()
print(capitals)
