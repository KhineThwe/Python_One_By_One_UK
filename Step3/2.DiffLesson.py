#list
#ordered,changeable,allow duplicate values,can access with index no
myList = ["juice","glasses","glasses","flower"]
myList[0] ="orange"#overwrite
print(myList)

#Tuple
#ordered,allow duplicate values,unchangeable,can access with index no
myTuple = ("juice","glasses","glasses","flower")
# myTuple[0] = "stawberry"#TypeError
print(myTuple[2])

#Set
#unordered,don't allow duplicate values,unchangeable,can't access with index no
mySet = {"flower","juice","glasses","glasses"}
#print(mySet[0])#'set' object is not subscriptable

#Dictionary
#ordered,don't allow duplicate value,changeable,
#can access with key name
myDict = {
    "flower":"rose",
    "juice":"orange juice",
    "glasses":"sunglasses",
    "glasses": "sunglasses"
}
myDict['juice'] = "stawberry juice"
print(myDict)