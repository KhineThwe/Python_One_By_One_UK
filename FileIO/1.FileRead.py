"""
readline()     ---> return string
readlines()      ---> return list
"""
file = open('data.txt','r')#r for read mode
print("Sucess of opening file")
data = file.readlines()
print(data)
print(type(data))