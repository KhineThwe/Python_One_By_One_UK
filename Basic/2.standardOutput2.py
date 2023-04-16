#.format နဲ့ထုတ်တာ
name = "Khine"
age = 24
status = 'active'
print(name,age)
print("Hello,{}".format(name))
print("Hello,{}.You are {}".format(name,age))
print("Hello,{1}.You are {2}.Your status is: {0}".format(name,age,status))
                                                         #0     1    2

#keyword argument
print("{name2}:{name1}:{name3}".format(name1="Harry",name2="Potter",name3="Draco"))

#last
print(f"Hello,{name}")
print(f"Hello,{name} and Age: {age}")