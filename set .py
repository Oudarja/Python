#set=which is the collection of distinct value and unordered and unindexed value
utensils={"fork","spoon","knife"}
for i in utensils:
    print(i)
utensils1={"fork","spoon","knife","knife","knife"}
for i in utensils1:
    print(i)

utensils.add("napkin")
print(utensils)
utensils.add("book")
print(utensils)
utensils.remove("book")
print(utensils)
utensils.clear()
print(utensils)
utensils.update(utensils1)
print(utensils)
dishes={"bowl","plate","cup","knife"}
dinner_table=utensils.union(dishes)
print(dinner_table)
#what utensils have but dishes have not
print(utensils.difference(dishes))
#what dishes have but utensils have not
print(dishes.difference(utensils))
#intersection of utensils and dishes
print(dishes)
print(utensils)
print(utensils.intersection(dishes))
