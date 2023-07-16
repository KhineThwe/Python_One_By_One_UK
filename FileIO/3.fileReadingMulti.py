file = open('data.txt','r')
# content = file.read()
# print(content)
# print(type(content))

content = file.readline()
while content:
    print(content)
    content = file.readline()

file.close()