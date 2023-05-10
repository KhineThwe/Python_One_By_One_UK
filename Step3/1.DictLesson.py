user = {
    'name':'Khine',
    'age':24,
    'gender':'female',
    'course':'CS'
}
#{key:value} pair

#data accessing
print(user['age'])#24
print(user['name'])#Khine
print(user['gender'])#female

print(user.get('name'))
# print(user.get('course'))#None
print(user.get('course','Python'))#default value

print(user.values())#return list

