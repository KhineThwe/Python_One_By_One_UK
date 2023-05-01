import random

#for random.choice
name = ['Harry','Potter','John','Marry']
number_list = [1,99,2,88,3,77]
random_no = random.choice(name)#random.choice(seq)
print("Random value with random.choice :   ",random_no)
print("Random value with number list: ",random.choice(number_list))

#for random.sample
random_no1 = random.sample(name,2)
print("Selected element is : ",random_no1)
print("Random value with number list: ",random.sample(number_list,2))