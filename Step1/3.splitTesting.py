#split() သည် default သည် space မှစ၍ split လုပ်ပေးတယ်။
#separator ,maxsplit ---> optional
#test1
# txt = "Welcome from python course"
# x = txt.split()
# print(x)#return list
#default ---> space

#test2
# txt = "hello, my name is Peter, I am 24 years old"
# x = txt.split(",")
# print(x)

#test3
# txt = "apple#banna#orange#cherry"
# x = txt.split("#",2)
# print(x)

#test4
cars = 'BMW-Telsa-Range Rover'
x = cars.split("-",1)
print(x)

