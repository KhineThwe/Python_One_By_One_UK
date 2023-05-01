import random

random_number = random.random()#return floating point between 0 and 1
print("Random number: ",random_number)

#randint ---> return int no ---> randint(lower,upper) #lower,upper ---> both inclusive
random_number1 = random.randint(4,10)#4,10 ရောပါထွက်လာနိုင်သည်။
print("Random number with randint method: ",random_number1)

#randrange --> return int no ---> randrange(start,stop,step)#step ---> optional , stop ---> exclusive
random_number2 = random.randrange(0,10,2)# 0 2 4 6 8
print("Random number with randrange method: ",random_number2)

print("Testing : ",random.randrange(0,1))



