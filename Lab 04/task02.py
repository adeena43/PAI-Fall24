list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
newList=[]

for var1 in range(len(list1)):
    for var2 in range(len(list2)):
        newList.append(list1[var1] +" "+ list2[var2])

print(newList)
