#list comprehension
numbers = [1,2,3,4,5,6,7,8,9,10]
# new_list = [num for num in numbers if num %2 == 0]
# print(new_list)
#
# #2,4,6,8,10
# new_list1 = [num for num in numbers if num %2 ==0 if num %3 ==0]
# print(new_list1)
#
# #if else
new_list2 = [num *2 if num%2 ==0 else num for num in numbers]

new_list3 = []
for num in numbers:
    if num %2 ==0:
        new_list3.append(num*2)
    else:
        new_list3.append(num)
print(new_list3)


#nested if
#NumPy
#Pandas
#Matplotib
#Scikit-learn
#Tensor-Flow
#Keras
#PyTorch