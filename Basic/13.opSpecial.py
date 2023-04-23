#Identity Operator
# to check if two values are stored on the same part of the memory.
#is
#is not

x1 = 5#int x1 and y1 are same values, same in memory.
y1 = 5
x2 = 'Hello'#str x2 and y2 are same values,same in memory
y2 = 'Hello'
x3 = [1,2,3]
#list x3 and y3 are same values,not identical.It is because the interpreter locates them separately in
#memory although they are equal.
y3 = [1,2,3]

print(x1 is y1)
print(x2 is y2)
print(x3 is y3)

#Membership Operator
#check if a var in sequence
#in
#not in
#sequence ---- > string,list,tuple,set and dictionary

str1 = 'Hello,world'
print('H' in str1)#if presents return True else False
print('H' not in str1)#if not present return True else False

print('h' in str1)
