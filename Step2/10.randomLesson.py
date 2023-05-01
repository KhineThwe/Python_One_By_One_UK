#random.shuffle
import random
name = ['Harry','Potter','John','Marry']
print("Before Shuffle: ",name)
random.shuffle(name)
print("After shuffle",name)

#for random.uniform ---> return floating no ---> random.uniform(lower,upper) ---> both inclusive
random_no = random.uniform(4.5,10.6)
print("Random no from uniform is: ",random_no)

#for random.triangular --> return floating no---> random.triangular(low,high,mode) --> high exclusive
random_no1 = random.triangular(10.0,20.0,2.0)
print("Random no from triangular: ",random_no1)

