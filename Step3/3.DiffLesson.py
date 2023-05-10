#List methods
#Accessing list items
myList = ["juice","glasses","glasses","flower"]
print(myList[1])

#Change list items
myList[1] = "blackberry"
print(myList)
#['juice', 'blackberry', 'glasses', 'flower']

myList[1:3] = ["gg","hh"]
print(myList)
#['juice', 'gg', 'hh', 'flower']

#insert
myList.insert(0,"Element0")
print(myList)
#['Element0', 'juice', 'gg', 'hh', 'flower']

#append
myList.append("Len")
print(myList)
#['Element0', 'juice', 'gg', 'hh', 'flower',"Len]

#extend
newList = ["new1","new2"]
myList.extend(newList)
print(myList)

#remove list items
myList.remove("gg")
print(myList)

#loop
for x in myList:
    print(x)

print(len(myList))