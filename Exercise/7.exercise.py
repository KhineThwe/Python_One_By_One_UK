import random

user_num = int(input("Enter user number"))
computer_num = random.randint(0,99)
print(f'Computer number : {computer_num}')

if user_num == computer_num:
    print("Loterry Won!!!")
elif user_num < computer_num:
    print("Your number is lower than computer number!!!")
elif user_num > computer_num:
    print("Your number is greater than computer number!!!")