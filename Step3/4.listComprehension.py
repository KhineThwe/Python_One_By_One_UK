#List comprehension
myList = ['phone',"laptop","tablet"]
newList = []

# for x in myList:
#     if x in myList:
#         newList.append(x)
# print(newList)

newList1 = [x for x in myList if x in myList]
#a = a+1
#syntax
#newList1 = [expression for item in iterable if condition == True]
print(newList1)
