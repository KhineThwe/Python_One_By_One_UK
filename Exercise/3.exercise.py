ls = [1,2,3,4]
print("Length: ",len(ls))
ls.append(5)
print(ls)
#ls  = [1,2,3,4,5]
ls.insert(2,99)
print(ls)
#ls = [1,2,99,3,4,5]
ls.remove(3)
print(ls)
#ls = [1,2,99,4,5]
ls.pop(4)
print(ls)
#ls = [1,2,99,4]
ls.sort(reverse=True)
print("After sorting: ",ls)


