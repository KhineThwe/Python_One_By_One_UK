my_dictonary = {'first':1,"second":2,"third":3}

new_dictionary = {key.upper():value*2 for key,value in my_dictonary.items()}

print(new_dictionary)

# for key,value in my_dictonary.items():
#     print(key.upper())
#     print(value*2)