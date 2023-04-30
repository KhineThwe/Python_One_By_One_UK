import string
string1 = "Hello"
          #01234
          #   H  e   l   l   o
          #  -5  -4  -3  -2  -1
#string slicing
print(string1[0])
print(string1[4])
print(string1[0:2])#start:stop(exclusive)
#He  0,1
print(string1[2:4])

print(string1[:2])#default 0
print(string1[2:])

print(string1)
print(string1[:])#the whole

#negative index
print(string1[-5:-2])
print(string1[::-1])#reverse order