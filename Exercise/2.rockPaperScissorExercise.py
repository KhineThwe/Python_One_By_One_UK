#random require
import random

user_choice = input("What is your choice?\n'r' for rock,'p' for paper and 's' for scissor\n")
computer  = ['r','p','s']
computer_choice = random.choice(computer)#r
print(f'Computer Choice: {computer_choice}')

if user_choice == computer_choice:#r == r/# p == p/ s == s
    print("It's a tie")
elif user_choice == "r": #p,s
    if computer_choice == "p":
        print("Paper covers rock! You lose!")
    elif computer_choice == "s":
        print("Rock smashes scissors!You win!")
elif user_choice == "p":#s,r
    if computer_choice == "r":
        print("Paper covers rock!You win!")
    elif computer_choice == "s":
        print("Scissors cuts paper!You lose!")
elif user_choice == "s":#r,p
    if computer_choice == "r":
        print("Rock smashes scissors!You lose!")
    elif computer_choice == "p":
        print("Scissors cut papers!You win!")