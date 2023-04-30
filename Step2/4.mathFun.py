import math
print(math.pi)

#area
r  = 4
pie = math.pi
area = pie * r*r
print("Area", area)

#ceil
a = 2.8
print(math.ceil(a))
print(math.floor(a))

#factorial
factorial_no = 5
result = math.factorial(factorial_no)
print("The factorial of 5 is ",result)#5*4*3*2*1 = 120

#pow
print("Power: ",pow(2,3))

#logarithm
print("Log 2 with base 10",math.log(2, 10))
print("Log 2 base 10 value : ",math.log2(10))#log 2 with base 16 #3.321928094887362
print("Log 10 base 10 value : ",math.log10(10))

#sqrt
print(math.sqrt(4))#2.0
# Round square root numbers downward to the nearest integer
print(math.isqrt(4))

#trigonometric
print("The value of sine",math.sin(math.pi/3))
print("The value of tan",math.tan(math.pi/3))
print("The value of cos",math.cos(math.pi/6))

