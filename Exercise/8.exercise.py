import random

print("Welcome from Our Lottery Game!!!")
user_amount = int(input("Please enter your amount: "))#5000 --> 500*2 = 1000 --> 5500
#5000-500 ====> 4500 - 500
option = int(input("Press 1 to play game!Press 2 to quit!!"))
computer_no = random.randint(0,99)

while option == 1:
    play_amount = int(input("Please enter your play amount: "))
    if user_amount < play_amount:
        print("Insufficient Balance!!Please sufficient balance again!!")
        user_amount = int(input("Please enter your amount: "))
    else:
        play_no = int(input("Please enter your play no: "))
        user_amount -= play_amount
        if play_no == computer_no:
            print("Hit!!!")
            user_amount += play_amount * 2
        else:
            print("Lose")
        print("Your current cash : ",user_amount)
        if user_amount == 0:
            exit(0)
        option = int(input("Press 1 to play game!!Press 2 to quitt!!!"))

