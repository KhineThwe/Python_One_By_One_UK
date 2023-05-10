mynewList = [1,2,3,4,5]
newList = []
for x in mynewList:
    if x in mynewList:
        newList.append(x)
print(newList)

newList1 = [x*2 for x in mynewList if x in mynewList]
print("My newList 1 : ",newList1)
