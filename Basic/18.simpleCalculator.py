print("Press 1: For Add")
print("Press 2: For Subtract")
print("Press 3: For Multiply")
print("Press 4: For Divide")
firstNumber = int(input("Enter first number: "))
secondNumber = int(input("Enter second number: "))
option = int(input("Please enter 1 or 2 or 3 or 4: "))

if option == 1:
    total = firstNumber+secondNumber
    print("Adding result: ",total)
elif option == 2:
    total = firstNumber - secondNumber
    print("Subtracting result: ",total)
elif option == 3:
    total = firstNumber * secondNumber
    print("Multiplying result: ",total)
elif option == 4:
    total = firstNumber/secondNumber
    print("Dividing result: ",total)
else:
    print("Wrong option")


